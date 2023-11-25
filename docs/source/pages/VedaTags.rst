#########
VEDA Tags
#########

This section describes the genesis and design purpose of the Veda syntax, which started with the Flexible Import tag - **~FI_T** - in Excel VBA at the turn of the 21st century.
Various tags and conventions have evolved over two decades to serve the `core design philosophy of Veda <https://veda-documentation.readthedocs.io/en/latest/pages/introduction.html#philosophy-and-core-principles>`_.

Regions and Time dimension
==========================
The system settings file (SysSettings) supports some tags that specify the basic structure of the model in terms of regions, time periods,
time slices, currencies and units.

~BookRegions_map
^^^^^^^^^^^^^^^^


~StartYear
^^^^^^^^^^^
The first year of the model horizon.

~TimePeriods
^^^^^^^^^^^^


~MileStoneYears
^^^^^^^^^^^^^^^
This is an alternate way to specify the model periods - by directly specifying the milestone years for which the model will run.
TIMES computes the period spans automatically when milestone years are specified. The last year of the model horizon can be specified (optional).

~DefaultYear
^^^^^^^^^^^^
The default year to be used for any timeseries parameter.

~Currencies
^^^^^^^^^^^

~DefUnits
^^^^^^^^^

Getting started with the RES
============================
These tags define the key elements - processes and commodities, and the topology and core parameters. These tags don't support wild cards


~FI_Process
^^^^^^^^^^^

~FI_Commodity
^^^^^^^^^^^^^

~FI_T
^^^^^

The data workhorses
===================

These tags enable bulk insert or update of parameters via technology/commodity filters that are based on set membership, shortname, description,
and topology. It is also possible to include existing parameters (and their values) as filter criteria.

~TFM_INS
^^^^^^^^

Variants:
    * `TFM_INS-TS`:
    * `TFM_INS-AT`:
    * `TFM_INS-TSL`:

~TFM_DINS
^^^^^^^^^

Variants:
    * `TFM_DINS-TS`:
    * `TFM_DINS-AT`:
    * `TFM_DINS-TSL`:

~TFM_UPD
^^^^^^^^

Variant:
    * `TFM_UPD-TS`:
    * `TFM_UPD-AT`:

~TFM_MIG
^^^^^^^^

~TFM_FILL
^^^^^^^^^

To create sets
===============

~TFM_CommGrp
^^^^^^^^^^^^

~TFM_PSets
^^^^^^^^^^

~TFM_CSets
^^^^^^^^^^

Other Tags
==========

~UC_T
^^^^^

~TFM_INS-txt
^^^^^^^^^^^^
This works exactly like the INS tag, but supports **text values** for the following Veda attributes that can be used to override values that come from the original process/
commodity definition tables: PRC_PCG, PRC_TSL, PRC_VINT, COM_LIM, COM_TSL, COM_TYPE.

~COMEMI
^^^^^^^^^^^
**This is a legacy tag. Use attribute VDA_EMCB via any regular Veda tag instead.**

~PRCCOMEMI
^^^^^^^^^^
**This is a legacy tag. Use attribute FLO_EMIS via any regular Veda tag instead.**