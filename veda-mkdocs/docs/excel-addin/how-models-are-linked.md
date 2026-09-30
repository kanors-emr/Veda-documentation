# How models are linked

## What this is for

Every add-in request must know **which model** to use. For a workbook **saved under an imported model folder**, the add-in does **not** silently use whatever model is selected in the VEDA 2.0 window. It ties the model to that folder.

Files that are **not** under an imported model (Desktop, unsaved, and similar) use the model open in VEDA instead. See [Files outside the model](files-outside-the-model.md).

## Logic (user view)

1. You open a workbook that lives under a model directory on disk.
2. The add-in looks at that workbook’s folder path.
3. It asks VEDA which **imported** model owns that folder (the same import registry VEDA 2.0 uses when you import a model).
4. If a match is found, that model name is used for all API calls from Excel, and the ribbon shows it (for example `Model: MyModel`).
5. If VEDA answers that the folder is **not imported**, the add-in uses the **model currently open in VEDA 2.0**. Add Tag / Evaluate Row / Add Column Headers can run; Cell Info stays blocked. If that lookup call fails (timeout or error), the command **stops** instead of using the open model.

Opening a scenario file from Model A while VEDA’s UI is focused on Model B still uses **Model A**, as long as Model A is imported and the path matches.

## Why this matters

- Work under an imported model always follows the file’s folder, not the VEDA window’s selected model.
- A copy on the Desktop is not Model A just because the name looks like a scenario file; tags and members come from whichever model is open in VEDA.
- An unsaved workbook has no folder, so it also uses the open VEDA model for tag work.
