# Values, wildcards and filters

This page says how the content of a cell is read: names, numbers, lists
and patterns; how the process and commodity filters select what a row
applies to; how attributes are named; and what each index takes when its
cell is empty.

## Cell values

- Leading and trailing spaces, tabs and line breaks are removed from
  every value.
- A cell is **empty** if it holds nothing, only spaces, or an Excel error
  value.
- Numbers are read as Excel stores them, independent of the display
  format or the language settings of the computer.
- Text in a value column that is not a number produces no value, except
  where a tag gives text a meaning (the operators of
  [`~TFM_UPD`](data-tags.md#value-cells-in-tfm_upd) and
  [`~TFM_MIG`](migrate.md), the `IN`/`OUT` of [topology](topology.md),
  the text attributes of [`~TFM_INS-TXT`](data-tags.md#tfm_ins-txt)). In
  `~TFM_INS`, `~TFM_UPD` and `~TFM_MIG`, a row with no number at all is
  reported ("The value is not a number", or "The value is not specified"
  when the value cells are empty). A text cell next to other numbers in
  the same row, and text anywhere in `~TFM_DINS` and `~FI_T`, is dropped
  without a message.
- An explicit `0` is a value, not a blank: it is written to TIMES, where
  it counts as "given as zero". A blank writes nothing.

## Names

- Names of regions, processes, commodities, sets, timeslices, attributes
  and user constraints are **not case-sensitive**: `ELC`, `Elc` and `elc`
  are the same commodity.
- Names and descriptions must not contain the apostrophe or typographic
  quotes (`'`, `‘`, `’`). TIMES data is written for GAMS, where `'`
  delimits text; a stray apostrophe (as in a place name) breaks the run.
- Avoid in names the characters that have a meaning in cells: `,` (list
  separator), `~` (header qualifier), `*`, `?`, `%` (wildcards), and a
  leading `-` (exclusion).
- Process names may have up to 32 characters; keep them to 27, because
  Veda adds suffixes for some generated processes.

## Lists, exclusions and wildcards

These rules apply in every column that the [tag catalog](reference.md)
marks as accepting a list or pattern; all filter columns do.

**Lists.** A cell may hold a comma list. Items are trimmed; empty and
repeated items are ignored. Items are alternatives: a name is selected if
it matches any of them.

**Exclusions.** An item that begins with `-` is an exclusion: names that
match it are removed. `-RW*` and `- RW*` are the same.

**Wildcards.** Each item is matched against the **whole** name, not a
part of it, ignoring case:

| In the cell | Matches |
| --- | --- |
| `*` or `%` | any run of characters, including none |
| `?` or `_` | exactly one character |
| `[c]`, where `c` is one of `_ - * ? # % ^ ! \|` or `\` | the character `c` itself |
| any other character | itself |

| Pattern | Matches | Does not match |
| --- | --- | --- |
| `COAL*` | `COAL`, `COALPLANT` | `OLDCOAL` |
| `*COAL*` | `COAL`, `OLDCOAL`, `COALPLANT` | `COA` |
| `PWR??01` | `PWRAB01` | `PWRA01` |
| `ELC,GAS*` | `ELC`, `GAS`, `GASNAT` | `ELCX` |
| `*,-*OLD*` | every name without `OLD` in it | `PLANT_OLD1` |
| `E[_]WON*` | `E_WON_FAR` | `EXWON_FAR` |

!!! warning "`_` is a wildcard"

    In a filter, `ELC_GAS` matches `ELC_GAS` **and** `ELCXGAS`, and
    `E_*` matches `ELC`. Write `ELC[_]GAS` when only the literal name is
    meant. Most of the time the extra match does not exist in the model,
    so the problem stays hidden until it does. `~TFM_DINS` and
    `~TFM_TOPDINS` read names literally and do not have this issue.

## Process and commodity filters

### The filter columns

Rule-based tables (`~TFM_INS`, `~TFM_UPD`, `~TFM_MIG`, `~TFM_TOPINS`,
`~TFM_FILL-R`, `~TFM_AVA`, `~TFM_COMGRP`, `~UC_T`, the set rules)
select the processes and commodities a row applies to with these
columns:

| Column | Main aliases | Selects |
| --- | --- | --- |
| `pset_pn` | `process`, `techname` | processes by name |
| `pset_pd` | — | processes by description |
| `pset_set` | — | processes in a process set |
| `pset_ci` | — | processes with a matching commodity as an **input** |
| `pset_co` | — | processes with a matching commodity as an **output** |
| `cset_cn` | `commodity`, `commname` | commodities by name |
| `cset_cd` | — | commodities by description |
| `cset_set` | — | commodities in a commodity set |

The forms `pset:pn`, `pset: pn` and so on are accepted aliases of every
filter column.

Process sets are the `Sets` given in [`~FI_Process`](res-templates.md#process-definition-table-fi_process)
(`ELE`, `CHP`, `DMD`, …) and the sets defined in `Set*` workbooks with
[`~TFM_PSets`](sets-and-groups.md#process-and-commodity-sets-tfm_psets-tfm_csets). Commodity sets are the
`Csets` of [`~FI_Comm`](res-templates.md#commodity-definition-table-fi_comm)
(`NRG`, `DEM`, `ENV`, …) and those of
[`~TFM_CSets`](sets-and-groups.md#process-and-commodity-sets-tfm_psets-tfm_csets).

`pset_ci` and `pset_co` use the model's topology: the inputs and outputs
declared in `~FI_T`, trade links and topology tags. They classify
processes by what they do, not by how they are named, and keep working
when new technologies are added.

### How the columns combine

Selection is made per **(process, region)** or **(commodity, region)**:
a process is selected in the regions where it exists and matches.

1. **Within one cell**, items are alternatives (OR).
2. **Across columns**, all conditions must hold (AND) by default:
   `pset_pn` and `pset_pd` and `pset_ci` and `pset_co`, and the set
   column `pset_set`. The same for `cset_cn`, `cset_cd` and `cset_set`.
3. **Exclusions** from any column are collected together (OR) and
   removed from the selection: an item excluded by any column is dropped.
4. A row with exclusions but no positive item starts from **all**
   processes (or commodities) in scope, then removes the exclusions.
5. A row of a tag that needs a process but has no process filter at all
   produces nothing, and the sync log says "The process is required but
   not provided by the user" (the same for commodities).

The defaults in rules 2 and 3 can be changed per row with these columns,
each holding `AND` or `OR`:

| Column (alias) | Changes how … combine |
| --- | --- |
| `t_pos_andor` (`p_pos_andor`) | the positive process conditions `pset_pn`, `pset_pd`, `pset_ci`, `pset_co` |
| `t_pos_andor_forsets` (`p_pos_andor_forsets`) | the result of those with `pset_set` |
| `t_neg_andor` (`p_neg_andor`) | the process exclusions |
| `t_neg_andor_forsets` (`p_neg_andor_forsets`) | the excluded process conditions with the excluded sets |
| `c_pos_andor`, `c_pos_andor_forsets`, `c_neg_andor`, `c_neg_andor_forsets` | the same for commodities |

Example: `pset_pn = *COAL*`, `pset_ci = COA`, `t_pos_andor = OR` selects
processes whose name contains `COAL` **or** that consume `COA`.

### Scope

- In `BY_Trans` and `SubRES_<name>_Trans`, process filters see only the
  parent's processes ([transformation workbooks](files-and-layers.md#transformation-workbooks)).
  Commodity filters always see the whole model.
- Veda's built-in climate-module commodities are never selected by a
  commodity filter. Its built-in commodity groups (`NRGO`, `DEMI`, …) are
  selected only for attributes whose commodity index may be a group.

## Attributes

An attribute is named by a **Veda attribute name** or one of its
aliases. Each maps to one TIMES parameter, and several Veda names may
map to the same TIMES parameter with different fixed indexes or defaults:
`INVCOST` and `NCAP_COST` both write `NCAP_COST`; `EFF`, `EFFICIENCY` and
`VDA_EFF` write efficiencies. Aliases of one attribute are the same
attribute: a later `INVCOST` replaces an earlier `NCAP_COST` for the same
process and year.

The full list, with each attribute's indexes, defaults and the process
and commodity types it applies to, is in Veda under
[Model Info → TIMES Attributes](../model-info.md#times-attributes).

## Index values

Every index value, whether in a cell, in the tag text or in a header,
must be a known element:

| Index | Valid values |
| --- | --- |
| region | regions of [`~BookRegions_Map`](system-settings.md#bookregions_map); region groups of [`~RegionGroup_Map`](system-settings.md#regiongroup_map) (expanded to their regions) |
| year | whole numbers, including `0`; `BOH`, `EOH`; for range attributes a range `y1-y2` |
| timeslice | timeslices of [`~TimeSlices`](system-settings.md#timeslices); `ANNUAL`, `SEASON`, `WEEKLY`, `DAYNITE` |
| limit type | `LO`, `UP`, `FX`, `N` |
| currency | currencies of [`~Currencies`](system-settings.md#currencies) |
| process, commodity | declared names; for commodities also commodity groups of [`~TFM_COMGRP`](sets-and-groups.md#tfm_comgrp) and the built-in groups |

**Year 0** is not a year: it carries the interpolation/extrapolation
option of a time series (for example `5`), or a control value for a few
attributes.

**Year ranges** (`2020-2050`, `BOH-2027`, `2030-EOH`) are used by
attributes whose meaning is a period, such as `PRC_AOFF`, `PRC_NOFF`,
`COM_OFF` and cumulative bounds.

## Defaults for empty indexes

| Index | When the cell is empty |
| --- | --- |
| region | in a `VT_<book>_…` workbook: the regions of that book; elsewhere: all model regions. An `AllRegions` column gives a value to every region of the row that has no column of its own. |
| year | the year of [`~DefaultYear`](system-settings.md#defaultyear), else the start year. Attributes that take a period default to `BOH-EOH`. |
| currency | the first currency in [`~Currencies`](system-settings.md#currencies) |
| limit type, timeslice | the attribute's own default (for example `ACT_BND`: `UP` and `ANNUAL`; `NCAP_CHPR`: `FX`) |
| other indexes | the attribute's own default, if it has one |

An index the attribute does not have is ignored. An index the attribute
requires, with no value and no default, is reported for the row.

## Conditions on existing values

`~TFM_INS`, `~TFM_UPD`, `~TFM_MIG`, `~TFM_FILL-R` and `~UC_T` rows can be
restricted to items that already have data:

- **`attrib_cond`** (`attribute_condition`): the row applies only to items
  that already have this attribute. A leading `-` reverses it (only items
  that do *not* have it). The columns `avc_year`, `avc_timeslice` and
  `avc_limtype` restrict which existing records of that attribute the
  condition looks at (for example only those of year 2020).
- **`val_cond`** (`value_condition`): the row applies only where the
  existing value meets the condition: `>1`, `>=0.5`, `<.001`, `<=10`,
  `=0`, `<>0` (or `!=0`). A bare number means `=`.

Existing values are the [seed values](files-and-layers.md#seed-values)
of the layer, together with what earlier rows of the same layer have
written.
