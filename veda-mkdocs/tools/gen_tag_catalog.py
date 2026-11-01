"""Generate docs/tags/reference.md (the VedaTL tag catalog) from Veda's own catalog.

Reads the seed files of two catalog tables in the Veda-PostgreDb repository:
  veda_front_end.scentype_taglist            which tags exist, where they are allowed, table kind, status
  veda_front_end.veda_supported_tags_structure  known columns of each tag, aliases, comment class, carry-down

Usage:
  python gen_tag_catalog.py <path to Veda-PostgreDb> <output reference.md>

Purpose lines and page links are kept in PURPOSE below; everything else comes from the catalog.
Do not edit reference.md by hand: change PURPOSE or the catalog, then regenerate.
"""
import os
import re
import sys
from collections import defaultdict

TABLES_DIR = "veda_front_end tables and views"

# tag (lower case) -> (page, anchor, purpose). Anchor may be "".
PURPOSE = {
    "startyear": ("system-settings.md", "startyear", "First year of the model"),
    "activepdef": ("system-settings.md", "activepdef", "Period definition active by default"),
    "timeperiods": ("system-settings.md", "timeperiods", "Period lengths, by named definition"),
    "milestoneyears": ("system-settings.md", "milestoneyears", "Milestone years, by named definition"),
    "endyear": ("system-settings.md", "endyear", "Last year of the horizon"),
    "defaultyear": ("system-settings.md", "defaultyear", "Year given to values without a year"),
    "bookregions_map": ("system-settings.md", "bookregions_map", "Regions and their books"),
    "regiongroup_map": ("system-settings.md", "regiongroup_map", "Region groups"),
    "parentregions_map": ("system-settings.md", "parentregions_map", "Parent regions for reporting"),
    "timeslices": ("system-settings.md", "timeslices", "Timeslice tree"),
    "currencies": ("system-settings.md", "currencies", "Currencies; the first is the default"),
    "defunits": ("system-settings.md", "defunits", "Default units by sector"),
    "unitconversion": ("system-settings.md", "unitconversion", "Unit conversion factors for results"),
    "nopcol": ("system-settings.md", "nopcol", "Column headers ignored model-wide"),
    "md_dimensions": ("metadata.md", "md_dimensions", "Metadata fields"),
    "fi_comm": ("res-templates.md", "commodity-definition-table-fi_comm", "Declare commodities"),
    "fi_process": ("res-templates.md", "process-definition-table-fi_process", "Declare processes"),
    "fi_t": ("res-templates.md", "flexible-import-table-fi_t", "Topology and base data"),
    "tfm_comgrp": ("sets-and-groups.md", "tfm_comgrp", "Commodity groups"),
    "tfm_psets": ("sets-and-groups.md", "process-and-commodity-sets-tfm_psets-tfm_csets", "User process sets"),
    "tfm_csets": ("sets-and-groups.md", "process-and-commodity-sets-tfm_psets-tfm_csets", "User commodity sets"),
    "vbeviews": ("sets-and-groups.md", "", "Saved browse views"),
    "tfm_dins": ("data-tags.md", "tfm_dins", "Insert, fully enumerated"),
    "tfm_dins-at": ("data-tags.md", "layouts-at-ts-tsl", "DINS, attributes across"),
    "tfm_dins-ts": ("data-tags.md", "layouts-at-ts-tsl", "DINS, years across"),
    "tfm_dins-tsl": ("data-tags.md", "layouts-at-ts-tsl", "DINS, timeslices across"),
    "tfm_ins": ("data-tags.md", "tfm_ins", "Insert by rule"),
    "tfm_ins-at": ("data-tags.md", "layouts-at-ts-tsl", "INS, attributes across"),
    "tfm_ins-ts": ("data-tags.md", "layouts-at-ts-tsl", "INS, years across"),
    "tfm_ins-tsl": ("data-tags.md", "layouts-at-ts-tsl", "INS, timeslices across"),
    "tfm_ins-txt": ("data-tags.md", "tfm_ins-txt", "INS for text attributes"),
    "tfm_upd": ("data-tags.md", "tfm_upd", "Update existing values"),
    "tfm_upd-at": ("data-tags.md", "layouts-at-ts-tsl", "UPD, attributes across"),
    "tfm_upd-ts": ("data-tags.md", "layouts-at-ts-tsl", "UPD, years across"),
    "tfm_mig": ("migrate.md", "", "Copy existing values to new indexes"),
    "tfm_mig-at": ("migrate.md", "", "MIG, attributes across"),
    "tfm_mig-ts": ("migrate.md", "", "MIG, years across"),
    "tfm_topins": ("topology.md", "tfm_topins", "Add topology by rule"),
    "tfm_topins-a": ("topology.md", "tfm_topins-a", "Add topology, compact form"),
    "tfm_topdins": ("topology.md", "tfm_topdins", "Add topology, enumerated"),
    "tfm_fill-r": ("fill.md", "", "Write existing values to a sheet"),
    "tfm_ava": ("availability.md", "tfm_ava", "Regions where repository processes exist"),
    "tfm_ava-c": ("availability.md", "tfm_ava-c", "Regions where repository commodities exist"),
    "replicateinregions": ("availability.md", "replicateinregions", "Clone a process per region"),
    "tradelinks": ("trade.md", "tradelinks", "Trade links, matrix form"),
    "tradelinks_dins": ("trade.md", "tradelinks_dins", "Trade links, row form"),
    "tradelinks_c1c2": ("trade.md", "tradelinks_c1c2", "Trade links, different commodity per side"),
    "tradelinks_desc": ("trade.md", "tradelinks_desc", "Trade process descriptions"),
    "fi_process_trades": ("trade.md", "fi_process_trades", "Trade process characteristics"),
    "commodity_geo": ("trade.md", "commodity_geo", "Map coordinates of commodity nodes"),
    "uc_t": ("user-constraints.md", "uc_t", "User constraints"),
    "uc_sets": ("user-constraints.md", "uc_sets", "Domain of user constraints"),
    "uc_gent": ("user-constraints.md", "uc_gent", "Read with ~UC_T"),
    "inputcell": ("parametric.md", "inputcell", "Run index of a parametric file"),
    "osemosyscsv": ("", "", "Marker for OSeMOSYS CSV imports"),
}
NOT_RECOMMENDED_EFFECT = {"comemi", "prccomemi", "comagg", "comagg_r1c2", "tfm_fill"}
READ_AS_UPD = {"tfm_upd-n", "tfm_upd-ns", "tfm_upd-t"}
NO_EFFECT = {"fi_genprocess", "fi_gencomm", "tfm_pins", "tfm_cins", "tfm_pcins", "tfm_pcopy",
             "tfm_adrcreate", "tfm_gams", "tfm_attribset", "impsettings", "rfinput", "trade_param",
             "tradelinks_genlinks", "uc_s", "comagg_r2c1", "drvr_scenario"}
