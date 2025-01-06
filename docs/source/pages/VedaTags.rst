#########
VEDA Tags
#########

This section describes the genesis and design purpose of the Veda syntax, which started with the Flexible Import tag - **~FI_T** - in Excel VBA at the turn of the 21st century.
Various tags and conventions have evolved over two decades to serve the `core design philosophy of Veda <https://veda-documentation.readthedocs.io/en/latest/pages/introduction.html#philosophy-and-core-principles>`_.

Regions and Time
================
The system settings file (SysSettings) supports some tags that specify the basic structure of the model in terms of regions, time periods,
time slices, currencies, and units.

~BookRegions_map
^^^^^^^^^^^^^^^^
The concept of `BookRegions` serves a core Veda principle that `structures that are common across regions should be declared only once`.
This applies to the `BaseYear templates` that exist in the root of the Veda model folder.
They are named as `VT` (Veda Template) _ `BookRegion` _ `Sector` _ `Version`.
For example, a model may have 'VT_ElecReg_ELC_v01' and 'VT_DemReg_EndUse_v01' in the root folder to describe electricity supply in the first file
and the demand in the second one. ElecReg could map to Electricity grid regions, which is a reasonable way to represent electricity supply, and DemReg could map to states or provinces, which is
a reasonable way to represent demands.

This tag maps the book region (also called `super region`) to model regions. All declarations in base year templates that do not have a region
specification apply to all regions mapped to their book region.

~StartYear
^^^^^^^^^^^
The first year of the model horizon.

~TimePeriods
^^^^^^^^^^^^
To specify period lengths. TIMES automatically computes the middle years as milestone years (along with the StartYear).

~MileStoneYears
^^^^^^^^^^^^^^^
This is an alternate way to specify the model periods - by directly specifying the milestone years for which the model will run.
TIMES computes the period spans automatically when milestone years are specified. The last year of the model horizon can be specified (optional).

~DefaultYear
^^^^^^^^^^^^
The default year to be used for any timeseries parameter.

~Currencies
^^^^^^^^^^^
List of currencies used in the model. The first entry in this table works as the `default currency` in Veda.

~DefUnits
^^^^^^^^^
This tag is used to declare the default process (activity and capacity) and commodity units by sector.

Getting started with the RES
============================
These tags define the key elements - processes, commodities, topology, and core parameters. **These tags don't support wild cards**.


Commodity Definition Table (~FI_COMM)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The **Commodity Definition Table (~FI_COMM)** is used to declare the non-numerical characteristics of commodities in the model. Each commodity must be declared only once within these tables to avoid conflicts, such as inconsistent attributes (e.g., different time slice levels).

The **~FI_COMM** table is supported in B-Y templates, SubRES files, and the SysSettings template. For large and complex models, a best practice is to centralize all commodity declarations in a single template, such as the SysSettings template, to maintain consistency and avoid duplication.

Valid column headers for the **~FI_COMM** table are described in Table 1 below. Their order in the table can be changed.

**Best Practice:**
Declare commodities only once in a single template location to prevent errors or conflicting definitions.


Table Layout and Usage
----------------------
Figure 7 illustrates how a **~FI_COMM** table is used. Each commodity is declared once with its associated attributes and properties.

.. figure:: path/to/figure7.png
   :alt: Example of ~FI_COMM Table
   :align: center
   :figclass: align-center

   Figure 7: Example of a Commodity Definition Table (~FI_COMM)

Valid Column Headers
--------------------
The valid column headers for a **~FI_COMM** table are listed below (refer to Figure 7 for context):

