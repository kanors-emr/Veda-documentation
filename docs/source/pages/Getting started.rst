================
Getting started
================

Installation
#############



* .. raw:: html

    <a href="https://github.com/kanors-emr/Veda2.0-Installation" target="_blank">Download Veda</a>

* It is recommended that the new user first takes a look at the video:

    .. raw:: html

        <iframe width="560" height="315" src="https://www.youtube.com/embed/QQzZi2_vWBs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

* There are two ways to go about it:
    * Localhost: This just needs to be extracted.
    * Installer: This is a setup executable.


Getting a Trial license
#######################

If you have registered an evaluation version request on the ETSAP website, then you would already have a Trial license key. If not, you can get one as shown here.

Demo video:

    .. raw:: html

        <iframe width="560" height="315" src="https://www.youtube.com/embed/6FFAw-rXD8A" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Once setup, to start using VEDA2.0, the user is required to get licence. Launching Veda will present an Activation screen:

.. image:: images/license_form.png
    :width: 600

If you don't have the Trial key:
    *	Click 'Get Trial Key'
    *	Complete the Registration form to get Trial key by email

Paste it into the Activation form, and request Activation. This will then bring you to the VEDA2.0 Start Page, if activated successfully.


Setting up GAMS
################

As part of registering VEDA2.0 a request is sent to the ETSAP Liaison Officer who will arrange for an evaluation GAMS license file to be created, sending it to the new user along with the download and install procedures here:

1.	Copy the GAMSLICE someplace on your computer.
2.	Head to http://www.gams.com/download/ and select the Windows download option for either Win-64/32, as appropriate
3.	Run Setup by clicking on it in Windows Explorer

    a)	Check “Use advanced installation mode” at the bottom of the GAMS Setup form.
    b)	Let GAMS get installed into the default folder (\GAMS\<Win#>\<ver>.
    c)	Check the Add GAMS directory to PATH environment variable.
    d)	Have the GAMSLICE.TXT copied from wherever it currently resides.

You may need to restart your computer to have the GAMS Path activated.

Once you have VEDA installed you can try a TIMES model run.


Uninstallation
###############

* Installer version:

    If you installed Veda 2.0 using installer, the process of uninstalling is very straight forward.

    Steps:
        * Go to Control panel.
        * Select Veda 2.0 and click uninstall.

        .. image:: images/uninstall.PNG
            :width: 400

        * Make sure that Postgres has also been removed. Usually the process of uninstallation also removes Postgres from the computer.
        * Sometimes uninstallation ends prematurely (image below) and Postgres is not removed. In such case, please go to :ref:`Uninstalling Postgres` for further instructions.

        .. image:: images/Veda_Premature_Error.PNG
            :width: 400

* Localhost version:

    * Launch the Veda2.0 version you are using.
    * In the main menu -> Model –> Stop server and exit

    .. image:: images/stop_server.PNG

    * Now you can go ahead and delete the localhost directory.


Updation
#########

Right now the process of updation requires the user to uninstall the old version
and install the new version of Veda2.0 manually.

Refer the following links for help:
    * :ref:`Uninstallation`
    * :ref:`Installation`



