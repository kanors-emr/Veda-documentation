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

## Tags with no effect

These tags are accepted without error but produce nothing. Most belong
to VEDA_FE features that Veda2.0 did not carry over. Remove them from
models, or rewrite them with the tag in the last column.

| Tag | Allowed in | Instead |
| --- | --- | --- |
| `~FI_GenProcess` | BY, SubRES | `~FI_Process` |
| `~FI_GenComm` | BY, SubRES | `~FI_Comm` |
| `~TFM_PINS`, `~TFM_CINS`, `~TFM_PCINS` | trans, scenario files | `~TFM_INS` |
| `~TFM_PCopy` | trans, scenario files | — |
| `~TFM_ADRCREATE` | BY_Trans, scenario files | — |
| `~TFM_GAMS` | trans, scenario files, SysSettings | the `RFCmd` attributes ([Run Manager](../run-manager.md)) |
| `~TFM_AttribSet` | SysSettings | — |
| `~ImpSettings` | SysSettings | dummy imports are set in Veda's user settings |
| `~RFInput` | SysSettings | the `RFCmd` / `RFSwitch` attributes |
| `~Trade_Param` | trade files | `~TFM_INS` / `~TFM_DINS` in a [trade workbook](trade.md#trade-workbooks) |
| `~TradeLinks_GenLinks` | trade-links file | `~TradeLinks` or `~TradeLinks_DINS` |
| `~UC_S` | SysSettings, scenario files | [`~UC_T`](user-constraints.md) |
| `~COMAGG_R2C1` | BY, SubRES | `~TFM_INS` with attribute `COM_AGG` |
| `~DRVR_Scenario` | demand files | — |

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
