# DINS - Direct Insert tables

!!! note "Note"

    DINS tables are designed for adding large chunks of data, when it is
    fully enumerated.

| **XX RFInput** | | |
| --- | --- | --- |
| **S.No** | **Attribute** | **Text** |
| 1 | RFSwitch | `*GG*` Set LevelizedCost/OBJ Method/Cost_NPV switches |
| 2 | RFSwitch | $SET ANNCOST LEV |
| 3 | RFSwitch | $SET OBJ AUTO |
| 4 | RFSwitch | $SET OBLONG YES |
| 5 | RFSwitch | $SET MID_YEAR YES |
| 6 | RFSwitch | $SET RPT_OPT NCAP.1 -1 |
| 7 | RFCmd | `*GG*` Invest $/HR split & UC/PRC_MARK marginals to VBE |
| 8 | RFCmd | RPT_OPT('OBJ','1') = 1; |
| 9 | RFCmd | RPT_OPT('COMPRD','4') = 1; |

| **~TFM_DINS-AT** | | | |
| --- | --- | --- | --- |
| **Pset_PN** | **RFCmd_FLAGS** | **RFCmd_GAMS** | **Other_Indexes** |
| IMPNRGZ | 1 | | `*GG*` Set LevelizedCost/OBJ Method/Cost_NPV switches |
| IMPNRGZ | 2 | | $SET ANNCOST LEV |
| IMPNRGZ | 3 | | $SET OBJ AUTO |
| IMPNRGZ | 4 | | $SET OBLONG YES |
| IMPNRGZ | 5 | | $SET MID_YEAR YES |
| IMPNRGZ | 6 | | $SET RPT_OPT NCAP.1 -1 |
| IMPNRGZ | | 7 | `*GG*` Invest $/HR split & UC/PRC_MARK marginals to VBE |
| IMPNRGZ | | 8 | RPT_OPT('OBJ','1') = 1; |
| IMPNRGZ | | 9 | RPT_OPT('COMPRD','4') = 1; |
