################
Version History
################

4.1.1.1 [21May25]
^^^^^^^^^^^^^^^^^

.. important::

   **New Feature in ADVANCED and ACADEMIC Licenses:** Veda now supports full interoperability between **TIMES** and **OSeMOSYS**!

   Two primary workflows are supported:
    * **Starting from OSeMOSYS CSVs**: Import data directly to seamlessly create OSeMOSYS or TIMES models.
    * **Starting from Veda Templates**: Any simple model built with Veda templates can now be viewed and executed as either TIMES or OSeMOSYS.
   Additionally, you can combine both workflows by starting from OSeMOSYS CSVs (treated as BaseYear templates) and further expanding your model using standard Veda input components like **SubRES** and **Scenario files**. A powerful use-case is conducting detailed sensitivity analyses around an existing OSeMOSYS reference case using Veda's parametric scenario files.


**ALL VERSIONS**

**[New]**

- Users can define and manage TIMES attributes with enhanced control - via UserTimesAttributes.xlsx file in the Model folder.
- Allows SysSettings to see seed values across all scenarios - including NSV and parametric scenarios.
- Introduces a new process IMPDUCZ to supply the dummy commodities used to relax User Constraints. `[See details] <https://forum.kanors-emr.org/showthread.php?tid=1213&pid=8049#pid8049>`_
- New ~FI_PROCESS_Trades tag supported in the Trade links file for better control on Trade processes.
- Improved support in tags INS, UC_T, R_E, and R_S in RegionGroup.
- RegionGroup can now be used in both rows and columns in FI_T Tag.

**[Enhancements]**

- Controlled Splitting of Other_Indexes `[See details] <https://forum.kanors-emr.org/showthread.php?tid=1367&pid=8043#pid8043>`_
- TFM_COMMGRP Tag can now be used in BY/SubRES files.
- Multiple UI upgrades including splash screen, grid icons, paddings, color schemes, and startup visuals.
- PostgreSQL Server version upgraded to 15.9.

**[Fixes]**

- Skip Fill-R Comparison When Output Sheet Is Missing.
- Fixed entries that were incorrectly marked with “X” for Timeseries Data Correction.
- Fix for Commodity Group Filtering in cset_set
- Removed Workbook Dependency in Excel Merge Logic
- Decimal Separator and Unit Conversion resolved in pivot and export formatting.
- Incorrect Numbers in Turkish Locales
- Excel Sheet Naming Restrictions replaces invalid characters with ~ in Batch Export.
- Validation on Sheet Name Entry for Results Views

**ADVANCED VERSION**

- Reporting enhancements
    * GIS Trades Enhanced with VAR_CAP and VAR_NCAP Support
    * Includes multiplication support, parent region mapping, and improved unit conversion to TS_Ratios.

4.0.0.0 [07Nov24]
^^^^^^^^^^^^^^^^^

**[Enhancements]**

- Introducing metadata in Veda.
- WildCard support for User Constraint field in INS and UPD tags.


3.2.1.0 [07Nov24]
^^^^^^^^^^^^^^^^^

.. note::
    Users of licenses with maintenance expiration before **October 25, 2024** are advised to use this version, which is the final release within the major version **3** (`download <https://github.com/kanors-emr/Veda2.0-Installation/releases/tag/v3.2.1.0>`_).


**[Enhancements]**

- Included XLSM (macro enabled) workbook tag reading which contains FILL tag. Such workbooks were earlier being skipped.
- Introduced a button for SubResTrans file in the Navigator grid
- Simplified import of VO runs in Veda2.0
- UI enhancements
- Set default relative tolerance in GDXDiff to 1e-4

**[Fixes]**

- Can't create new or view existing Table Master groups or select tables by filtering `#44 <https://github.com/kanors-emr/Veda2.0-Installation/issues/44>`_
- Expanded Excel export limit in Items List `#43 <https://github.com/kanors-emr/Veda2.0-Installation/issues/43>`_
- Enabled Excel export in Times and Veda Attributes `#43 <https://github.com/kanors-emr/Veda2.0-Installation/issues/43#issuecomment-2269648594>`_
- Shorter list of VDA_FLOP Deletions `#42 <https://github.com/kanors-emr/Veda2.0-Installation/issues/42#issuecomment-2452224383>`_
- Issue with UC on cum subsidies for period of years `[See details] <https://forum.kanors-emr.org/showthread.php?tid=1431&pid=7644#pid7644>`_
- Controversial handling of CG indexes by VEDA (FI_T) `[See details] <https://forum.kanors-emr.org/showthread.php?tid=1426&pid=7648#pid7648>`_
- Priority resolution of dimensions for tag processing `[See details] <https://forum.kanors-emr.org/showthread.php?tid=1426&pid=7598#pid7598>`_
- CG declarations in col headers `[See details] <https://forum.kanors-emr.org/showthread.php?tid=1426&pid=7614#pid7614>`_


