#######################################
Efficiency considerations in UPD tables
#######################################
.. note::
    Veda2.0 reports the processing time of each tag under Information > Model > Tag details. This note can help you reduce the time taken by UPD tables.

Good and bad UPD tables
=========================
There can be two reasons to use the UPD tag:

    *	To numerically transform existing values (seed values)
    *	To identify indexes for applying absolute values. For example, MINOIL could have ACT_BND(LO) in various regions and years. If one wanted to replace *all* of them by 0, UPD is a good option.

UPD is a particularly heavy tag to process because each row involves fetching seed values from a potentially large table.
UPD tables that have only a few rows, even if each row affects a large number of records, work quite well. For example, see the table below where investment costs for onshore wind technologies are being differentiated based on the distance information embedded in the name, and additionally based on depth, in the case of offshore wind.

    .. csv-table:: Table 1: Example of a "worthy" update table
        :file: update_worthy_table.csv
        :widths: 1,1,1
        :header-rows: 1

But very long UPD tables can be very slow to process, even if each row doesn’t affect a lot of records.
The table shown below took 4 minutes to process on a very fast machine. The function of this table is to apply factors to demand projection, by year and sub-sector.

    .. csv-table:: Table 2: Example of a "heavy" update table
        :file: heavy_update_table.csv
        :widths: 1,1,1,1,1
        :header-rows: 1

An alternative to UPD tables
=============================

You can get the seed values via a FILL-R table, and prepare a DINS (or even INS) table with transformed values.
The table shown below will write COM_PROJ values for qualifying demands on a sheet “Demandupdate”.

    .. csv-table:: Table 3: FILL-R table to pull values to be updated
        :file: FILL-R_table.csv
        :header-rows: 1

The output of the FILL-R table above is shown below.

    .. csv-table:: Table 4: Output of the FILL-R table (Cell A1 of sheet Demandupdate)
        :file: FILL-R_output_table.csv
        :header-rows: 1

The table above, combined with the multipliers (in last column below), can be used to set up the DINS table shown below.

    .. csv-table:: Table 5: DINS table with updated values
        :file: updated_DINS_table.csv
        :header-rows: 1

The combination of FILL-R and DINS takes a fraction of the time that the original UPD took.