# Add Process Set and Add Commodity Set

## What it is for

**Add Process Set** and **Add Commodity Set** list TIMES and user sets for the model open in VEDA and append the ones you choose to the active tag row.

| Command | Writes to |
|---------|-----------|
| **Add Process Set** | `pset_set` |
| **Add Commodity Set** | `cset_set` |

This is a local sheet edit. Sync is **not** required. The active cell must be in a tag table whose tag defines that column. Under an imported model the workbook must be **classified**. Files outside the model folder are also allowed; see [Files outside the model](files-outside-the-model.md).

## How to use

1. Connect to VEDA and place the active cell on a data row in a tag table ([Add Tag](add-tag.md)).
2. Choose **Add Process Set** or **Add Commodity Set** from the **VEDA** ribbon or right-click menu.
3. In the dialog, filter if needed, then check sets in the TIMES and user lists.
4. Confirm to append the selected names to that column on the row.

Names already in the cell stay. A name already present is not added again. If the column header is not on the sheet yet but the tag defines it, the header is added before the names are written.

If the file is inside a model folder and not recognized, the tag has no such column, or the active cell is not in a tag table, the command is blocked with a clear message. If VEDA is not connected, or the model has no sets of that kind, the dialog does not open.
