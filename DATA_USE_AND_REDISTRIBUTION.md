# Data use and redistribution

This public snapshot preserves source provenance and does not grant a blanket license over third-party data. Each source remains subject to the provider's terms recorded in `00_metadata/master_manifest.csv` and the archived documentation.

The public archive deliberately omits files for which redistribution is prohibited or an item-specific redistribution grant was not established. The exact rules, reasons, and official acquisition links are listed in `00_metadata/public_release_exclusions.csv`. Scripts, logs, manifest rows, and source links remain so a qualified user can reproduce the acquisition directly from the provider under the applicable terms.

The main exclusions are:

- TxDOT Roadway Inventory 2019 raw content, related QA records, and archived provider content. TxDOT's published terms prohibit third-party distribution without written consent.
- Hawaii State GIS HPMS 2022 and 2023 ZIPs. The items were publicly downloadable, but the item metadata did not state a redistribution license.
- The `rhodes351/ASR_26_RTW` historical CBP archive. That repository declares no license, and its README credits IPUMS NHGIS. NHGIS requires permission for redistribution outside a publication-specific subset.

The private research snapshot and the public snapshot therefore have different hashes and member counts. Do not use the private snapshot's split manifest or reconstruction scripts with the public release.

Repository presence is not a warranty of fitness, geographic comparability, or panel balance. Suppression, missingness, source breaks, and geography exceptions remain documented in the database metadata and QA outputs.
