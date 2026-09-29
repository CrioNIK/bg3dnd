The Polish localization is missing 109 entries added since the last reviewed translation, and both Durable descriptions still describe maximum healing. This updates Polish to match the current English source on `0f0ab55c10ce531e8a81f66a61a2ce19fb35b21c`.

- Add Dragon Domain, Warrior of the Mystic Arts, the revised Conjurer and Enchanter, Charm Monster and its scroll, the Arcane Eye scroll, Swift Retribution, Speedy Recovery, and Short Resting.
- Update both Durable descriptions to version 3: spend one Hit Point Die as a Bonus Action and regain hit points equal to the roll.
- Preserve the already updated Improved Shillelagh text and both `Przywrócenie honoru` names.
- Change only `Localization/Polish/polish.xml`: 109 added entries and 2 updated entries; 5,353 existing entries remain unchanged.

Terminology follows the official Polish BG3 localization first, verified against saved paired English/Polish game strings by contentuid. Where no game equivalent was found, Polish D&D sources were used: `Zauroczenie potwora` is attested in Polish community spell cards and POLTERGEIST; `Wytrzymały przywołaniec` is confirmed in [Rebel's official Polish PHB errata](https://files.rebel.pl/images/wydawnictwo/zapowiedzi/DnD/PHB_PL_errata_v1-2019.pdf). New feature names without an attested equivalent are editorial translations, not claimed official names. Previously reviewed mod terminology is retained.

Validation:

- 5,464 English and 5,464 Polish entries; no missing, extra, duplicate, or empty entries.
- All contentuids, versions, entry order, embedded tags, placeholders, and numbers in changed entries match the English source; XML and embedded markup parse correctly.
- All 758 groups of repeated English text have consistent Polish translations.
- Independent language and mechanics reviews covered all 111 changed entries; local Polish LanguageTool findings were reviewed.
- `git diff --check` passes; the patch applies in both directions and reconstructs the delivered XML byte-for-byte with Git line-ending conversion disabled.
- Upstream main and the English source were rechecked before publication. No in-game test was performed.

Please retain the existing translation credit: **Polish Translation: TableTop BRAMA community**.
