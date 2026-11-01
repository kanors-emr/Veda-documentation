# Sets and groups

Named groups of processes and commodities let a rule say "all coal power
plants" once and reuse it everywhere.

## ~TFM_COMGRP

Defines **commodity groups**: named groups of commodities, used where a
TIMES attribute needs a commodity group (for example `FLO_SHAR`,
`FLO_FUNC`, a process's primary commodity group) and in commodity
filters. Accepted in `VT_*`, `SubRES_*` and SysSettings (BY and SubRES
since release 4.2.1.0).

| Column | Meaning |
| --- | --- |
| `Name` | The group name. |
| `Description` | Description. |
| `cset_set`, `cset_cn`, `cset_cd` | Which commodities belong to the group ([filters](values-and-filters.md#process-and-commodity-filters); wildcards and exclusions allowed). |
| `AllRegions`, region columns | In which regions the group is defined. |

| ~TFM_COMGRP | | | |
| --- | --- | --- | --- |
| **Name** | **Description** | **AllRegions** | **cset_cn** |
| IIS_Gases | Iron and steel gases | y | INDNGA,INDIIS,INDCOG |
| ELC_gc | Electricity, grid + curtailed | y | ELC,ELCCurt |
| cg_NGAHH2 | Natural gas + hydrogen | y | GASNGA,HH2 |

Veda also has built-in groups for every process: `NRGI` / `NRGO`
(energy inputs / outputs), `MATI` / `MATO`, `DEMI` / `DEMO`, `ENVI` /
`ENVO`, `FINI` / `FINO`.

## Process and commodity sets (~TFM_PSets, ~TFM_CSets)

**User-defined sets** are defined in set-rules workbooks: files in the
model root whose name starts with `Set` (for example
`Sets-DemoModels.xlsx`). Each row defines one set by a filter, and the
set can then be used in any `pset_set` / `cset_set` column of any layer,
and in reports.

| Column (aliases) | Meaning |
| --- | --- |
| `SetName` (`set_name`) | Name of the set. |
| `SetDesc` (`set_desc`) | Description. |
| `pset_set` / `cset_set` | Membership of other sets, including user sets defined above it. |
| `pset_pn`, `pset_pd`, `pset_ci`, `pset_co` / `cset_cn`, `cset_cd` | Name, description and topology filters. |
| `T_Pos_AndOr`, `T_Neg_AndOr`, … / `C_Pos_AndOr`, … | How the filters combine ([details](values-and-filters.md#how-the-columns-combine)). |
| `Comment` | Free text. |

| ~TFM_PSets | | | | |
| --- | --- | --- | --- | --- |
| **pset_set** | **pset_pn** | **pset_ci** | **SetName** | **SetDesc** |
| | IMP*Z | | DUMIMP | Dummy imports |
| ELE | | *COA | ECOA | Coal power plants |
| ELE | | ELCBIO | ELEBIO | Biomass power plants |

| ~TFM_CSets | | | |
| --- | --- | --- | --- |
| **cset_set** | **cset_cn** | **cset_cd** | **SetName** |
| | \*ELC\* | ,-\*PLANTS\* | NRG_ELC |
| NRG,-NRG_ELC,-NRG_GAS | \* | | NRG_MISS |

The second `~TFM_CSets` row collects every energy commodity not already
in `NRG_ELC` or `NRG_GAS`. Sets are re-evaluated at every sync, so they
pick up new processes and commodities that match their rules.

`Set*` workbooks may also hold `~VbeViews` (saved views for browsing) and
metadata tags.
