# Migrate (~TFM_MIG)

`~TFM_MIG` copies **existing values** to new indexes: under another
attribute, year, commodity, timeslice, currency, limit type, other index,
stage or state of the world, optionally rescaling them on the way. It
selects its sources like [`~TFM_UPD`](data-tags.md#tfm_upd): rule-based
filters, applied to the [seed values](files-and-layers.md#seed-values) of
the layer, with `SourceScen` to name the source layer.

Accepted in `BY_Trans`, `SubRES_*_Trans`, SysSettings, trade, regular,
NSV and generated parametric files. The layouts `~TFM_MIG-AT` and
`~TFM_MIG-TS` work as for the other tags ([layouts](data-tags.md#layouts-at-ts-tsl)).

## Source and destination columns

Most index columns come in pairs. The plain column selects the source
values; the column with the suffix `2` gives the destination. Where no
`2` column is given, the index keeps its source value.

| Source (filter) | Destination | Typical use |
| --- | --- | --- |
| `Attribute` | `Attribute2` | write the same numbers under another attribute |
| `Year` | `Year2` | move a base-year value to another year |
| `cset_cn` (`commodity`) | `cset_cn2` (`commodity2`) | move data from one commodity to another |
| `TimeSlice` | `TimeSlice2` | move data between timeslices |
| `Curr` | `Curr2` | convert a currency (with a multiplier) |
| `LimType` | `LimType2` | turn a lower bound into a fixed one, … |
| `Other_Indexes` | `Other_Indexes2` | change a commodity group or curve number |
| `Stage`, `SOW` | `Stage2`, `SOW2` | stochastic stages and states of the world |

These columns filter the source only and have no destination form: the
process filters (`pset_*`), `cset_cd`, `cset_set`, `Region`,
`SourceScen`, and the conditions `attrib_cond`, `val_cond`. **Region and
process cannot be migrated**: a MIG row writes in the same region and for
the same process as its source.

Destination cells take literal values; a comma list writes one copy per
item (`Attribute2 = NCAP_BND,ACT_BND`). Wildcards are not expanded,
except in `cset_cn2`, which is resolved like a commodity filter.

## The value cell

The value cell (`Value`, alias `AllRegions`, or region columns) works as
in UPD: `*0.5` multiplies the source value, `/`, `+`, `-` apply the other
operations, a bare number or `~`-prefixed number replaces it. **Write
`*1` to copy the value unchanged.** A row whose value cell is empty
produces nothing (the sync log says "The value is not specified").

## Examples

**Conditional copy to a later year.** Wherever `STOCK` exceeds 1 for
processes with geothermal, solar-thermal or heat inputs, write the same
value for 2100:

| ~TFM_MIG: attribute=STOCK | | | |
| --- | --- | --- | --- |
| **Year2** | **Val_Cond** | **Value** | **pset_ci** |
| 2100 | >1 | `*1` | `???GEO,???STH,???HET` |

**Rescale and move in one row.** Take `PASTI` of the trade transport
processes, scale it by 0.062, and write it for 2019:

| ~TFM_MIG | | | |
| --- | --- | --- | --- |
| **Attribute** | **pset_pn** | **Year2** | **AllRegions** |
| PASTI | `Trd[_]*` | 2019 | `*0.0620343872322709` |

**Set default interpolation options** (from a SysSettings): migrate every
`ACT_BND~UP` to year `0` with the option 5.

| ~TFM_MIG | | | | |
| --- | --- | --- | --- | --- |
| **LimType** | **Attribute** | **Year2** | **AllRegions** | **pset_pn** |
| UP | ACT_BND | 0 | 5 | `*` |

## When to use MIG

- The same numbers must appear under another attribute, year,
  commodity, currency or limit type.
- A layer rescales a family of existing values.
- The change reads naturally as "wherever X is given, also give Y",
  rather than an enumeration of Y.

For values that do not depend on existing data, use
[`~TFM_INS` / `~TFM_DINS`](data-tags.md). Like UPD, MIG is one of the
slower tags.

!!! warning "MIG and UPD on the same item"

    MIG and UPD tables of one layer run side by side, and neither sees the
    other's output. If both write the same item in one layer, which value
    survives is not defined ([processing order](processing-order.md)).
