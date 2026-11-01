# How a table is read

All model data is written in tables: rectangular blocks of cells on a
worksheet, each introduced by a tag. This page says how Veda finds a
table, which cells belong to it, how the tag text and the column headers
are read, and which rows and columns are skipped. What the values mean is
covered in [Values, wildcards and filters](values-and-filters.md).

## The tag cell

- A **tag cell** is a cell whose value, after trimming spaces, begins
  with `~`. Formulas count by their result, so a tag can be built by
  formula.
- The **tag name** is the text after `~` up to the first `:` (or the end
  of the cell). Tag names are not case-sensitive: `~fi_t`, `~FI_T` and
  `~Fi_T` are the same tag.
- The **tag text** is everything after the first `:`. It gives values
  that apply to the whole table ([below](#tag-text)).
- A cell beginning with `~` whose name is not a Veda tag is ignored, with
  its table.
- A tag that exists but is not allowed in the file type where it appears
  is reported in the sync log and ignored ([tag catalog](reference.md)).
- Cells are read by their displayed value. A cell holding an Excel error
  (`#N/A`, `#DIV/0!`, …) is read as empty.
- Hidden sheets, rows and columns are read like visible ones.

!!! tip "Switching a table off"

    Because a tag must *begin* with `~`, anything in front of it switches
    the table off. The house convention is the prefix `Deact`:
    `Deact~TFM_INS`. The cell still shows what the table would be, and a
    formula can switch it on and off ([parametric scenarios](parametric.md#what-the-input-cell-can-drive)).

## Where a table starts and ends

The table occupies the Excel **current region** of the tag cell: the
block of non-empty cells around it, bounded on every side by an empty row
or column (or the sheet edge). In practice:

- **Leave at least one fully empty row and one fully empty column
  between neighbouring tables**, including tables placed side by side. A
  single stray value in the gap merges two tables into one region.
- If a tag cell lies inside the region of another tag, Veda stops the
  sync and reports both tags.
- The table starts at the tag's row. Cells of the region above the tag
  row are not part of it.

Tags come in two kinds, which differ only in where the table starts
horizontally:

- **Corner tags** (most settings tags, `~TFM_TOPINS`, `~TFM_MIG`,
  `~TFM_AVA`, `~TFM_COMGRP`, `~TFM_FILL-R`, `~UC_Sets`, `~TradeLinks`, …):
  the table starts at the tag's column. Region columns to the left are not
  part of it.
- **Floating tags** (`~FI_T`, `~FI_Process`, `~FI_Comm`, `~TFM_INS`,
  `~TFM_DINS`, `~TFM_UPD` and their variants, `~UC_T`, …): the table spans
  the whole width of the region, so the tag may sit above any of its
  columns.

The [tag catalog](reference.md) gives the kind of every tag.

## Rows

- The **header row** is the row directly below the tag cell. Data rows
  follow it to the bottom of the region.
- **Single-value tags** (`~StartYear`, `~ActivePDef`, `~EndYear`,
  `~DefaultYear`) have no header: the value is the cell directly below the
  tag.
- A table with no data rows contributes nothing.

## Tag text

The tag text sets values for the whole table. It has two forms.

**Key–value form.** If the text contains `=`, it is a list of
`key=value` items separated by `;`. Keys are column names (any of their
aliases); a value may be a comma list. Spaces around keys and values are
ignored.

```
~TFM_INS-TS: attribute=FLO_EMIS; limtype=UP
~TFM_DINS-TS: attribute=COM_BNDPRD; LimType=LO
~TFM_INS-TS: Region=Reg_Dev,Reg_Eme
~TFM_FILL-R: w=RoadTra_BY; hcol=region
```

An item acts as a column of that name holding the same value in every
row. A region given here may be a region group or a comma list.

**Token form** (`~FI_T`, `~UC_T`). If the text has no `=`, it is a list
of tokens separated by `~`. Each token must be a known element: a
currency, a limit type, a region, a timeslice, a year or an attribute.
Veda places each token in the index it belongs to.

```
~FI_T: USD24          every value is in USD24 unless a column says otherwise
~FI_T: UP             every attribute that has a limit type defaults to UP
~FI_T: MEUR2000~FX    both
~UC_T: UC_RHSRT       the default attribute of the table
```

A token sets a default only for attributes that have that index: `~FI_T:
UP` leaves costs and efficiencies untouched because they have no limit
type.

**Precedence.** In `~FI_T` and `~UC_T`, a qualifier in a value-column
header beats the row's own cell in that index's column, which beats the
tag text. In the other tags, the row's cell beats the tag text, and an
empty cell falls back to the tag text. Region-named columns take the
place of a `Region` column.

!!! warning "Always put the currency on cost tables"

    A cost table without a currency is read in the model's default
    currency (the first entry of `~Currencies`, often `USD00`). TIMES then
    converts the numbers through its deflators, which can silently change
    costs by tens of percent. Write it on the tag (`~FI_T: USD24`,
    `~TFM_INS: curr=USD24`), in a `~FI_T` header (`INVCOST~USD24`), or in
    a `Curr` column.

## Column headers

### Known columns and aliases

Each tag has a set of **known columns**, and most have several accepted
names (aliases): `TechName`, `process` and `pset_pn` all name the process
column of `~FI_T`. Headers are not case-sensitive. The
[tag catalog](reference.md) lists every column of every tag with its
aliases.

Two headers in one table that name the same known column (identical, or
two aliases of one column) are a fatal error: the sync stops and reports
them. (The check applies to tables that have data rows.)

### Value columns and header qualifiers

A header that is not a known column is a **value column**: it says what
the numbers below it are.

**In `~FI_T` and `~UC_T`**, a value-column header is split at `~` into
tokens, and each token must be a known element: an attribute, a year, a
region, a timeslice, a limit type, a currency or a commodity.

| Header | Meaning of the numbers in the column |
| --- | --- |
| `INVCOST` | attribute `INVCOST` |
| `PASTI~2015` | attribute `PASTI`, year 2015 |
| `ACT_BND~UP~2030` | attribute `ACT_BND`, limit type `UP`, year 2030 |
| `NCAP_COST~USD21` | attribute `NCAP_COST`, currency `USD21` |
| `UC_RHSRT~2030` | (in `~UC_T`) right-hand side for 2030 |
| `REG1` | region `REG1` (one column per region) |

A header whose tokens do not all resolve is reported as "column is not
recognized or invalid", and the column is not read.

**In the other tags** (`~TFM_INS`, `~TFM_DINS`, `~TFM_UPD`, `~TFM_MIG`,
…), a value-column header is **one** element, not split at `~`: a region
or region group, `AllRegions`/`Value`, or — in the
[layouts](data-tags.md#layouts-at-ts-tsl) — a year (`-TS`), an attribute
(`-AT`) or a timeslice (`-TSL`). A header such as `PASTI~2015` is not
read in these tags; give the year in a `Year` column or use a `-TS`
layout.

### Comment columns

A column whose header starts with `*` or `\I:` is a comment column and is
ignored. In `~FI_T`, any header containing `*`, `\I:` or `%` is ignored.
Such headers may repeat.

### Columns ignored for the whole model

Header names listed in [`~NOpCol`](system-settings.md#nopcol) are ignored
in every table of the model, and their warnings are suppressed. A listed
name is still read in a tag for which it is a known column: listing
`Sets` silences a stray `Sets` column next to a `~FI_T` table without
affecting the `Sets` column of `~FI_Process`.

## Comment rows

A data row is skipped when, in one of the table's index columns, its cell
starts with `\I:`, or starts with `*` in a column where `*` cannot be a
wildcard. Precisely:

- In columns that never hold patterns (`attribute`, `year`, `region`,
  `limtype`, `timeslice`, `currency`, `other_indexes`, value columns
  whose header contains `~`, …), a cell starting with `*` or `\I:` makes
  the row a comment.
- In columns that may hold patterns (`pset_*`, `cset_*`, `commodity`,
  `value`, …), only `\I:` does, because `*` there is a wildcard.

`\I:` is therefore the safe comment marker everywhere. Model Info → Veda
Tags shows which marker applies to each column of each tag.

## Values carried down the rows

In a few columns an empty cell takes the value of the nearest non-empty
cell above it in the same table:

| Tag | Column |
| --- | --- |
| `~FI_T` | `TechName` (process) |
| `~FI_Process` | `Sets` |
| `~FI_Comm` | `Csets` |
| `~UC_T` | `UC_N` |

So a process is named once on its first row in `~FI_T`, and the rows
below add more inputs, outputs or attributes to it. No other column is
carried down; in particular, years are not.

## Wide and long layouts

An index that is usually a column can instead be spread across columns,
one per element. Veda turns such a table into the equivalent long table
(one row per filled cell); empty cells produce nothing.

- **Regions.** A header that is a region name, or a region group (expanded
  to its regions), holds the value for that region. An `AllRegions`
  column holds the value for every region of the row that has no column of
  its own.
- **Years.** In the `-TS` layouts, headers that are years (and `0`) hold
  the time series.
- **Attributes.** In the `-AT` layouts, headers are attribute names.
- **Timeslices.** In the `-TSL` layouts, headers are timeslice names.

## Sheets

Every worksheet is read; sheet names carry no meaning, with two
exceptions: in the trade-links file the first letter of the sheet name
decides whether links are two-way (`B…`) or one-way
([Trade](trade.md#tradelinks)), and in `SubRES` files the sector of a
declaration is taken from the sheet name.
