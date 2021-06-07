################
Version History
################

233 [07Jun21]
^^^^^^^^^^^^^

**ALL VERSIONS**

    * Several UI updates; smoother loading of Navigator
    * Smart filter box color changed to dull orange - throughout the application
    * Excel export formatting improvement
    * GDXDiff imports files when Diff is requested and works much faster
        * No need to import GDX files via Tools menu
    * Added support for the following TIMES attributes: ACT_FLO, CM_GHGMAP, NCAP_BPME, NCAP_CDME, NCAP_CEH, NCAP_CLAG, NCAP_ISPCT, RCAP_BLK

**ADVANCED VERSION**

    * Report creation process smoother

231 [17Apr21]
^^^^^^^^^^^^^

**ALL VERSIONS**

    * Several UI updates on Start page and run mananger
    * Bulk CSV export faster
    * Debug: GAMS instructions were not being written to RUN and DD files
    * More layout changes are being saved in Appdata folder
    * Item Details in context menu along with ExRes
    * Parametric scenarios not imported in batch sync
    * Application reopens the modules that were open at the time of closing
    * Any GDX file can be used in reference section (only those produced on the current machine were usable earlier)
    * Tools menu - option added to open the folder with application error logs

**ADVANCED VERSION**

    * **Major update in default layout of Reports**

230 [31Mar21]
^^^^^^^^^^^^^

**ALL VERSIONS**

    * In pivot grids, elements are displayed for dimensions that are in the aggregated section, and have single items.
    * **Batch SYNC option available on Start page**
    * **Backup and Restore state options added in Model menu**
    * **Default layout settings enhanced (further) for pivot grids in all modules**

227 [12Mar21]
^^^^^^^^^^^^^

**ALL VERSIONS**

    * Default layout settings enhanced for pivot grids in all modules
    * Layouts can be saved with names in Browse

225 [05Mar21]
^^^^^^^^^^^^^

**ALL VERSIONS**

    * Automatic import of data GDX discontinued
    * Dbl-click on data values inserted by Veda shows appropriate messages
    * Veda checks for a healthy version of Excel on the machine
    * Windows alert sound while reading Excel files suppressed
    * **Default layout improved in all pivot grids**
    * **Layout can be saved with names in Browse**
    * **Item details pivot layout is saved, like ExRES**

219 [20Feb21]
^^^^^^^^^^^^^

**ALL VERSIONS**

    * License and maintenance status reflect on the main form
    * Application version displayed on bottom right of the screen (not on the title of main form anymore)
    * **localhost version should work on some machines where it did not**
    * **Results: View names QC for characters that are not permissible as Excel sheet names**
    * **Results: Close all button added**
    * **Results: views can be exported to CSV without loading into pivot grids**
    * **several enhancements on GDX reference forms (Run manager)**
    * **Debug: "too many clients" error when writing a large number of DD files (DD writing more efficient)**
    * **Debug: sub-totals were appearing after some pivoting operations**

**ACADEMIC/STANDARD/ADVANCED**

    * **Scenario groups (from Run manager) available to filter scenarios in Browse (like process/commodity sets)**

213 [25Jan21]
^^^^^^^^^^^^^

    * Debug: ExRes layout
    * Run manager: Filter added for GDX file lists
    * **Major efficiency improvement in Results refresh**
    * Right-click option to see Item details from Items lists, set browser, and set editor.
    * Commgrp handling for NCAP_AFC
    * Added a few process sub-types
    * Default TS for STG_CHRG = ANNUAL
    * Added a few missing attributes and set TS_OFF


205 [06Jan21]
^^^^^^^^^^^^^^

    * Bugfix: user-defined sets, as set specification for other set, were not working in the new sets editor functionality.
    * Bugfix: BRATIO under properties in Run manager was an integer field; it is now text so that it can be left blank.
    * **Browse enhancement: "Select in list" option on right-click in pivot grid, to select items in the filter lists.**
    * **ExRes: layout and filters are saved.**
    * **Pop-ups from the auxiliary EXEs, after run completion, have been suppressed.**

