##########
Main Menu
##########
* Model
    * Add new: to add new model folder. (Better done via the Start page)
    * Select: to select from models that have already been synced. (Better done via the Start page)
    * Manage disc space: shows all models and the associated GDX/VD files.
    * Stop server and Exit: to stop PosgreSQL server and exit (only in the localhost installation).
* Modules: to launch the main functions:
    * Navigator (keyboard shortcut F6) - to see all Excel files that are included in the model.
    * Browse (F7) - for a tabular view of the input data - across all Excel files.
    * Items List - lists of all items - processes, commodities, commodity groups, and user constraints.
    * Items Detail (F8) - to see topology and input parameters for items.
    * Run Manager (F9)  - to define and run cases.
    * Results (F10) - to analyse model output.
* Information
    * TIMES attribute: presents all the TIMES model generator attributes/parameters.
    * VEDA tags: list of all VEDA tags by template (e.g.~FI_T).
    * Model:
        * Sync log: the synchronization log that is displayed at the end of the synchronization process.
        * NSV candidates: scenarios that can be converted to "no seed value" scenarios, because they don't provide seed values to any other scenario.
        * UD sets usage: usage of user-defined sets in different data files.
        * Tag details: processing time by data table.
        * Manage duplicates: displays duplicate declarations of processes and commodities across files.
* Tools
    * User Options:
        * Syncing options:
            * Threads count: Number of cores used by Veda can be restricted. -1 will use all cores of the machine during Synchronization and DD writing.
            * Dummy imports: Dummy imports will be created by default for the selected commodity types. Dummy commodities can also be created for user constraints.
        * Layout settings: To restore the saved layouts to default ones.
        * GAMS Engine: To declare GAMS engine credentials.
    * Update TIMES Code: to update the TIMES source code.
    * Delete Log: to delete model log files.
    * Convert XLS to XLSX/M: converting xls files into xlsx/m files.
    * Jacobian Analysis: this option can be used to improve the scaling of models, showing all equations (and variables) where the largest and smallest coefficients are different by more than 4 orders of magnitude.
    * Import GDX Files: to import data GDX files.
    * Import VD Files: to import VD files.
    * License information: to deactivate licenses or to change the license key (deactivate first).
    * Sets
        * Browser
        * Editor: this is a very powerful functionality that also updates the set definitions in the Excel file.
* Reports: available only in the advanced version.
    * Select: to select one of the reports that have been created.
    * Create: to create a new report.