#!/usr/bin/env python3
import argparse
import csv
import hashlib
import json
import math
import os
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("archive", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--part-bytes", type=int, default=1_900_000_000)
    parser.add_argument("--expected-sha256", required=True)
    args = parser.parse_args()

    archive = args.archive.resolve()
    out_dir = args.output_dir.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    total = archive.stat().st_size
    count = math.ceil(total / args.part_bytes)
    archive_hash = hashlib.sha256()
    records = []

    with archive.open("rb") as src:
        for index in range(count):
            remaining = min(args.part_bytes, total - index * args.part_bytes)
            part_hash = hashlib.sha256()
            part_size = remaining
            while remaining:
                block = src.read(min(16 * 1024 * 1024, remaining))
                if not block:
                    raise RuntimeError("Unexpected end of archive")
                part_hash.update(block)
                archive_hash.update(block)
                remaining -= len(block)
            records.append({
                "part_number": index + 1,
                "part_name": f"{archive.name}.part{index + 1:03d}",
                "byte_start": index * args.part_bytes,
                "bytes": part_size,
                "sha256": part_hash.hexdigest(),
            })
            print(json.dumps({"status": "HASHING_PARTS", "part": index + 1, "parts": count, "percent": round(100 * (index + 1) / count, 1)}), flush=True)

    actual = archive_hash.hexdigest()
    if actual != args.expected_sha256.lower():
        raise RuntimeError(f"Archive SHA256 mismatch: {actual}")

    manifest = out_dir / "split_manifest.csv"
    temp = manifest.with_suffix(".csv.tmp")
    with temp.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=["part_number", "part_name", "byte_start", "bytes", "sha256"])
        writer.writeheader()
        writer.writerows(records)
    os.replace(temp, manifest)

    metadata = {
        "archive": archive.name,
        "archive_bytes": total,
        "archive_sha256": actual,
        "part_bytes": args.part_bytes,
        "parts": count,
    }
    (out_dir / "split_metadata.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "VERIFIED", **metadata}), flush=True)


if __name__ == "__main__":
    main()

