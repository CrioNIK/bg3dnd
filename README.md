# BG3 DnD translation preservation — 30 September 2026

Archival snapshot of Ukrainian and Polish translation work from three local project folders. This branch preserves work; it is not a new mod release or a translation update.

- **27 local branch heads** are represented by exact matching GitHub branch refs. See [branches.json](preservation/branches.json) for every original branch name, SHA and preserved branch.
- **24 output files** are available directly under `projects/*/outputs/`, retaining their original filenames and bytes.
- Scripts, terminology sources, translation caches, editorial changes, reviews, validation, publication records and extracted localization resources are preserved.
- Large original `.pak` files are assets of the [archival release](https://github.com/CrioNIK/bg3dnd/releases/tag/preservation-artifacts-2026-09-30). There are **25 unique large assets**; duplicate local files map to the same asset by SHA-256. Original paths are recorded in the manifest.
- 1516 selected source files, 1001 unique contents, 4,088,777,102 logical bytes. Files are never replaced by Git LFS pointer stubs.

## Finding and restoring files

`preservation/files.json.gz` is a gzip-compressed UTF-8 JSON manifest. Each record gives the source project and relative path, byte size, SHA-256, and either a Git path/blob SHA or a GitHub Release asset URL. Files under `resources/` are stored once by content hash. To reconstruct a source path, copy its referenced Git file or download its release asset, then check the SHA-256 and size. The manifest contains no absolute local paths.

The source project keys are `initial-2026-08-24`, `polish-2026-09-12`, and `ukrainian-2026-09-12`. September XML and patches are the published translation updates. Earlier companion and integrated `.pak` files are historical artifacts; their old installation notes are retained as historical records.

## Exact output files

- [initial-2026-08-24/outputs/D&D_5.5e_Beyond_Ukrainian.pak](projects/initial-2026-08-24/outputs/D&D_5.5e_Beyond_Ukrainian.pak) — 389,173 bytes; SHA-256 `4fd5af3f5bc840eeb8206d24d20ce5217d03c42690f45d35405ac2d4c5fddcb5`
- [initial-2026-08-24/outputs/D&D_5.5e_Beyond_Ukrainian.pre_editorial_20260825.pak](projects/initial-2026-08-24/outputs/D&D_5.5e_Beyond_Ukrainian.pre_editorial_20260825.pak) — 554,102 bytes; SHA-256 `122fa1ce31bec71540e06e483ac7d3033c15cb29e86fec56c9bfb99562800588`
- [initial-2026-08-24/outputs/D&D_5.5e_Beyond_Ukrainian_Audit.txt](projects/initial-2026-08-24/outputs/D&D_5.5e_Beyond_Ukrainian_Audit.txt) — 1,504 bytes; SHA-256 `b4591494dffdfc3adef694e2f55b299b853d763b6f9e702dd941512ac77eb768`
- [initial-2026-08-24/outputs/DnD2024_Ukrainian.pak](projects/initial-2026-08-24/outputs/DnD2024_Ukrainian.pak) — 389,173 bytes; SHA-256 `4fd5af3f5bc840eeb8206d24d20ce5217d03c42690f45d35405ac2d4c5fddcb5`
- [initial-2026-08-24/outputs/DnD2024_Ukrainian.xml](projects/initial-2026-08-24/outputs/DnD2024_Ukrainian.xml) — 1,301,066 bytes; SHA-256 `aa8da075f7dbc19f3b93f3eff8f30897662599a752b1b97d17123b4a3ab57930`
- [initial-2026-08-24/outputs/DnD2024_Ukrainian.zip](projects/initial-2026-08-24/outputs/DnD2024_Ukrainian.zip) — 292,808 bytes; SHA-256 `619bef2af13e7587acd7fe3af225722a1337cea76260c157f6e875201ac9e884`
- [initial-2026-08-24/outputs/installed_DnD2024_Ukrainian_pre_editorial_20260825.pak](projects/initial-2026-08-24/outputs/installed_DnD2024_Ukrainian_pre_editorial_20260825.pak) — 554,102 bytes; SHA-256 `122fa1ce31bec71540e06e483ac7d3033c15cb29e86fec56c9bfb99562800588`
- [initial-2026-08-24/outputs/README_DnD2024_Ukrainian.txt](projects/initial-2026-08-24/outputs/README_DnD2024_Ukrainian.txt) — 1,902 bytes; SHA-256 `e5c458ceb0f5c67276823d84252388ff84f6719fac4ecba336965ed950dbc50d`
- [polish-2026-09-12/outputs/polish-update.patch](projects/polish-2026-09-12/outputs/polish-update.patch) — 28,637 bytes; SHA-256 `90b40970c864393318d8e64b19540c2691da56b04908588d0f1832714de8f5c6`
- [polish-2026-09-12/outputs/polish.xml](projects/polish-2026-09-12/outputs/polish.xml) — 1,160,430 bytes; SHA-256 `5cbd3b47f7de56d5f84321fe0897925d961f98b357da67dd120dfbdc1496d193`
- [polish-2026-09-12/outputs/publication.json](projects/polish-2026-09-12/outputs/publication.json) — 2,150 bytes; SHA-256 `22b6fc110c4fb7b54a9fad3c057619fd581f634e7d0edc2b3f1074e54a5dd4d3`
- [polish-2026-09-12/outputs/report.md](projects/polish-2026-09-12/outputs/report.md) — 8,895 bytes; SHA-256 `0b30435d0b9c99664968934872e9ad0fcd457c7178a5647de8c24fb46d3b343d`
- [polish-2026-09-12/outputs/review.tsv](projects/polish-2026-09-12/outputs/review.tsv) — 36,463 bytes; SHA-256 `3806c6283f13b8ec5efd4152c68d4676e577c56dc2f46f0e8bea0c444090c16a`
- [polish-2026-09-12/outputs/terminology-sources.md](projects/polish-2026-09-12/outputs/terminology-sources.md) — 10,980 bytes; SHA-256 `02279573bb09a301ec6e3592ba8c800ac4412108c6fbda2d8a927ba605b9b118`
- [polish-2026-09-12/outputs/validation.json](projects/polish-2026-09-12/outputs/validation.json) — 2,081 bytes; SHA-256 `026d71f1d56a4769145edef7995c93d1a2d30043dfb0d33017446db239ec70cc`
- [ukrainian-2026-09-12/outputs/changes.tsv](projects/ukrainian-2026-09-12/outputs/changes.tsv) — 49,659 bytes; SHA-256 `bbcc2e01b2574e0accd7f5eef4b862eaee3e4f5b5e3f80e2cf1999b12dca3bbf`
- [ukrainian-2026-09-12/outputs/publication.json](projects/ukrainian-2026-09-12/outputs/publication.json) — 1,514 bytes; SHA-256 `2d9c1a8355b87b834bf3375a180970150cc9a920c01c486c33ef9d50b67d0a11`
- [ukrainian-2026-09-12/outputs/release-audit-2026-09-23.json](projects/ukrainian-2026-09-12/outputs/release-audit-2026-09-23.json) — 3,283 bytes; SHA-256 `a8d1fbe6dad4cf98bdec72af2e69f0351afbdc49731f0c94788a50ffe535b94b`
- [ukrainian-2026-09-12/outputs/release-audit-2026-09-23.md](projects/ukrainian-2026-09-12/outputs/release-audit-2026-09-23.md) — 5,027 bytes; SHA-256 `58d3540b0127c6f724997efffe88f51caefcc302a2cec678934483d5466a24b5`
- [ukrainian-2026-09-12/outputs/report.md](projects/ukrainian-2026-09-12/outputs/report.md) — 8,903 bytes; SHA-256 `74cda3ec96820c9ee786e59cda59bd22535d6e4313543f3c7102a37b620762b3`
- [ukrainian-2026-09-12/outputs/terminology-sources.md](projects/ukrainian-2026-09-12/outputs/terminology-sources.md) — 14,709 bytes; SHA-256 `9dd30cfa921f0f4d1897314698eb1d339a1159bcee576665b7b20c0f04370cfe`
- [ukrainian-2026-09-12/outputs/ukrainian.patch](projects/ukrainian-2026-09-12/outputs/ukrainian.patch) — 43,260 bytes; SHA-256 `6ba0153399cedf82dec3b404c6bd6e10158ca93fd8cd02720f7e2a872d1f96c7`
- [ukrainian-2026-09-12/outputs/ukrainian.xml](projects/ukrainian-2026-09-12/outputs/ukrainian.xml) — 1,581,386 bytes; SHA-256 `59cef3006a9ee17ee3485f38922292ac06c64ccd2644eb5e505a3a7506eeef4c`
- [ukrainian-2026-09-12/outputs/validation.json](projects/ukrainian-2026-09-12/outputs/validation.json) — 4,865 bytes; SHA-256 `df10ddaee0d197fcee4b3325576caf6088b16f457357dabaff7e9163dfa48b8d`

## Exclusions and scope

Re-downloadable runtimes, model caches and tools (.NET, ExportTool, LanguageTool), installers, Python caches, process logs/PIDs, credentials/environment files, and local game profile state are not publication materials. Bulk repeated full game/mod extractions are not copied again: their full built PAKs and the source repository are preserved, while extracted localization files and module metadata remain independently available. See `preservation/exclusions.json.gz` for the complete excluded-file list and `preservation/exclusions.json` for its summary.

No local source files were deleted, no existing branch was overwritten, no force push was used, and no changes were pushed to Yoonmoonsik/bg3dnd. Private messages, application sessions and credentials are not part of this archive.
