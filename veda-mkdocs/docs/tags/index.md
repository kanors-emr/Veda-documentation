# Veda Tag Language (VedaTL)

A Veda model is a folder of Excel workbooks. Everything Veda reads from
those workbooks is written as **tagged tables**: a cell that starts with
`~` (the *tag*) followed by a block of cells that the tag gives meaning
to. The tags, the rules for laying out their tables, and the rules for how
their rows are applied together form the **Veda Tag Language**, VedaTL.

The language began in 1998 with the Flexible Import table, `~FI_T`, in
Excel VBA, when Veda served MARKAL. It grew through VEDA_FE (from 2001)
and Veda2.0 (from 2019). This section is its reference: what each tag
means, and the general rules every tag follows.

!!! note "Status of this reference"

    This reference describes the language as Veda2.0 implements it
    (version 5.0, November 2026). It is the working basis for a formal,
    openly published VedaTL specification. Where Veda's current behaviour
    is known to be unintended, the text says so.

## Why a tag language

Two principles, present since the first version, explain most of the
design ([philosophy](../introduction.md#philosophy-and-core-principles)):

1. **Data as the analyst keeps it.** Tables can be laid out the way the
   source data is laid out: years, regions, attributes or timeslices
   across the columns, filters down the rows, defaults in the tag itself.
   No conversion to a fixed CSV layout is needed.
2. **Rules as data.** Values can be inserted, updated and migrated by
   rule: "every coal plant", "every process that outputs `ELC`",
   "multiply the existing value by 1.1". The rules sit in the workbooks,
   next to the data, and are applied every time the model is
   synchronized.

## How to read this section

Start with the four general pages. Each tag page assumes them.

| Page | What it settles |
| --- | --- |
| [Files and layers](files-and-layers.md) | Which workbooks Veda reads, what each kind is for, which data a rule can see (seed values), and how a case puts layers together |
| [How a table is read](reading-tables.md) | Where a table starts and ends, the tag text, column headers and their aliases, comment rows and columns, values carried down the rows, wide layouts |
| [Values, wildcards and filters](values-and-filters.md) | Names, lists, exclusions, wildcards, the `pset_*` / `cset_*` filters and how they combine, attribute names, and the default for every empty index |
| [Processing order](processing-order.md) | In which order files and tags are applied, and which value wins when two rows set the same thing |

Then the tags, by family:

| Page | Tags |
| --- | --- |
| [System settings](system-settings.md) | `~StartYear`, `~ActivePDef`, `~TimePeriods`, `~MileStoneYears`, `~EndYear`, `~DefaultYear`, `~BookRegions_Map`, `~RegionGroup_Map`, `~TimeSlices`, `~Currencies`, `~DefUnits`, `~NOpCol`, `~UnitConversion`, `~ParentRegions_Map` |
| [Declarations (RES templates)](res-templates.md) | `~FI_Comm`, `~FI_Process`, `~FI_T` |
| [Insert and update](data-tags.md) | `~TFM_DINS`, `~TFM_INS`, `~TFM_UPD` and their `-AT`, `-TS`, `-TSL` layouts; `~TFM_INS-TXT` |
| [Migrate](migrate.md) | `~TFM_MIG`, `~TFM_MIG-AT`, `~TFM_MIG-TS` |
| [Topology](topology.md) | `~TFM_TOPINS`, `~TFM_TOPINS-A`, `~TFM_TOPDINS` |
| [Fill](fill.md) | `~TFM_FILL-R` |
| [SubRES availability](availability.md) | `~TFM_AVA`, `~TFM_AVA-C`, `~ReplicateInRegions` |
| [Trade](trade.md) | `~TradeLinks`, `~TradeLinks_DINS`, `~TradeLinks_c1c2`, `~TradeLinks_Desc`, `~FI_Process_Trades`, `~commodity_geo` |
| [User constraints](user-constraints.md) | `~UC_T`, `~UC_Sets`, `~UC_GENT` |
| [Sets and groups](sets-and-groups.md) | `~TFM_COMGRP`, `~TFM_PSets`, `~TFM_CSets` |
| [Parametric scenarios](parametric.md) | `~InputCell` |
| [Metadata](metadata.md) | `~MD-*`, `~MD_Dimensions` |
| [Not recommended](not-recommended.md) | Tags still read for old models, and tags that no longer do anything |
| [Tag catalog](reference.md) | Every tag: where it is allowed, its columns, their aliases (generated from Veda's own catalog) |

The tags of report-definition files (`ReportDefs-*` / `LMADefs-*`) are
described with [Reports](../reports.md).

## Words used in this section

**Workbook** — one Excel file in the model folder.

**Layer** — a named body of model data that is switched on or off as a
unit when a run is put together. Veda's screens call it a *scenario*. In
this reference, *scenario* keeps its modelling sense (a storyline), and
the unit of data is called a layer. A layer usually comes from one
workbook; `BASE` comes from all `VT_*` workbooks plus `BY_Trans`.

**Case** — an ordered list of layers that makes one TIMES run.

**Declare** — introduce a new process or commodity into the model. Only
some workbooks may declare.

**Seed value** — a value that already exists in the model when a rule is
applied, and that the rule reads (for example, the value that a relative
update multiplies).

**Attribute** — a Veda parameter name such as `INVCOST` or `ACT_BND`.
Each maps to a TIMES parameter, sometimes with fixed indexes or defaults.
