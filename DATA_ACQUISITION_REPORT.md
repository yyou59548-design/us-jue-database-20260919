# DATA ACQUISITION REPORT

Snapshot: 2026-09-19T12:26:24+00:00.

**Not complete.** P0 raw data, the four foundational products, and multiple P1 modules are physically present. Collection has stopped at the user request for packaging. The archive contains the acquired snapshot; incomplete targets, credential restrictions and provider gaps remain explicit. A file-integrity pass does not certify a balanced panel or historical geographic comparability.

## What was found?

All36 requested P0 assets plus supplementary LODES RAC have explicit records. 82 asset records now include P1 mechanisms and historical sources. The521-item asset map is not treated as a download target. Source entry points and exact releases are retained in `00_metadata/source_registry.csv` and the file manifest.

## What was actually downloaded?

There are **18,737 unique verified raw/documentation objects, 118.04 GiB**. Partial transfers are excluded. The table counts unique physical target paths within each asset; multiple URLs for one target do not inflate its denominator. Shared archives can fulfill more than one asset.

| Asset | Dataset | Verified / target objects | Acquisition status |
|---|---|---:|---|
| P0-01 | BDS County x Firm Age | 2 / 2 | DOWNLOADED_VERIFIED |
| P0-02 | BDS County x Firm Size | 1 / 1 | DOWNLOADED_VERIFIED |
| P0-03 | BDS County x Establishment Age | 1 / 1 | DOWNLOADED_VERIFIED |
| P0-04 | BDS County x Sector | 1 / 1 | DOWNLOADED_VERIFIED |
| P0-05 | CBP county industry files | 38 / 38 | DOWNLOADED_VERIFIED |
| P0-06 | CBP county all-industry summary (derived from P0-05) | 38 / 38 | DOWNLOADED_VERIFIED |
| P0-07 | LODES8 OD | 2199 / 2199 | DOWNLOADED_VERIFIED |
| P0-08 | LODES8 WAC | 1100 / 1100 | DOWNLOADED_VERIFIED |
| P0-09 | LODES8 Documentation and release lock | 51 / 51 | DOWNLOADED_VERIFIED |
| P0-10 | 2020 PL94-171 population and housing | 56 / 56 | DOWNLOADED_VERIFIED |
| P0-11 | County population estimates and components | 5 / 5 | DOWNLOADED_VERIFIED |
| P0-12 | 2020 County | 1 / 1 | DOWNLOADED_VERIFIED |
| P0-13 | 2020 Census tract | 52 / 52 | DOWNLOADED_VERIFIED |
| P0-14 | 2020 Census block | 56 / 56 | DOWNLOADED_VERIFIED |
| P0-15 | 2020 Geographic relationship files | 113 / 114 | DOWNLOADED_NEEDS_VALIDATION |
| P0-16 | 2020 County Gazetteer | 1 / 1 | DOWNLOADED_VERIFIED |
| P0-17 | CAGDP1 | 1 / 1 | DOWNLOADED_VERIFIED |
| P0-18 | CAGDP2 | 1 / 1 | DOWNLOADED_VERIFIED |
| P0-19 | CAGDP9 | 1 / 1 | DOWNLOADED_VERIFIED |
| P0-20 | CAINC1 | 1 / 1 | DOWNLOADED_VERIFIED |
| P0-21 | CAINC4 | 1 / 1 | DOWNLOADED_VERIFIED |
| P0-22 | CAEMP25N | 1 / 1 | DOWNLOADED_VERIFIED |
| P0-23 | Regional metadata and documentation | 0 / 0 | DOWNLOADED_VERIFIED |
| P0-24 | Annual single files / annual averages | 78 / 94 | DOWNLOADED_NEEDS_VALIDATION |
| P0-25 | County migration inflow | 33 / 33 | DOWNLOADED_VERIFIED |
| P0-26 | County migration outflow | 33 / 33 | DOWNLOADED_VERIFIED |
| P0-27 | Annual HPMS geospatial releases | 1772 / 1790 | DOWNLOADED_NEEDS_VALIDATION |
| P0-28 | 1947 Interstate Highway Plan | 1 / 1 | DOWNLOADED_VERIFIED |
| P0-29 | Historical exploration routes | 42 / 42 | DOWNLOADED_VERIFIED |
| P0-30 | USDA ERS commuting zones 1980 | 1 / 1 | DOWNLOADED_VERIFIED |
| P0-31 | USDA ERS commuting zones 1990 | 1 / 1 | DOWNLOADED_VERIFIED |
| P0-32 | USDA ERS commuting zones 2000 | 1 / 1 | DOWNLOADED_VERIFIED |
| P0-33 | USDA ERS commuting zones 2020 | 4 / 4 | DOWNLOADED_VERIFIED |
| P0-34 | Long historical CBP county panel | 1 / 1 | DOWNLOADED_VERIFIED |
| P0-35 | Fowler CommutingZones2020 county20 | 1 / 1 | DOWNLOADED_VERIFIED |
| P0-36 | Jeffrey Lin 1947 Interstate plan | 1 / 1 | DOWNLOADED_VERIFIED |
| P0-RAC | LODES8 RAC | 1122 / 1122 | DOWNLOADED_VERIFIED |
| P1-3DEP | 3DEP one arcsecond current elevation tiles | 266 / 1413 | DOWNLOADED_NEEDS_VALIDATION |
| P1-3DHP | 3D Hydrography Program 2025 frozen annual FileGDB release | 1 / 2 | DOWNLOADED_NEEDS_VALIDATION |
| P1-ACS | ACS 5-year selected socioeconomic Detailed Tables, estimates and MOEs | 5031 / 5052 | DOWNLOADED_NEEDS_VALIDATION |
| P1-BFS | Annual Business Applications by County | 1 / 1 | DOWNLOADED_VERIFIED |
| P1-BPS-COUNTY | Annual Building Permits County | 36 / 36 | DOWNLOADED_VERIFIED |
| P1-BPS-PLACE | Annual Building Permits Place | 184 / 184 | DOWNLOADED_VERIFIED |
| P1-FHFA | Annual all-transactions County House Price Index | 1 / 1 | DOWNLOADED_VERIFIED |
| P1-HERD | Higher Education R&D institution public-use data | 28 / 28 | DOWNLOADED_VERIFIED |
| P1-HERD-HISTORICAL | Academic R&D expenditures predecessor public-use data | 38 / 38 | DOWNLOADED_VERIFIED |
| P1-HIST-ATACK-INDUSTRY | Historical manufacturing census samples 1850–1880 | 8 / 8 | DOWNLOADED_VERIFIED |
| P1-HIST-ATACK-RAIL | Atack railroads 1826–1911 revised 2023 | 1 / 1 | DOWNLOADED_VERIFIED |
| P1-HIST-ATACK-WATER | Atack canals and steamboat-navigated rivers | 2 / 2 | DOWNLOADED_VERIFIED |
| P1-HIST-COMMUTING-1990 | 1990 county/MCD commuting OD | 2 / 2 | DOWNLOADED_VERIFIED |
| P1-HIST-COMMUTING-2000 | 2000 county and MCD commuting OD | 4 / 4 | DOWNLOADED_VERIFIED |
| P1-HIST-DECENNIAL-POP | Historical population of states and counties 1790–1990 | 3 / 3 | DOWNLOADED_VERIFIED |
| P1-HIST-DH-NETWORK | Donaldson Hornbeck rail/water network and transportation costs v1 | 0 / 1 | HTTP_ERROR |
| P1-HIST-HR-NETWORK | Hornbeck Rotemberg historical transportation network v2 | 1 / 1 | DOWNLOADED_VERIFIED |
| P1-HIST-HR-REPLICATION | Hornbeck Rotemberg JPE2024 replication: historical Census manufacturing and transportation cost inputs | 355 / 358 | DOWNLOADED_NEEDS_VALIDATION |
| P1-HIST-NBER-POP-CROSSCHECK | NBER transcription of Census historical county population | 1 / 1 | DOWNLOADED_VERIFIED |
| P1-HIST-NHGIS | NHGIS selected historical population urban status and industry tables | 0 / 1 | ACCESS_RESTRICTED |
| P1-HOUSING-UNITS | County annual housing-unit estimates, separately identified vintages | 5 / 5 | DOWNLOADED_VERIFIED |
| P1-IPEDS-C | Completions by CIP and award level | 67 / 67 | DOWNLOADED_VERIFIED |
| P1-IPEDS-EF | Fall and twelve-month enrollment | 184 / 184 | DOWNLOADED_VERIFIED |
| P1-IPEDS-GEOCODE | Public institution address geocoding against Census2020 | 121 / 136 | DOWNLOADED_NEEDS_VALIDATION |
| P1-IPEDS-HD | Institution directory and response flags | 46 / 46 | DOWNLOADED_VERIFIED |
| P1-IPEDS-HR | Human resources staff and faculty | 184 / 184 | DOWNLOADED_VERIFIED |
| P1-IPEDS-IC | Institutional characteristics | 130 / 130 | DOWNLOADED_VERIFIED |
| P1-NLCD-IMP | Annual NLCD Fractional Impervious Surface C1V2 | 10 / 41 | DOWNLOADED_NEEDS_VALIDATION |
| P1-NLCD-LC | Annual NLCD Land Cover C1V2 | 3 / 41 | DOWNLOADED_NEEDS_VALIDATION |
| P1-PADUS | Protected Areas Database full inventory, overlap-removed analysis and summaries | 1 / 3 | DOWNLOADED_NEEDS_VALIDATION |
| P1-PADUS-SERVICE | PAD-US 4.1 complete Protection Mechanism Category official feature-service snapshot | 341 / 1314 | DOWNLOADED_NEEDS_VALIDATION |
| P1-PATENT-APPLICATION | Grant application and filing dates | 1 / 1 | DOWNLOADED_VERIFIED |
| P1-PATENT-ASSIGNEE | Disambiguated assignees and patent-assignee links | 1 / 1 | DOWNLOADED_VERIFIED |
| P1-PATENT-CITATION | US patent citation links | 1 / 1 | DOWNLOADED_VERIFIED |
| P1-PATENT-CPC-CURRENT | CPC classifications at frozen release | 1 / 1 | DOWNLOADED_VERIFIED |
| P1-PATENT-CPC-ISSUE | CPC classifications at grant | 1 / 1 | DOWNLOADED_VERIFIED |
| P1-PATENT-CPC-TITLE | CPC classification titles | 1 / 1 | DOWNLOADED_VERIFIED |
| P1-PATENT-DICT | Granted patent data dictionary archived from PatentsView | 0 / 0 | DOWNLOADED_VERIFIED |
| P1-PATENT-DOC | PatentsView methods, dictionaries and release metadata | 0 / 0 | DOWNLOADED_VERIFIED |
| P1-PATENT-INVENTOR | Disambiguated inventors and patent-inventor links | 1 / 1 | DOWNLOADED_VERIFIED |
| P1-PATENT-LIVE | Current official PatentsView disambiguated grants release | 0 / 3 | API_KEY_REQUIRED |
| P1-PATENT-LOCATION | Disambiguated inventor and assignee locations | 1 / 1 | DOWNLOADED_VERIFIED |
| P1-PATENT-MIRROR-META | Zenodo frozen PatentsView 2024 snapshot metadata | 0 / 0 | DOWNLOADED_VERIFIED |
| P1-PATENT-PATENT | Granted patent metadata | 1 / 1 | DOWNLOADED_VERIFIED |
| P1-QWI | Quarterly Workforce Indicators county and NAICS sector | 87 / 104 | DOWNLOADED_NEEDS_VALIDATION |