3.1.3.0 [17Jul24]
^^^^^^^^^^^^^^^^^

**ALL VERSIONS**

    * [Enhancements]

        * Removed more spurious sync log entries from FI_T tag processing.
        * The announcements on Start page ("from the developers") will show up in higher security environments as well.

3.1.2.0 [13Jul24]
^^^^^^^^^^^^^^^^^

.. note::
    Reports and some other Advanced license features have been activated for the ETSAP license. This will be reviewed at the Winter 2024 ETSAP meeting.


**ALL VERSIONS**

    * [Enhancements]

        * **Major Enhancement**: New feature on right click on any file on the navigator - all tags supported for that particular file will be listed under the `Copy Veda-tag to clipboard` option.
        * New tag ~NOPCOL (No operation column headers) supported in SysSettings `See details <https://forum.kanors-emr.org/showthread.php?tid=1364&pid=7484>`_
        * Items view: Processes and commodities in the auxiliary flow boxes are also color-coded (as per the set membership) like they are in the main flow boxes.
        * Removed more spurious sync log entries from FI_T tag processing.
        * Search in Attributes master section looks at attribute description as well.
        * [Bugfix]: Handled a language issue in the new Fill-R data comparison feature.

**ADVANCED VERSION**

    * Multiple enhancements in Reports - focused on making it easier to create Sankey diagrams.


3.1.1.0 [27Apr24]
^^^^^^^^^^^^^^^^^

**ALL VERSIONS**

    * [Enhancements]

        * Enhanced data validation for Sync
        * Enhanced GDX file reference on Run Manager `See details <https://veda-documentation.readthedocs.io/en/latest/pages/Run%20Manager.html#managing-gdx-files>`_
        * Input validation - non-numeric values. `User request <https://github.com/kanors-emr/Veda2.0-Installation/issues/35>`_
        * Sync log warning if a single row uses seed values from multiple scenarios. `See details <https://forum.kanors-emr.org/showthread.php?tid=1377&pid=7380#pid7380>`_
        * Sync logs in a text file.  `User request <https://github.com/kanors-emr/Veda2.0-Installation/issues/39>`_
        * New user option to not write Fill-R tables if the contents have not changed. Turned on by default. `User request <https://github.com/kanors-emr/Veda2.0-Installation/issues/37>`_

    * [Fixes]
        * TFM_Fill-R tag writing during Sync was starting from cell B1 instead of A1 when column A was empty
        * Data type checking for hidden rows during tag reading
        * SolveTime reporting (GAMS version 32 or higher is required as a minimum).  `See details <https://github.com/kanors-emr/Veda2.0-Installation/issues/33>`_
        * Remove filter option from check all tables in result viewer.  `See details <https://github.com/kanors-emr/Veda2.0-Installation/issues/40>`_

**ADVANCED VERSION**

    * Multiple enhancements in Reporting, especially in creating Sankey diagrams.
    * Option on Run manager to automatically generate data to plot a histogram that guides the choice of cplex parameter `barcolnz`.


3.0.7.0 [23Feb24]
^^^^^^^^^^^^^^^^^

**ALL VERSIONS**

* [Enhancements]

    * IRE_XBND parameter handle `See details <https://forum.kanors-emr.org/showthread.php?tid=1348&pid=7171>`_
    * Enhanced QC of non-FI_T tags and DINS tags.
    * HiGHS solver made available on Run Manager.
    * TOP_IRE entries for trade processes coming from BY/SubRES `#28 <https://github.com/kanors-emr/Veda2.0-Installation/issues/28>`_
    * Enhanced GDX file reference on Run Manager

* [Fixes]

    * Units Conversion in Update Excel
    * A bug was introduced in version 3.0.3 with FI_T tag QC. DINS tables in BY/SubRES trans files **could** lead to duplication.


3.0.3.0 [26Jan24]
^^^^^^^^^^^^^^^^^

**ALL VERSIONS**

