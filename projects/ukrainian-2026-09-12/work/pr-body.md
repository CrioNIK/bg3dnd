Updates the Ukrainian localization to match the current English source on main (`0f0ab55c10ce531e8a81f66a61a2ce19fb35b21c`): 109 missing entries translated and 4 outdated entries corrected. Only `Localization/Ukrainian/ukrainian.xml` changes.

Adds Dragon Domain, Warrior of the Mystic Arts, the Conjurer and Enchanter reworks, Charm Monster and its scroll, the Arcane Eye scroll, Swift Retribution, Speedy Recovery, and Short Resting. Both Durable descriptions now use version 3 and correctly describe spending one Hit Point Die as a Bonus Action to heal the rolled amount. Both outdated Reassert Honor titles now read “Відновлення честі”. The existing Improved Shillelagh correction is preserved.

Terminology was checked against English/Ukrainian localization packages extracted from the installed BG3 game, with Ukrainian D&D community terminology used where appropriate. New feature names use consistent Ukrainian wording; existing mod terms such as “очки зосередження” are preserved. The new descriptions follow the current English mechanics, including all timing, resource, and targeting restrictions. A separate language review and independent mechanics review were completed.

Validation:
- All 5,464 English IDs are present in the same order; no missing, extra, duplicate, or empty entries, and all versions match.
- Inline tags, status links, placeholders, numbers, and repeated translations checked; all 5,351 unaffected entries preserved.
- XML → LOCA → XML round-trip with Divine 1.20.4 preserves every ID, version, text, and record order.
- `git diff --check` passes. Upstream main and the English source were rechecked before submission and remain unchanged.

Validation was performed offline; no in-game playtest was performed.
