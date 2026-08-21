# Workbook recognition

## What this is for

Not every Excel file under a model is treated the same. The add-in classifies the **active workbook** using the same folder location and filename patterns as VEDA 2.0. That classification decides which commands are allowed and which tags appear in Add Tag.

Recognition is refreshed when you activate a workbook and before gated commands run.

## Concepts

| Concept | Meaning |
|---------|---------|
| **Type** | Scenario kind from the matched rule (for example RegularScenario, SubRES) |
| **Classified** | Path and filename match a VEDA file-reading rule |
| **Synced** | This file’s stem appears in the model’s synced scenario catalog (the model has been synchronized with this file) |

The Add Tag pane footer shows `Type: …` when the file is classified. Unsynced but classified local work may show a status such as `Local file (not synced)`.

## What each feature allows

| Feature | Classified and synced | Classified, not synced | Not classified |
|---------|----------------------|------------------------|----------------|
| **Cell(s) Info** | Allowed — reads flat-file data from the model | Blocked — file is not synced | Blocked — not a recognized scenario file |
| **Add Tag** | Tag list for **this workbook** | Tag list for that **Type** only (not all tags) | Empty list — file not recognized |
| **Evaluate Row** | Works on tag tables on the sheet | Allowed; status may note not synced | Blocked |
| **Add Column Headers** | Allowed for the current tag | Allowed (local Excel; sync not required) | Blocked |

Add Tag never falls back to “all tags in the catalog.” Tags must match the synced file or the classified type, and must have column definitions in the catalog.

## Practical examples

- A scenario file in the usual folder with a valid name, after a successful sync: full Cell Info and workbook-specific tags.
- A new file with a valid name in the right folder, not yet synced: you can still Add Tag (by type) and Evaluate Row, but Cell Info is blocked until you sync in VEDA.
- Wrong name or wrong folder: not recognized; tag list empty; Cell Info / Evaluate Row / Add Column Headers blocked.