* [Enhancements]

    * Enhanced synchronization log for FI_T/UC_T tags.
    * Performance enhancements in set rules consolidation step of synchronization.
    * Several UI enhancements on Run Manager.

* [Fixes]

    * Blank spaces after the Minus sign are removed in exclusion rules.
    * Solving a case with multiple time slice definitions selected. `See details <https://github.com/kanors-emr/Veda2.0-Installation/issues/29>`_
    * Super region is now case insensitive.
    * Veda assigns dimension based on the element in FI_T/UC_T col headers and table tags. The allocation will be done in the following priority order: attribute,currency,lim_type,region,side,time_slice,year,commodity.

* [New]

    *  Veda version introduced in the title of LST files.
    *  Attrib_cond/Val_cond feature was purely a process filter so far. It now works as a process-commodity filter if the attribute in question has process and commodity indexes.

**ADVANCED VERSION**

    * Reporting variables that are generated to support SANKEY diagrams are not shown in the list of variables.
    * Multi-user support in Results and Reports views.

3.0.2.0 [18Dec23]
^^^^^^^^^^^^^^^^^

**ALL VERSIONS**
    * `ACT` and `NRG` will be recognized as commodity groups during the synchronization process.
    * Commodity definition has been added as a dependency dimension. So far Veda used process definition, seed values for UPD/MIG, and source data for FILL tables as dependency indicators.
    * Single-user view has been restored in Groups and Cases for Academic and Standard licenses. Multi-user support was enabled recently but it was causing `some confusion <https://github.com/kanors-emr/Veda2.0-Installation/issues/23>`_.
    * Synchronization window will close automatically (if no errors) when it opens to read SysSettings and Set definitions during Results and Sets processing operations.


**ADVANCED VERSION**
    * Improved indication of shared Groups on Run manager.

2.020.2.1 [18Dec23]
^^^^^^^^^^^^^^^^^

.. note::
    Users of licenses with maintenance expiration before **November 28, 2023** are advised to use this version, which is the final release within the major version **2.20** (`download <https://github.com/kanors-emr/Veda2.0-Installation/releases/tag/v2.20.2.1>`_).

    
* Single-user view has been restored in Groups and Cases for Academic and Standard licenses. Multi-user support was enabled recently but it was causing `some confusion <https://github.com/kanors-emr/Veda2.0-Installation/issues/23>`_.


3.0.1.0 [08Dec23]
^^^^^^^^^^^^^^^^^

.. caution::
    This is a major release. Your license should be under maintenance on **28 November 2023** to be able to use this version (and above)


**ALL VERSIONS**
    * **Major Enhancement**: Excel file reading and writing are now done using a third-party library `ASPOSE <https://products.aspose.com/cells/>`_. This makes the synchronization process much faster, and also more robust, because we no longer rely on the local Excel installation.
    * Duplicate column headers will be identified even if the duplication is on account of aliases. `See details <https://github.com/kanors-emr/Veda2.0-Installation/issues/11>`_
    * A warning will be issued if there are unsaved modifications in groups in the Run Manager. `See details <https://github.com/kanors-emr/Veda2.0-Installation/issues/17>`_

2.020.1.1 [10Nov23]
^^^^^^^^^^^^^^^^^^^

**ALL VERSIONS**

    * [Fixes] 
        * RES view in Item Details was missing some IRE process - UC links. `See details <https://github.com/kanors-emr/Veda2.0-Installation/issues/20>`_
        * Topology tags (TFM_TOPINS*) tags were not being processed in the correct order. This would create issues only if there were interdependencies within the topology tags.
        * Topology tags were not being read from SysSettings. See Information - Veda tags for all files where they are supported.
        * Removed spurious TOP_IRE entries. `See details <https://forum.kanors-emr.org/showthread.php?tid=1310>`_

    * [New] 
        *  Modules refreshed after Sync.
        *  Open Case Folder button on Run Manager.
        *  "Delete All" menu option in the groups and cases menu sets up groups and cases afresh from JSON files.
        *  Multiple UI enhancements on Run Manager

**ADVANCED VERSION**
        *  Commodity units displayed in Endogenous trade variable.
        *  Possible to use groups and cases created by other users.


2.018.1.1 [01Sep23]
^^^^^^^^^^^^^^^^^^^

**ALL VERSIONS**

    * Batch export did not work with some foreign languages - fixed.

**ADVANCED VERSION**

    * If there is a scenario map table in reports, the "Scen" column will appear in the Results view.

