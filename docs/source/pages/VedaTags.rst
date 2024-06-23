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


~FI_Process
^^^^^^^^^^^
This tag defines processes. The only other way to create processes is via the Trade links table.

~FI_Commodity
^^^^^^^^^^^^^
This tag defines commodities. The following commodities (climate module) can be used without being defined:
BEOHMOD,CH4-ATM,CH4-GTC,CH4-LO,CH4-MT,CH4-PPB,CH4-PPM,CH4-PREIND,CH4-UP,CO2-ATM,CO2-GTC,CO2-LO,CO2-PPM,CO2-PREIND,CO2-UP,CS,DELTA-ATM,
DELTA-LO,EXT-EOH,FORCING,GAMMA,LAMBDA,N2O-ATM,N2O-GTC,N2O-LO,N2O-MT,N2O-PPB,N2O-PPM,N2O-PREIND,N2O-UP,PHI-AT-UP,PHI-CH4,PHI-LO-UP,PHI-N2O,PHI-UP-AT,PHI-UP-LO,
SIGMA1,SIGMA2,SIGMA3,TOTCH4,TOTN2O.

~FI_T
^^^^^
Preparing input data for models usually imposes a significant data processing burden on the modeler because the input is expected in a particular format, which is different from the format
that is used to maintain the data.

The data workhorses
===================

The TFM (Transformation) tags enable bulk insert or update of parameters in a **rule-based manner** - via technology/commodity filters that are based on set membership, shortname, description,
and topology. It is also possible to include existing parameters (and their values) as filter criteria.

~TFM_INS
^^^^^^^^

Variants:
    * `TFM_INS-AT`: value fields have `attributes` as column headers.
    * `TFM_INS-TS`: value fields have `years` as column headers.
    * `TFM_INS-TSL`: value fields have `timeslices` as column headers.

~TFM_DINS
^^^^^^^^^

Variants:
    * `TFM_DINS-AT`: value fields have `attributes` as column headers.
    * `TFM_DINS-TS`: value fields have `years` as column headers.
    * `TFM_DINS-TSL`: value fields have `timeslices` as column headers.

~TFM_UPD
^^^^^^^^

Variants:
    * `TFM_UPD-AT`: value fields have `attributes` as column headers.
    * `TFM_UPD-TS`: value fields have `years` as column headers.

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
^^^^^^^^^^^

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