# Trade

Inter-regional trade is declared in the **trade-links file**,
`SuppXLS\Trades\ScenTrade__Trade_Links.xlsx` (two underscores). Its tags
declare which regions trade which commodities, and the trade processes
that carry the flows. Data for those processes (costs, bounds,
efficiencies) then goes in **trade workbooks**, `ScenTrade_<name>.xlsx`,
with the ordinary [insert and update tags](data-tags.md).

## ~TradeLinks

The matrix form. The first column's header is the traded commodity, and
its cells list exporting regions; the other column headers are importing
regions. A cell holding `1` (or another non-zero whole number) creates a
link with a generated process name, `T<B|U>_<commodity>_<from>_<to>_01`;
`0` or empty creates none; a cell holding text creates a link and uses
the text as the trade process name. Links to regions that are not in the
model are dropped.

| ~TradeLinks | | | |
| --- | --- | --- | --- |
| **ELC** | **REG1** | **REG2** | **REG3** |
| REG1 | | 1 | |
| REG2 | 1 | | 1 |
| REG3 | | 1 | |

**The sheet name sets the direction**: on a sheet whose name starts with
`B`, links are bilateral (two-way); on any other sheet they are
unidirectional (exporter → importer). Models usually keep two sheets,
`Bi` and `Uni`.

Writing `distr` in the tag text marks the links as distribution links.

!!! tip "Marketplace regions"

    A column headed by a market region (for example `GBL`, which must be a
    region of the model), with the same trade process name in the cells of
    every participating region, creates one process linking the market
    with each of them. TIMES then treats `GBL` as a marketplace.

## ~TradeLinks_DINS

The row form: one link per row, with explicit commodities on each side.

| Column | Meaning |
| --- | --- |
| `Reg1`, `Reg2` | The two regions (may be the same, for links inside a region) |
| `Comm` | The traded commodity (a label for the link) |
| `Comm1`, `Comm2` | The commodity in `Reg1` and in `Reg2` |
| `Tech` | The trade process |
| `TradeLink` | `B` (bilateral) or `U` (unidirectional) |

Use it when the commodity has a different name in each region, or for
networks (grid lines, pipelines) where every link is its own process.

## ~TradeLinks_c1c2

A matrix like `~TradeLinks` for links where the commodity differs between
the exporting and the importing region. As with `~TradeLinks`, the sheet
name sets the direction.

## ~TradeLinks_Desc

Descriptions of the trade processes declared by `~TradeLinks_DINS`:
process name and description.

## ~FI_Process_Trades

Declares the characteristics of trade processes (as `~FI_Process` does
for other processes): units, timeslice level, description.

## ~commodity_geo

Geographic coordinates of commodity nodes, for drawing grids on a map:
columns `region`, `commodity`, `lat`, `lng`, `shape`. It has no effect on
the model data.

## Trade workbooks

`ScenTrade_<name>` files hold data for the trade processes, using
`~TFM_INS`, `~TFM_DINS`, `~TFM_UPD` and so on. A common pattern is a
`~TFM_DINS-AT` table with `Region`, `Process`, `Year` and one column per
attribute (`ACT_COST`, `INVCOST`, `EFF`, `LIFE`, `START`, …).

!!! note

    Process filters in trade workbooks currently see every process in the
    model, not only trade processes.

The legacy trade tags `~Trade_Param` and `~TradeLinks_GenLinks` no
longer have any effect ([not recommended](not-recommended.md)).
