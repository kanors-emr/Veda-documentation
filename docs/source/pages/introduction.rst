============
Introduction
============
VEDA means “Knowledge” in Sanskrit. It is a software tool to convert modelers knowledge into model input, and numerical output from models into knowledge.
Veda2.0 is a data handling system for The Integrated MARKAL-EFOM System (TIMES) - a bottom-up optimization model for energy-environment systems.
It is based on a modular approach that organizes the model input data, and results, into an integrated database.
Information is visible via tabular browsing (data cubes) and network diagrams.
It is used to develop and manage model runs and to analyse model results.

Philosophy and core principles
    * Most of the data used by energy modelers is already in spreadsheets, or it can get there easily. The interface should be able to read formats that analysts find intuitive, rather than forcing them to enter information via a separate UI.
    * Assumptions should be expressed in the original form; data preprocessing should be minimal.
    * System should be modular – easy to activate/deactivate/replace sectors or regions. Different analysts should be able to work on different sectors or regions in parallel.
    * Structures and data that is common across regions should be declared only once.
    * Different layers of assumptions should coexist so that they can be activated/deactivated/permuted at run-time.


All VEDA-TIMES model input data is organized in Excel workbooks. Veda then integrates information from all of these workbooks into a single database to generate a TIMES model.
    * The models managed by VEDA-FE are stored in a specific folder (by default \\VEDA\\VEDA_Models). Within this folder, there is a sub-folder for each individual model a user is working with, including all of the VEDA-TIMES Demo Models ((\\VEDA\\VEDA_Models\\DemoS_001, etc.).
    * Model results are stored, for each model name, in a specific folder Veda\\GAMS_WrkTIMES\\<model name>.
    * e.g. for DemoS_012 will be Veda\\GAMS_WrkTIMES\\DemoS_012

.. image:: images/data_flow_and_files.PNG
    :width: 700


