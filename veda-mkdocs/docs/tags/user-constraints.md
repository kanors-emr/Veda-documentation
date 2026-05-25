# User constraints

## User Constraints

### ~UC_T

The User Constraint **time-series** row format. The tag header carries
the UC's identifier, year, and limit-type using `~`-separated
parameters: `~UC_T: <UC_id>~<year>~<limtype>`. A real example from
`Scen_RE-Targets_EMBER.xlsx :: Ember` (the `UC_RHSRT~2030~LO`
identifier sets a 2030 lower-bound RHS for the constraint):

| **~UC_T: UC_RHSRT~2030~LO** | **UC_N** | **`*`** | **Bangladesh** | **Indonesia** | **Malaysia** | **pset_set** | **UC_CAP** | **0** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UCE_EMBER_GW-Bioenergy | Bioenergy | 0 | 3.5 | 0.98 | E_Bio | 1 | 5 |
| UCE_EMBER_GW-Hydro | Hydro | 0.38 | 0 | 15.68 | E_Hydro | 1 | 5 |
| UCE_EMBER_GW-Solar | Solar | 3.03 | 0 | 13.72 | E_Solar | 1 | 5 |
| UCE_EMBER_GW-Wind | Wind | 1.14 | 0 | 0 | E_Wind | 1 | 5 |

Key columns from this and other UC_T tables:

| Column                                                  | Meaning                                                       |
| --- | --- |
| `UC_N`                                                  | The user-constraint instance name                             |
| `*`                                                     | Default value across regions                                  |
| Per-region columns (`Bangladesh`, `Indonesia`, …)       | Region-specific value                                         |
| `pset_set` / `pset_pn` / standard process filter columns| Which processes participate                                   |
| `cset_set` / `cset_cn` / standard commodity filters     | Which commodities participate                                 |
| `attribute` (aliases `prmtr`, `parameter`)              | The TIMES parameter being constrained                         |
| `attrib_cond` (alias `attribute_condition`)             | Optional conditional clause                                   |
| `avc_year` / `avc_timeslice` / `avc_limtype`            | "Availability condition" — when/where the row is active       |

**RegionGroup support** was extended to UC_T in **4.1.1.1** (May 2025),
so the `region` column (or any region-named column) can carry
RegionGroup names. **Dimension allocation priority** for column
headers: attribute → currency → lim_type → region → side → time_slice →
year → commodity.

### ~UC_Sets

Defines element sets that subsequent `~UC_T` rows reference by name. The
tag header carries a region scope via `R_E:` (the regions over which
this set applies). Each row binds a set name to its members.

Real example from `Scen_RE-Targets_EMBER.xlsx :: Ember`:

| **~UC_Sets: R_E: Bangladesh,Indonesia,Malaysia,Philippines,Thailand,Vietnam** | |
| --- | --- |
| Bioenergy | E_Bio |
| Hydro | E_Hydro |
| Solar | E_Solar |
| Wind | E_Wind |
| Onshore Wind | E_WON |

The first column is the set name (used in `UC_N` of subsequent UC_T
rows); the second column lists the member processes or process sets.