.. list-table::
   :header-rows: 1

   * - **Header**
     - **Description**
   * - **Csets**
     - The sets to which commodities belong. Valid entries are:
       - ``NRG`` (energy)
       - ``MAT`` (material)
       - ``DEM`` (demand service)
       - ``ENV`` (emissions)
       - ``FIN`` (financial)
       *Note:* These declarations are inherited until the next entry is encountered.
   * - **Region**
     - Specifies the region. By default, it applies to all regions unless explicitly declared.
       *Note:* This column is used only in B-Y templates and is not allowed in SubRES files.
   * - **CommName**
     - The name of the commodity (e.g., ``COA`` for coal).
   * - **CommDesc**
     - A description of the commodity (e.g., "Solid Fuels").
   * - **Unit**
     - The unit associated with the commodity throughout the model (e.g., ``PJ``).
       *User Responsibility:* Ensure unit consistency throughout the model.
   * - **LimType**
     - Defines the sense of the balance equation for the commodity.
       Valid entries:
       - ``LO`` (Production >= Consumption, default for all but MAT commodities)
       - ``FX`` (Production = Consumption, default for MAT commodities)
       - ``UP`` (Production <= Consumption)
   * - **CTSLvl**
     - Specifies the commodity time-slice tracking level.
       Valid entries:
       - ``ANNUAL`` (default)
       - ``SEASON``
       - ``WEEKLY``
       - ``DAYNITE``
   * - **PeakTS**
     - Defines peak time slice monitoring.
       Valid entries:
       - ``ANNUAL`` (default)
       - Specific time slices defined in the SysSettings file (comma-separated).
   * - **CType**
     - Indicates electricity and heat commodities.
       Valid entries:
       - ``ELC`` (electricity)
       - ``HTHEAT`` (high-temperature heat)
       - ``LTHEAT`` (low-temperature heat)

*Note:* Comma-separated elements are allowed in fields like **Csets** and **PeakTS**.



Example Table
-------------
Below is an example of a **~FI_COMM** table for commodity definitions:

.. list-table::
   :header-rows: 1

   * - **~FI_COMM**
     - **CommName**
     - **CommDesc**
     - **Csets**
     - **Unit**
     - **LimType**
     - **CTSLvl**
   * -
     - COA
     - Solid Fuels
     - NRG
     - PJ
     - LO
     - ANNUAL
   * -
     - ELEC
     - Electricity
     - NRG
     - PJ
     - FX
     - SEASON

In this example:
- ``COA`` is defined as a solid fuel energy commodity, measured in petajoules (PJ), with a default limit type of ``LO`` and time-slice tracking at the ``ANNUAL`` level.
- ``ELEC`` is defined as an electricity commodity with a balance equation of ``FX`` and time-slice tracking at the ``SEASON`` level.


Best Practices
--------------
1. Declare each commodity only once to prevent conflicts.
   *Tip:* Centralize declarations in the SysSettings template for large models.
2. Ensure consistent use of units across the model for all commodities.
3. Verify attributes such as **LimType** and **CTSLvl** for correctness, particularly when working with complex time-slice structures.
4. Use comma-separated entries cautiously and only where appropriate, such as for time-slice monitoring (**PeakTS**).

By adhering to these practices, users can efficiently manage commodity definitions and avoid potential modeling errors.


.. note::

    The following commodities (climate module) can be used without being defined:
    BEOHMOD,CH4-ATM,CH4-GTC,CH4-LO,CH4-MT,CH4-PPB,CH4-PPM,CH4-PREIND,CH4-UP,CO2-ATM,CO2-GTC,CO2-LO,CO2-PPM,CO2-PREIND,CO2-UP,CS,DELTA-ATM,
    DELTA-LO,EXT-EOH,FORCING,GAMMA,LAMBDA,N2O-ATM,N2O-GTC,N2O-LO,N2O-MT,N2O-PPB,N2O-PPM,N2O-PREIND,N2O-UP,PHI-AT-UP,PHI-CH4,PHI-LO-UP,PHI-N2O,PHI-UP-AT,PHI-UP-LO,
    SIGMA1,SIGMA2,SIGMA3,TOTCH4,TOTN2O.


