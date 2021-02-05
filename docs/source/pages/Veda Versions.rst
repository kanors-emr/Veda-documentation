=============
Veda Versions
=============
There are three different versions of Veda2.0: Basic, Standard, and Advanced. The basic version works on a single core, but is still much faster than VEDA_FE/BE.
Standard version uses multiple cores for certain operations, like processing FI_T and DINS tags, and writing DD files. In smaller models (academic use), the difference would be imperceptible.
Advanced version has two additional features - Collaboration, and Reports.

Collaborative working on a server
---------------------------------
Multiple users working on the same model on a server will be able to share the following:
    * Model runs
        * Runs from multiple users, even with the same name, will be usable in the Results module. “User” will be a dimension in the data, like region, scenario etc.
    * Input Data GDX
    * Results views definitions
    * Various groups and case definitions for Run Manager

Custom reports
--------------
VEDA_BE and the Results functionality in Veda2.0 work well for interactive and production reporting. But I see two limitations, removing which can make this a lot more powerful and flexible.
First, the *reporting variables* are trapped in tables – we don’t have direct control over them.
Second, we cannot add dimensions to the output views – we are limited to process and commodity sets in terms of segmenting the output beyond the native indexes like attribute, region and time.
Let’s take transportation final energy (in a rich model like the JRC_EU-TIMES) as an example: I want to see energy consumption by scenario, region, fuel, mode, size, and technology.
Scenario and region are separate indexes, and fuel can be managed with commodity sets. But we have only process sets to deal with mode, size and technology.
The entirely new approach of custom reports uses an Excel template to define reporting variables in a very efficient manner, and freely add
dimensions based process/commodity names, regions and scenarios.


License are priced as per institutions as well, like before. Basic version is accessible only to academic institutions.

.. image:: images/veda_versions.png
   :width: 300