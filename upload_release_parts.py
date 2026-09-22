#!/usr/bin/env python3
import argparse
import concurrent.futures
import csv
import hashlib
import json
import os
import subprocess
import threading
import time
from pathlib import Path


def run_json(command):
    completed = subprocess.run(command, check=True, text=True, capture_output=True)
    return json.loads(completed.stdout)


def assets(gh, repo, tag):
    # `releases/tags/{tag}` does not expose an unpublished draft release.
    # The gh release command resolves both draft and published releases.
    release = run_json([str(gh), "release", "view", tag, "--repo", repo, "--json", "assets"])
    return {item["name"]: int(item["size"]) for item in release.get("assets", [])}


def materialize(archive, destination, offset, size, expected_sha):
    if destination.is_file() and destination.stat().st_size == size:
        h = hashlib.sha256()
        with destination.open("rb") as existing:
            for block in iter(lambda: existing.read(16 * 1024 * 1024), b""):
                h.update(block)
        if h.hexdigest() == expected_sha:
            return
    h = hashlib.sha256()
    remaining = size
    with archive.open("rb") as src, destination.open("wb") as dst:
        src.seek(offset)
        while remaining:
            block = src.read(min(16 * 1024 * 1024, remaining))
            if not block:
                raise RuntimeError("Unexpected end of archive")
            dst.write(block)
            h.update(block)
            remaining -= len(block)
    if h.hexdigest() != expected_sha:
        destination.unlink(missing_ok=True)
        raise RuntimeError(f"Materialized part failed SHA256: {destination.name}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gh", required=True, type=Path)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--tag", default="data-20260919")
    parser.add_argument("--archive", required=True, type=Path)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--temp-dir", required=True, type=Path)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--upload-timeout-seconds", type=int, default=1200)
    args = parser.parse_args()

    args.temp_dir.mkdir(parents=True, exist_ok=True)
    rows = list(csv.DictReader(args.manifest.open(newline="", encoding="utf-8-sig")))
    uploaded = assets(args.gh, args.repo, args.tag)

    print_lock = threading.Lock()

    def emit(record):
        with print_lock:
            print(json.dumps(record), flush=True)

    def upload_one(row):
        name = row["part_name"]
        size = int(row["bytes"])
        if uploaded.get(name) == size:
            emit({"status": "ALREADY_UPLOADED", "part": row["part_number"], "name": name})
            return
        if name in uploaded:
            raise RuntimeError(f"Remote asset has unexpected size: {name}")

        temp = args.temp_dir / name
        try:
            materialize(args.archive, temp, int(row["byte_start"]), size, row["sha256"])
            for attempt in range(1, 6):
                emit({"status": "UPLOADING", "part": row["part_number"], "parts": len(rows), "attempt": attempt, "name": name, "bytes": size})
                try:
                    completed = subprocess.run(
                        [str(args.gh), "release", "upload", args.tag, str(temp), "--repo", args.repo],
                        text=True,
                        capture_output=True,
                        timeout=args.upload_timeout_seconds,
                    )
                except subprocess.TimeoutExpired:
                    completed = subprocess.CompletedProcess([], 124, "", f"upload timed out after {args.upload_timeout_seconds} seconds")
                if completed.returncode == 0:
                    break
                current = assets(args.gh, args.repo, args.tag)
                if current.get(name) == size:
                    break
                if attempt == 5:
                    raise RuntimeError(f"Upload failed after retries: {name}: {completed.stderr.strip()}")
                emit({"status": "RETRYING", "part": row["part_number"], "attempt": attempt, "error": completed.stderr.strip()[-500:]})
                time.sleep(10 * attempt)
            emit({"status": "UPLOADED", "part": row["part_number"], "parts": len(rows), "name": name})
        finally:
            temp.unlink(missing_ok=True)

    if args.workers < 1:
        raise RuntimeError("workers must be at least 1")
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = [executor.submit(upload_one, row) for row in rows]
        try:
            for future in concurrent.futures.as_completed(futures):
                future.result()
        except BaseException:
            for future in futures:
                future.cancel()
            raise

    final_assets = assets(args.gh, args.repo, args.tag)
    missing = [row["part_name"] for row in rows if final_assets.get(row["part_name"]) != int(row["bytes"])]
    if missing:
        raise RuntimeError(f"Remote verification failed for {len(missing)} parts")
    emit({"status": "ALL_PARTS_VERIFIED", "parts": len(rows)})


if __name__ == "__main__":
    main()
