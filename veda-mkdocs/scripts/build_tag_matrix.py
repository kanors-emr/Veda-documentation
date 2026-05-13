"""Build a filtered tag-scope matrix limited to tags actually documented in
veda-tags.md, with curated short descriptions where the source has none."""
import openpyxl

# Allowlist: tags that have a heading in veda-tags.md (case-insensitive).
DOCUMENTED = {t.lower() for t in [
    "BookRegions_Map",
    "StartYear",
    "TimePeriods",
    "MileStoneYears",
    "DefaultYear",
    "Currencies",
    "DefUnits",
    "RegionGroup_Map",
    "FI_T",
    "FI_Comm",
    "FI_Process",
    "FI_Process_Trades",
    "COMEMI",
    "PRCCOMEMI",
    "INPUTCELL",
    "MD-V_R",
    "MD-V_S",
    "MD-V_W",
    "MD-V_C",
    "MD-V_TR",
    "MD-V_TC",
    "MD-T_W",
    "MD-T_S",
    "MD-T_R",
    "MD-T_C",
    "MD-C_W",
    "MD-C_S",
    "MD-C_R",
    "MD-C_C",
    "MD_Dimensions",
    "NOpCol",
    "TimeSlices",
    "ReplicateInRegions",
    "TFM_AVA",
    "TFM_AVA-C",
    "TFM_COMGRP",
    "TFM_CSets",
    "TFM_PSets",
    "TFM_INS",
    "TFM_INS-TS",
    "TFM_INS-AT",
    "TFM_INS-TSL",
    "TFM_INS-TXT",
    "TFM_UPD",
    "TFM_UPD-T",
    "TFM_UPD-TS",
    "TFM_UPD-AT",
    "TFM_DINS",
    "TFM_DINS-TS",
    "TFM_DINS-AT",
    "TFM_DINS-TSL",
    "TFM_FILL",
    "TFM_FILL-R",
    "TFM_MIG",
    "TFM_TOPINS",
    "TFM_TOPINS-A",
    "TFM_TOPDINS",
    "TFM_GAMS",
    "TradeLinks",
    "TradeLinks_DINS",
    "TradeLinks_Desc",
    "TradeLinks_GenLinks",
    "UC_T",
    "UC_SETS",
]}

# Curated descriptions for documented tags that have no description in scentype_taglist.
# Skipped when the source already supplies a description.
DESC_OVERRIDES = {
    "bookregions_map": "Map book (super) regions to model regions",
    "startyear": "First year of the model horizon",
    "milestoneyears": "Alternate way to specify model periods by directly listing milestone years",
    "defaultyear": "Default year for any time-series parameter",
    "defunits": "Default process activity, capacity, and commodity units by sector",
    "regiongroup_map": "Map native regions to logical RegionGroups for rule-based declarations",
    "fi_t": "Flexible Import Table — primary parameter-value input format",
    "fi_comm": "Commodity Definition Table — declares commodities and their properties",
    "fi_process": "Process Definition Table — declares technologies and their properties",
    "fi_process_trades": "Per-trade-process metadata for TradeLinks files",
    "comemi": "Legacy — use VDA_EMCB via a regular Veda tag instead",
    "prccomemi": "Legacy — use FLO_EMIS via a regular Veda tag instead",
    "inputcell": "Mark cells in a parametric-scenario sheet as input cells whose values Veda varies across runs",
    "replicateinregions": "Enumerate per-region replications of processes from a SubRES template",
    "tfm_ins": "Insert parameter values with filters and year/timeslice column headers",
    "tfm_ins-ts": "INS variant with years as column headers (time series)",
    "tfm_ins-at": "INS variant with attributes as column headers",
    "tfm_ins-tsl": "INS variant with timeslices as column headers",
    "tfm_ins-txt": "INS variant supporting text values (PRC_PCG, PRC_TSL, PRC_VINT, COM_LIM, COM_TSL, COM_TYPE)",
    "tfm_upd": "Update existing parameter values matching filters",
    "tfm_upd-t": "UPD variant with year-targeted column headers",
    "tfm_upd-ts": "UPD variant with year-series column headers",
    "tfm_upd-at": "UPD variant with attributes as column headers",
    "tfm_dins": "Direct insert of values — fully enumerated (process, commodity) rows",
    "tfm_dins-ts": "DINS variant with years as column headers",
    "tfm_dins-at": "DINS variant with attributes as column headers",
    "tfm_dins-tsl": "DINS variant with timeslices as column headers",
    "tfm_fill": "Legacy — use TFM_FILL-R instead",
    "tfm_fill-r": "Wide-data importer — translates a separate data sheet into long-format rows",
    "tfm_mig": "Conditional value-transformation — modify values where conditions are met",
    "tfm_topins": "Topology-aware INS — restricted to (process, commodity) pairs in the model topology",
    "tfm_topins-a": "Attribute form of TFM_TOPINS",
    "tfm_topdins": "Topology-aware DINS — fully-enumerated topology-restricted insert",
    "tfm_gams": "Inject custom GAMS code (largely superseded by RFCmd attributes)",
    "tfm_psets": "Define named process sets via rule expressions",
    "tfm_csets": "Define named commodity sets via rule expressions",
    "tradelinks_dins": "Direct-insert form of trade-link declarations — one explicit row per link",
    "tradelinks_genlinks": "General rules that programmatically generate trade links from filter expressions",
    "uc_t": "User constraint time-series — defines one piece of a UC indexed by attribute, year, side, and filters",
    "uc_sets": "Define element sets that subsequent UC_T rows can reference",
}


