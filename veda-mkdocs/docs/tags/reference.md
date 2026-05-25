# Tag reference

## Tag scope reference

This matrix lists the tags documented above and the file types where
each tag is accepted (taken from `scentype_taglist` in
`VEDA_TIMES_sets-attributes_veda_parameters.xlsx`). The file-type
identifiers used in the *Available in* column:

| Name | Meaning |
| --- | --- |
| `BY` | Base Year template (`VT_*.xlsx`) |
| `BY_Trans` | Base Year transformation scenario (`BY_Trans.xlsx`) |
| `SubRES` | SubRES technology template |
| `SR_Trans` | SubRES transformation scenario (`SubRES_*_Trans.xlsx`) |
| `SysSettings` | The model's `SysSettings.xlsx` |
| `RegScen` | Regular scenario file |
| `ParScen` | Parametric scenario file |
| `SubParScen` | Sub-parametric scenario |
| `TradeScen` | Trade scenario file |
| `TradeLinks` | Dedicated trade-links file |
| `LMADefs` | Reports definitions file (`LMADefs-*.xlsx` / `ReportDefs-*.xlsx`) |
| `setrules` | Set-rules file (used by `~TFM_PSets` / `~TFM_CSets`) |
| `NoSeedValueScenario` | A scenario file flagged not to carry seed values |

