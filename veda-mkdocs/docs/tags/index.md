# Veda Tags

This section describes the genesis and design purpose of the Veda
syntax, which started with the Flexible Import tag - **~FI_T** - in
Excel VBA at the turn of the 21st century. Various tags and conventions
have evolved over two decades to serve the [core design philosophy of
Veda](../introduction.md#philosophy-and-core-principles).

## What's in this section

Veda Tags is a reference for the tagged tables that describe a Veda model. Each sub-page covers one family of tags:

* **[System settings](system-settings.md)** — region and time structure, units, currencies, region groups, and SysSettings utility tags.
* **[RES templates](res-templates.md)** — building the Reference Energy System through `~FI_COMM`, `~FI_PROCESS`, and `~FI_T`.
* **[Data tags (INS / DINS / UPD)](data-tags.md)** — the data workhorses, all their variants, topology-aware forms, `~TFM_MIG`, `~TFM_FILL-R`, and `~TFM_GAMS`.
* **[Sets and groups](sets-and-groups.md)** — `~TFM_COMGRP`, `~TFM_PSets`, `~TFM_CSets`.
* **[Trade](trade.md)** — TradeLinks family, `~TFM_AVA` / `~TFM_AVA-C`, `~ReplicateInRegions`, `~FI_Process_Trades`.
* **[User constraints](user-constraints.md)** — `~UC_T`, `~UC_Sets`.
* **[Parametric scenarios](parametric.md)** — `~INPUTCELL`.
* **[Metadata](metadata.md)** — the `~MD-*` tag family.
* **[Reference](reference.md)** — tag scope matrix and legacy tags.

## Process and Commodity Filtering

### The Foundation of VEDA's Rule-Based Processing

Process and commodity filtering is the core mechanism that enables
VEDA's powerful rule-based data processing. This system allows users to
apply parameters, transformations, and operations to groups of processes
and commodities based on flexible criteria, eliminating the need for
repetitive individual declarations.

- **Applications Across VEDA:**

    - **Transformation Tables** (INS, UPD, MIG): Bulk parameter
      insertion and updates
    - **Reports**: Multi-dimensional classification and aggregation
    - **Set Definitions**: Dynamic process and commodity groupings

### Five Filtering Dimensions

VEDA provides five complementary methods for identifying processes and
commodities:

- **1. Set Membership** (`pset_set`, `cset_set`)

    - Filter by predefined VEDA process or commodity sets
    - Most robust for administrative groupings
    - Example: `pset_set: ELEGEN` (all electricity generation
      processes)

- **2. Name Patterns** (`pset_pn`, `cset_cn`)

    - Filter by process or commodity name patterns
    - Supports wildcards and exclusions
    - Example: `pset_pn: *COAL*` (processes with "COAL" in name)

- **3. Description Patterns** (`pset_pd`, `cset_cd`)

    - Filter by process or commodity description text
    - Useful when names are cryptic but descriptions are clear
    - Example: `pset_pd: *Combined Cycle*`

- **4. Input Topology** (`pset_ci`)

    - Filter processes by input commodities (most robust for
      functional classification)
    - Based on actual energy flows, not naming conventions
    - Example: `pset_ci: TRDELC` (all processes consuming electricity
      for transport)

- **5. Output Topology** (`pset_co`)

    - Filter processes by output commodities
    - Functional classification based on what processes produce
    - Example: `pset_co: ELC` (all electricity-producing processes)

### Pattern Syntax

- **Wildcards:**

    - `*`: Multi-character wildcard (zero or more characters)
    - `?`: Single-character wildcard (exactly one character)
    - `[_]`: Literal underscore (when not used as wildcard)

- **Examples:**

    - `*COAL*`: Contains "COAL" anywhere
    - `COAL*`: Starts with "COAL"
    - `*COAL`: Ends with "COAL"
    - `PWR??01`: "PWR" + exactly 2 characters + "01"

- **Comma-Separated Lists (OR Logic):**

    - `COA,GAS,OIL`: Coal OR Gas OR Oil
    - `*ELEC*,*GRID*`: Contains "ELEC" OR contains "GRID"

- **Exclusion Syntax:**

    - `-*OLD*`: Exclude processes with "OLD" in name
    - `*,--RETIRED*`: All processes EXCEPT those with "RETIRED"

### Logic Control Architecture

VEDA provides sophisticated control over how filtering conditions are
combined through six logic control columns:

**Two-Block Architecture:**

| **Block** | **Columns** | **Logic control** |
| --- | --- | --- |
| Set Block | `pset_set`, `cset_set` | `_forsets` columns (block integration) |
| Name/Desc/Input/Output Block | `pset_pn`, `pset_pd`, `pset_ci`, `pset_co` | `_andor` columns (within-block logic) |

The Set Block joins the Name/Desc/Input/Output Block via `_forsets` columns; within each block, `_andor` columns control how conditions combine.

**Logic Control Columns:**

- **Within Name/Desc/Input/Output Block:**

    - `t_pos_andor`: Process positive conditions (AND/OR across
      pset_pn, pset_pd, pset_ci, pset_co)
    - `c_pos_andor`: Commodity positive conditions (AND/OR across
      cset_cn, cset_cd)
    - `t_neg_andor`: Process negative/exclusion conditions (AND/OR
      across exclusion fields)
    - `c_neg_andor`: Commodity negative/exclusion conditions (AND/OR
      across exclusion fields)

- **Set Block Integration:**

    - `t_pos_andor_forsets`: How process sets join with other process
      conditions
    - `c_pos_andor_forsets`: How commodity sets join with other
      commodity conditions

- **Default Behavior (when columns omitted):**

    - **All logic = AND** (most restrictive)
    - **Within comma-separated values = OR** (always)

### Logic Control Examples

**Example 1: Standard AND Logic (Default)**

| **Filter** | **Value** | **Note** |
| --- | --- | --- |
| `pset_set` | ELEGEN | Set membership |
| `pset_pn` | `*COAL*` | Name pattern |
| `pset_ci` | COA | Input commodity |
| **Result** | Processes in ELEGEN set AND name contains COAL AND consumes COA | |

**Example 2: OR Logic Within Block**

| **Filter** | **Value** | **Note** |
| --- | --- | --- |
| `pset_pn` | `*COAL*` | Name pattern |
| `pset_ci` | COA | Input commodity |
| `t_pos_andor` | OR | Name OR Input |
| **Result** | Processes with COAL in name OR consuming COA | |

**Example 3: Set Block OR Integration**

| **Filter** | **Value** | **Note** |
| --- | --- | --- |
| `pset_set` | ELEGEN | Set membership |
| `pset_pn` | `*RENEW*` | Name pattern |
| `t_pos_andor_forsets` | OR | Set OR Name |
| **Result** | Processes in ELEGEN set OR with RENEW in name | |

**Example 4: Complex Mixed Logic**

*Positive conditions*

| **Filter** | **Value** | **Note** |
| --- | --- | --- |
| `pset_set` | PWRGEN | Power generation set |
| `pset_pn` | `*COAL*,*GAS*` | Coal or gas in name |
| `pset_ci` | COA,GAS | Consumes coal or gas |
| `t_pos_andor` | OR | Name patterns OR input commodities |
| `t_pos_andor_forsets` | AND | Set AND (name OR input) |

*Negative conditions*

| **Filter** | **Value** | **Note** |
| --- | --- | --- |
| `pset_pn` | `-*OLD*` | Exclude old plants |
| `pset_pd` | `-*RETIRED*` | Exclude retired plants |
| `t_neg_andor` | OR | Exclude if old OR retired |

*Result:* (PWRGEN set) AND (coal/gas name OR coal/gas input) AND NOT (old name OR retired description)

**Example 5: Commodity Filtering**

| **Filter** | **Value** | **Note** |
| --- | --- | --- |
| `cset_set` | ALLELC | Electricity commodity set |
| `cset_cn` | `*H2*` | Hydrogen commodities |
| `c_pos_andor_forsets` | OR | Set OR name pattern |
| **Result** | All electricity commodities OR hydrogen commodities | |

### Filtering Method Selection Guidelines

- **Use Topology-Based Filtering When:**

    - Functional relationships are primary concern (`pset_ci`,
      `pset_co`)
    - Model has inconsistent naming conventions
    - New technologies added frequently
    - Cross-model compatibility required

- **Use Set-Based Filtering When:**

    - Predefined VEDA process sets exist (`pset_set`, `cset_set`)
    - Administrative or organizational groupings needed
    - Consistent with existing model structure

- **Use Pattern-Based Filtering When:**

    - Topology insufficient for distinction (`pset_pn`, `pset_pd`,
      `cset_cn`, `cset_cd`)
    - Regional, size, or vintage distinctions needed
    - Legacy compatibility required

- **Recommended Approach:**

    1. **Start with topology** (`pset_ci`, `pset_co`) for primary
       functional classification
    2. **Add sets** (`pset_set`) for administrative groupings
    3. **Supplement with patterns** (`pset_pn`, `pset_pd`) for
       secondary attributes
    4. **Use logic control** to create sophisticated combination rules

### Best Practices

- **Efficiency:**

    - **Topology first**: Most robust and maintenance-free
    - **Specific patterns last**: Place most restrictive conditions at
      the end
    - **Avoid over-complexity**: Use simplest logic that achieves the
      goal

- **Maintainability:**

    - **Document logic choices**: Explain why specific combinations
      are used
    - **Test edge cases**: Verify filtering captures intended
      processes/commodities
    - **Plan for growth**: Design filters that handle new technologies
      automatically

- **Performance:**

    - **Use sets when available**: Faster than pattern matching
    - **Minimize wildcards**: More specific patterns process faster
    - **Combine related conditions**: Group related filters in single
      operations


## Wildcard Support

The columns **PSET_PN**, **PSET_PD**, **PSET_CO**, **PSET_CI** (for
process filters), and **CSET_CN**, **CSET_CD** (for commodity filters)
support the use of comma-separated entries, with wild cards, in all TFM
tables apart from DINS:

1. **Comma-Separated Entries**: You can specify multiple entries in
    these columns by separating them with commas (`,`).

    Example: `Process1,Process2,Process3`

2. **Wildcards**: Wildcards allow flexible and broad pattern-matching
    for process or commodity names.

### Wildcards Overview

1. **Asterisk (`*`)** — multi-character wildcard, matching zero or more characters.

    * `Elec*` matches `Elec`, `Electricity`, `ElecGen`, etc.
    * `*Gen` matches `ElecGen`, `HeatGen`, etc.

2. **Question Mark (`?`) or Underscore (`_`)** — single-character wildcard, matching exactly one character.

    * `Tech_?` matches `Tech_A`, `Tech_B`, etc.
    * `Fuel_?` matches `Fuel_X`, `Fuel_Y`, etc.

3. **Square Brackets for Literal `_`**

    - If you want to refer to `_` as an actual character (not a wildcard), enclose it in square brackets `[ ]`.

    - Example: `Tech[_]_` matches `Tech_A`, `Tech_B`, etc.

### Examples

**Process Set Columns (PSET_...)**

- Entry: `PSET_PN`
    - Value: `Elec*`
    - Matches: `Electricity_Generation`, `ElecStorage`, etc.
    - Value: `Fuel?_Gen`
    - Matches: `Fuel1_Gen`, `Fuel2_Gen`, etc.
    - Value: `Tech_[_]X`
    - Matches: `Tech_X`.

**Commodity Set Columns (CSET_...)**

- Entry: `CSET_CN`
    - Value: `Elec, Heat*`
    - Matches: `Elec`, `Heat`, `HeatPump`, etc.
    - Value: `Gas?_Supply`
    - Matches: `Gas1_Supply`, `Gas2_Supply`, etc.