2.017.1.1 [10Aug23]
^^^^^^^^^^^^^^^^^^^

**ALL VERSIONS**

    * Export capacity from pivot table to xlsx is increased to 1.048 million rows.

2.016.1.1 [25Jul23]
^^^^^^^^^^^^^^^^^^^

**ALL VERSIONS**

    * Handling links in Excel files: Files with remote links were freezing the application during Sync process in some cases. Excel objects are now opened with the following settings:
        * Application.AskToUpdateLinks = False
        * Application.DisplayAlerts = False
        * getWorkbook=Workbooks.Open(bkPath,updatelinks:=0,readonly:=false)
    * CmdF_Top attribute introduced to inject code before the GAMS call in VTRUN.CMD file.

2.015.1.1 [14Jul23]
^^^^^^^^^^^^^^^^^^^

**ALL VERSIONS**

    * GAMS Engine: Users can specify namespace and model under GAMS Engine settings (Case Manager). This will enable users to use their own GAMS Engine account to launch runs in the cloud.
    * Attribute master: Interpolation option indication (green color) has been removed. Complete information on default I/E option is available in the table at the bottom of that form.
    * Case Manager: Select all option for saved cases.
    * Pop-ups will appear on the same screen as the application (when using multiple screens).

2.014.1.1 [08Jul23]
^^^^^^^^^^^^^^^^^^^

**ALL VERSIONS**

    * VA update: Process/commodity lists are shown on VA - as per the process/commodity filters.
    * Variables $case_name and $vd_file_name introduced in the VTRUN.CMD file, which can help automatic post-processing routines.
    * Display issues with 4k monitors and higher zoom levels have been fixed.
    * DD writing has been revamped. There is no change in the output but large models will see significant performance improvement.
    * Veda2.0 has two very powerful features for managing sets - Sets Browser and Sets Editor. They have been moved from the Tools section to a new module - Sets, hoping that visibility will make more users take advantage of this feature.

2.011.1.1 [27May23]
^^^^^^^^^^^^^^^^^^^

**ALL VERSIONS**

    * [Debug] update excel was writing only two decimals.
    * **Veda Assistant: Create Tag button on Information - Veda and TIMES parameters screen. We will call this VA**
    * Context menu on lists in Items View: You can copy items to clipboard from lists in Items View.
    * GDXDiff cleanup: GDX import - a legacy menu item has been removed. GDX and Model diff data is deleted when the application is launched.

2.010.1.7 [07May23]
^^^^^^^^^^^^^^^^^^^

**ALL VERSIONS**

    * [Debug] Default PCG allocation was wrong for some processes if parameter declarations triggered the creation of a single-commodity CG. Here is the streamlined logic:
        * PRC_PCG declaration via SysSettings has the highest priority.
        * PCG declaration via the primary_cg col of ~FI_Process has the second priority.
        * Veda default PCG will be used only if no declarations are found from the above sources.
        * If a parameter declaration triggers the creation of a single-member CG, which is also the commodity that Veda has identified as the default primary commodity, then the CG will be used (instead of the commodity) as PCG - ONLY FOR DMD processes.


2.010.1.4 [24Apr23]
^^^^^^^^^^^^^^^^^^^

**ALL VERSIONS**

    * [Debug] Enabling the CMD file edit parameters: CmdF_GAMS, CmdF_Title, and CmdF_bot.
        * **Note that these attributes will not be available under Veda online**.


2.010.1.1 [17Mar23]
^^^^^^^^^^^^^^^^^^^

**ALL VERSIONS**

    * [Debug] Tag time export from the Sync feedback form
    * Support new TIMES feature: Logit Market Share Allocation
    * The message "Selected files do not contain any Tag(s) which can be read with veda" has been suppressed
    * Information - Model - NSV Candidates: No-seed-value scenarios can be converted to Scen_NSV* directly via the UI
    * Sync performance improvement for large INS tables
    * PostgreSQL Server upgraded to version 14.6
    * Direct access to LST files for cases after run completion - in the Logs panel on Run Manager
    * Handled quotation marks in GAMS statements declared via RF/SFCMd tags
    * Support attribute PRC_GMAP

2.005.1.2 [21Oct22]
^^^^^^^^^^^^^^^^^^^

**ALL VERSIONS**

    * Bugfix: Submitting runs to GAMS Engine works again

2.005.1.1 [11Oct22]
^^^^^^^^^^^^^^^^^^^