DEMAND = {"drvr_allocation", "drvr_table", "series"}

FILE_TYPE_NAMES = {
    "by": "BY", "by_trans": "BY_Trans", "subres": "SubRES", "sr_trans": "SR_Trans",
    "syssettings": "SysSettings", "regscen": "RegScen", "noseedvaluescenario": "NSV",
    "parscen": "ParScen", "subparscen": "SubParScen", "tradescen": "TradeScen",
    "tradelinks": "TradeLinks", "setrules": "SetRules", "lmadefs": "ReportDefs",
    "demscen": "DemScen", "demalloc": "DemAlloc", "by_ose": "BY_OSe",
}


def sql_values(line):
    """Parse the VALUES (...) tuple of one INSERT line into Python values."""
    m = re.search(r"VALUES\s*\((.*)\)\s*;\s*$", line, re.I)
    if not m:
        return None
    s, out, i = m.group(1), [], 0
    while i < len(s):
        c = s[i]
        if c in " ,":
            i += 1
        elif c == "'":
            j, buf = i + 1, []
            while j < len(s):
                if s[j] == "'" and j + 1 < len(s) and s[j + 1] == "'":
                    buf.append("'"); j += 2
                elif s[j] == "'":
                    break
                else:
                    buf.append(s[j]); j += 1
            out.append("".join(buf)); i = j + 1
        else:
            j = i
            while j < len(s) and s[j] != ",":
                j += 1
            tok = s[i:j].strip()
            out.append(None if tok.upper() == "NULL" else tok)
            i = j
    return out


def read_inserts(path):
    rows = []
    with open(path, encoding="utf-8-sig") as f:
        for line in f:
            if line.lstrip().upper().startswith("INSERT INTO"):
                v = sql_values(line.strip())
                if v:
                    rows.append(v)
    return rows


def status_of(tag, offer):
    t = tag.lower()
    if t in READ_AS_UPD:
        return "read as `~TFM_UPD`"
    if t in NO_EFFECT:
        return "**no effect**"
    if t in NOT_RECOMMENDED_EFFECT:
        return "not recommended"
    if t in DEMAND:
        return "demand tool"
    if str(offer) == "0":
        return "not offered"
    return ""


def link(tag):
    t = tag.lower()
    if t in PURPOSE:
        page, anchor, _ = PURPOSE[t]
        if page:
            return page + ("#" + anchor if anchor else "")
    if t in NO_EFFECT or t in READ_AS_UPD or t in NOT_RECOMMENDED_EFFECT:
        return "not-recommended.md"
    return ""


