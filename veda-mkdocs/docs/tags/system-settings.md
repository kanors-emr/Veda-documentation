# System settings

These tags live in `SysSettings.xlsx` and define the frame of the model:
time, regions, timeslices, currencies and units. Except for `~TimeSlices`,
they are accepted only in SysSettings.

## Time

### ~StartYear

Single-value tag: the cell below holds the first year of the model (the
base year).

### ~TimePeriods

Period lengths, by named definition. Each column is one definition; its
header is the definition's name, and the cells below are the lengths of
successive periods, starting from `~StartYear`.

| ~TimePeriods | | |
| --- | --- | --- |
| **Pdef-1** | **Pdef-5** | **Pdef-11** |
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| | 5 | 5 |
| | 5 | 5 |

Veda computes the milestone year of each period as its middle year. Several
definitions can coexist; the Run Manager chooses one per case. A column
headed `<- ending year` is a note and is ignored.

### ~ActivePDef

Single-value tag: the name of the period definition (a column of
`~TimePeriods` or `~MileStoneYears`) that is active by default.

### ~MileStoneYears

An alternative to `~TimePeriods`: each column is a definition that lists
the milestone years directly. TIMES derives the period boundaries from
them. A row whose `type` cell starts with `e` gives the end year of the
horizon instead of a milestone year.

### ~EndYear

Single-value tag: the last year of the model horizon.

### ~DefaultYear

Single-value tag: the year given to any value whose year is left empty.
Without it, the start year is used.

## Regions

### ~BookRegions_Map

Declares the model's regions and groups them into **books**. Columns
`BookName` and `Region`; an empty `BookName` cell carries down the book
above it.

| ~BookRegions_Map | |
| --- | --- |
| **BookName** | **Region** |
| ElecReg | NSW |
| | VIC |
| DemReg | NSW_N |
| | NSW_S |

A book is the region scope of a set of base-year templates: a
`VT_ElecReg_ELC_v01.xlsx` workbook describes the regions of book
`ElecReg`, and every declaration in it that has no region applies to all
of them. This serves the principle that structures common to several
regions are declared once.

- A book with no `VT_<book>_…` workbook makes its regions external
  (exogenous) regions.
- A region listed twice in one table keeps its last row.
- The external regions `IMPEXP` and `MINRNW` are always added.

### ~RegionGroup_Map

Defines **region groups**: names that stand for several regions. Columns
`RegionGroup` (aliases `region_group`, `reg_group`) and `Region`. A region
may belong to several groups.

| ~RegionGroup_Map | |
| --- | --- |
| **RegionGroup** | **Region** |
| weo_EU | France |
| weo_EU | Germany |
| Reg_Dev | France |
| Reg_Dev | Germany |
| Reg_Dev | USA |

A group name can be used wherever a region is expected: in a `region`
column (alone or in a comma list), as a value-column header, and in tag
text (`~TFM_INS-TS: Region=Reg_Dev`). Veda replaces it by its regions,
and the result is the same as writing the regions out.

So data available for external classifications (WEO regions, steel
regions, development status) can be used as it is, one row per group.
To give one region a different value, add a row for that region **below**
the group row: as with any two rows in a layer, the
[later row wins](files-and-layers.md#each-layer-is-processed-on-its-own).

!!! tip

    Use a prefix per grouping scheme (`weo_`, `Reg_`) and do not mix
    schemes in one table: rows of two schemes that cover the same region
    overwrite each other, and the result then depends on row order.

`~RegionGroup_Map` is also used in report definitions, and region groups
are accepted in the column headers of [`~TFM_FILL-R`](fill.md) data sheets
and in [`~UC_T`](user-constraints.md) and [`~UC_Sets`](user-constraints.md#uc_sets).
[`~TFM_TOPDINS`](topology.md#tfm_topdins) is the exception: it does not
expand region groups.

## Timeslices

### ~TimeSlices

The timeslice tree. Columns `Season`, `Weekly` and `DayNite`, each
listing the elements of that level. Every element of a level is combined
with every element of the level above; a timeslice's name is the
concatenation of its parts (`S` + `D` → `SD`).

| ~TimeSlices | | |
| --- | --- | --- |
| **Season** | **Weekly** | **DayNite** |
| S | | D |
| W | | N |

This gives the seasons `S` and `W` and the timeslices `SD`, `SN`, `WD`,
`WN`. Leave a level's column empty to skip that level.

`~TimeSlices` is also accepted in regular scenario files and generated
parametric files, so a layer can change the temporal resolution. The tag
text may list the regions the tree applies to; otherwise it applies to all
regions. These region names must be written exactly as declared —
matching is case-sensitive, and region groups are not accepted here. The share of the year of each timeslice is a normal attribute,
`YRFR`, given with `~TFM_INS` or `~TFM_DINS`.

## Currencies and units

### ~Currencies

The currencies used in the model, in a `Currency` column. **The first one
is the model's default currency**: every cost without an explicit
currency is read in it
([always put the currency on cost tables](reading-tables.md#tag-text)).

### ~DefUnits

Default units of process activity, process capacity and commodities, by
sector. Rows `Process_ActUnit`, `Process_CapUnit`, `Commodity_Unit` in the
`Option` column; one column per sector, matched to the sector part of the
`VT_<book>_<sector>` file name.

| ~DefUnits | | | |
| --- | --- | --- | --- |
| **Option** | **ELC** | **IND** | **TRA** |
| Process_ActUnit | PJ | PJ | kPk |
| Process_CapUnit | GW | GW | 000_Units |
| Commodity_Unit | PJ | PJ | kPk |

A unit cell left empty in [`~FI_Process`](res-templates.md#process-definition-table-fi_process)
or [`~FI_Comm`](res-templates.md#commodity-definition-table-fi_comm) takes
the default of its sector.

### ~UnitConversion

Conversion factors between units, used when browsing results and in
reports: columns `from_unit`, `to_unit`, `multiplier`.

## Other settings tags

### ~NOpCol

"No-operation columns". Header names listed in the `name` column are
ignored in every table of the model, and the warnings for them are
suppressed. A name is still read in a tag where it is a known column
([details](reading-tables.md#columns-ignored-for-the-whole-model)). Useful
for annotation columns (`source`, `notes`) and for switching columns off
by formula in [parametric files](parametric.md).

### ~ParentRegions_Map

Maps sub-regions to parent regions for reporting: columns `parent_region`
and `sub_region` (a comma list is allowed). Used by `~TS_Ratios` in
[report definitions](../reports.md).

### ~MD_Dimensions

The metadata fields captured by the `~MD-*` tags
([Metadata](metadata.md)).

## Modification tables in SysSettings

SysSettings is a layer present in every case. Besides the settings tags,
it accepts `~FI_Comm`, `~TFM_COMGRP`, `~TFM_INS-TXT`, the insert, update
and migrate tags, `~TFM_FILL-R`, and the user-constraint tags. It is
processed **last**, after all other layers, so rules placed here can act
on everything. Typical uses: model-wide constants (`G_DYEAR`, `Discount`,
`YRFR`), default interpolation options (a `~TFM_MIG` or `~TFM_INS` row
writing year `0`), and commodity groups.