202 [25Dec20]
^^^^^^^^^^^^^

    * **Veda.FrontEnd.exe has been renamed as Veda2.0.exe**
    * Sets Browser: Processes and Commodities on different tabs
    * Batch export: Results.xlsx file has a time stamp and opens on creation
    * Pivot Grids enhancement: Page field dimensions where items are being aggregated are higlighted with an orange line
    * Subtotals option available in pivot grids
    * New functionality Information - Model - Manage duplicates: shows duplicate declarations of processes/commodities
    * Tools menu has a new item Sets, with browser and editor as sub-menus
    * **Sets editor: a major new functionality that allows interactive creation/editing/copying of sets. Definitions in Excel file are updated seamlessly.**

197 [12Dec20]
^^^^^^^^^^^^^

    * Attribute **RFCmd_bot** added to introduce GAMS commands at the bottom of RUN files
    * **Element descriptions on mouseover in Results pivot grids**

196 [06Dec20]
^^^^^^^^^^^^^

    * Bugfix: Information - Model - tag details had duplication
    * **RFCmd* and SFCmd* attributes can introduce GAMS code in RUN and DD files**
    * **Run manager: New menu item "Reorder scenarios" that makes it easier to manage scenario groups**
    * Start page: Right click on a folder to remove it from "New" section
    * Information - TIMES attributes updated to the current version of documentation

194 [02Dec20]
^^^^^^^^^^^^^

    * Bugfix: using ENDYEAR with the new ~Milestoneyears tag was producing a "0" in list of periods
    * Bugfix: resolved duplication in commodity-only attributes from SubRES
    * **Results - update Excel**
    * All SET COM entries appear in BASE.DD
    * Adding windows info in error log
    * Results will automatically read Sets definition file (on launch) if it has been modified
    * Veda_SnT to Excel migration.xlsm handles possible duplication in Setrules table of Veda_SnT.MDB
    * NSV candidates reporting improved; Open File button added
    * Arrow keys supported in PivotGrid

189 [21Nov20]
^^^^^^^^^^^^^

    * Bugfix: Processes no longer required to be in .VDS files
    * Bugfix: TS filtering (year2=0/1) was not able to ignore records that came from BASE
    * Dummy UC variables not created for non-binding constraints
    * Browse: Proc/comm units are displayed along with description on mouseover
    * Results: chart window visibility saved with view layout
    * Attribute master: Timeseries cell is green for attributes that are interpolated/extrapolated by default
    * Results: Cancel button to interrupt processing
    * No limit on length of model folder name
    * Disabled default loading of DemoS_012 model
    * **Units handling in Results [See ~UnitConversion table on Defaults sheet in SysSettings - DemoS models]**

182 [07Nov20]
^^^^^^^^^^^^^

    * Bugfix: bilateral trade processes with reg1=reg2 were getting deleted.
    * Bugfix: Parametric scenario selection was ignored while editing multiple cases.
    * Bugfix: RunManager layout changes were problematic; can restore default settings now.
    * **GamsWrk files (\*.VD, .LST, .GDX and QACheck) can be browsed and deleted using Model -> Manage disc space -> Text files, or the Text icon on Start page.**
    * Check introduced to trap GAMS path with spaces.
    * **Run manager now reports key solution metrics after runs finish.**

178 [28Oct20]
^^^^^^^^^^^^^

    * Added validations for Gams source folder selected for cases.
    * ExRes works from pivot grid in Results.
    * Sets file appears on Navigator and shows its Sync status.
    * SysSettings, BY-Tans and Sets files will be synced if inConsistent, without selecting any other file.
    * ~MileStoneYears table supports a new column "type", which can be used to declare an "EndYear" for each period specification. The milestone years don't need any value in this column.
    * More tags, like FI_Process/Comm included in Information-Model tags.
    * Seed values for UPD,MIG,FILL tags are based on a two-level sorting: If Scenario B looks for seed values that exist in SubRES S, and scenarios A and C, then the value from scenario A will be selected.

