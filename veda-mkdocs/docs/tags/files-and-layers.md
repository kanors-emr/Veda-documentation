# Files and layers

A Veda model is a folder of workbooks. This page says how Veda decides
what each workbook is, what each kind is for, which data a rule in one
workbook can see, and how a case puts the pieces together. Every tag
page relies on these terms.

## Which workbooks Veda reads

Veda gives each workbook a **file type** from its folder and file name.
Names are matched case-insensitively. A workbook that matches none of
these patterns is not part of the model.

| Folder | File name | File type | Layer |
| --- | --- | --- | --- |
| model root | `SysSettings` | SysSettings | `SysSettings` |
| model root | `VT_<book>_<sector>[_<anything>]` | BY (base year template) | `BASE` |
| model root | `BY_Trans` | BY_Trans | `BASE` |
| `SubRES_TMPL` | `SubRES_<name>` | SubRES | `<name>` |
| `SubRES_TMPL` | `SubRES_<name>_Trans` | SR_Trans | `<name>` (same layer as its SubRES) |
| `SuppXLS\Trades` | `ScenTrade__Trade_Links<anything>` (two underscores) | TradeLinks | trade links |
| `SuppXLS\Trades` | `ScenTrade_<name>` (one underscore) | TradeScen | `<name>` |
| `SuppXLS` | `Scen_<name>` | RegScen (regular) | `<name>` |
| `SuppXLS` | `Scen_NSV_<name>` or `Scen_NSV-<name>` | NoSeedValueScenario | `<name>` |
| `SuppXLS` | `Scen_Par-<name>` | ParScen (parametric controller) | generates layers |
| `SuppXLS\ParScenFiles` | `Scen_Par-<name>_NNNN` | SubParScen (generated child) | one per child |
| `SuppXLS\Demands` | `ScenDem_<name>`, `Dem_Alloc+Series` | DemScen, DemAlloc | demand projection tool |
| model root | `Set<anything>` | setrules | not a layer |
| model root | `ReportDefs-<name>`, `ReportDefs_<name>`, `LMADefs-<name>`, `LMADefs_<name>` | LMADefs | not a layer ([Reports](../reports.md)) |

Notes:

- `Scen_<name>` does not include `Scen_Par-…` or `Scen_NSV…` files;
  `SubRES_<name>` does not include its `_Trans` file; `ScenTrade_<name>`
  does not include the trade-links file.
