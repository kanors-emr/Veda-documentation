# Introduction

The **VEDA Excel Add-In** connects Microsoft Excel to a running **VEDA 2.0** desktop session. From Excel you can explore model data behind cells, work with tag tables (`~` tags), and check which processes and commodities a row’s filters match.

Commands appear in two places and do the same things:

- The **VEDA** tab on the Excel ribbon
- The **VEDA** submenu on the cell right-click menu

![VEDA ribbon tab](../images/excel-addin/excel-addin_ribbon.png)

![VEDA submenu on the cell right-click menu](../images/excel-addin/excel-addin_context-menu.png)

## Prerequisites

- Microsoft Excel 2016 or later
- VEDA Excel Add-In installed and loaded ([Installation](installation.md) — from the **VedaExcelAddOnItemsView** `.vsto` shipped with VEDA 2.0)
- **VEDA 2.0** running on the same machine, with your model imported

You do not use the add-in without VEDA 2.0. Connection details are in [How we connect](how-we-connect.md). How the open workbook is tied to a model is in [How models are linked](how-models-are-linked.md). You can also insert and evaluate tag tables on a file that is **not** under a model folder; see [Files outside the model](files-outside-the-model.md).

## Ribbon layout

The **VEDA** tab is organized into four groups:

1. **Tag model info**
    - **Cell(s) Info** — explore flat-file data for the selection in a pivot view
    - **By Row** / **By Column** — same pivot view for an entire row or column within the current table region
    - **Evaluate Row** — check which processes and commodities match the filter values in the active tag row
2. **Tag tables**
    - **Add Tag** — insert tag tables on the sheet
    - **Add Column Headers** — add missing column headers
3. **About** — who provides the add-in and basic requirements
4. **Session** — connection status (**Connected**), add-in version, and linked model name (**Model: …**)
