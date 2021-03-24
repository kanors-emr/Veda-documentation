#####################
Tags processing order
#####################
.. note::
    Here is the order in which files and tags are processed in Veda2.0. **|| indicates that multiple files/tables are processed on parallel threads**.

All files selected for synchronization are scanned for Veda tags, in parallel, and all identified tags are read as tables into PostgreSQL. Tags are processed in the following order:
    * || FI_process and FI_commodity (all BY and SubRES)
    * || FI_T (all BY and SubRES)
    * COMEMI, PRCCOMEMI, and COMMAGG
    * AVA
    * Trade links
    * COMGRP
    * TOPDINS and TOPINS
    * BY Trans (works with processes defined in BY workbooks and commodities defined in SysSettings + BY)
        * || DINS
        * INS
        * UPD
        * MIG
    * || SubRES trans (works with processes defined in own SubRES and commodities defined in SysSettings + BY + own SubRES)
        * || DINS
        * INS/UPD/MIG
    * Demands
    * Trade scenarios
        * || DINS
        * INS/UPD/MIG
    * Regular Scenarios
        * || DINS
        * INS/UPD/MIG
    * || NSV scenarios
        * || DINS
        * INS/UPD/MIG
    * || Parametric scenarios
        * || DINS
        * INS/UPD/MIG
    * || UC_T
    * SysSettings
        * || DINS
        * INS/UPD/MIG