**ALL VERSIONS**

    * New TIMES attribute NCAP_AFSX supported.
    * Bugfix: Parallel processing of SubRES files used to create deadlocks.
    * Sync performance enhancement (re-imports).

2.004.1.1 [11Sep22]
^^^^^^^^^^^^^^^^^^^

**ALL VERSIONS**

    * **Upgrade to PostgreSQL version 13**
    * **Retaining VD files is optional now.** `Details <https://veda-documentation.readthedocs.io/en/latest/pages/Run%20Manager.html#managing-output-files>`_ .
    * License key activations accessible directly via Help - License operations menu.
    * Several UI cleanups and enhancements.

**ADVANCED VERSION**
    * **Aggregation facility in Reports**

2.000.0.1 [24Jun22]
^^^^^^^^^^^^^^^^^^^

**ALL VERSIONS**

    * **Layout master functionality in pivot grids. See the new button to the left of Excel Export icon. This will be particularly useful in Reports**
    * Some topology defaults have been changed to Input in the FI_T tag. See Information - Veda parameters for details.
    * "Copy <element>" option available on right-click in the index areas of pivot grid.

**ADVANCED VERSION**
    * **Ratios of variables can be computed**
    * **Improved way to include exogenous data, like history or results from other models, in reports.**

1.253.1.1 [11Apr22]
^^^^^^^^^^^^^^^^^^^

**ALL VERSIONS**

    * **PostgreSQL Server updated to 13 (from 10.20)**
    * **~TimeSlices table is supported in regular scenario files**
    * View name and units information is included when copying from pivot grid to clipboard
    * Information - Veda tags has information on more tags

**ADVANCED VERSION**
    * **process and commodity map tables support all filters available in TFM tables (only name was available earlier)**
    * Significant improvement in Reports processing efficiency when working with a large number of scenarios

1.251.1.1 [05Mar22]
^^^^^^^^^^^^^^^^^^^

**ALL VERSIONS**

    * **PostgreSQL Server updated to 10.20 (from 10.16)**
    * **Table master functionality has been added to Results and Reports**
    * Date/time stamp added to Excel export from Items lists
    * Deleted items view improved and moved to Information - Model menu (from Tools)
    * A group named all_<Parametric scenario name> is created automatically for each parametric scenario
    * Items view - Commodity: Right-click on processes will point to the topology declaration

1.248.1.1 [07Feb22]
^^^^^^^^^^^^^^^^^^^

**ALL VERSIONS**

    * [Bugfix] Items list view was not loading

1.248.1.1 [05Feb22]
^^^^^^^^^^^^^^^^^^^

**ALL VERSIONS**

    * [Bugfix] GDXDiff records had stopped showing up in Browse after multiple tabs were allowed
    * UC_ATTR is now displayed in the Browse data grid
    * The following indexes are written in DD files without quotation marks: group, import_export, in_out, lim_type, name, parent, peak_time_slice, side, sow, stage, time_slice, time_slice_level, time_slice2, year, year2
    * Handling the case where UC names appear in multiple case formats (used to result in $172)
    * Parametric scenario group <Parscen name>_all is created automatically
    * Topology check can be disabled in UC_T with "No" in top_check column
    * ExRES can now be launched from pivot grid even when display type is different from "code only"
    * Parameters deleted during Quality checks is reported in the Sync log and under Tools - Delete logs menu

**ADVANCED VERSION**
    * **New feature - ModelDiff in Browse module: Another model can be selected and differences with the active model can be identified. It is like GDXDiff, but it works across models rather than cases. It can be very useful to see differences by data file when merging different versions of a model.**

1.247.1.3 [23Dec21]
^^^^^^^^^^^^^^^^^^^

**ALL VERSIONS**

    * [Bugfix] Export functionality from pivot grids was not working on some machines.

1.247 [15Dec21]
^^^^^^^^^^^^^^^

**ALL VERSIONS**

    * QA_Check log file will open automatically after the run if it reports "FATAL ERROR" or "INVALID PARAMETER".
    * Option to Compact Database under Tools menu.
    * Batch runs are launched in the order in which they appear in the list on Run Manager.
    * [Bugfix] DD files are written for one case at a time when Max Runs < 2.
    * When Restart Option is active in Run Manager, Region and period selections are dumped in a file <casename>_input_data.JSON.

