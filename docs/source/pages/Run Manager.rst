===============
Run Manager
===============


Overview
#########

* The Run Manager is used to compose and submit model runs (`youtube video <https://youtu.be/3EkFqLyl5ZE>`_)
* Each model run is based on a Case run definition comprised  of:
    * Scenarios
    * Regions
    * Settings
    * Properties

.. image:: images/run_manager_1.PNG
    :width: 600


DD and script files
###################

* There are three different possible structure of the GAMS_Wrk.. Folder and sub-folders based on the following inputs.
    * Max Runs =1
    * Max Runs >1
    * Parametric scenario case (irrespective of Mas Runs)

.. image:: images/dd_files.PNG
    :width: 600


Case definition
###############
.. image:: images/case_definition.png
    :width: 400

* Create a New Case by providing the core information for the case definition (or start from an existing Case)
    * Case Name - case run name
    * Description - run description
    * Scenario Groups - scenarios to be included in this run
    * Region Groups - regions to be included in this run
    * Parametric Groups - driver scenario for a suite of runs
    * Properties Groups - what GAMS options/switch are to be employed
    * Periods Definition - what periods is the model be run for
    * Ending Year - what is the last period for the run
    * Source TIMES - where does the TIMES code reside
    * Solver - which solver is to be used
    * Solver Options - which solver options to use
    * GDX References - gdx to be used


Model run submission
####################

.. image:: images/cases_grid.png
    :height: 150

* Ticking one (or more) of the available cases in the Managed Save Cases and clicking SOLVE a model run start

* Solving a model opens a CMD window showing all of the GAMS steps and the model solution

.. image:: images/solve_cmd.png
