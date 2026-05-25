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