**ADVANCED VERSION**
    * Reporting: WAttribute col in TS_Defs table can be used to compute dynamic weighted averages. See example in `Veda Adv Demo <https://github.com/kanors-emr/Model_Demo_Adv_Veda.git>`_.

1.244 [04Nov21]
^^^^^^^^^^^^^^^

**ALL VERSIONS**

    * Menu layout enhanced for convenience in Results module.

243 [25Oct21]
^^^^^^^^^^^^^

**ALL VERSIONS**

    * [Bugfix] User-defined sets were not available for processing if only BY_Trans was synchronized.
    * Several UI enhancements.

**ADVANCED VERSION**
    * Reporting: timeslice_map (like process_map and commodity_map) can be used create timeslice aggregations. For example, months and hours can be different dimensions.

242 [27Sep21]
^^^^^^^^^^^^^

**ALL VERSIONS**

    * [BugFix] related to lower case in Super-region name; introduced in version 241.

241 [25Sep21]
^^^^^^^^^^^^^

**ALL VERSIONS**

    * Any Base/SubRES import triggers Demand processing.
    * Runmanager: Scenario group refresh button appears on reordering cases (it used to appear only when on change of selections).
    * [Bugfix] Group delete in Case Manager.
    * Possible to import VD files without VDE/S/T (via Tools menu).
    * Control on sort order of views in Results and Reports.
    * Added search in all dropdown lists.
    * "Help" tab added in Veda menu.
    * User-defined CG will be usable in the commodity columns of Veda tables.
    * Process and commodity filters can be used in table tags. For example, ~TFM_INS: CSET_SET=DEM.
    * TSLVL and SIDE forced to be upper case.
    * UC_ATTR displayed under Items Detail of UC; also on mouseover (along with description) in Browse.

**ACADEMIC/STANDARD/ADVANCED**
    * **BrowseForm: multiple pivot tabs can be opened, like in Results. Use the "Add Pivot" button.**

**ADVANCED VERSION**
    * Several enhancements in Reports processing.

239 [23Aug21]
^^^^^^^^^^^^^

**ALL VERSIONS**

    * **Reports functionality will be available under all license types till 31 Dec 21.**
    * If a run fails for any reason, then the contents of command window will be displayed in a text file automatically.
    * Leading and trailing spaces will be removed each cell at the time of reading from Excel.
    * Excel export format improved.
    * Reporting of duplicate declarations improved (Information >> Model >> Manage Duplicates)

238 [07Aug21]
^^^^^^^^^^^^^

**ALL VERSIONS**

    * **Items detail view uses colors to indicate set membership and an icon to identify the PCG**
    * Mouseover in pivot grids displays numbers with full precision

**ADVANCED VERSION**

    * `Reports <https://veda-documentation.readthedocs.io/en/latest/pages/Reports.html>`_ section has been added in Veda documentation
    * TS_Defs tag supports fields "show_me" and "discard" to give more control over aggregations

237 [23Jul21]
^^^^^^^^^^^^^

**ALL VERSIONS**

    * Debug: Batch sync had stopped working in the previous version

**ADVANCED VERSION**

    * Major efficiency improvement in reports processing
    * Additional dimensions don't need the source dimensions in "group by" anymore

236 [17Jul21]
^^^^^^^^^^^^^

**ALL VERSIONS**

    * Debug: it was not possible to drag a case to the first position in Run Manager
    * Debug: unselecting SubRES was throwing an error during DD writing in some cases
    * Debug: Excel export from pivot grid was rounding numbers to two decimals
    * MaxRuns will apply to parametric scenarios as well
    * Localhost version uses port 65001 - will be easier to work on machines that have a non-Veda PostgreSQL installation
    * Date modified (instead of created) shown on VD file import form
    * GAMS engine credentials can be declared under user options

**ADVANCED VERSION**

    * perCapita and perGDP reporting

234 [26Jun21]
^^^^^^^^^^^^^

**ALL VERSIONS**

    * Several UI updates
    * A button on the top of pivot grids (in the center) to make pivot grids full screen on all forms where they appear
    * Absolute negative values can be declared prefixed with "~" in UPD/MIG tables.
        * Use case: ACT_BND FX can have ~-1 in the Interpolation options MIG table in SysSettings
    * Commodities selected for Browse will be searched in all commodity and commodity_group fields

**ADVANCED VERSION**

    * Report browser enhancements

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
    * Pivot Grids enhancement: Page field dimensions where items are being aggregated are highlighted with an orange line
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
