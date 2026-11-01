# User constraints

User constraints are TIMES equations written by the modeler: a
left-hand side made of terms on capacity, activity, flows, new capacity
and so on, compared with a right-hand side. Veda writes them with two
tags: `~UC_T` gives the terms and right-hand sides; `~UC_Sets` says whether
each constraint is written per region or summed over regions.

Both are accepted in SysSettings, regular, NSV and generated parametric
files, not in templates, transformation or trade files. `~UC_T` tables are
processed after all regular layers, so that parametric layers can modify
them ([processing order](processing-order.md)).

## ~UC_T

### Columns

| Column (aliases) | Meaning |
| --- | --- |
| `UC_N` (`user_constraint`) | Name of the constraint. **Carries down**; a row without one writes nothing. |
| `UC_Desc` (`description`) | Description of the constraint. |
| process and commodity filters | Which processes and commodities enter the constraint ([filters](values-and-filters.md#process-and-commodity-filters)). |
| `Attribute` (`prmtr`, `parameter`) | The UC attribute of the row's values: `UC_ACT`, `UC_CAP`, `UC_NCAP`, `UC_FLO`, `UC_COMPRD`, `UC_COMCON`, `UC_COMNET`, `UC_RHSRT`, … |
| `Side` | `LHS` or `RHS`, for terms on the right-hand side. |
| `UC_ATTR` | Dynamic constraint options: `"<group>, <option>"`, e.g. `CAP, GROWTH`, `NCAP, BUILDUP`; the header `UC_ATTR~RHS` puts it on the right-hand side. |
| `Region`, `Year`, `TimeSlice`, `LimType`, `Curr`, `Other_Indexes` | Indexes, as elsewhere. |
| `Top_Check` | With a process and a commodity, the pair must be connected in the topology: `a` (default, either direction), `i` (as input), `o` (as output); `n` turns the check off. |
| conditions | `attrib_cond`, `val_cond` and the `avc_*` columns ([conditions](values-and-filters.md#conditions-on-existing-values)). |
| value columns | Headers made of `~`-separated tokens ([value columns](reading-tables.md#value-columns-and-header-qualifiers)): `UC_CAP`, `UC_FLO~ELC`, `UC_RHSRT~2030`, `UC_RHSRT~0` (interpolation option), or region names. |

When a value-column header could be read in more than one way, its tokens
are assigned in this order: attribute, currency, limit type, region,
side, timeslice, year, commodity.

The **tag text** gives table-wide tokens, typically the right-hand-side
attribute and its limit type: `~UC_T: UC_RHSRT~LO`. Region groups are
accepted wherever a region is.

### Example

A renewable-capacity floor in several regions:

| ~UC_T: UC_RHSRT~2030~LO | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| **UC_N** | **UC_Desc** | **pset_set** | **UC_CAP** | **Bangladesh** | **Indonesia** | **Malaysia** |
| UCE_GW-Solar | Solar | E_Solar | 1 | 3.03 | 0 | 13.72 |
| UCE_GW-Wind | Wind | E_Wind | 1 | 1.14 | 0 | 0 |

Each row is one constraint: the capacity of the processes in the set
(coefficient 1 in `UC_CAP`) must be at least the region's value in 2030.
The region columns hold the right-hand side, whose attribute, year and
limit type come from the tag text.

### Soft constraints

When the option **Create Dummy Imports for UC** is on (Veda's user
settings), Veda makes every user constraint soft: it adds terms on the
dummy import process `IMPDUCZ` (two dummy commodities per constraint),
priced by the dummy import price. Expect them in the data and the
results.

## ~UC_Sets

`~UC_Sets` declares the **region domain** of the constraints in the
`~UC_T` tables near it: one constraint for each region, or one summed
over regions. It is a one-cell tag: everything is in the tag text,
`~UC_Sets: <set>: <regions>`.

| Tag text | TIMES set | Meaning |
| --- | --- | --- |
| `R_E: <regions>` | `UC_R_EACH` | one constraint for each listed region |
| `R_S: <regions>` | `UC_R_SUM` | one constraint summed over the listed regions |

Regions are a comma list, region groups, or `AllRegions`.

```
~UC_Sets: R_E: AllRegions
~UC_T: UC_RHSRT~LO
```

**Periods and timeslices** are set by the right-hand-side attribute, not
by `~UC_Sets`: its letters after `UC_RHS` say what the constraint is
written for — `R` each region, `T` each period, `S` each timeslice — and
whatever is not named is summed. So `UC_RHSRT` is one constraint per
region and period, `UC_RHSRTS` per region, period and timeslice, and
`UC_RHS` a single constraint summed over everything. The forms `T_E:`,
`T_S:`, `T_SUC:`, `TS_E:` and `TS_S:` are accepted by `~UC_Sets` but
currently produce nothing.

**Which tables a `~UC_Sets` applies to.** A `~UC_T` table uses the
nearest `~UC_Sets` above it, or to its left on the tag row; `R_E` and
`R_S` count as one. If there is none above, the sheet's first
`~UC_Sets` applies. An `R_E:` with no regions takes the regions of the
sheet's first `R_E`/`R_S` that has some, and otherwise means
`AllRegions`.

!!! warning "Always put a `~UC_Sets` on a sheet with `~UC_T` tables"

    A sheet with no `~UC_Sets` at all gets no region domain from Veda.

## ~UC_GENT

Read together with `~UC_T` tables. New models should use `~UC_T`.