173 [20Oct20]
^^^^^^^^^^^^^

    * New feature: Tools - Sync AppData folder, to import/export results table definitions, scenario groups and cases from other users.
    * New feature: Direct specification of MILESTONEYEARS via new tags ~MileStoneYears and ~EndYear (optional), in SysSettings.


172 [16Oct20]
^^^^^^^^^^^^^

    * Bugfix: Results - batch export Excel file was locked in some cases.
    * Bugfix: Sync froze if SysSettings did not generate any records.
    * GAMS output had stopped appearing in CMD window for GAMS version 32+.
    * Handled the case where Sets col is blank in FI_Process/Comm tables. Defaults PRE/NRG apply.
    * UPD, MIG and FILL tags can handle complex operands now (\*-1, \*0,25, for example)


168 [10Oct20]
^^^^^^^^^^^^^

    * Bugfix: all but BY templates turned "not imported" after renaming scenario files.
    * Licensing included.
    * Veda_SnT to Excel migration.xlsm updated.
    * Start page now includes Recent and New models, and Veda News (pulled from the Internet).
    * Dummy commodities for UCs can be used in CSET_CN col of TFM tables.
    * GDX and VD manual import - Default folder location from Model settings.
    * TFM_DINS tables support UC_N col.
    * TS_filter col supported in TFM_INS-TS.
    * Multiple result views are exported on different sheets of a single Excel file.
    * No empty cells in Row header section of Excel export.


161 [24Sep20]
^^^^^^^^^^^^^

    * Bugfix: Process column was not showing the right values in AttributeMaster.
    * "Add new" button added in "Model" menu.
    * Delete for saved layouts of Results added on UserOptions form.


159 [19Sep20]
^^^^^^^^^^^^^

    * Results: Tool tip on scenario list: Date | VD file path | Model | User | Study.
    * Results: Unsaved tabs named with time stamp.
    * Bugfix: GAMS root settings were not being saved in some cases.
    * UI refinements in Run Manager, Navigator and Attributes master.
    * Known bug: Add dimension combo on Browse gets duplicate entries.


155 [13Sep20]
^^^^^^^^^^^^^

    * Combos for scenario groups on run manager, and on case definition form, now work as a filter box.
    * Multiple cases can be edited together.
    * Close button added on Sync feedback form.
    * Dependency check form debugged.
    * Attribute master revamped.


154 [08Sep20]
^^^^^^^^^^^^^

    * bugfix: Trade processes with multiple commodity types were getting multiple PCGs. Now they are assigned in the following priority order: DEM - MAT - NRG - ENV - FIN.
    * Performance improvement in AVA-C processing.
    * Sets browser introduced under Tools menu.
    * Model tags details enhanced (under Information - Model menu).


152 [05Sep20]
^^^^^^^^^^^^^

    * bugfix: TFM_AVA-C had introduced case-sensitivity in commodities.
    * batch export (CSV and Excel) for Results
    * All layout changes in Results, Navigator and Run manager are retained, across Veda updates as well.


148 [29Aug20]
^^^^^^^^^^^^^

    * TFM_AVA-C supported
    * User-defined CG recognized as valid commodity names by Veda (no implications on DD files)
    * UI enhancement in Results
    * Indication when sets selected in results tables have common elements
    * <Model>\Appdata\ folder has priority over the Resource folder for solver options files


145 [25Aug20]
^^^^^^^^^^^^^

    * bugfix: * as the first character in PSET_PN was ignoring rows in TFM_PSET; it applies only to SetName col.
    * Several UI improvements
    * Configuration of the dimension lists in Results section is saved


143 over 139 [22Aug20]
^^^^^^^^^^^^^^^^^^^^^^

    * Several UI changes in Run manager and Results
    * Icon on "New" button in navigator
    * gams check disabled for now
    * QC on length of case names
    * GAMS option RESLIM added under properties on Run manager
    * Toggle name/desc in pivot grid (process, commodity, attribute, uc; proc/comm sets pending)
    * backup xls files before conversion to xlsx/m
    * on double click in items list opens the definition in Excel
    * Veda tag information added for set definition tags