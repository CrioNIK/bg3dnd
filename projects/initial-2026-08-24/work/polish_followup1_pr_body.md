## Summary

- Restores the missing space in one temporary-hit-point formula: `2k4 +[1]` becomes `2k4 + [1]`.
- This matches the spacing in the English source and renders correctly as `2k4 + 1` after placeholder substitution.
- Changes only `Localization/Polish/polish.xml`.

## Validation

- 5,355/5,355 handles remain present, with all `contentuid` and `version` attributes unchanged.
- Localization, coverage, and spell audits report zero errors.
- The LanguageTool finding for this formula is resolved, with no new findings introduced.