Process Definition Table (~FI_PROCESS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The **Process Definition Table (~FI_PROCESS)** is used to declare the **non-numerical characteristics** of processes in Veda. Each process must be defined only once in this table, and it serves as the foundational structure for assigning essential attributes like process name, description, activity unit, capacity unit, and more. These tables are supported in both Base-Year (B-Y) Templates and SubRES files.

.. note::

   The **~FI_PROCESS** table provides a flexible layout: the column order can be changed, and valid entries for each header are well-defined.

Key Features
------------
1. **Process Declaration**
   - Each process is declared only once using its name, description, and associated attributes.
   - Supported in B-Y Templates and SubRES files. However, region declarations are only valid in B-Y templates.

2. **Non-Numerical Attributes**
   - This table focuses on defining process characteristics rather than numerical data.

3. **Flexible Layout**
   - The order of columns is user-defined, as long as valid headers are used.

4. **Region-Specific Data**
   - Region declarations can be used in B-Y Templates but are not allowed in SubRES files.


Valid Column Headers
--------------------
The following are valid column headers for the **~FI_PROCESS** table:

.. list-table::
   :header-rows: 1

   * - **Header**
     - **Description**
   * - **Sets**
     - Sets to which processes belong, indicating the process type.
       Valid entries include:
            - ``ELE``: Thermal or other power plant
            - ``CHP``: Combined heat and power
            - ``PRE``: Generic process
            - ``DMD``: Demand device
            - ``IMP``: Import process
            - ``EXP``: Export process
            - ``MIN``: Mining process
            - ``HPL``: Heating plant
            - ``IPS``: Inter-period storage
            - ``NST``: Night storage device
            - ``STG``: General timeslice storage
            - ``STS``: Simultaneous DayNite/Weekly/Seasonal storage
            - ``STK``: Combined DayNite/Weekly/Seasonal and inter-period storage.
   * - **Region**
     - Specifies the region(s) where the process exists (comma-separated entries allowed).
       - Default: Applied to all regions if not specified.
       - Valid only in B-Y templates (regional data for SubRES processes must be provided in ``SubRES_<sector>_Trans`` files).
   * - **TechName**
     - The name of the process (e.g., ``MINCOA1``), up to 32 characters.
       - Recommendation: Limit to 27 characters to account for potential VEDA2.0 additions (e.g., for vintaging or dummy imports).
   * - **ProcessDesc**
     - A descriptive name for the process (e.g., ``Domestic supply of Solid Fuels Step 1``), up to 255 characters.
   * - **Tact**
     - The activity unit of the process (e.g., ``PJ``). Users must ensure unit consistency.
   * - **Tcap**
     - The capacity unit of the process. Users must ensure unit consistency.
   * - **Tslvl**
     - The operational time-slice level of the process.
       Valid entries:
           - ``ANNUAL``
           - ``SEASON``
           - ``WEEKLY``
           - ``DAYNITE``
       Default behavior:
           - ``DAYNITE`` for ``ELE``, ``STGTSS``, and ``STGIPS`` processes.
           - ``SEASON`` for ``CHP`` and ``HPL`` processes.
           - ``ANNUAL`` for all other process types.
   * - **PrimaryCG**
     - The Primary Commodity Group (PCG) of the process.
       - Normally, this is left unspecified as VEDA assigns a default PCG.
       - Specify only if overriding the default or creating a new PCG.
   * - **Vintage**
     - Indicates whether the process uses vintage tracking.
       Valid entries:
           - ``YES``: Vintage tracking enabled.
           - ``NO`` (default): Vintage tracking disabled.

.. note::
   Comma-separated entries are allowed for applicable columns (e.g., ``Region``, ``Sets``).


Example Layout
--------------
Below is an example of a **~FI_PROCESS** table:

.. list-table::
   :header-rows: 1

   * - **~FI_PROCESS**
     - **Region**
     - **TechName**
     - **ProcessDesc**
     - **Tact**
     - **Tcap**
     - **Tslvl**
   * -
     - US
     - MINCOA1
     - Domestic supply of coal
     - PJ
     - MW
     - ANNUAL
   * -
     - US
     - EXPCOA1
     - Export process for coal
     - PJ
     - MW
     - DAYNITE


Best Practices
--------------
- **Consistency:** Ensure consistency in units for activity (``Tact``) and capacity (``Tcap``).
- **Region-Specific Data:** Use the ``Region`` column only in B-Y templates, and provide SubRES process regional data in appropriate SubRES transaction files.
- **Naming:** Keep process names concise (maximum 27 characters recommended) to avoid issues with internal naming extensions in VEDA2.0.
- **Default Values:** Allow defaults (e.g., ``Tslvl``, ``PrimaryCG``, ``Vintage``) unless specific customizations are required.

By defining processes in the **~FI_PROCESS** table, users create a robust framework for modeling non-numerical characteristics, ensuring clarity and consistency across the energy system model.


Flexible Import Table (~FI_T)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Preparing input data for models usually imposes a significant data processing burden on the modeler because the input is expected in a particular format, which is different from the format
that is used to maintain the data.

The **Flexible Import Table (~FI_T)** is a versatile table used primarily to create the model topology, defining process inputs, outputs, and parameters in Base-Year (B-Y) templates and SubRES files. Its flexible structure allows users to specify parameters and their numerical values with minimal intervention. Data is imported as provided, without modification during the import process.


Key Features
------------
1. **Flexible Structure**
    * The table layout can be adapted to match source data, minimizing preprocessing efforts.
    * Indexes for attributes such as region, year, and timeslice can be specified as either row identifiers or column headers.

2. **Direct Data Import**
    * Data is not altered or expanded during import.
    * This behavior is consistent with the **UC** tables (see Section 2.4.7), making it ideal for precise, user-defined parameter definitions.

3. **Row and Column Organization**
    * Row identifiers and column headers define the dimensions for data rows.
    * Numerical data is input directly into the corresponding cells.

Layout and Regions
------------------
The **~FI_T** table consists of six distinct regions:
    .. image:: images/use_FIT_table.png
        :width: 600
        :height: 300
        :align: center

1. **Row ID Column Headers**
   These columns define the dimensions for data rows. Valid headers are listed below (see Table 3 for details):

   - **Region**: Declares the region.
   - **TechName**: Declares the technology name.
   - **Comm-IN / Comm-IN-A**: Input commodities / Auxiliary input commodities.
   - **Comm-OUT / Comm-OUT-A**: Output commodities / Auxiliary output commodities.
   - **Attribute**: Defines the attribute (e.g., ``DEMAND``, ``ACT_BND``).
   - **Year**: Specifies the year(s); comma-separated values are allowed.
   - **TimeSlice**: Specifies time slices; comma-separated values are allowed.
   - **LimType**: Specifies limit types (``UP``, ``LO``, ``FX``, ``N``).
   - **CommGrp**: User-defined commodity group.
   - **Curr**: Currency declaration.
   - **Stage / SOW**: Multi-stage decision points and states of the world for stochastic models.
   - **Other_Indexes**: Special dimensions required by certain attributes (e.g., ``EnvLimit`` attributes).

   *Note: Comma-separated elements are allowed in these headers.*

2. **Row Identifiers**
    The specific elements for the dimensions defined in the row ID column headers.

3. **Data Area Column Headers**
    Columns define additional dimensions for the data. These can include:

    - Attribute
    - Year
    - TimeSlice
    - LimType
    - Commodity
    - CommGrp (internal VEDA groups only: ``DEMO``, ``DEMI``, ``NRGO``, etc.)
    - Region
    - Currency

   *Multiple dimensions can be combined in column headers, separated by a ``~``.*

4. **Data**
   Numerical values that correspond to the row and column dimensions.

5. **Table-Level Declarations**
   Global declarations in the table header (following a colon ``:``) apply to all data without an explicit index value.
   Example:
   ``~FI_T: DEMAND`` assigns ``DEMAND`` as the attribute for all rows lacking a specific attribute.

6. **Comments**
   Comment rows can be identified by:

   - A ``*`` character at the beginning of any cell in the row.
   - A ``\I:`` prefix, which is safer and avoids confusion with wildcard or operation symbols.

Example Layout
--------------
.. list-table::
   :header-rows: 1

   * - **~FI_T**
     - **Region**
     - **TechName**
     - **Comm-IN**
     - **Attribute**
     - **2020~UP**
   * -
     - US
     - PowerPlant1
     - Coal
     - ACT_BND
     - 500
   * -
     - US
     - PowerPlant1
     - NaturalGas
     - ACT_BND
     - 200

In this example:
- The table defines activity bounds (``ACT_BND``) for the ``PowerPlant1`` process in the ``US`` region for the year 2020.
- Coal has an upper bound of 500, and Natural Gas has an upper bound of 200.

Best Practices
--------------
- Ensure row and column dimensions are clearly defined and consistent.
- Use the ``~FI_T`` placement correctly, preceding the first data column to allow for flexible row identifiers.
- Use table-level declarations to simplify repetitive data entries.
- Avoid using ``*`` for comments when it might conflict with wildcard usage; prefer ``\I:`` for clarity.

By leveraging the flexibility of the **~FI_T** table, users can efficiently configure process inputs, outputs, and parameters, aligning the model structure with source data seamlessly.


The data workhorses
===================

The TFM (Transformation) tags enable bulk insert or update of parameters in a **rule-based manner** - via technology/commodity filters that are based on set membership, shortname, description,
and topology. It is also possible to include existing parameters (and their values) as filter criteria.

DINS, INS, and UPD Tables
^^^^^^^^^^^^^^^^^^^^^^^^^

Veda supports three main transformation table types for inputting data:**DINS (Direct Insert)**, **INS (Insert)**, and **UPD (Update)**. Each serves a distinct purpose, with varying degrees of efficiency and complexity depending on the dataset's structure and the modeling requirements.

.. important::

   The **~TFM_DINS** tag offers the highest processing efficiency, followed by `~FI_T <#flexible-import-table-fi-t>`_ and **~TFM_INS**.

   Tags **~TFM_UPD** and **~TFM_MIG** are the least efficient. Whenever possible, users are encouraged to use **DINS** or **INS**, provided the logic can be transferred.


1. ~TFM_DINS (Transformation Direct Insert Tables)
--------------------------------------------------
**Purpose:**
~TFM_DINS is the preferred table type when the dataset is fully enumerated, meaning all fields are explicitly defined without any wildcards or comma-separated lists.

**Key Characteristics:**
- **Processes** are identified using only the ``pset_pn`` column.
- **Commodities** (if applicable) are defined explicitly via the ``cset_cn`` column.
- **No wildcards** (e.g., ``?``, ``*``) or **comma-separated values** are allowed.

**Advantages:**
- The most efficient tag.

**Use Case:**
When all model elements are clearly defined in advance, such as a process-specific bound (``ACT_BND``) applied to individual processes without any `rules`.

2. ~TFM_INS (Transformation Insert Tables)
------------------------------------------
**Purpose:**
INS is the general-purpose table for inserting new data into the database. It allows for greater flexibility in specifying model elements.

**Key Characteristics:**
- Supports **wildcards** (e.g., ``ALL``, ``*``) and **comma-separated values** in fields like ``pset_pn`` and ``cset_cn``.
- Inserts **absolute values** directly into the database without referencing existing seed data.

**Advantages:**
- Provides flexibility for users who work with less granular or generic data definitions.
- Easy to use for scenarios where exact enumeration is not required.

**Use Case:**
    .. image:: images/use_TFM_INS.png
       :width: 400

In this example from DemoS_001, it is used to declare three new attributes
(G_DYEAR, Discount, and YRFR) by row.

3. ~TFM_UPD (Transformation Update Tables)
------------------------------------------
**Purpose:**
UPD is used when data modifications depend on the presence of existing seed values in the database.

**Key Characteristics:**
- Performs **numerical transformations** on seed values (e.g., multiplying or dividing an existing value).
- Supports **conditional insertion**, where new data is added only if a corresponding seed value exists.
- Requires prior existence of seed data `in an alphabetically inferior scenario` in the database.

**Advantages:**
- Ensures data integrity by operating conditionally on existing entries.
- Enables dynamic adjustments of seed values without overwriting them.

**Use Case:**
    .. image:: images/use_TFM_UPD.png
        :width: 850
        :height: 100

In this figure it sets default prices (ACTCOST) for the backstop dummy processes for energy commodities (IMP*Z - dummy IMPort processes ending with “Z”)
and demands (IMPDEMZ - a dummy IMPDEMZ process that can feed any demand). Note that the process and attribute MUST already have been specified for the qualifying process. Though
not shown in the example above the data specification field may also contain operators (+, *, -, /) there the resulting value is applied to the existing value for the qualifying processes.

.. note::

   **UPDate and Replacing Data:**
   UPDate is sometimes confused with replacing data. Any of these tags will replace data if they exist in ``BY_Trans`` or ``SubRES`` trans files and data for the same indexes has been declared in the ``BY`` or ``SubRES`` files. Otherwise, they will simply create new entries in the scenario where they exist. The "replacing" will happen if this scenario file appears after the scenario with the original data in the **scenario group** selected for the case.

Comparison of DINS, INS, and UPD
--------------------------------
.. list-table::
   :header-rows: 1

   * - **Feature**
     - **DINS**
     - **INS**
     - **UPD**
   * - **Data Enumeration**
     - Fully enumerated
     - Supports wildcards/lists
     - Relies on existing data
   * - **Wildcards / Comma-Separated Values**
     - Not allowed
     - Allowed
     - Not applicable
   * - **Seed Data Requirement**
     - Not required
     - Not required
     - Required
   * - **Primary Use Case**
     - Explicit, enumerated data
     - Flexible data insertion
     - Conditional modifications
   * - **Performance**
     - Fastest
     - Moderate
     - Slowest

Best Practices
--------------
- Use **DINS** wherever possible for maximum efficiency, especially when handling large datasets that are fully enumerated.
- Use **INS** for flexible data insertion when working with generic definitions or multiple entries defined using wildcards or lists.
- Use **UPD** sparingly, only for cases where transformations or conditional insertions are explicitly required, as it involves additional computational overhead.

By understanding the distinct roles and advantages of each table type, users can optimize their data preparation workflows and improve overall model performance.


.. tip::

    By default, **DINS**, **INS**, and **UPD** tables use **regions** (or ``Value/AllRegions``) as the data value column headers. However, there are scenarios where it is beneficial to organize data differently, such as: 1. **Improving Table Readability:** Wider tables with alternative column headers can reduce data preprocessing and make data easier to interpret. 2. **Enhancing Efficiency:** Minimizing the number of rows in a table reduces the processing overhead for rule application.

    To support these needs, Veda provides several variants of **DINS**, **INS**, and **UPD** tables. These variants allow the user to specify **attributes**, **years**, or **timeslices** as value column headers.

    ~TFM_INS Variants
    The **~TFM_INS** variants offer flexible table layouts for inserting data. The following variants are available:

    - **TFM_INS-AT:**
      The value fields use **attributes** as column headers.

    - **TFM_INS-TS:**
      The value fields use **years** as column headers.

    - **TFM_INS-TSL:**
      The value fields use **timeslices** as column headers.

    ---

    ### ~TFM_DINS Variants
    The **~TFM_DINS** variants allow fully enumerated data to use alternative column headers. The following variants are supported:

    - **TFM_DINS-AT:**
      The value fields use **attributes** as column headers.

    - **TFM_DINS-TS:**
      The value fields use **years** as column headers.

    - **TFM_DINS-TSL:**
      The value fields use **timeslices** as column headers.

    ---

    ### ~TFM_UPD Variants
    The **~TFM_UPD** variants allow update tables to organize value fields differently. The supported variants include:

    - **TFM_UPD-AT:**
      The value fields use **attributes** as column headers.

    - **TFM_UPD-TS:**
      The value fields use **years** as column headers.

    Example Table Layouts
    **TFM_INS-TS Example**
    .. list-table::
       :header-rows: 1

       * - **~TFM_INS-TS**
         - **Region**
         - **TechName**
         - **Attribute**
         - **2020**
         - **2025**
       * -
         - US
         - PowerPlant1
         - ACT_BND
         - 500
         - 550
       * -
         - US
         - PowerPlant2
         - ACT_BND
         - 300
         - 320

    In this example:
    - The value fields use **years** (2020, 2025) as column headers.
    - Each row specifies the activity bounds (`ACT_BND`) for a technology in a region.


     **TFM_UPD-AT Example**
    .. list-table::
       :header-rows: 1

       * - **~TFM_UPD-AT**
         - **Region**
         - **TechName**
         - **2020~UP**
         - **2025~UP**
       * -
         - US
         - PowerPlant1
         - ACT_BND=500
         - ACT_BND=550
       * -
         - US
         - PowerPlant2
         - ACT_BND=300
         - ACT_BND=320

    In this example:
    - The value fields use **attributes** (`ACT_BND`) as column headers, enabling a compact layout for multiple attributes.


     Best Practices
    1. **Choose Variants Wisely:**
       Select a table variant that aligns with the structure of your source data to minimize preprocessing.

    2. **Keep Tables Wide:**
       Wider tables (fewer rows) are more efficient, as they reduce the rule processing required for each row.

    3. **Simplify Preprocessing:**
       Use the variant that closely matches your source data layout, reducing the need for manual restructuring.

    4. **Fully Enumerate Data for DINS Variants:**
       Ensure all data is fully enumerated (no wildcards or lists) when using **DINS** variants for optimal performance.


    By leveraging these variants, users can efficiently configure their tables for improved readability and reduced computational overhead, while ensuring that data aligns seamlessly with Veda’s processing structure.





~TFM_MIG
^^^^^^^^

~TFM_FILL-R
^^^^^^^^^^^

To create sets
===============
The following tags enable creation of named groups of processes and commodities.

~TFM_CommGrp
^^^^^^^^^^^^

~TFM_PSets
^^^^^^^^^^

~TFM_CSets
^^^^^^^^^^

Other Tags
==========

~Tradelinks
^^^^^^^^^^^

~Tradelinks_DINS
^^^^^^^^^^^^^^^^

~Tradelinks_Desc
^^^^^^^^^^^^^^^^


~UC_T
^^^^^

~TFM_INS-txt
^^^^^^^^^^^^
This works exactly like the INS tag, but supports **text values** for the following Veda attributes that can be used to override values that come from the original process/
commodity definition tables: PRC_PCG, PRC_TSL, PRC_VINT, COM_LIM, COM_TSL, COM_TYPE.

~TFM_TOPINS
^^^^^^^^^^^

~TFM_TOPDINS
^^^^^^^^^^^^

Legacy Tags
===========
It is not recommended to use these tags anymore, but they are still supported for backward compatibility reasons.

~COMEMI
^^^^^^^^^^^
Use attribute VDA_EMCB via any regular Veda tag instead.

~PRCCOMEMI
^^^^^^^^^^
Use attribute FLO_EMIS via any regular Veda tag instead.

~TFM_Fill
^^^^^^^^^
Use TFM_Fill-R instead.

Wildcard Support
================

The columns **PSET_PN**, **PSET_PD**, **PSET_CO**, **PSET_CI** (for process filters), and **CSET_CN**, **CSET_CD** (for commodity filters) support the use of comma-separated entries, with wild cards ,
in all TFM tables apart from DINS:

1. **Comma-Separated Entries**:
   You can specify multiple entries in these columns by separating them with commas (`,`).

   Example:
   ``Process1,Process2,Process3``

2. **Wildcards**:
   Wildcards allow flexible and broad pattern-matching for process or commodity names.

Wildcards Overview
^^^^^^^^^^^^^^^^^^

1. **Asterisk (`*`)**:
   - Acts as a **multi-character wildcard**, matching zero or more characters.

     Examples:
       - ``Elec*`` matches ``Elec``, ``Electricity``, ``ElecGen``, etc.
       - ``*Gen`` matches ``ElecGen``, ``HeatGen``, etc.

2. **Question Mark (`?`) or Underscore (`_`)**:
   - Acts as a **single-character wildcard**, matching exactly one character.

     Examples:
       - ``Tech_?`` matches ``Tech_A``, ``Tech_B``, etc.
       - ``Fuel_?`` matches ``Fuel_X``, ``Fuel_Y``, etc.

3. **Square Brackets for Literal `_`**:
   - If you want to refer to `_` as an actual character (not a wildcard), enclose it in square brackets ``[ ]``.

     Example:
       - ``Tech[_]_`` matches ``Tech_A``, ``Tech_B``, etc.

Examples
^^^^^^^^

**Process Set Columns (PSET_...)**

- Entry: ``PSET_PN``

  - Value: ``Elec*``
    Matches: ``Electricity_Generation``, ``ElecStorage``, etc.

  - Value: ``Fuel?_Gen``
    Matches: ``Fuel1_Gen``, ``Fuel2_Gen``, etc.

  - Value: ``Tech_[_]X``
    Matches: ``Tech_X``.

**Commodity Set Columns (CSET_...)**

- Entry: ``CSET_CN``

  - Value: ``Elec, Heat*``
    Matches: ``Elec``, ``Heat``, ``HeatPump``, etc.

  - Value: ``Gas?_Supply``
    Matches: ``Gas1_Supply``, ``Gas2_Supply``, etc.