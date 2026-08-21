# Installation

## What this is for

Install the VEDA Excel Add-In on a PC that already has Microsoft Excel. The add-in is **shipped with VEDA 2.0** as installation files. Do **not** rely on a website download for the add-in.

## What you need

- Microsoft Excel 2016 or later
- The **VedaExcelAddOnItemsView** install folder from your VEDA 2.0 package (the folder that contains the `.vsto` installer)
- Permission to install software for your Windows user (ClickOnce / VSTO install)

## How to install

1. Fully **quit Excel** (close every Excel window).
2. Open the **VedaExcelAddOnItemsView** folder provided with VEDA 2.0.
3. Run the **`.vsto`** file in that folder (double-click it).
4. Follow the ClickOnce / VSTO install prompts to install **VEDA Excel Add-In**.
5. Start Excel.
6. Confirm the **VEDA** tab appears on the ribbon.

Optional check: open **VEDA → About** and note the version.

## Upgrade

1. Fully quit Excel.
2. Use the **VedaExcelAddOnItemsView** folder from the **newer** VEDA 2.0 package.
3. Run the `.vsto` file again and accept the update prompts.
4. Restart Excel and confirm the **VEDA** tab and About version.

If Windows shows more than one “VEDA Excel Add-In” entry under Programs and Features after upgrades, remove the older unused entries, then install again from the current package’s `.vsto`.

## After install

- Start **VEDA 2.0** before using add-in features that need the model ([How we connect](how-we-connect.md)).
- Open a workbook under an imported model ([How models are linked](how-models-are-linked.md)).

## If the VEDA tab is missing

See [Troubleshooting](troubleshooting.md) — check that the COM add-in is enabled and that Excel was fully restarted after install.
