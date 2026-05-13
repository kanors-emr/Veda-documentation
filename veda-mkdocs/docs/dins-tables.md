# DINS - Direct Insert tables

!!! note "Note"

    DINS tables are designed for adding large chunks of data, when it is
    fully enumerated.

| XX RFInput |           |                                                          |
| ---------- | --------- | -------------------------------------------------------- |
| S.No       | Attribute | Text                                                     |
| 1          | RFSwitch  | \*GG\* Set LevelizedCost/OBJ Method/Cost\_NPV switches   |
| 2          | RFSwitch  | $SET ANNCOST LEV                                         |
| 3          | RFSwitch  | $SET OBJ AUTO                                            |
| 4          | RFSwitch  | $SET OBLONG YES                                          |
| 5          | RFSwitch  | $SET MID\_YEAR YES                                       |
| 6          | RFSwitch  | $SET RPT\_OPT NCAP.1 -1                                  |
| 7          | RFCmd     | \*GG\* Invest $/HR split & UC/PRC\_MARK marginals to VBE |
| 8          | RFCmd     | RPT\_OPT('OBJ','1') = 1;                                 |
| 9          | RFCmd     | RPT\_OPT('COMPRD','4') = 1;                              |

| \~TFM\_DINS-AT |              |             |                                                          |
| -------------- | ------------ | ----------- | -------------------------------------------------------- |
| Pset\_PN       | RFCmd\_FLAGS | RFCmd\_GAMS | Other\_Indexes                                           |
| IMPNRGZ        | 1            |             | \*GG\* Set LevelizedCost/OBJ Method/Cost\_NPV switches   |
| IMPNRGZ        | 2            |             | $SET ANNCOST LEV                                         |
| IMPNRGZ        | 3            |             | $SET OBJ AUTO                                            |
| IMPNRGZ        | 4            |             | $SET OBLONG YES                                          |
| IMPNRGZ        | 5            |             | $SET MID\_YEAR YES                                       |
| IMPNRGZ        | 6            |             | $SET RPT\_OPT NCAP.1 -1                                  |
| IMPNRGZ        |              | 7           | \*GG\* Invest $/HR split & UC/PRC\_MARK marginals to VBE |
| IMPNRGZ        |              | 8           | RPT\_OPT('OBJ','1') = 1;                                 |
| IMPNRGZ        |              | 9           | RPT\_OPT('COMPRD','4') = 1;                              |
