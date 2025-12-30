#####################
Tags processing order
#####################
.. note::
    Here is the order in which files and tags are processed in Veda2.0. **|| indicates that multiple files/tables are processed on parallel threads**.

.. warning::
    
    **Parallel processing requires unique declarations**: Because FI_process and FI_commodity tags are processed in parallel, duplicate or inconsistent declarations can lead to non-deterministic results. Each commodity and process must be declared exactly once with consistent attributes. See the FI_COMM and FI_PROCESS sections in VedaTags documentation for details.

All files selected for synchronization are scanned for Veda tags, in parallel, and all identified tags are read as tables into PostgreSQL. Tags are processed in the following order:
    * || FI_process and FI_commodity (all BY and SubRES)
    * || FI_T (all BY and SubRES)
    * COMEMI, PRCCOMEMI, and COMMAGG
    * AVA
    * Trade links
    * COMGRP
    * TOPDINS and TOPINS
        * Across all files - BY_Trans, SubRES_Trans and scenario files.
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
    * || UC_T
        * UC tags collected till this point are processed so that they are fully available for modifications in parametric scenarios.
    * || Parametric scenarios
        * || DINS
        * INS/UPD/MIG
    * || UC_T
    * SysSettings
        * || DINS
        * INS/UPD/MIG
