# System settings tags

## Regions and Time

The system settings file (SysSettings) supports some tags that specify
the basic structure of the model in terms of regions, time periods, time
slices, currencies, and units.

### ~BookRegions_map

The concept of `BookRegions` serves a core Veda principle that `structures that are common across regions should be declared only once`. This applies to the `BaseYear templates` that exist in the root of the Veda model folder. They are named as `VT` (Veda Template) _ `BookRegion` _ `Sector` _ `Version`. For example, a model may have
`VT_ElecReg_ELC_v01` and `VT_DemReg_EndUse_v01` in the root folder
to describe electricity supply in the first file and the demand in the
second one. ElecReg could map to Electricity grid regions, which is a
reasonable way to represent electricity supply, and DemReg could map to
states or provinces, which is a reasonable way to represent demands.

This tag maps the book region (also called `super region`) to model regions. All declarations in base year templates
that do not have a region specification apply to all regions mapped to
their book region.

### ~StartYear

The first year of the model horizon.

### ~TimePeriods

To specify period lengths. TIMES automatically computes the middle years
as milestone years (along with the StartYear).

### ~MileStoneYears

This is an alternate way to specify the model periods - by directly
specifying the milestone years for which the model will run. TIMES
computes the period spans automatically when milestone years are
specified. The last year of the model horizon can be specified
(optional).

### ~DefaultYear

The default year to be used for any timeseries parameter.

### ~Currencies

List of currencies used in the model. The first entry in this table
works as the `default currency` in Veda.

### ~DefUnits

This tag is used to declare the default process (activity and capacity)
and commodity units by sector.

### ~RegionGroup_map

The **RegionGroups** feature enables efficient rule-based declarations
by grouping multiple native regions under logical identifiers. This
powerful feature eliminates repetitive region-specific declarations and
enables consistent parameterization across related regions.

**Purpose and Benefits:**

RegionGroups solve a fundamental modeling challenge: applying the same
parameters or characteristics to multiple regions without manual
preprocessing. Instead of creating individual entries for each native
region, modelers can define RegionGroups and make declarations at the
group level, which automatically propagate to all constituent regions.

**Key advantages include:**

- **Elimination of repetitive declarations**: Instead of 29 separate entries for each technology parameter, use 1 entry per RegionGroup
- **Rule-based parameterization**: Technology characteristics available by external regional classifications (e.g., WEO regions, steel regions) can be directly applied
- **Flexible override capability**: Native region declarations take precedence over RegionGroup declarations in the same table
- **Maintenance efficiency**: Changes to RegionGroup parameters automatically propagate to all constituent regions

**Implementation:**

The RegionGroups feature is implemented through the `regiongroup_map`
table in the `SysSettings.xlsx` file. This table establishes the mapping
between native regions and their logical groupings.

**Table Structure:**

The `regiongroup_map` table allows each native region to belong to
multiple RegionGroups, enabling different grouping schemes for different
purposes. However, **it is the user's responsibility to ensure that only
one grouping scheme is used within any single VEDA tag**.

**Example with Two Grouping Schemes:**

| **regiongroup**                       | **Region**    |
| --- | --- |
| **WEO Regional Classification**       |               |
| weopg_European Union                 | EU_north     |
| weopg_European Union                 | EU_northeast |
| weopg_European Union                 | France        |
| weopg_European Union                 | Germany       |
| weopg_India                          | India         |
| weopg_China                          | China         |
| weopg_United States                  | USA           |
| weopg_United States                  | Canada        |
| **Development Status Classification** |               |
| Reg_Dev                              | EU_north     |
| Reg_Dev                              | EU_northeast |
| Reg_Dev                              | France        |
| Reg_Dev                              | Germany       |
| Reg_Dev                              | USA           |
| Reg_Dev                              | Canada        |
| Reg_Eme                              | India         |
| Reg_Eme                              | China         |
| Reg_Eme                              | Africa_north |
| Reg_Eme                              | Brazil        |

**Key Points:**

