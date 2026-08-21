# Troubleshooting

Use this page for common problems.

## No VEDA tab / add-in not loaded

| Check | Action |
|-------|--------|
| Add-in installed? | Install from the **VedaExcelAddOnItemsView** `.vsto` in your VEDA 2.0 package ([Installation](installation.md)). Confirm it appears under Excel **File → Options → Add-ins** (COM / disabled items). |
| Disabled by Excel? | Enable it from the Disabled Items list if present, then restart Excel. |
| Excel restarted after install? | Fully quit Excel (all windows) and reopen. |

## Ribbon shows `Model: (none)` or “import this model first”

| Check | Action |
|-------|--------|
| Workbook saved? | Save the file under the model folder tree. Unsaved workbooks have no folder to match. |
| Model imported in VEDA? | In VEDA 2.0, import the model that owns this folder, then retry in Excel. |
| File under the right tree? | Open a workbook that lives inside the imported model’s directories, not a random copy elsewhere. |

The add-in does not silently use the model selected in the VEDA UI. See [How models are linked](how-models-are-linked.md).

## Connection fails / features cannot reach VEDA

| Check | Action |
|-------|--------|
| Is VEDA 2.0 running? | Start VEDA and leave it open. |
| Port file present? | Confirm `%LocalAppData%\VEDA\assistant_api_port.txt` exists while VEDA is running. |
| Restart both? | Close Excel and VEDA, start VEDA first, then Excel. |
| Still failing? | Collect `%LocalAppData%\VEDA\addin.log` ([Logs](logs.md)). |

## File not recognized / empty tag list

| Check | Action |
|-------|--------|
| Correct folder? | Scenario files must sit in the folders VEDA expects for that type (same rules as VEDA 2.0). |
| Correct filename? | Name must match the pattern for that scenario type. |
| Footer / message | Add Tag may show “File not recognized — no tags available.” |

See [Workbook recognition](workbook-recognition.md).

## “File is not synced” (Cell Info blocked)

| Check | Action |
|-------|--------|
| Was the scenario synchronized? | In VEDA 2.0, sync the model (or that scenario) so the file appears in the synced catalog. |
| New local file? | You can still use Add Tag (by type) and Evaluate Row; Cell Info waits until sync. |

## Tag In Tag error

The active cell lies in more than one overlapping tag table region.

| Check | Action |
|-------|--------|
| Overlapping `~` tables? | Move tables apart or clear overlapping blocks so only one tag region contains the cell. |
| Nested tags? | Avoid placing one tag table inside another’s current region. |

## “No tag table contains the active cell”

| Check | Action |
|-------|--------|
| Are you in a tag table? | Click a cell in the data or header area of a `~` tag table. |
| Is there a `~` tag on the sheet? | Insert a tag with [Add Tag](add-tag.md) or open a sheet that already has tags. |
| Header row missing? | The row under `~` must hold headers within the tag’s table region. |

## Stale tags or empty catalog after reconnect

| Check | Action |
|-------|--------|
| VEDA was restarted? | Open Add Tag again so the catalog reloads from the live session. |
| Wrong model folder? | Confirm the ribbon model name matches the workbook’s model. |

Switching the active workbook refreshes classification and the Add Tag footer for that file.

## Unknown attribute when typing in a cell

In Evaluate Row mode, only catalog attribute names are accepted in empty attribute cells. Unknown text is cleared and the status line shows an error. Pick the attribute from the pane list, or type the exact catalog name.
