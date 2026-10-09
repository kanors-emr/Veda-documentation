# Installation

## What this is for

Install the VEDA Excel Add-In on a PC that already has Microsoft Excel. The add-in is the **VedaExcelAddIn** package on the same VEDA 2.0 release (`VedaExcelAddIn_<version>.zip`). Install from those extracted files. Excel does not download or update the add-in on its own.

## What you need

- Microsoft Excel 2016 or later
- `VedaExcelAddIn_<version>.zip` from the VEDA 2.0 GitHub release (with VEDA 5.0.0.0 this is `VedaExcelAddIn_1.0.0.20.zip`)
- Permission to install software for your Windows user (ClickOnce / VSTO install)

## How to install

1. Fully **quit Excel** (close every Excel window).
2. Download `VedaExcelAddIn_<version>.zip` from the VEDA 2.0 release and extract it.
3. Run the **`.vsto`** file in that folder (`Veda.ExcelAddIn.vsto`).
4. Follow the ClickOnce / VSTO install prompts to install **VEDA Excel Add-In**.
5. Start Excel.
6. Confirm the **VEDA** tab appears on the ribbon.

Optional check: open **VEDA → About** and note the version.

## Upgrade

1. Fully quit Excel.
2. Uninstall **VEDA Excel Add-In** from Windows **Settings → Apps** (or **Programs and Features**). Remove every existing entry for it.
3. Download `VedaExcelAddIn_<version>.zip` from the **newer** VEDA 2.0 release and extract it.
4. Run `Veda.ExcelAddIn.vsto` and follow the install prompts.
5. Start Excel and confirm the **VEDA** tab and About version.

## After install

- Start **VEDA 2.0** before using add-in features that need the model ([How we connect](how-we-connect.md)).
- Open a workbook under an imported model ([How models are linked](how-models-are-linked.md)).

## If the VEDA tab is missing

See [Troubleshooting](troubleshooting.md) — check that the COM add-in is enabled and that Excel was fully restarted after install.