wb = openpyxl.load_workbook(
    '/sessions/blissful-ecstatic-einstein/mnt/Veda-PostgreDb/veda_front_end tables and views/VEDA_TIMES_sets-attributes_veda_parameters.xlsx',
    data_only=True, read_only=True,
)
ws = wb['scentype_taglist']

rows = []
for i, row in enumerate(ws.iter_rows(values_only=True)):
    if i == 0:
        continue
    if row[1] is None:
        continue
    tag = str(row[1]).strip()
    if tag.lower() not in DOCUMENTED:
        continue
    scen_types = str(row[2]).strip() if row[2] is not None else ""
    desc = str(row[5]).strip() if len(row) > 5 and row[5] is not None else ""
    if not desc:
        desc = DESC_OVERRIDES.get(tag.lower(), "")
    rows.append((tag, scen_types, desc))

rows.sort(key=lambda r: r[0].lower())

print("## Tag scope reference")
print()
print("This matrix lists the tags documented above and the file types where")
print("each tag is accepted (taken from `scentype_taglist` in")
print("`VEDA_TIMES_sets-attributes_veda_parameters.xlsx`). The file-type")
print("identifiers used in the *Available in* column:")
print()
print("| Name | Meaning |")
print("|---|---|")
print("| `BY` | Base Year template (`VT_*.xlsx`) |")
print("| `BY_Trans` | Base Year transformation scenario (`BY_Trans.xlsx`) |")
print("| `SubRES` | SubRES technology template |")
print("| `SR_Trans` | SubRES transformation scenario (`SubRES_*_Trans.xlsx`) |")
print("| `SysSettings` | The model's `SysSettings.xlsx` |")
print("| `RegScen` | Regular scenario file |")
print("| `ParScen` | Parametric scenario file |")
print("| `SubParScen` | Sub-parametric scenario |")
print("| `TradeScen` | Trade scenario file |")
print("| `TradeLinks` | Dedicated trade-links file |")
print("| `LMADefs` | Reports definitions file (`LMADefs-*.xlsx` / `ReportDefs-*.xlsx`) |")
print("| `setrules` | Set-rules file (used by `~TFM_PSets` / `~TFM_CSets`) |")
print("| `NoSeedValueScenario` | A scenario file flagged not to carry seed values |")
print()
print("| Tag | Available in | Description |")
print("|---|---|---|")
for tag, scen_types, desc in rows:
    sc = ", ".join(part.strip() for part in scen_types.split(","))
    desc_md = (desc or "—").replace("|", "\\|")
    print(f"| `~{tag}` | {sc} | {desc_md} |")
