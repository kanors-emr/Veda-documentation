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


DD and script files
===================

* There are three different possible structures of the GAMS_Wrk.. folder and sub-folders based on the following inputs:
    * Max Runs =1
    * Max Runs >1
    * Parametric scenario case (irrespective of Max Runs)

.. image:: images/dd_files.PNG
    :width: 600


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
