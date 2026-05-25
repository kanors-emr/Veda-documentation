# Sets and groups

## To create sets

The following tags enable creation of named groups of processes and
commodities.

### ~TFM_COMGRP

Defines named commodity groups that can be referenced anywhere a
commodity filter is accepted. Each row binds a group name to a
membership rule built from the standard commodity filter columns.

Real example from `SysSettings.xlsx :: CommGrp`:

| **~TFM_COMGRP** | **Name** | **Description** | **AllRegions** | **Cset_CN** |
| --- | --- | --- | --- | --- |
| | IIS_Gases | IIS CommGrp for gases | y | INDNGA, INDIIS, INDCOG, INCOP |
| | ELC_gc | Electricity - grid + curtailed | y | ELC,ELCCurt |
| | cg_NGAHH2 | Nat gas + Hydrogen - primary | y | GASNGA,HH2 |
| | cg_NAPBIO | Naphtha + biofuels - primary | y | OILNAP,BIOGSL,BIODST |

The columns are `Name`, `Description`, `AllRegions` (set to `y` when the
group is the same across all regions), and the standard commodity
filter columns (`Cset_Set`, `Cset_CN`, `Cset_CD`). Wildcards and
exclusion patterns are supported in the filter columns.

Since **4.2.1.0** (Oct 2025), `~TFM_COMGRP` is also accepted in BY and
SubRES files in addition to SysSettings.

### ~TFM_PSets

Defines named *process sets*: a rule-driven shortcut for the set
membership filter `pset_set`. Each row binds a set name to a filter
expression using the standard process filter columns (`pset_pn`,
`pset_pd`, `pset_ci`, `pset_co`, with wildcards and
`t_{pos,neg}_andor[_forsets]` connectors).

Useful when the same multi-clause process filter is reused across many
TFM rows or report definitions — define it once as a set, then reference
the set name afterwards.

### ~TFM_CSets

The commodity-set analogue of `~TFM_PSets`. Uses the commodity filter
columns to define named commodity sets that can then be referenced
wherever a `cset_set` is accepted.

