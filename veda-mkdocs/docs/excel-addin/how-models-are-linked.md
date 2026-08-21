# How models are linked

## What this is for

Every add-in request must know **which model** to use. The add-in does **not** silently use whatever model is selected in the VEDA 2.0 window. It ties the model to the **folder of the active workbook**.

## Logic (user view)

1. You open a workbook that lives under a model directory on disk.
2. The add-in looks at that workbook’s folder path.
3. It asks VEDA which **imported** model owns that folder (the same import registry VEDA 2.0 uses when you import a model).
4. If a match is found, that model name is used for all API calls from Excel, and the ribbon shows it (for example `Model: MyModel`).
5. If no match is found, the ribbon shows `Model: (none)` and you get a message that includes the opened folder (and any detected model folder). You are asked to **import this model first** in VEDA 2.0.

There is no silent fallback to “whatever model is active in VEDA.” If the folder is not linked through import, features that need the model will not proceed until you import (or open a file under an already imported model).

## Why this matters

- Opening a scenario file from Model A while VEDA’s UI is focused on Model B still uses **Model A**, as long as Model A is imported and the path matches.
- An unsaved workbook (no folder yet) cannot resolve a model.
- Copying files outside the imported model tree breaks the link until you put them back or re-import.
