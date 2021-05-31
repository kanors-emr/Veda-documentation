#######################################
FILL tables should be handled with care
#######################################
.. note::
    FILL tables provide a lot of control, but can create surprises in the long run, if data source is not controlled properly.

This note is triggered by the following incident: A model used a FILL table to pull heating demands, to create user constraints restricting district heat. The scenario was not controlled (SourceScen col), but there was only one scenario with this information when this table was
set up. Later, an experimental demand scenario was created, which was actually not used in any of the cases. But based on the scenario hierarchy, the FILL table started pulling records from this experimental scenario.

FILL tables are typically used to pull calibration year information or reference projections, like characteristics of existing technology stock or demand projections. The source scenario
should always be specified to avoid surprises like the one described above. Further, FILL tables slow down the Sync process, and also modify the host files each time they are processed,
which can be awkward for version control systems. If the information contained in the FILL tables is relatively stable, I would consider deactivating them till the source information is updated.
