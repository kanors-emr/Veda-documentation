=====================
Migrating to Veda 2.0
=====================
This is an incomplete list of things to keep in mind, or do, when migrating to Veda2.0

Before you start
#################
• First time you import a new model folder, you may need resolve two types of issues that were working OK with old veda:
    * Multiple Veda tables in the same Excel range
        * Need to insert empty rows/cols around tables
    * Duplicate column names
        * Can append redundant info like ~ANNUAL or ~<baseyear> to differentiate columns. For example, if an FI_T table has two columns called “Input”, then one of them can be named “Input~2010” (if 2010 is the base year).

• Veda_SnT to Excel migration.xlsm, which is in the new Veda folder, can be used to migrate sets and table definitions from a VEDA_SnT.MDB file.

Things that are different
#########################

• interpolation settings table in SysSettings needs to be converted to a MIG table.
    • if updating with year=0 (without an actual seed value) then need to convert it to in INS
• text values like for PRC_TSL will need a new tag - TFM_INS-txt
• Not supported:
    • comm1/comm2 in matrix form trade links declarations
    • Trade parameter declarations in matrix form (~TRADE_Param)
        • There will be a utility to migrate trade links and parameters to alternate formats
• Sets-<Model name>.xls with sets declarations expected in model root folder, if user-defined sets are used in any TFM table.
    • There is a utility (Veda_SnT to Excel migration.xlsm) to export your current sets from a Veda_SnT.MDB file, if you don’t already have them in Excel. This utility also exports VBE views.
• Column “other_indexes” to be renamed to UC_N in any INS/DINS tables used to declare UC names.
• Ignore characters are not supported in unsupported columns. Exceptions: Unit, End-Use, TechDesc,..
• IRE_FLOSUM: bug fix. other_indexes should hold commodity2
• Sheet names in SubRES files had to start with sector names. This restriction has been removed
    • techs might appear in new regions unless controlled via AVA.
• “Deact~UC_T” was actually not respected earlier, but now it will be.
    • The previous version searched for *<tag>*, and the new one looks for <tag>*
• Blank cells in header rows used to mark the end of tables. Now each table will be read as per the "current region" of the table tag.
• Column position of FI_T/UC_T tags are not important anymore
    • extra columns would appear from tables where FI_T/UC_T tags were misplaced
• No QC of process/commodity/UC names. <list of characters> used to be replaced with "_".
    • Now the DD files are always written with <'> around each element and all names are retained as in their original form.
• The default year has been changed from the first milestone year to the start year. For example, if first period was 2008-2012, the default year would be 2010 in the previous version and 2008 in Veda2.0.
    • There is a new tag ~defaultyear: <year> to have direct control on this value. It defaults to start year.
• Table ~ImpSettings in SysSettings is no longer read. Dummy variables control is available under Tools – user options.
• Veda2.0 does not provide any default costs for dummy imports. Very high default costs for dummy imports often created numerical issues for solvers. Users should use appropriate costs for IMP*Z processes in SysSettings or some other scenario file.
• Veda2.0 doesn’t refresh files while reading them
    • Veda2.0 opens files as Excel objects to search for tags and to establish the range to be read for each tag, and closes them without saving. Then they are read as XML via Exceldatareader in a second pass. Multiple files are processed in parallel for searching as well as reading. This approach has resulted in a major performance improvement and it is far more robust.
        • Files are still refreshed and saved in cases where Veda writes to them – any scenario or trans file with FILL tables and parametric scenarios.
    • Old Veda makes temp copies of files before reading them, so they are refreshed if the calculation mode is set to automatic. Each file is read in via an Excel object, which makes Excel practically unusable during the entire Sync process.


Migration steps
###############
• `Download Veda 2.0 <https://github.com/kanors-emr/Veda2.0-Installation>`_
• Update the current VEDA_FE and VEDA_BE
• Get the latest TIMES code from `this link <https://github.com/etsap-TIMES/TIMES_model>`_.
• Make a copy of the model and activate in current Veda
• Check option “Create data-only GDX” under Tools-user options
• Advanced functions – case master – export
    • To export current case definitions
• Run a Ref case from current Veda
    .. image:: images/old_veda_ref_case.png
• Edit the templates for points in :ref:`Things that are different`.
• Install and launch Veda2.0 and point it to the model
• Convert XLS to XLSX/M from Tools menu
• Migrate set and table definitions using Veda_SnT to Excel migration.xlsm
• Synchronize
    • You may have to edit templates for conflicting ranges and duplicate col names in tables
    • Will need to synchronize from scratch in this case
• Open the Run Manager and set GAMS root path
• Click Restore cases under Settings
    .. image:: images/restore_case_run_manager.png

    • This will import cases as scenario groups
    • File must be named <modelname>_exportedCases.csv
• Create a Ref case and Solve
• Compare input data (GDXDiff) and results.