- In `VT_<book>_<sector>`, **book** is a group of regions declared in
  [`~BookRegions_Map`](system-settings.md#bookregions_map), and
  **sector** is a free label (it is also used to look up default units in
  [`~DefUnits`](system-settings.md#defunits)). A `VT_` file name needs at
  least these three parts; a shorter one is skipped.
- Which tags a workbook may contain depends on its file type. The
  [tag catalog](reference.md) lists, for every tag, the file types where
  it is accepted. A tag in a file type that does not accept it is
  reported in the sync log and ignored.

## Kinds of layer

| Kind | Workbooks | What it is for |
| --- | --- | --- |
| **Settings** | `SysSettings` | The frame of the model: regions, start year, periods, timeslices, currencies, default units. Also a layer that is present in every case, so it may carry modification tables and user constraints that apply everywhere. |
| **Base** | `VT_*`, then `BY_Trans` | The base-year energy system: processes and commodities that exist at the start, with their data (`VT_*`), then rule-based edits to that system (`BY_Trans`). |
| **Technology repository** | `SubRES_<name>`, then `SubRES_<name>_Trans` | New technologies, declared once without regions; the `_Trans` workbook decides in which regions they exist and adds region-specific data. |
| **Trade links** | `ScenTrade__Trade_Links*` | Which regions trade which commodities, and the trade processes that carry them. |
| **Trade** | `ScenTrade_<name>` | Data for trade processes. |
| **Regular** | `Scen_<name>` | Changes to what is declared elsewhere, and user constraints. |
| **No seed value (NSV)** | `Scen_NSV_<name>` | A regular layer that other layers never read from (see [below](#no-seed-value-layers)). |
| **Parametric** | `Scen_Par-<name>` and its children | One controller workbook that generates numbered child layers ([Parametric scenarios](parametric.md)). |

`Set*` workbooks are not layers: they define named process and commodity
sets ([Sets and groups](sets-and-groups.md)) that tables in any layer can
use.

## Who may declare

Only these workbooks may introduce new processes and commodities:

| What is declared | Tags | Allowed in |
| --- | --- | --- |
| processes | `~FI_Process`, `~FI_T` | `VT_*`, `SubRES_*` |
| commodities | `~FI_Comm` | `VT_*`, `SubRES_*`, `SysSettings` |
| commodity groups | `~TFM_COMGRP` | `VT_*`, `SubRES_*`, `SysSettings` |
| trade links and trade processes | `~TradeLinks`, `~TradeLinks_DINS`, `~TradeLinks_c1c2`, `~FI_Process_Trades` | trade-links file |

Every other workbook only changes things. A rule that names a process or
commodity that does not exist produces nothing for that name.

## Transformation workbooks

`BY_Trans` and `SubRES_<name>_Trans` are **transformation workbooks**.
Each has a parent: `BY_Trans` belongs to the `VT_*` files, and
`SubRES_<name>_Trans` to `SubRES_<name>`.

- **Narrower process universe.** A process filter in a transformation
  workbook (`pset_pn`, `pset_set`, `pset_ci`, …) matches only the
  processes its parent declared. A rule "all processes starting with `E`"
  in `SubRES_NewTechs_Trans` means the new technologies of that
  repository, not every such process in the model. Commodity filters are
  not narrowed: there is one set of commodities for the whole model.
- **Seeds from the parent.** Rules that read existing values read the
  base or repository data, not regular layers.
- **Tags.** Transformation workbooks accept the tags of a regular
  scenario file except the user-constraint tags and `~TimeSlices`.
  `SubRES_<name>_Trans` also accepts `~TFM_AVA`, `~TFM_AVA-C` and
  `~ReplicateInRegions`.

The narrowing keeps the work local: a repository's rules are applied
with the repository and are not re-applied each time an unrelated regular
layer changes.

!!! note "Trade workbooks"

    `ScenTrade_<name>` workbooks are meant to work like transformation
    workbooks for trade processes, but in Veda2.0 their process filters
    currently see every process in the model.

## Seed values

Some rules read values that already exist: `~TFM_UPD` multiplies or
shifts them, `~TFM_MIG` copies them to new indexes, `~TFM_FILL-R` writes
them out to a sheet, and the `attrib_cond` / `val_cond` columns test
them. These existing values are called **seed values**. Which layers a
rule may read seeds from is fixed by the **seed order**:

1. First come the declaring and trade layers: `BASE`, every technology
   repository, the trade layers, and demand projections.
2. Then all other layers that provide seeds (regular layers), ranked by
   layer name.

A rule in layer *X* reads seeds from the first group and from the
regular layers whose name sorts **at or before** *X*. `SysSettings` and
parametric layers are exempt from the name ranking: they read from all
seed-providing layers.

When several of those layers hold a value for the same item, the rule
reads one value, chosen in two steps:

1. the layer of the **latest kind**, in this order: `BASE`, repositories,
   demand, trade, regular, parametric, SysSettings. So a value in any
   regular layer beats the same item in `BASE`, whatever the names;
2. among layers of that kind, the one whose name **sorts last**.

**`SourceScen`** overrides this: it restricts the row to the named
layer(s). Use it whenever a rule must read from one particular layer.
Without it, adding a new layer whose name happens to sort in between can
silently change what an existing rule reads (see the warning on
[Fill](fill.md#pitfalls)).

In `BY_Trans` and `SubRES_<name>_Trans`, `SourceScen` is set by Veda:
`~TFM_UPD` and `~TFM_MIG` read their own layer, and `~TFM_FILL-R` reads
`BASE`.

Names are compared after lower-casing, character by character. Digits
sort before letters, so a numeric prefix (`Scen_01_Policy`,
`Scen_02_Prices`) is the reliable way to control the order.

!!! warning "Hyphens and underscores in layer names"

    Veda runs the layers in one order (where `-` is ignored and `_` sorts
    before letters) but compares names for seeds in another (plain
    character codes: `-` before digits, `_` after upper-case letters and
    before lower-case ones). The two can disagree when names differ only
    around `-` or `_`. Until this is aligned, avoid relying on those
    characters to order layers that read seeds from each other.

### Why the order is fixed

Without a fixed order, what a layer sees would depend on which layers
happened to be processed before it: the same workbooks could give
different data on a first import and on a later re-sync. With the
ranking, the data of a layer is determined by its own workbooks and the
layers ranked before it. Re-synchronizing a layer, with nothing changed,
gives the same data; synchronizing only the changed layers gives the same
data as synchronizing everything from scratch.

### No-seed-value layers

A no-seed-value (NSV) layer reads seeds like a regular layer of the same
name, but no other layer reads seeds from it (the one exception is
SysSettings, which reads from all layers). Its data is used only
in the cases that include it. Because nothing depends on it, Veda can
synchronize NSV layers in parallel, and changing one never forces any
other layer to be processed again. Generated parametric children behave
the same way.

Veda lists regular layers that no other workbook reads seeds from as
**NSV candidates**, and can rename them to `Scen_NSV_<name>`. Converting
a layer this way does not change its data.

## Each layer is processed on its own

A layer is built from its own workbooks and the seeds it may read. It
does not depend on which cases will later use it, so it is built once and
reused by every case.

Within one layer, when two rows produce a value for exactly the same item
(same attribute, region, year, process, commodity, timeslice, limit type,
currency and other indexes), **the one applied later wins**. Within a
table that means the row further down; between tag types the order is
given in [Processing order](processing-order.md). Aliases of one attribute
(for example `INVCOST` and `NCAP_COST`) count as the same attribute.

## Cases

A case is an ordered list of layers chosen in the Run Manager; a case
normally starts with `SysSettings` and `BASE`. When two layers in a case
give a value for the same item, the layer **later in the case** wins.

Seed order and case order are independent. Suppose layers `CO2_Tax` and
`HighGas` both exist, and `HighGas` multiplies existing gas prices by
1.2. Because `co2_tax` sorts before `highgas`, `HighGas` reads its seeds
from `CO2_Tax` (among others), and that is fixed when `HighGas` is
synchronized. A case may still list `HighGas` before `CO2_Tax`; then any
value that both layers set directly is taken from `CO2_Tax`, which comes
later in the case.

By default a later layer overrides an earlier one **year by year**: a
later 2030 value replaces the earlier 2030 value but leaves the earlier
2020 and 2050 values in place. The `TS_Filter` column of `~TFM_INS` and
`~TFM_DINS` changes this to whole-series replacement
([details](data-tags.md#ts_filter-replace-a-whole-time-series)).
