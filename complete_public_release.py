#!/usr/bin/env python3
"""Resume, verify, and safely publish the redistribution-screened release.

The repository remains private until every expected data part and helper asset
has been verified against its local SHA256. The older private release is
deleted before repository visibility changes so restricted source material can
never become public accidentally.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


HELPER_ASSETS = (
    "DATA_ACQUISITION_REPORT.md",
    "DATA_USE_AND_REDISTRIBUTION.md",
    "package_report.json",
    "public_release_exclusions.csv",
    "reassemble.ps1",
    "reassemble.sh",
    "split_manifest.csv",
    "split_metadata.json",
    "US_JUE_DATABASE_20260919_PUBLIC.zip.sha256",
)


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(16 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def run(command: list[str], *, cwd: Path | None = None, check: bool = True) -> subprocess.CompletedProcess:
    print(json.dumps({"time": utc_now(), "status": "RUN", "command": command}), flush=True)
    completed = subprocess.run(command, cwd=cwd, text=True, capture_output=True)
    if completed.stdout:
        print(completed.stdout, end="" if completed.stdout.endswith("\n") else "\n", flush=True)
    if completed.stderr:
        print(completed.stderr, end="" if completed.stderr.endswith("\n") else "\n", file=sys.stderr, flush=True)
    if check and completed.returncode:
        raise RuntimeError(f"Command failed ({completed.returncode}): {' '.join(command)}")
    return completed


def run_json(command: list[str], *, cwd: Path | None = None) -> dict:
    completed = subprocess.run(command, cwd=cwd, check=True, text=True, capture_output=True)
    return json.loads(completed.stdout)


def write_status(path: Path, status: str, **extra) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {"updated_at_utc": utc_now(), "status": status, **extra}
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload), flush=True)


def release(gh: Path, repo: str, tag: str) -> dict:
    return run_json(
        [str(gh), "release", "view", tag, "--repo", repo, "--json", "assets,isDraft,name,tagName,url"]
    )


def asset_map(release_info: dict) -> dict[str, dict]:
    return {item["name"]: item for item in release_info.get("assets", [])}


def verify_remote_assets(args, rows: list[dict]) -> dict:
    info = release(args.gh, args.repo, args.public_tag)
    remote = asset_map(info)
    expected_parts = {row["part_name"] for row in rows}
    remote_parts = {name for name in remote if name.startswith(args.part_prefix)}
    if remote_parts != expected_parts:
        missing = sorted(expected_parts - remote_parts)
        unexpected = sorted(remote_parts - expected_parts)
        raise RuntimeError(f"Part-name mismatch: missing={missing[:5]} unexpected={unexpected[:5]}")

    verified_parts = []
    total = 0
    for row in rows:
        name = row["part_name"]
        expected_size = int(row["bytes"])
        expected_digest = row["sha256"].lower()
        item = remote[name]
        actual_digest = (item.get("digest") or "").removeprefix("sha256:").lower()
        if int(item["size"]) != expected_size or actual_digest != expected_digest:
            raise RuntimeError(
                f"Remote part verification failed: {name} size={item.get('size')} digest={item.get('digest')}"
            )
        total += expected_size
        verified_parts.append(
            {"name": name, "bytes": expected_size, "sha256": expected_digest}
        )

    if total != args.archive.stat().st_size:
        raise RuntimeError(f"Part total {total} differs from archive size {args.archive.stat().st_size}")

    verified_helpers = []
    for name in HELPER_ASSETS:
        local = args.repo_dir / name
        if not local.is_file():
            raise RuntimeError(f"Missing local helper asset: {local}")
        if name not in remote:
            raise RuntimeError(f"Missing remote helper asset: {name}")
        expected_size = local.stat().st_size
        expected_digest = sha256(local)
        actual_digest = (remote[name].get("digest") or "").removeprefix("sha256:").lower()
        if int(remote[name]["size"]) != expected_size or actual_digest != expected_digest:
            raise RuntimeError(f"Remote helper verification failed: {name}")
        verified_helpers.append(
            {"name": name, "bytes": expected_size, "sha256": expected_digest}
        )

    archive_digest = args.archive_hash.read_text(encoding="utf-8").split()[0].lower()
    if sha256(args.archive) != archive_digest:
        raise RuntimeError("Local archive SHA256 changed before publication")

    return {
        "status": "VERIFIED",
        "verified_at_utc": utc_now(),
        "repository": args.repo,
        "release_tag": args.public_tag,
        "release_url": info["url"],
        "archive_name": args.archive.name,
        "archive_bytes": total,
        "archive_sha256": archive_digest,
        "part_count": len(verified_parts),
        "part_bytes_total": total,
        "helper_asset_count": len(verified_helpers),
        "parts": verified_parts,
        "helper_assets": verified_helpers,
    }


def upload_with_resume(args) -> None:
    command = [
        sys.executable,
        str(args.repo_dir / "upload_release_parts.py"),
        "--gh",
        str(args.gh),
        "--repo",
        args.repo,
        "--tag",
        args.public_tag,
        "--archive",
        str(args.archive),
        "--manifest",
        str(args.manifest),
        "--temp-dir",
        str(args.temp_dir),
        "--workers",
        str(args.workers),
        "--upload-timeout-seconds",
        str(args.upload_timeout_seconds),
    ]
    last_error = None
    for attempt in range(1, args.upload_pass_attempts + 1):
        write_status(args.status_file, "UPLOADING", pass_attempt=attempt)
        completed = run(command, cwd=args.repo_dir, check=False)
        if completed.returncode == 0:
            return
        last_error = f"upload pass {attempt} exited {completed.returncode}"
        write_status(args.status_file, "UPLOAD_RETRY_WAIT", error=last_error)
        if attempt < args.upload_pass_attempts:
            time.sleep(args.retry_wait_seconds)
    raise RuntimeError(last_error or "Upload did not complete")


def publish(args, verification: dict) -> None:
    verification_path = args.repo_dir / "GITHUB_UPLOAD_VERIFICATION.json"
    verification_path.write_text(json.dumps(verification, indent=2) + "\n", encoding="utf-8")

    run(["git", "add", "--", verification_path.name], cwd=args.repo_dir)
    staged = run(["git", "diff", "--cached", "--quiet"], cwd=args.repo_dir, check=False)
    if staged.returncode == 1:
        run(["git", "commit", "-m", "Record verified public release upload"], cwd=args.repo_dir)
        run(["git", "push", "origin", "main"], cwd=args.repo_dir)
    elif staged.returncode != 0:
        raise RuntimeError("Unable to inspect staged verification record")

    run(
        [
            str(args.gh),
            "release",
            "upload",
            args.public_tag,
            str(verification_path),
            "--repo",
            args.repo,
            "--clobber",
        ]
    )
    refreshed = asset_map(release(args.gh, args.repo, args.public_tag))
    remote_verification = refreshed.get(verification_path.name)
    if not remote_verification:
        raise RuntimeError("Verification asset did not appear on the draft release")
    remote_digest = (remote_verification.get("digest") or "").removeprefix("sha256:").lower()
    if int(remote_verification["size"]) != verification_path.stat().st_size or remote_digest != sha256(verification_path):
        raise RuntimeError("Verification asset differs from local file")

    repository = run_json(
        [str(args.gh), "repo", "view", args.repo, "--json", "isPrivate,visibility,url"]
    )
    if not repository.get("isPrivate"):
        raise RuntimeError("Safety stop: repository became public before private-release cleanup")

    old = run(
        [str(args.gh), "release", "view", args.old_tag, "--repo", args.repo],
        check=False,
    )
    if old.returncode == 0:
        run(
            [
                str(args.gh),
                "release",
                "delete",
                args.old_tag,
                "--repo",
                args.repo,
                "--cleanup-tag",
                "--yes",
            ]
        )
    old_check = run(
        [str(args.gh), "release", "view", args.old_tag, "--repo", args.repo],
        check=False,
    )
    if old_check.returncode == 0:
        raise RuntimeError("Old private release still exists; refusing to make repository public")

    run(
        [
            str(args.gh),
            "release",
            "edit",
            args.public_tag,
            "--repo",
            args.repo,
            "--draft=false",
            "--latest",
            "--target",
            "main",
        ]
    )
    run(
        [
            str(args.gh),
            "repo",
            "edit",
            args.repo,
            "--visibility",
            "public",
            "--accept-visibility-change-consequences",
        ]
    )

    final_repo = run_json(
        [str(args.gh), "repo", "view", args.repo, "--json", "isPrivate,visibility,url"]
    )
    final_release = release(args.gh, args.repo, args.public_tag)
    if final_repo.get("isPrivate") or str(final_repo.get("visibility", "")).upper() != "PUBLIC":
        raise RuntimeError("Repository visibility verification failed")
    if final_release.get("isDraft"):
        raise RuntimeError("Release is still a draft after publication")

    request = urllib.request.Request(final_repo["url"], headers={"User-Agent": "US-JUE-release-verifier/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            if response.status != 200:
                raise RuntimeError(f"Anonymous repository check returned HTTP {response.status}")
    except urllib.error.HTTPError as error:
        raise RuntimeError(f"Anonymous repository check failed: HTTP {error.code}") from error

    if args.remove_local_archive_on_success:
        args.archive.unlink(missing_ok=True)
        args.archive_hash.unlink(missing_ok=True)
        for path in args.temp_dir.glob("*"):
            if path.is_file():
                path.unlink(missing_ok=True)

    write_status(
        args.status_file,
        "COMPLETE",
        repository_url=final_repo["url"],
        release_url=final_release["url"],
        archive_sha256=verification["archive_sha256"],
        archive_bytes=verification["archive_bytes"],
        parts=verification["part_count"],
        local_archive_removed=args.remove_local_archive_on_success,
    )


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gh", required=True, type=Path)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--repo-dir", required=True, type=Path)
    parser.add_argument("--archive", required=True, type=Path)
    parser.add_argument("--archive-hash", required=True, type=Path)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--temp-dir", required=True, type=Path)
    parser.add_argument("--status-file", required=True, type=Path)
    parser.add_argument("--public-tag", default="data-20260919-public")
    parser.add_argument("--old-tag", default="data-20260919")
    parser.add_argument("--part-prefix", default="US_JUE_DATABASE_20260919_PUBLIC.zip.part")
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--upload-timeout-seconds", type=int, default=3600)
    parser.add_argument("--upload-pass-attempts", type=int, default=24)
    parser.add_argument("--retry-wait-seconds", type=int, default=300)
    parser.add_argument("--remove-local-archive-on-success", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.gh = args.gh.resolve()
    args.repo_dir = args.repo_dir.resolve()
    args.archive = args.archive.resolve()
    args.archive_hash = args.archive_hash.resolve()
    args.manifest = args.manifest.resolve()
    args.temp_dir = args.temp_dir.resolve()
    args.status_file = args.status_file.resolve()

    for path in (args.gh, args.archive, args.archive_hash, args.manifest):
        if not path.is_file():
            raise RuntimeError(f"Required file missing: {path}")
    if args.workers < 1:
        raise RuntimeError("workers must be at least 1")
    args.temp_dir.mkdir(parents=True, exist_ok=True)

    rows = list(csv.DictReader(args.manifest.open(newline="", encoding="utf-8-sig")))
    if len(rows) != 77:
        raise RuntimeError(f"Expected 77 split parts, found {len(rows)}")

    write_status(args.status_file, "STARTING", parts=len(rows), workers=args.workers)
    try:
        upload_with_resume(args)
        write_status(args.status_file, "VERIFYING_REMOTE", parts=len(rows))
        verification = verify_remote_assets(args, rows)
        write_status(args.status_file, "PUBLISHING", parts=len(rows))
        publish(args, verification)
    except BaseException as error:
        write_status(args.status_file, "FAILED", error=repr(error))
        raise


if __name__ == "__main__":
    main()
