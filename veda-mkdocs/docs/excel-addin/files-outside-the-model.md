# Files outside the model

## What this is for

You can use **Add Tag**, **Evaluate Row**, and **Add Column Headers** on an Excel file that is **not** saved under an imported VEDA model folder (for example a file on the Desktop, in Downloads, or an unsaved `Book1`).

**Cell(s) Info** is not available on those files. It still needs a **synced scenario workbook** under an imported model. See [Workbook recognition](workbook-recognition.md).

Files that already live under an imported model are unchanged. See [How models are linked](how-models-are-linked.md).

## Which model is used

The workbook folder does not map to an imported model, so the add-in uses the **model currently open in VEDA 2.0**. The ribbon **Session** group shows that name on the **Model** line.

That open-model fallback is used only when VEDA **confirms** the folder is not imported (or the workbook has no folder). If the lookup call fails (timeout or error), the command stops instead of using the open model, so a real model file is not treated as a Desktop file.

Start VEDA 2.0 and open a model first. If no model is open, commands that need the catalog ask you to open one.

Process and commodity lists, tag columns, and attributes all come from that open model — not from the random file’s folder.

## Is it a scenario file?

The add-in looks only at the **file name** (the same name patterns VEDA uses, such as `Scen_*` or `SubRES_*`). The folder path is ignored.

| File name | Add Tag list |
|-----------|----------------|
| Looks like a scenario file | Tags for that **file type** only (for example RegularScenario tags) |
| Anything else, including unsaved `Book1` | **All** tags that have column definitions in the catalog |

Tags not offered for new tables are omitted from those lists. Evaluate Row still works on existing `~` tables with those tags.

Under an imported model, a wrong name or wrong folder still shows an **empty** tag list. The “all tags” list is only for files **outside** the imported model tree.

## What each command does

| Command | On a file outside the model |
|---------|-----------------------------|
| **Add Tag** | Inserts a tag table using the list above. Catalog is the open VEDA model. |
| **Evaluate Row** | Allowed on `~` tag tables on the sheet. Matching members come from the open model. |
| **Add Column Headers** | Allowed when the active cell is in a tag table. |
| **Cell(s) Info** | Blocked. Message: needs a synced scenario file under an imported model folder. |

## Practical examples

- `Desktop\Notes.xlsx` with VEDA’s demo model open: Add Tag shows every tag that has columns; you can insert and evaluate tables; Cell Info is blocked.
- `Desktop\Scen_Trial.xlsx` with the same model open: Add Tag shows RegularScenario tags only.
- The same Desktop file with VEDA running but **no** model open: you are asked to open a model.
- `SuppXLS\Scen_Base.xlsx` under an imported model: still classified by **folder + name**, tags for that workbook or type, Cell Info after sync — same as before.
