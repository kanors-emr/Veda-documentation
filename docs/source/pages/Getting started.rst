################
Getting started
################

Hardware/software requirement
=============================

Veda2.0 works on Windows portables, desktops, servers, and VMs, with Windows 8/Windows server 2012 or above. Microsoft Excel is a prerequisite.

Suggested hardware
^^^^^^^^^^^^^^^^^^^
Hardware needed depends on the size and complexity of models, but here is a configuration suitable for typical TIMES models under Veda2.0:

    * CPU: Minimum 4 cores are recommended for STANDARD and ADVANCED licenses. 8 - 16 would be desirable for larger models
    * RAM: 4-8 GB is enough for Veda, but GAMS needs more RAM for larger models. 32 GB would accomodate most models
    * HDD: 500GB - 1TB free space for Veda and GAMS files

Veda accesses Internet for the following functions:
    * Licensing
        * Source: provided on request
    * Displaying announcements on the Start page
        * Source: https://veda-news.readthedocs.io/
    * Updating TIMES source code from Github
        * Source: https://api.github.com/repos/etsap-TIMES/TIMES_model/releases/latest
    * Gams Engine for running GAMS jobs in cloud environments via REST API
        * Source: https://www.gams.com/engine/engine-api.html

Software prerequisites
^^^^^^^^^^^^^^^^^^^^^^^

    * Veda makes a local connection to a PostgreSQL database. In case you see “No database response” message on Veda startup and it does not go away, please make sure that the system firewall is not blocking Veda in making the said connection (This could require permissions from your IT department).
    * Veda uses Excel in background and in case of any pending popups in Excel that require user attention, Excel will not work which in turn will stop Veda to carry out important processes like synchronization of model. One such popup is the user sign-in popup, so we advise user to make sure they are signed in to Excel properly.

.. _installation_section:

Installation
============

* It is recommended that the new user first takes a look at the video:
    .. raw:: html

        <iframe width="560" height="315" src="https://www.youtube.com/embed/QQzZi2_vWBs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

* There are two ways to go about it:
    * Localhost: This just needs to be extracted
        * .. raw:: html

             <a href="https://github.com/kanors-emr/Veda2.0-Installation/tree/master/Localhost%20Version%20Prerequisites" target="blank">Download and install prerequisites</a>

        * .. raw:: html

             <a href="https://github.com/kanors-emr/Veda2.0-Installation/releases/latest" target="blank">Download localhost</a>

        * Give full read and write permissions to the folder where it is extracted
        * Port 65001 should be accessible to PostgreSQL

    * Installer: This is a setup executable
        * .. raw:: html

            <a href="https://github.com/kanors-emr/Veda2.0-Installation/releases/latest" target="blank">Download installer</a>

        * Create a folder where you wish to install and give it full read and write permissions
        * Port 65000 should be accessible to PostgreSQL


Setting up GAMS
================

As part of registering VEDA2.0 a request is sent to the ETSAP Liaison Officer who will arrange for an evaluation GAMS license file to be created, sending it to the new user along with the download and install procedures here:

1.	Copy the GAMSLICE someplace on your computer
2.	Head to https://www.gams.com/download/ and select the Windows download option for either Win-64/32, as appropriate
3.	Run Setup by clicking on it in Windows Explorer

    a)	Check “**Use advanced installation mode**” at the bottom of the GAMS Setup form
    b)	Let GAMS get installed into the default folder (\GAMS\<Win#>\<ver>
    c)	Have the GAMSLICE.TXT copied from wherever it currently resides to the GAMS directory
    d)	Verify and add the GAMS directory to the PATH environment variable

        * After installation, open a Command Prompt and type “gams” to see if GAMS is recognized      
            .. image:: images/gams_command_recognized.png
                :width: 400
        
        * If GAMS is not recognized        
            .. image:: images/gams_command_not_recognized.png
                :width: 400

        Follow the below steps to add GAMS directory Path to the environment variables.
        
            * Let suppose your GAMS installation directory Path is C:\\GAMS\\32            
                .. image:: images/gams_location_c_drive.png
                    :width: 275
            
            * Steps to add GAMS directory path to Environment Variables           
                .. image:: images/environment_variables.png
                    :width: 400

            * After clicked on Environment Variables > {System variables} Path  > Edit
                .. image:: images/system_variables_path_edit.png
                    :width: 400

            * Click on New and add the GAMS directory path (C:\\GAMS\\32) to the list
                .. image:: images/add_gams_path.png
                    :width: 400     

You may need to restart your computer to have the GAMS Path activated.

Once you have VEDA installed you can try a TIMES model run.

.. _unistallation_section:

Uninstallation
===============

* Installer version:

    If you installed Veda 2.0 using installer, the process of uninstalling is very straight forward.

    Steps:
        * Go to Control panel
        * Select Veda 2.0 and click uninstall

        .. image:: images/uninstall.PNG
            :width: 400

        * Make sure that Postgres has also been removed. Usually the process of uninstallation also removes Postgres from the computer
        * Sometimes uninstallation ends prematurely (image below) and Postgres is not removed. In such case, please go to :ref:`Uninstalling Postgres <Uninstalling_Postgres>` for further instructions

        .. image:: images/Veda_Premature_Error.PNG
            :width: 400

* Localhost version:

    * Launch the Veda2.0 version you are using
    * In the main menu -> Model –> Stop server and exit

    .. image:: images/stop_server.PNG

    * Now you can go ahead and delete the localhost directory

.. _Backup and Restore:

Backup and Restore
==================
The Backup and Restore feature makes upgrading Veda much easier. You can back up the "state", meaning, all models that are synchronized, and all Cases that are imported in Veda.
This is available starting version 230.

Steps:

    * **Backup**

            * Go to Model > Backup state
                .. image:: images/backup_state_menu.PNG
            * Save the backup file in a directory of your choice
                .. image:: images/save_backup_form.PNG
                    :width: 400
            * Go to Model > Stop server and exit (Terminate Veda)

    * **Restore**

        * Launch the new version of Veda
        * Go to Model > Restore state, to restore your models and cases
        * Select the saved backup file
        * Once the file is loaded, you can select the models/cases that you want to get restored
            .. image:: images/restore_form.PNG
                :width: 400
        * Click "Restore" to synchronize all selected models and import all selected cases


Updating
=========
The process of updating requires the user to uninstall the old version
and install the new version of Veda2.0 manually.

Refer the following links for help:
    * :ref:`Backup and Restore <Backup and Restore>`
    * :ref:`Uninstallation <unistallation_section>`
    * :ref:`Installation <installation_section>`