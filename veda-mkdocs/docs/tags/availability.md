# SubRES availability

Technology repositories (`SubRES_<name>`) declare processes and
commodities without regions. Their `_Trans` workbook decides where they
exist. These tags are accepted only in `SubRES_<name>_Trans` files.

## ~TFM_AVA

Says in which regions the repository's processes exist. Columns: one or
more process filters (`pset_pn` / `process`, `pset_pd`, `pset_set`,
`pset_ci`, `pset_co`), `AllRegions`, and one column per region. Cells
hold `1` (available) or `0` (not available). Process filters see only
this repository's processes.

| ~TFM_AVA | | | |
| --- | --- | --- | --- |
| **pset_pn** | **AllRegions** | **GBL** | **Brazil** |
| `*` | 1 | 0 | |
| `INMcem_*_BRA` | 0 | | 1 |

The first row makes every process available everywhere except `GBL`;
the second restricts the Brazil-specific processes to Brazil.

How the cells combine:

- Within a row, the **rightmost** filled column wins for a region. Put
  `AllRegions` to the left of the region columns, so that region columns
  override it.
- Across rows, the **later** row wins. A catch-all row first, then
  exceptions, is the usual pattern.
- **If the tables switch nothing on** — no `~TFM_AVA` at all, an empty
  table, or only zeros — every process of the repository is available in
  every region.
- **Once at least one process is switched on somewhere**, a process that
  no row switches on is available nowhere. So a table that only names a
  few processes makes all the others disappear; start with a catch-all
  row (`*`, `AllRegions` = 1) when only some processes need restricting.
- One wide table with region columns is faster to process than several
  narrow ones.

## ~TFM_AVA-C

The commodity counterpart: commodity filters (`cset_cn`, `cset_cd`,
`cset_set`), `AllRegions`, and region columns.

## ~ReplicateInRegions

Clones a template process from the repository into region-specific
copies, for example one per country.

| ~ReplicateInRegions | | | |
| --- | --- | --- | --- |
| **Region** | **incode** | **indesc** | **Process** |
| Africa_North | DZA | Algeria - [Export] | LNG_New-Export |

`Region` is the model region of the copy, `incode` the code plugged into
the copy's name (an ISO code, say), `indesc` the text for its
description, and `Process` the template process.
