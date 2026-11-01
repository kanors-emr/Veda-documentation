# Processing order

When a model is synchronized, Veda reads every selected workbook (in
parallel), then applies the tables in a fixed order. The order matters in
two ways: a rule can only find what has already been built, and when two
rows of one layer set the same value, the one applied later wins
([Files and layers](files-and-layers.md#each-layer-is-processed-on-its-own)).
Between layers, which value a case uses is decided by the case order
instead ([Cases](files-and-layers.md#cases)).

**||** marks steps whose files or tables are processed in parallel.

## 1. The base model

1. **||** `~FI_Process` and `~FI_Comm` in all `VT_*` and `SubRES_*`
   files, and `~FI_Comm` in `SysSettings`.
2. **||** `~FI_T` in all `VT_*` and `SubRES_*` files.
3. The tags that are [not recommended](not-recommended.md) but still
   have an effect: `~COMEMI`, `~PRCCOMEMI`, `~COMAGG`, `~COMAGG_R1C2`.
4. `~TFM_AVA` / `~TFM_AVA-C` / `~ReplicateInRegions`: repository
   processes and commodities are placed in their regions.
5. Trade links.
6. `~TFM_COMGRP`.
7. The [topology tags](topology.md), by file type in the order
   `BY_Trans`, `SubRES_*_Trans`, trade, regular, NSV, `SysSettings`; for
   each type, `~TFM_TOPDINS` and then `~TFM_TOPINS`.

!!! warning "Declare each process and commodity once"

    Because the declaration tables are read in parallel, two
    declarations of the same process or commodity with different
    characteristics (for example two timeslice levels) give a result that
    can change from one sync to the next. Declare each item exactly once.

## 2. The layers

Then each layer is built, one after another, in this order:

1. `BY_Trans`.
2. **||** `SubRES_*_Trans` files.
3. Demand projections.
4. Trade layers, by name.
5. Regular layers, by name, one at a time.
6. **||** No-seed-value layers.
7. `~UC_T` tables collected so far, so that parametric layers can modify
   the user constraints.
8. Parametric layers.
9. `~UC_T` tables of the parametric layers.
10. `SysSettings`.

Within each layer's workbook, the tag types are applied in this order:

1. `~TimeSlices`
2. `~TFM_FILL-R`
3. `~TFM_DINS` (and variants)
4. `~TFM_INS` (and variants)
5. `~TFM_UPD` and `~TFM_MIG` (and variants), side by side

Within one tag type, tables are taken by file name, sheet position, tag
row and tag column, and each table row by row. So within a layer, a UPD
row always comes after every INS row, wherever the two sit on the sheet,
and a row further down a table comes after the rows above it.

!!! warning "UPD and MIG on the same item"

    `~TFM_UPD` and `~TFM_MIG` of one layer run side by side and do not see
    each other's output. If both write the same item, which one survives
    is not defined. Keep such rules in separate layers, or combine them in
    one tag.

Rules in `~TFM_UPD` and `~TFM_MIG` read their seeds from the layers that
are already finished ([seed values](files-and-layers.md#seed-values)),
not from rows of their own table: the rows of one UPD table are
independent of each other. Conditions (`attrib_cond`, `val_cond`) also
see what earlier `~TFM_DINS` / `~TFM_INS` rows of the same layer wrote.
