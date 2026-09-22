# U.S. JUE Database public snapshot (2026-09-19)

This repository is the public delivery index for the collected U.S. Domain–Anchor / Journal of Urban Economics database snapshot.

The redistribution-screened data archive is stored in the GitHub Release `data-20260919-public` as numbered binary parts because the verified ZIP64 archive exceeds GitHub's per-asset limit. Download every `US_JUE_DATABASE_20260919_PUBLIC.zip.partNNN` asset into one directory together with `split_manifest.csv`, `split_metadata.json`, and a reconstruction script.

## Archive

- Filename: `US_JUE_DATABASE_20260919_PUBLIC.zip`
- Bytes: `145975256041`
- SHA256: `9025b59c1f7afe1b93b348fa75e91ec9e7176a19af15cfad89679515d72a3fc9`
- ZIP members: `34681`
- Payload files: `34678`
- Integrity: every archived payload was read back and verified against SHA256; ZIP CRC checks passed.

## Reconstruct on Windows

```powershell
powershell -ExecutionPolicy Bypass -File .\reassemble.ps1
```

## Reconstruct on Linux or macOS

```bash
bash ./reassemble.sh
```

Both scripts verify every part against `split_manifest.csv`, reconstruct the archive, and verify its final SHA256 using `split_metadata.json`.

## Redistribution screen

This public archive differs from the complete private research snapshot. It excludes files whose provider prohibits third-party redistribution and files for which an item-specific redistribution grant was not established. The exclusions preserve source URLs and reasons in [public_release_exclusions.csv](public_release_exclusions.csv). See [DATA_USE_AND_REDISTRIBUTION.md](DATA_USE_AND_REDISTRIBUTION.md) before reuse.

## Scope

This is a frozen snapshot of the files collected when acquisition stopped. It includes raw data, processed products, scripts, documentation, provenance, download logs, QA outputs, and explicit records of incomplete or unavailable assets. It does not claim that every planned data source is complete or that every series forms a balanced, geographically harmonized panel.
