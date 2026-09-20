#!/usr/bin/env bash
set -euo pipefail

parts_dir="${1:-.}"
output="${2:-US_JUE_DATABASE_20260919.zip}"
expected="7f930eec678bcce9c62084b7d68c5e75417cbeb07b1c4cd4cd56a1e42c2447db"

python3 - "$parts_dir" "$output" "$expected" <<'PY'
import csv, hashlib, pathlib, sys

root = pathlib.Path(sys.argv[1])
output = root / sys.argv[2]
expected = sys.argv[3]
rows = sorted(csv.DictReader((root / "split_manifest.csv").open(newline="", encoding="utf-8-sig")), key=lambda r: int(r["part_number"]))

with output.open("wb") as dst:
    for row in rows:
        path = root / row["part_name"]
        h = hashlib.sha256()
        with path.open("rb") as src:
            for block in iter(lambda: src.read(16 * 1024 * 1024), b""):
                h.update(block)
                dst.write(block)
        if h.hexdigest() != row["sha256"]:
            raise SystemExit(f"SHA256 mismatch: {path.name}")

h = hashlib.sha256()
with output.open("rb") as src:
    for block in iter(lambda: src.read(16 * 1024 * 1024), b""):
        h.update(block)
if h.hexdigest() != expected:
    raise SystemExit("Final archive SHA256 mismatch")
print(f"Verified: {output}")
PY