## Foundational products

| Product | Rows |
|---|---:|
| `03_processed/county_master_2020.parquet` | 3,234 |
| `03_processed/county_year_economic_master_2001_2023.parquet` | 72,289 |
| `03_processed/lodes_county_od_2002_2022.parquet` | 13,601,384 |
| `03_processed/domain_validation_crosswalk.parquet` | 3,234 |


The economic scaffold contains 3,143 counties and 72,289 county-years. 67,431 rows have all12 required measures. Duplicate county-year keys: 0. Missingness and boundary exceptions remain visible; this is not a claim of a fully comparable balanced economic panel.

QCEW2015 now uses twelve observed monthly employment counts and four disjoint observed quarterly wage/establishment records for02158 and46102. No suppressed/unavailable quarter was filled with zero; native annual rows remain unchanged. See `qa_qcew_2015_transition.json` and [BLS annual formulas](https://www.bls.gov/cew/publications/employment-and-wages-annual-averages/2024/).

LODES: 13601384 directed county OD rows; 43 states in the fixed2002-2022core. All available selected JT00/S000 block files are preserved. Alternative job types and demographic cuts are inventoried and must not be added together.

## P1 products and validation

Acquisition and semantic QA are separate. Each module report is regenerated from its own completed files; current coverage tables take precedence over a stale prose snapshot.

- Housing/ACS/BFS/BPS/FHFA: `07_documentation/P1_HOUSING_ACS_REPORT.md`; `p1_housing_variable_dictionary.csv`, `acs_selected_variable_dictionary.csv`, and module coverage tables.
- Inventor-based patents: `07_documentation/P1_PATENTS_REPORT.md`; nine raw ZIPs plus native Parquet, fractional inventor measures and CPC/citation outputs. Current official credentials and frozen mirror provenance remain distinct.
- IPEDS/HERD and historical data: module reports, source dictionaries, geocoder receipts and exceptions in `00_metadata/` and `07_documentation/`.
- QWI: `qwi_state_release_coverage.csv`, `qwi_state_quarter_coverage.csv`, `qa_qwi.json`; completed files only.
- Modern HPMS: `07_documentation/P0_HPMS_MODERN_REPORT.md`, `hpms_modern_year_status.csv`, native geometry QA and separate long event tables.
- Land: `nlcd_county_year/`, `terrain_tile_county/`, coverage-bearing available aggregates and per-file QA. An available aggregate is explicitly partial until all selected tiles/years are present.

Market-access inputs are in `03_processed/market_access_inputs/`: GDP/employment mass,2020county internal-point nodes and1947planned-highway exposure. The GDP units are dollars, including chained2017dollars for real GDP. Plan distance is metric geometric proximity; it is not a network travel-time matrix. No decay parameter, agglomeration threshold or causal effect is selected by acquisition code.

## What failed? Why did it fail?

`00_metadata/unresolved_or_superseded_downloads.csv` lists exact failed URLs, HTTP status/error and whether the same physical target succeeded through an alternate source. `download_log.csv` preserves retries. A failed alternate URL remains in the audit trail after successful acquisition.

- HTTP403/404 and HTML/JSON error payloads from Census/BLS/legacy catalog endpoints are recorded as errors, never promoted to data.
- ScienceBase migrated some files to manager endpoints that returned HTML; documented catalog downloads or an official distribution endpoint are used where working. Interrupted large transfers retain partials and do not count as success.
- Some official HPMS service listings return application-level404. Historical eleven ZIPs have valid archive CRC but truncated native DBF members; downloading again cannot reconstruct missing source records.
- Connections can terminate early. Range downloads pin strong ETags or provider checksums; ZIP-only fallback pins central-directory/footer hashes plus validates every member CRC. These are distinct validation methods, not an invented official SHA.
- All download queues are stopped for packaging. ACS selected bulk files are complete; QWI/raster/vector coverage remains partial. Their unfinished objects are not unavailable by inference; current explicit status and partial coverage are retained.

## What requires API credentials?

The current official USPTO Open Data Portal PatentsView release requires login/API credentials in this environment. The nine-table2024snapshot actually downloaded is a labeled replication mirror, not proof of current API access. ScienceBase signed-cloud downloads for the original PAD-USFileGDB returned UNAUTHENTICATED; ordinary public catalog streams were also attempted but truncated. A separate USGS-linked public4.1feature service has been partially acquired and frozen with its own metadata and full feature-ID coverage checks; that route does not require credentials. ACS selected bulk files were downloaded without a Census API key; no claim is made that ACS API access is configured. Selected BEA and other P0 bulk files do not require keys. Keys must remain in environment variables.

## What requires restricted access?

NHGIS needs a registered account and selected extract. The DataLumos2018-2024HPMS convenience GIS archive currently redirects to ICPSR login/returns403; it has not been downloaded. See module access evidence. No commercial dataset is being used as an undocumented substitute.

## What is still missing for JUE?

1. Completion and QA of the stopped, incomplete selected P1 queues and remaining official historical/transport sources. The module/status tables are the operative missing list.
2. Research decisions for BEA combined counties and historical boundary changes. FIPS equality alone cannot make historical geography identical to2020.
3. BEA county employment2023 is unpublished after discontinuation. It remains missing; QCEW/CBP are explicitly separate concepts.
4. A defensible treatment of IRS duplicate/conflicting publications and documented methodological breaks.
5. Routable network construction, topology QA and measured network travel times/distances. HPMS event records and geometry are inputs, not a validated travel network.
6. The requested NHGIS extract and some institution/geographic matches remain unresolved. Historical population/urban inputs from the authors archive are already available in native historical geography; this does not imply NHGIS was downloaded or mapped to2020.
7. Domain/anchor persistence and identification analysis. This acquisition task does not assert that either empirical proposition has passed.

## Geography, units and release discipline

**BEA:** CAEMP25N ends2022. Combined/historical counties are not allocated. 2024 is extension-only.

**QCEW:** 2015 code-only renames resolved with four disjoint observed quarters. Historical boundaries and SIC/NAICS changes remain explicit.

**CBP:** Native suppression/noise retained. 1986-2023 industry archives; main summaries2001-2023.

**POPULATION:** Three total-population vintage segments; component vintages retained separately. CT old-county totals recovered exactly from towns, components not imputed.

**LODES:** Frozen LODES8.4 vintage20251202_1657, JT00 and S000. All available selected OD/main+aux, WAC, RAC. 43-state2002-2022 balanced core, not a national balanced panel.

**CZ:** Vintage-specific zone labels. Exact CT town membership; no inferred transfer of planning-region containment to old counties.

**HPMS:** Historical native DBF truncations retained. Modern official GIS and event tables have separate year/version QA; spatial availability does not establish routability.

**EXPLORATION:** Three native invalid geometries and anomalous original period filename retained and flagged.

**PLAN1947:** NBER primary source and Lin replication agree. Four zero-length native features excluded only from analysis copy.

**REPLICATION:** Cross-check/digitization only; original official citation retained. Historical CBP imputation-related fields are not treated as native Census observations.

**GEOGRAPHY:** 2020 fixed geography complete. Historical positive-area intersections are not economic allocation weights.

**BDS:** Native suppression/status and changing classifications retained; no artificial cross-period sector harmonization.

**IRS:** Native specials/suppression and method breaks retained. 2013-14 duplicate pairs and94 conflicting2014-15 paired counts flagged; no summing inflow and outflow editions.

**DECENNIAL:** POP20/HOUSING20 from official TIGER2020 block product, exactly aggregated to tract and county.

**ACS:** Official bulk2009-2024 with estimates and MOE. Overlapping5-year windows; no national balanced claim before full year QA. CT geography varies by release.

**BFS:** County2005-2025. CT planning-region identifiers begin2022 in this publication.

**BPS:** County1990-2025/place1980-2025. Native permit counts retained; explicit geography and state-total reconciliation flags.

**FHFA:** Frozen2026-03-31 county HPI1975-2025. Current CT series is relabeled to planning regions across history. Missing small-county indexes retained.

**HOUSING:** Annual housing-unit estimates retained by official vintage; no seamless-vintage claim.

**QWI:** R2026Q3 pinned with provider uncompressed MD5. State starts vary; private and state/local/private universes remain separate. Selected county/all-industry/sector cut.

**PATENTS:** Current official USPTO ODP access requires credentials. Actual nine-table data are one frozen2024-12-31 Zenodo replication mirror, explicitly labeled. Inventor-location fractional counting; current release not claimed downloaded.

**IPEDS:** Selected final CSV releases and original dictionaries; UNITID tracking. Same-year coordinates/address geocoding only; unresolved institutions retained.

**HERD:** 1972-2024 standard and2012-2024 short-form public-use files. Pre2010 S&E versus later all-R&D concept break; historical FICE is not assumed UNITID.

**HISTORICAL:** Original historical county geography preserved. Atack and author/Dataverse digitizations remain replication provenance; NHGIS needs account/extract.

**NLCD:** Frozen Annual NLCD C1V2,1985-2025 LC/impervious. Only verified ZIPs processed. Pixel-center fixed2020CONUS aggregation; masks/unknowns/coverage separate.

**3DEP:** Selected one-arcsecond tiles intersecting fixed2020counties. Native XML vertical units/datum retained; metric30m slope processing with explicit partial coverage.

**3DHP:** Frozen2025 annual hydrography, not historical yearly exposure. New elevation-derived coverage is not uniform nationwide.

**PADUS:** PAD-US4.1 inventory and overlap-removed analysis are separate; protected categories are not automatically unbuildable land.

## Reproducibility and QA

Follow `README.md` and the module reports. `download.py --module ...` and `--priority P0/P1 --resume` restore registered targets; large-file ranges and provider-specific collectors are documented separately. `restore_locked.py` verifies original hashes and does not silently accept a newer release. All 18,737 successful unique objects have a recorded SHA256: True. The last whole-package rehash audit was 2026-09-19T08:52:07+00:00, covering 5,840 objects; it does not certify files acquired afterward. Those files carry their own download-time hashes and checks.

Required numeric IDs are strings. Raw native geographic identifiers and suppression/status fields are retained. No unsupported interpolation, zero-filling or economic allocation was applied. 2024+records remain separate or carry extension-only flags. GeoParquet preserves CRS; distance/slope calculations use suitable metric projections. Documentation downloads that fail remain explicit failures.
