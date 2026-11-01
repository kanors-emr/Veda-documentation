# Not recommended

Some tags are still accepted so that existing models keep working, but
should not be used in new models. Veda no longer offers them when a table
is added (Excel Add-In, Veda's tag builder). They fall into three groups.

## Tags that still have an effect

These tags still produce model data. Each has a modern equivalent.

| Tag | Allowed in | Use instead |
| --- | --- | --- |
| `~COMEMI` | BY, SubRES | `~FI_T` or `~TFM_INS` with the commodity emission attribute `VDA_EMCB` |
| `~PRCCOMEMI` | BY, SubRES | `~FI_T` or `~TFM_INS` with the process emission attribute `FLO_EMIS` |
| `~COMAGG`, `~COMAGG_R1C2` | BY, SubRES | `~TFM_INS` with attribute `COM_AGG` |
| `~TFM_FILL` | trans, scenario files, SysSettings | [`~TFM_FILL-R`](fill.md) |

## Tags read as another tag

The suffix of these tags once told VEDA_FE's database the data type of
the value column. The type is now inferred from the values, and each of
them means exactly [`~TFM_UPD`](data-tags.md#tfm_upd).

| Tag | Read as |
| --- | --- |
| `~TFM_UPD-N` | `~TFM_UPD` |
| `~TFM_UPD-NS` | `~TFM_UPD` |
| `~TFM_UPD-T` | `~TFM_UPD` (it is **not** a time-series layout; that is [`~TFM_UPD-TS`](data-tags.md#layouts-at-ts-tsl)) |

## Retired tags

These tags are no longer part of the language: Veda2.0 accepts them
without error but produces nothing from them. Most belong to VEDA_FE
features that were not carried over. If you find one in a model, the
table it heads is not used; remove it, or rewrite it as shown. The names
stay reserved, so that no tool gives them a new meaning.

- `~FI_GenProcess`, `~FI_GenComm` — use [`~FI_Process`](res-templates.md#process-definition-table-fi_process) and [`~FI_Comm`](res-templates.md#commodity-definition-table-fi_comm).
- `~TFM_PINS`, `~TFM_CINS`, `~TFM_PCINS` — use [`~TFM_INS`](data-tags.md#tfm_ins).
- `~TFM_GAMS`, `~RFInput` — use the `RFCmd` / `RFSwitch` attributes ([below](#attributes-instead-of-tags)).
- `~Trade_Param` — use `~TFM_INS` / `~TFM_DINS` in a [trade workbook](trade.md#trade-workbooks).
- `~TradeLinks_GenLinks` — use [`~TradeLinks`](trade.md#tradelinks) or [`~TradeLinks_DINS`](trade.md#tradelinks_dins).
- `~UC_S` — use [`~UC_T`](user-constraints.md).
- `~COMAGG_R2C1` — use `~TFM_INS` with attribute `COM_AGG`.
- `~ImpSettings` — dummy imports are switched on and off in Veda's user settings.
- `~TFM_PCopy`, `~TFM_ADRCREATE`, `~TFM_AttribSet`, `~DRVR_Scenario` — no replacement.

## Attributes instead of tags

GAMS code and run-file switches that `~TFM_GAMS` and `~RFInput` once
carried are now ordinary attributes, written with `~TFM_DINS-AT` or
`~TFM_INS` on a dummy process such as `IMPNRGZ`:

| ~TFM_DINS-AT | | | |
| --- | --- | --- | --- |
| **pset_pn** | **RFCmd_FLAGS** | **RFCmd_GAMS** | **Other_Indexes** |
| IMPNRGZ | 1 | | `$SET ANNCOST LEV` |
| IMPNRGZ | 2 | | `$SET OBJ AUTO` |
| IMPNRGZ | | 3 | `RPT_OPT('OBJ','1') = 1;` |

The number in the attribute column orders the lines; the text in
`Other_Indexes` is the line written to the run file.