- Each native region (e.g., `Germany`) appears in multiple RegionGroups (`weopg_European Union` and `Reg_Dev`)
- The **WEO scheme** provides detailed regional classifications (8+ groups)
- The **Development Status scheme** simplifies to just 2 groups (`Reg_Dev` vs `Reg_Eme`), reducing 29 regions to 2 categories
- **User Responsibility**: Never mix grouping schemes in the same table (e.g., don't use both `weopg_European Union` and `Reg_Dev` in the same declaration)

**Usage in Model Declarations:**

Once defined, RegionGroups can be used directly in the `region` column
of any VEDA table:

| **TechName**    | **region**            | **Comm-IN-A** | **INPUT** | **VAROM** |
| --- | --- | --- | --- | --- |
| Steel_BOF_CCS | weopg_European Union | INDCOA,INDNGA | 0.3456    | 250       |
| Steel_BOF_CCS | feIndia               | INDCOA,INDNGA | 0.3456    | 280       |

**Override Behavior:**

When both RegionGroup and native region declarations exist in the same
table, the native region declaration takes precedence:

| **TechName** | **region**            | **efficiency** | **cost** |
| --- | --- | --- | --- |
| PowerPlant   | weopg_European Union | 0.85           | 1000     |
| PowerPlant   | Germany               | 0.90           | 1200     |

**Result**: Germany gets efficiency=0.90, cost=1200 (native region
override), while all other weopg_European Union regions get
efficiency=0.85, cost=1000 (RegionGroup default).

**Technical Implementation:**

RegionGroups are resolved during tag processing, which means they follow
all standard VEDA overwriting rules within scenarios:

1. **Tag Processing Phase**: RegionGroups are expanded to their constituent native regions
2. **Precedence Rules Apply**: Standard VEDA precedence rules determine final parameter values
3. **Override Hierarchy**: Native region declarations override RegionGroup declarations in the same table
4. **Scenario Integration**: RegionGroup declarations can be overridden by subsequent scenario files

**Common Use Cases:**

- **WEO Regional Classifications**: Apply World Energy Outlook technology characteristics directly to RegionGroups without preprocessing
- **Development Status Groupings**: Group regions by economic development level (emerging vs. developed) for policy analysis
- **Sector-Specific Groupings**: Map regions to major production centers (e.g., steel regions, oil regions) for industry-specific technology data
- **Geographic Classifications**: Group regions by climate zones, resource availability, or trade relationships

**Multiple Grouping Schemes:**

VEDA allows each native region to belong to multiple RegionGroups
simultaneously, enabling flexible modeling approaches. For example,
`Germany` can be in both `weopg_European Union` (WEO classification) and
`Reg_Dev` (development status classification).

**Critical User Responsibility:**

!!! warning "Warning"

    **VEDA will not prevent you from mixing grouping schemes**, but you must ensure consistency within each table. Never use RegionGroups from different schemes in the same VEDA tag or table.

**Valid Usage (Consistent Scheme):**

| **TechName** | **region** | **efficiency** |
| --- | --- | --- |
| PowerPlant   | Reg_Dev   | 0.85           |
| PowerPlant   | Reg_Eme   | 0.75           |

**Invalid Usage (Mixed Schemes):**

| **TechName** | **region**            | **efficiency** |
| --- | --- | --- |
| PowerPlant   | weopg_European Union | 0.85           |
| PowerPlant   | Reg_Eme              | 0.75           |

*This mixes WEO classification (weopg_European Union) with development
status classification (Reg_Eme) in the same table, which should be
avoided.*

**Best Practices:**

- **Scheme Consistency**: Use only one grouping scheme per VEDA table/tag
- **Naming Conventions**: Use clear prefixes (e.g., `weopg_`, `Reg_`, `steel_`) to distinguish grouping schemes
- **Documentation**: Clearly document which grouping scheme is used in each model component
- **Efficiency Focus**: Prefer simpler schemes when possible (e.g., `Reg_Dev`/`Reg_Eme` reduces 29 regions to 2 groups)
- **Override Capability**: Leverage native region overrides for exceptions within RegionGroup defaults
- **Scenario Integration**: Combine with scenario files to create flexible policy analysis frameworks


## SysSettings utility tags

### ~TimeSlices

The full timeslice tree of the model — seasons, day-night levels, and
individual timeslices used throughout. Real example from
`SysSettings.xlsx :: Region-Time Slices`:

| **~TimeSlices** | **Season** | **Weekly** | **DayNite** |
| --- | --- | --- | --- |
| | F | | D |
| | R | | N |
| | S | | P |

Available in `SysSettings`, `RegScen`, and `SubParScen`, so the
timeslice structure can be overridden in scenarios that vary
temporal resolution.

### ~NOpCol

"No-operation column headers." Lists column-header names that Veda
should **ignore** during tag processing — useful when a template
carries annotation or audit columns alongside the real parameter
columns. Lives in `SysSettings`.

