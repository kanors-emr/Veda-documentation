# Metadata tags

The `MD-*` tags attach metadata (provenance, source URLs, data version,
notes) to any value, technology, or commodity in the model. Each tag
targets a different *scope*:

| **Suffix** | **Scope** |
| --- | --- |
| `_W` | Workbook |
| `_S` | Worksheet |
| `_R` | Row (a single row in the table) |
| `_C` | Column (a single column in the table) |
| `_TR` | Table-row scope (multiple values in a single row of a table) |
| `_TC` | Table-column scope (multiple values in a single column) |

In real models the most commonly used forms are the inline `_R` and
`_S` variants — they sit next to (or above) the table they annotate,
so the metadata is co-located with the data it describes.

A single value can also carry its own metadata through an Excel note on
that cell — see [Cell notes](#cell-notes-md) below.

### ~MD-V_S (worksheet-scope value metadata)

Real example from `BY_Trans.xlsx :: pumped hydro` (row 1, immediately
above the table it annotates):

`~md-v_s: default parameters for pumped hydro - assuming 6h storage`

A single free-text annotation that applies to every value on the
sheet.

### ~MD-V_R (row-scope value metadata)

Real example from `BY_Trans.xlsx :: Elec`, annotating one row of a
`~TFM_INS` table. The `~md-v_r` cell sits at the end of the data row
itself, carrying free-text metadata for that single row:

```
PRC_AOFF | … | BOH-2027 | 1 | ELE,CHP | | *-STN-* | ~md-v_r: placeholder assumption on standby power generation capacity; date: 01-02-2025; author: Amit Kanudia
```

### ~MD_Dimensions

Lives in `SysSettings`. Administrators specify which **dimensions of
metadata** they wish to capture (e.g. *source*, *quality flag*, *last
updated*, *contact*) by listing them in this table. The dimensions
declared here become the recognised metadata field names that can
appear inside `~MD-*` cells anywhere in the model.

### Other metadata variants

The remaining `~MD-V_*`, `~MD-T_*`, and `~MD-C_*` variants follow the
same conventions as the two above — only the scope (workbook, column,
table-row, table-column) and the target (value vs. technology vs.
commodity) differ. The `_W` / `_S` forms are placed at the top of the
workbook or sheet; the `_R` / `_C` forms sit inline on the row or
column they annotate.

## Writing metadata text

The same syntax is used in every `~MD-*` cell and in every `~md:` cell
note:

```
dimension: value; dimension: value; free text
```

- Pieces are separated by `;`. Spaces around a piece are ignored.
- A piece with a colon is a **dimension**. Only the first colon counts,
  so values such as URLs (`url: https://…`) are kept whole.
- Dimension names are not case-sensitive (`Source:` = `source:`). The
  value keeps the case it was written in.
- A piece without a colon is **free text**. It goes to the `comment`
  field. Several free-text pieces are kept in the order they were
  written, joined with `; `. A piece repeated word for word is kept once.
- A dimension given twice in the same text: the **last** one wins
  (`source: B; source: A` → source `A`).
- A dimension with no value (`author:`) is ignored.
- Text with no dimension name (`: reviewed`) is kept as free text.
- A dimension that is not declared in `~MD_Dimensions` is not dropped:
  it is added to the comment as `;name:value`
  (e.g. `Sheet-level note ;reviewer:QA team`).

## How the scopes combine

A value can be covered by several metadata tags at once — for example a
workbook tag, a sheet tag and a row tag. They are combined per
dimension, with the more specific scope winning:

| **Order (lowest → highest)** | **Scope** |
| --- | --- |
| 1 | `_W` workbook |
| 2 | `_S` worksheet |
| 3 | `_TC` table-column |
| 4 | `_C` column |
| 5 | `_TR` table-row |
| 6 | `_R` row |
| 7 | Cell note (`~md:`) |

- **Dimensions** (source, author, date, …): the highest scope that sets
  a dimension wins. A dimension set only at a lower scope is still
  shown — so a row tag with just `author:` keeps the `source:` of the
  sheet tag.
- **Comments**: the comments of all scopes are kept, **one per line**,
  in the order above (workbook first, cell note last).
- A table-row (`_TR`) or table-column (`_TC`) tag applies only to the
  values of its own table. A sheet tag applies only to its sheet; a
  workbook tag to every sheet of the file.
- If a workbook has more than one `_W` tag of the same kind, only one is
  used and the sync log shows the warning *duplicate metadata tag
  declaration detected at the workbook level. This tag will be
  ignored.*

## Cell notes (~md:)

To give one value its own metadata, add an Excel **note** to the data
cell and write `~md:` followed by the usual metadata text:

```
~md: source: Cell survey 2026; author: Deepak; checked by hand
```

- The marker `~md:` is not case-sensitive. Text before it is ignored —
  this includes the author line Excel puts at the top of a note.
- A note may contain several `~md:` markers; the text after each one is
  read and the pieces are joined with `; `.
- A note without `~md:` is an ordinary Excel note and is not read.
- Notes work in every workbook that sync reads, with or without
  `~MD-*` tags in it. No setting is needed.
- Only notes on **data cells** are used. A note on a header or an empty
  cell has nothing to attach to and is ignored.
- A cell note is the **highest scope**: its dimensions replace those of
  every tag, and its free text is added as the last line of the
  comment.
- In parametric scenarios, a note in the parent workbook applies to the
  generated child scenarios.
- Editing or removing a note takes effect when that workbook is synced
  again.

Example — cell `I13` on `Con_ELC` is covered by a workbook, sheet,
table, column and row tag, and has the note above. The value ends up
with:

| **Dimension** | **Value** | **From** |
| --- | --- | --- |
| source | Cell survey 2026 | cell note |
| author | Deepak | cell note |
| date | 01-10-2026 | row tag (`~MD-V_R`) |
| version | 1.0 | workbook tag (`~MD-V_W`) |
| comment | one line per tag, then `checked by hand` | all scopes |

## Where metadata appears

- **Value metadata** (`~MD-V_*` and cell notes) is stored with each
  value and shown in the **Metadata** tab when browsing data.
- **Technology / commodity metadata** (`~MD-T_*`, `~MD-C_*`) is shown in
  the **Details** section of the Master form. When several records
  apply, each is shown on its own line.
