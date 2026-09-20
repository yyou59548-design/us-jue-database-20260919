# U.S. JUE Database snapshot (2026-09-19)

This private repository is the delivery index for the collected U.S. Domain–Anchor / Journal of Urban Economics database snapshot.

The data archive is stored in the GitHub Release `data-20260919` as numbered binary parts because the verified archive is larger than GitHub's per-asset limit. Download every `US_JUE_DATABASE_20260919.zip.partNNN` asset into one directory, then run the included reconstruction script.

## Archive

- Original filename: `US_JUE_DATABASE_20260919.zip`
- Original bytes: `146316247853`
- Original SHA256: `7f930eec678bcce9c62084b7d68c5e75417cbeb07b1c4cd4cd56a1e42c2447db`
- ZIP members: `36328`
- Payload files: `36326`
- Integrity status: every archived payload was read back and verified against SHA256; ZIP CRC checks passed.

## Reconstruct on Windows

```powershell
powershell -ExecutionPolicy Bypass -File .\reassemble.ps1
```

## Reconstruct on Linux or macOS

```bash
bash ./reassemble.sh
```

Both scripts verify every part against `split_manifest.csv`, reconstruct the original ZIP, and verify the final archive SHA256.

## Scope

This is a frozen snapshot of the files collected by the time acquisition was stopped. It includes raw data, processed products, scripts, documentation, provenance, download logs, QA outputs, and explicit records of incomplete or unavailable assets. It is not a claim that every originally planned data source is complete.

