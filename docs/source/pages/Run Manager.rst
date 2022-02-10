###########
Run Manager
###########

Overview
=========

* The Run Manager is used to compose and submit model runs (`YouTube video <https://youtu.be/3EkFqLyl5ZE>`_)
* Each model run is based on a Case definition comprising:
    * Scenarios
    * Regions
    * Settings
    * Properties

.. image:: images/run_manager_1.PNG
    :width: 600


Sections
=================

+++++++++++++++
Scenario Group
+++++++++++++++
Check BASE/SysSettings and the list of scenario to be included in a “cluster” that is then given a name for inclusion later in a Case Definition for a model run.

+++++++++
Settings
+++++++++
To designate where the GAMS and TIMES files reside, in what folder the model is to be run, the Maximum number of runs that are to be submitted in parallel, 
the Solver to be used and the Solver Options file to be employed.

+++++++++++++
Region Group
+++++++++++++
Designation of the regions to be included in the Group definition.

+++++++++++
Properties
+++++++++++
Which GAMS switches are to be employed for the run.

++++++
Cases
++++++
List of Cases prepared identifying the Run name/Description, Scenario Group, list of regions, the Property specification to be used, 
period definition and ending year, and date information.


DD and script files
===================

* There are three different possible structures of the GAMS_Wrk.. folder and sub-folders based on the following inputs:
    * Max Runs =1
    * Max Runs >1
    * Parametric scenario case (irrespective of Max Runs)

.. image:: images/dd_files.PNG
    :width: 600


Modifying RUN files
===================

There are new attributes to write TIMES switches or GAMS code at five different locations in the RUN file. Further, these declarations can also be made
at the top or bottom of scenario DD files (last two attributes in the table below). The attributes are supported by regular INS/DINS tables, in any scenario file or in SysSettings.


.. csv-table::
        :file: tables/times_switches/Times_switches_attr_loc.csv
        :widths: 1,1,1
        :header-rows: 1

There is no need to modify the RUN file template manually.

Commands will be ordered by Value column; only rows with value>0 will be considered.
If multiple scenarios send commands to the RUN file,
the blocks will be ordered as per the order of scenarios in the case definition.

.. note::
    This also opens up some new possibilities. For example, you can run parametric scenarios where base prices for elastic demands are picked up from different Reference cases.

These examples are available in the `Advanced Demo <https://github.com/kanors-emr/Model_Demo_Adv_Veda.git>`_ model.

.. csv-table:: Example 1
        :file: tables/times_switches/Example1.csv
        :widths: 20,35,15,5,50
        :header-rows: 2


If you want to use single quotes <'> in your instructions, then it is necessary to use a DINS table, as shown below. DINS tables need process or commodity specification. You can use any valid
process instead of IMPNRGZ; it will have no impact on the outcome.

.. csv-table:: Example 2
        :file: tables/times_switches/Example2.csv
        :widths: 20,50,30
        :header-rows: 2

Case definition
================
.. image:: images/case_definition.png
    :width: 400

* Create a New Case by providing the core information for the case definition (or copy an existing Case to create a starting point)
    * Case Name - name of the case
    * Description - description of the case
    * Scenario Group - scenarios to be included in this run
    * Region Group - regions to be included in this run
    * Parametric Group - driver scenario for a suite of runs
    * Properties Group - what GAMS options/switch are to be employed
    * Periods Definition - period definition for the run
    * Ending Year - last period for the run
    * Source TIMES - where does the TIMES code reside
    * Solver - which solver is to be used
    * Solver Options - which solver options to use
    * GDX References - GDX files to be used for freezing periods, elastic demand base prices or IRE bounds/prices


Model run submission
=====================

.. image:: images/cases_grid.png
    :height: 150

* Select one (or more) of the cases in the Managed Save Cases section and click SOLVE

* Solving a model opens a CMD window showing the GAMS solution log

.. image:: images/solve_cmd.png