def main(repo, out):
    tdir = os.path.join(repo, TABLES_DIR)
    tags = read_inserts(os.path.join(tdir, "veda_front_end.scentype_taglist.sql"))
    cols = read_inserts(os.path.join(tdir, "veda_front_end.veda_supported_tags_structure.sql"))

    report_tags, model_tags = [], []
    for row in tags:
        _id, tag, scen_types, single, corner, _desc, offer = row[:7]
        types = [FILE_TYPE_NAMES.get(x.strip().lower(), x.strip()) for x in (scen_types or "").split(",") if x.strip()]
        rec = dict(tag=tag, types=types, single=str(single) == "1", corner=str(corner).lower() in ("t", "true", "1"),
                   offer=offer)
        (report_tags if types == ["ReportDefs"] else model_tags).append(rec)

    by_tag = defaultdict(list)
    for r in cols:
        tag, field, db_field, aliases, inherit, ignore = r[0], r[1], r[2], r[3], r[4], r[5]
        multi = r[10] if len(r) > 10 else None
        names = [a.strip().strip('"') for a in (aliases or "").strip("{}").split(",") if a.strip()]
        by_tag[tag.lower()].append(dict(field=field or db_field, aliases=names, inherit=bool(inherit),
                                        ignore=ignore, multi=str(multi) == "1"))

    L = []
    L += ["# Tag catalog", "",
          "<!-- Generated by tools/gen_tag_catalog.py from Veda's catalog tables. Do not edit by hand. -->", "",
          "Every tag Veda recognises, where it is allowed, and its known columns.",
          "This page is generated from the catalog Veda itself uses to read",
          "models, so it is complete and current; the tag pages explain what",
          "the tags mean.", "",
          "**File types**: BY = `VT_*`, BY_Trans, SubRES, SR_Trans = `SubRES_*_Trans`,",
          "SysSettings, RegScen = `Scen_*`, NSV = `Scen_NSV_*`, ParScen = `Scen_Par-*`,",
          "SubParScen = generated parametric children, TradeScen = `ScenTrade_*`,",
          "TradeLinks = `ScenTrade__Trade_Links*`, SetRules = `Set*`, ReportDefs,",
          "DemScen / DemAlloc = demand files ([Files and layers](files-and-layers.md)).", "",
          "**Kind**: *corner* tables start at the tag's column; *floating* tables",
          "span their whole region; *single value* tags read the cell below",
          "([How a table is read](reading-tables.md)).", "",
          "## All model tags", "",
          "| Tag | Purpose | Allowed in | Kind | Status |",
          "| --- | --- | --- | --- | --- |"]
    for r in sorted(model_tags, key=lambda x: x["tag"].lower()):
        t = r["tag"].lower()
        purpose = PURPOSE.get(t, ("", "", ""))[2]
        lk = link(r["tag"])
        name = f"[`~{r['tag']}`]({lk})" if lk else f"`~{r['tag']}`"
        kind = "single value" if r["single"] else ("corner" if r["corner"] else "floating")
        if t.startswith("md-"):
            purpose, name = "Metadata", f"[`~{r['tag']}`](metadata.md)"
        L.append(f"| {name} | {purpose} | {', '.join(r['types'])} | {kind} | {status_of(r['tag'], r['offer'])} |")
    L += ["", "Report-definition tags (allowed in ReportDefs files only) are described in",
          "[Reports](../reports.md): " + ", ".join(f"`~{r['tag']}`" for r in sorted(report_tags, key=lambda x: x['tag'].lower())) + ".", ""]

    L += ["## Columns of each tag", "",
          "Columns are not case-sensitive; any alias names the column. **Comment**: a cell starting",
          "with `\\I:` makes the row a comment in every column marked; `*` does so only in columns",
          "marked `* or \\I:` ([comment rows](reading-tables.md#comment-rows)). **Carries down**: an",
          "empty cell takes the value above. **List**: the cell may hold a comma list. Variant",
          "layouts (`-AT`, `-TS`, `-TSL`, `-A`, `-TXT`) use the columns of their parent tag.", ""]
    skip = {"fi_t_test", "tfm_ava_new", "scenmap_case_priority"}
    report_lc = {r["tag"].lower() for r in report_tags}
    for t in sorted(by_tag):
        if t in skip or t in report_lc:
            continue
        L += [f"### ~{t}", ""]
        L += ["| Column | Aliases | Comment | Carries down | List |", "| --- | --- | --- | --- | --- |"]
        for c in sorted(by_tag[t], key=lambda c: c["field"]):
            others = [a for a in c["aliases"] if a.lower() != (c["field"] or "").lower()]
            com = {"1": "`\\I:`", "2": "`*` or `\\I:`"}.get(str(c["ignore"]), "")
            L.append(f"| `{c['field']}` | {', '.join('`'+a+'`' for a in others)} | {com} | "
                     f"{'yes' if c['inherit'] else ''} | {'yes' if c['multi'] else ''} |")
        L.append("")
    with open(out, "w", encoding="utf-8", newline="\r\n") as f:
        f.write("\n".join(L).rstrip() + "\n")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
