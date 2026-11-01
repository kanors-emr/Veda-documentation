# Fill (~TFM_FILL-R)

`~TFM_FILL-R` works in the opposite direction to the other tags: it
**reads existing values out of the model and writes them into a sheet of
the workbook**, where formulas can use them. Typical uses are pulling
calibration-year data or reference projections into a workbook, to build
new values from them (for example in a `~TFM_DINS` table next to it).

Accepted in `BY_Trans`, `SubRES_*_Trans`, SysSettings, trade, regular,
NSV and parametric controller files.

## The tag text

Two settings, separated by `;`:

- `w=<sheet>` — the worksheet the values are written to;
- `hcol=<index>` — the index that goes across the columns of that sheet,
  usually `region` or `year`.

## The rows

Each row is a query: an `Attribute`, process and commodity
[filters](values-and-filters.md#process-and-commodity-filters), optional
`Year`, `TimeSlice` and other indexes, conditions, and **`SourceScen`**
(aliases `scenario`, `scen`): the layer(s) to read from. Values are read
from the layer's [seed values](files-and-layers.md#seed-values). In
`BY_Trans` and `SubRES_*_Trans`, Veda sets `SourceScen` to `BASE`: a
FILL-R table in a repository's `_Trans` file reads the base model, not
the repository. The value
cell (`AllRegions`) can scale what is written; `*1` writes the values
unchanged.

| ~TFM_FILL-R: w=Demandupdate; hcol=region | | | | |
| --- | --- | --- | --- | --- |
| **SourceScen** | **Attribute** | **cset_cn** | **Year** | **AllRegions** |
| BASE | COM_PROJ | `RBn*,RBe*,CB*` | | `*1` |

The result is written from cell A1 of the target sheet: one row per item,
with the columns `scenario`, `attribute`, `process`, `commodity`,
`lim_type`, `time_slice`, `year`, `commodity_group`, `currency`, `stage`,
`sow`, and one column per element of the `hcol` index (here, per region).
Region-group names are accepted as `hcol` headers.

[UPD tables](../upd-tables.md) shows FILL-R and DINS replacing a slow
`~TFM_UPD` table.

## Pitfalls

!!! warning "Always set SourceScen"

    Without `SourceScen`, a FILL-R row reads from whichever earlier layer
    holds the latest value. In one model, a FILL-R table pulled heating
    demands to build user constraints. When it was set up there was only
    one layer with these values. Later an experimental demand layer was
    added — not used in any case — and because of its name the FILL-R
    table started pulling its records instead.

- FILL-R **rewrites the target sheet at every sync**. This slows the sync
  and changes the workbook each time, which is awkward under version
  control. When the source data is stable, consider switching the table
  off (prefix the tag with `Deact`) until the source changes.
- The legacy `~TFM_FILL` tag is [not recommended](not-recommended.md).