| Tag | Available in | Description |
| --- | --- | --- |
| `~BookRegions_Map` | SysSettings | Map book (super) regions to model regions |
| `~COMEMI` | BY, SubRES | Legacy — use VDA_EMCB via a regular Veda tag instead |
| `~Currencies` | SysSettings | list of all currencies used in the model |
| `~DefaultYear` | SysSettings | Default year for any time-series parameter |
| `~DefUnits` | SysSettings | Default process activity, capacity, and commodity units by sector |
| `~FI_Comm` | BY, SubRES, SysSettings | Commodity Definition Table — declares commodities and their properties |
| `~FI_Process` | BY, SubRES | Process Definition Table — declares technologies and their properties |
| `~FI_Process_Trades` | TradeLinks | Per-trade-process metadata for TradeLinks files |
| `~FI_T` | BY, SubRES | Flexible Import Table — primary parameter-value input format |
| `~INPUTCELL` | ParScen | Mark cells in a parametric-scenario sheet as input cells whose values Veda varies across runs |
| `~MD-C_C` | BY, SubRES, SysSettings | metadata tag for commodity having column level scope |
| `~MD-C_R` | BY, SubRES, SysSettings | metadata tag for commodity having row level scope |
| `~MD-C_S` | BY, SubRES, SysSettings | metadata tag for commodity having worksheet scope |
| `~MD-C_W` | BY, SubRES, SysSettings | metadata tag for commodity having workbook scope |
| `~MD-T_C` | BY, SubRES | metadata tag for technology having column level scope |
| `~MD-T_R` | BY, SubRES | metadata tag for technology having row level scope |
| `~MD-T_S` | BY, SubRES | metadata tag for technology having worksheet scope |
| `~MD-T_W` | BY, SubRES | metadata tag for technology having workbook scope |
| `~MD-V_C` | BY, TradeScen, tradeLinks, setrules, SubRES, DemScen, DemAlloc, NoSeedValueScenario, ParScen, RegScen, SubParScen, SR_Trans, BY_Trans, syssettings, LMADefs | metadata tag for value(s) having column level scope |
| `~MD-V_R` | BY, TradeScen, tradeLinks, setrules, SubRES, DemScen, DemAlloc, NoSeedValueScenario, ParScen, RegScen, SubParScen, SR_Trans, BY_Trans, syssettings, LMADefs | metadata tag for value(s) having row level scope |
| `~MD-V_S` | BY, TradeScen, tradeLinks, setrules, SubRES, DemScen, DemAlloc, NoSeedValueScenario, ParScen, RegScen, SubParScen, SR_Trans, BY_Trans, syssettings, LMADefs | metadata tag for value(s) having worksheet scope |
| `~MD-V_TC` | BY, TradeScen, tradeLinks, setrules, SubRES, DemScen, DemAlloc, NoSeedValueScenario, ParScen, RegScen, SubParScen, SR_Trans, BY_Trans, syssettings, LMADefs | metadata tag for value(s) having table level scope in the same column |
| `~MD-V_TR` | BY, TradeScen, tradeLinks, setrules, SubRES, DemScen, DemAlloc, NoSeedValueScenario, ParScen, RegScen, SubParScen, SR_Trans, BY_Trans, syssettings, LMADefs | metadata tag for value(s) having table level scope in the same row |
| `~MD-V_W` | BY, TradeScen, tradeLinks, setrules, SubRES, DemScen, DemAlloc, NoSeedValueScenario, ParScen, RegScen, SubParScen, SR_Trans, BY_Trans, syssettings, LMADefs | metadata tag for value(s) having workbook scope |
| `~MD_Dimensions` | SysSettings | Administrators can specify the dimensions of metadata they wish to capture by configuring this table within SysSettings |
| `~MileStoneYears` | SysSettings | Alternate way to specify model periods by directly listing milestone years |
| `~NOpCol` | SysSettings | ~NOPCOL - No operation column headers. Veda would ignore, AND suppress sync log warnings, from columns with headers listed under this tag |
| `~PRCCOMEMI` | BY, SubRES | Legacy — use FLO_EMIS via a regular Veda tag instead |
| `~RegionGroup_Map` | SysSettings | Map native regions to logical RegionGroups for rule-based declarations |
| `~ReplicateInRegions` | SR_Trans | Enumerate per-region replications of processes from a SubRES template |
| `~StartYear` | SysSettings | First year of the model horizon |
| `~TFM_AVA` | SR_Trans | indicate availability of techs across regions |
| `~TFM_AVA-C` | SR_Trans | indicate availability of commodities across regions |
| `~TFM_COMGRP` | SysSettings | commodity group definitions |
| `~TFM_CSets` | setrules | Define named commodity sets via rule expressions |
| `~TFM_DINS` | BY_Trans, SR_Trans, SysSettings, RegScen, TradeScen, SubParScen, NoSeedValueScenario | Direct insert of values — fully enumerated (process, commodity) rows |
| `~TFM_DINS-AT` | BY_Trans, SR_Trans, SysSettings, RegScen, TradeScen, SubParScen, NoSeedValueScenario | DINS variant with attributes as column headers |
| `~TFM_DINS-TS` | BY_Trans, SR_Trans, SysSettings, RegScen, TradeScen, SubParScen, NoSeedValueScenario | DINS variant with years as column headers |
| `~TFM_DINS-TSL` | BY_Trans, SR_Trans, SysSettings, RegScen, TradeScen, SubParScen, NoSeedValueScenario | DINS variant with timeslices as column headers |
| `~TFM_FILL` | BY_Trans, SR_Trans, RegScen, TradeScen, ParScen, SysSettings, NoSeedValueScenario | Legacy — use TFM_FILL-R instead |
| `~TFM_FILL-R` | BY_Trans, SR_Trans, RegScen, TradeScen, ParScen, SysSettings, NoSeedValueScenario | Wide-data importer — translates a separate data sheet into long-format rows |
| `~TFM_GAMS` | BY_Trans, SR_Trans, SysSettings, RegScen, TradeScen, SubParScen, NoSeedValueScenario | Inject custom GAMS code (largely superseded by RFCmd attributes) |
| `~TFM_INS` | BY_Trans, SR_Trans, SysSettings, RegScen, TradeScen, SubParScen, NoSeedValueScenario | Insert parameter values with filters and year/timeslice column headers |
| `~TFM_INS-AT` | BY_Trans, SR_Trans, SysSettings, RegScen, TradeScen, SubParScen, NoSeedValueScenario | INS variant with attributes as column headers |
| `~TFM_INS-TS` | BY_Trans, SR_Trans, SysSettings, RegScen, TradeScen, SubParScen, NoSeedValueScenario | INS variant with years as column headers (time series) |
| `~TFM_INS-TSL` | BY_Trans, SR_Trans, SysSettings, RegScen, TradeScen, SubParScen, NoSeedValueScenario | INS variant with timeslices as column headers |
| `~TFM_INS-TXT` | SysSettings | INS variant supporting text values (PRC_PCG, PRC_TSL, PRC_VINT, COM_LIM, COM_TSL, COM_TYPE) |
| `~TFM_MIG` | BY_Trans, SR_Trans, SysSettings, RegScen, TradeScen, SubParScen, NoSeedValueScenario | Migrate parameters to a different set of indexes |
| `~TFM_PSets` | setrules | Define named process sets via rule expressions |
| `~TFM_TOPDINS` | BY_Trans, SR_Trans, SysSettings, RegScen, TradeScen, SubParScen, NoSeedValueScenario | Topology-aware DINS — fully-enumerated topology-restricted insert |
| `~TFM_TOPINS` | BY_Trans, SR_Trans, SysSettings, RegScen, TradeScen, SubParScen, NoSeedValueScenario | Topology-aware INS — restricted to (process, commodity) pairs in the model topology |
| `~TFM_TOPINS-A` | BY_Trans, SR_Trans, SysSettings, RegScen, TradeScen, SubParScen, NoSeedValueScenario | Attribute form of TFM_TOPINS |
| `~TFM_UPD` | BY_Trans, SR_Trans, SysSettings, RegScen, TradeScen, SubParScen, NoSeedValueScenario | Update existing parameter values matching filters |
| `~TFM_UPD-AT` | BY_Trans, SR_Trans, SysSettings, RegScen, TradeScen, SubParScen, NoSeedValueScenario | UPD variant with attributes as column headers |
| `~TFM_UPD-T` | BY_Trans, SR_Trans, SysSettings, RegScen, TradeScen, SubParScen, NoSeedValueScenario | UPD variant with year-targeted column headers |
| `~TFM_UPD-TS` | BY_Trans, SR_Trans, SysSettings, RegScen, TradeScen, SubParScen, NoSeedValueScenario | UPD variant with year-series column headers |
| `~TimePeriods` | SysSettings | time period definitions - in terms of period durations |
| `~TimeSlices` | SysSettings, RegScen, SubParScen | timeslice definition |
| `~TradeLinks` | TradeLinks | trade links in matrix format |
| `~TradeLinks_Desc` | TradeLinks | description of trade links that are defined in DINS |
| `~TradeLinks_DINS` | TradeLinks | Direct-insert form of trade-link declarations — one explicit row per link |
| `~TradeLinks_GenLinks` | TradeLinks | General rules that programmatically generate trade links from filter expressions |
| `~UC_SETS` | SysSettings, RegScen, SubParScen, NoSeedValueScenario | Define element sets that subsequent UC_T rows can reference |
| `~UC_T` | SysSettings, RegScen, SubParScen, NoSeedValueScenario | User constraint time-series — defines one piece of a UC indexed by attribute, year, side, and filters |


## Legacy Tags

It is not recommended to use these tags anymore, but they are still
supported for backward compatibility reasons.

### ~COMEMI

Use attribute VDA_EMCB via any regular Veda tag instead.

### ~PRCCOMEMI

Use attribute FLO_EMIS via any regular Veda tag instead.

### ~TFM_Fill

Use TFM_Fill-R instead.
