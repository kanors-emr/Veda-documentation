# Efficiency considerations in UPD tables

!!! note "Note"

    Veda2.0 reports the processing time of each tag under Information \>
    Model \> Tag details. This note can help you reduce the time taken by
    UPD tables.

## Good and bad UPD tables

There can be two reasons to use the UPD tag:

>   - To numerically transform existing values (seed values)
>   - To identify indexes for applying absolute values. For example,
>     MINOIL could have ACT\_BND(LO) in various regions and years. If
>     one wanted to replace *all* of them by 0, UPD is a good option.

UPD is a particularly heavy tag to process because each row involves
fetching seed values from a potentially large table. UPD tables that
have only a few rows, even if each row affects a large number of
records, work quite well. For example, see the table below where
investment costs for onshore wind technologies are being differentiated
based on the distance information embedded in the name, and additionally
based on depth, in the case of offshore wind.

> 
> 
> | \~TFM\_UPD |                           |            |
> | ---------- | ------------------------- | ---------- |
> | Attribute  | PSET\_PN                  | AllRegions |
> | INVCOST    | E\[\_\]WON\*Far\*         | \*1.75     |
> | INVCOST    | E\[\_\]WON\*Trans\*       | \*1.5      |
> | INVCOST    | E\[\_\]WON\*Near\*        | \*1        |
> | INVCOST    | E\[\_\]WOF\*deep\*Far\*   | \*1.8      |
> | INVCOST    | E\[\_\]WOF\*deep\*Inter\* | \*1.5      |
> | INVCOST    | E\[\_\]WOF\*deep\*Near\*  | \*1.35     |
> | INVCOST    | E\[\_\]WOF\*shal\*Far\*   | \*1.2      |
> | INVCOST    | E\[\_\]WOF\*shal\*Inter\* | \*1        |
> | INVCOST    | E\[\_\]WOF\*shal\*Near\*  | \*0.9      |
> | INVCOST    | E\[\_\]WOF\*tran\*Far\*   | \*1.32     |
> | INVCOST    | E\[\_\]WOF\*tran\*Inter\* | \*1.1      |
> | INVCOST    | E\[\_\]WOF\*tran\*Near\*  | \*0.99     |
> 

> Table 1: Example of a "worthy" update table

But very long UPD tables can be very slow to process, even if each row
doesn’t affect a lot of records. The table shown below took 4 minutes to
process on a very fast machine. The function of this table is to apply
factors to demand projection, by year and sub-sector.

> 
> 
> | SourceScen | Attribute | Year | AllRegions | Cset\_CN |
> | ---------- | --------- | ---- | ---------- | -------- |
> | BASE       | COM\_PROJ | 2020 | \*1        | RBn\*    |
> | BASE       | COM\_PROJ | 2021 | \*0.96     | RBn\*    |
> | BASE       | COM\_PROJ | 2022 | \*0.93     | RBn\*    |
> | BASE       | COM\_PROJ | 2023 | \*0.91     | RBn\*    |
> | BASE       | COM\_PROJ | 2024 | \*0.88     | RBn\*    |
> | BASE       | COM\_PROJ | 2025 | \*0.86     | RBn\*    |
> | BASE       | COM\_PROJ | 2026 | \*0.83     | RBn\*    |
> | BASE       | COM\_PROJ | 2027 | \*0.81     | RBn\*    |
> | BASE       | COM\_PROJ | 2028 | \*0.78     | RBn\*    |
> | BASE       | COM\_PROJ | 2029 | \*0.76     | RBn\*    |
> | BASE       | COM\_PROJ | 2030 | \*0.73     | RBn\*    |
> | BASE       | COM\_PROJ | 2031 | \*0.73     | RBn\*    |
> | BASE       | COM\_PROJ | 2032 | \*0.72     | RBn\*    |
> | BASE       | COM\_PROJ | 2033 | \*0.72     | RBn\*    |
> | BASE       | COM\_PROJ | 2034 | \*0.72     | RBn\*    |
> | BASE       | COM\_PROJ | 2035 | \*0.71     | RBn\*    |
> | BASE       | COM\_PROJ | 2036 | \*0.71     | RBn\*    |
> | BASE       | COM\_PROJ | 2037 | \*0.7      | RBn\*    |
> | BASE       | COM\_PROJ | 2038 | \*0.7      | RBn\*    |
> | BASE       | COM\_PROJ | 2039 | \*0.69     | RBn\*    |
> | BASE       | COM\_PROJ | 2040 | \*0.69     | RBn\*    |
> | BASE       | COM\_PROJ | 2041 | \*0.68     | RBn\*    |
> | BASE       | COM\_PROJ | 2042 | \*0.68     | RBn\*    |
> | BASE       | COM\_PROJ | 2043 | \*0.67     | RBn\*    |
> | BASE       | COM\_PROJ | 2044 | \*0.67     | RBn\*    |
> | BASE       | COM\_PROJ | 2045 | \*0.66     | RBn\*    |
> | BASE       | COM\_PROJ | 2046 | \*0.66     | RBn\*    |
> | BASE       | COM\_PROJ | 2047 | \*0.65     | RBn\*    |
> | BASE       | COM\_PROJ | 2048 | \*0.65     | RBn\*    |
> | BASE       | COM\_PROJ | 2049 | \*0.64     | RBn\*    |
> | BASE       | COM\_PROJ | 2050 | \*0.64     | RBn\*    |
> | BASE       | COM\_PROJ | 2020 | \*1        | RBe\*    |
> | BASE       | COM\_PROJ | 2021 | \*1        | RBe\*    |
> | BASE       | COM\_PROJ | 2022 | \*1        | RBe\*    |
> | BASE       | COM\_PROJ | 2023 | \*1        | RBe\*    |
> | BASE       | COM\_PROJ | 2024 | \*1        | RBe\*    |
> | BASE       | COM\_PROJ | 2025 | \*1        | RBe\*    |
> | BASE       | COM\_PROJ | 2026 | \*1        | RBe\*    |
> | BASE       | COM\_PROJ | 2027 | \*1        | RBe\*    |
> | BASE       | COM\_PROJ | 2028 | \*1        | RBe\*    |
> | BASE       | COM\_PROJ | 2029 | \*1        | RBe\*    |
> | BASE       | COM\_PROJ | 2030 | \*1        | RBe\*    |
> | BASE       | COM\_PROJ | 2031 | \*1        | RBe\*    |
> | BASE       | COM\_PROJ | 2032 | \*1        | RBe\*    |
> | BASE       | COM\_PROJ | 2033 | \*1        | RBe\*    |
> | BASE       | COM\_PROJ | 2034 | \*1        | RBe\*    |
> | BASE       | COM\_PROJ | 2035 | \*1        | RBe\*    |
> | BASE       | COM\_PROJ | 2036 | \*1        | RBe\*    |
> | BASE       | COM\_PROJ | 2037 | \*1        | RBe\*    |
> | BASE       | COM\_PROJ | 2038 | \*1        | RBe\*    |
> | BASE       | COM\_PROJ | 2039 | \*1        | RBe\*    |
> | BASE       | COM\_PROJ | 2040 | \*1        | RBe\*    |
> | BASE       | COM\_PROJ | 2041 | \*1        | RBe\*    |
> | BASE       | COM\_PROJ | 2042 | \*1        | RBe\*    |
> | BASE       | COM\_PROJ | 2043 | \*1        | RBe\*    |
> | BASE       | COM\_PROJ | 2044 | \*1        | RBe\*    |
> | BASE       | COM\_PROJ | 2045 | \*1        | RBe\*    |
> | BASE       | COM\_PROJ | 2046 | \*1        | RBe\*    |
> | BASE       | COM\_PROJ | 2047 | \*1        | RBe\*    |
> | BASE       | COM\_PROJ | 2048 | \*1        | RBe\*    |
> | BASE       | COM\_PROJ | 2049 | \*1        | RBe\*    |
> | BASE       | COM\_PROJ | 2050 | \*1        | RBe\*    |
> | BASE       | COM\_PROJ | 2020 | \*1        | CB\*     |
> | BASE       | COM\_PROJ | 2021 | \*0.98     | CB\*     |
> | BASE       | COM\_PROJ | 2022 | \*0.97     | CB\*     |
> | BASE       | COM\_PROJ | 2023 | \*0.96     | CB\*     |
> | BASE       | COM\_PROJ | 2024 | \*0.96     | CB\*     |
> | BASE       | COM\_PROJ | 2025 | \*0.95     | CB\*     |
> | BASE       | COM\_PROJ | 2026 | \*0.95     | CB\*     |
> | BASE       | COM\_PROJ | 2027 | \*0.94     | CB\*     |
> | BASE       | COM\_PROJ | 2028 | \*0.94     | CB\*     |
> | BASE       | COM\_PROJ | 2029 | \*0.93     | CB\*     |
> | BASE       | COM\_PROJ | 2030 | \*0.93     | CB\*     |
> | BASE       | COM\_PROJ | 2031 | \*0.92     | CB\*     |
> | BASE       | COM\_PROJ | 2032 | \*0.91     | CB\*     |
> | BASE       | COM\_PROJ | 2033 | \*0.9      | CB\*     |
> | BASE       | COM\_PROJ | 2034 | \*0.9      | CB\*     |
> | BASE       | COM\_PROJ | 2035 | \*0.89     | CB\*     |
> | BASE       | COM\_PROJ | 2036 | \*0.88     | CB\*     |
> | BASE       | COM\_PROJ | 2037 | \*0.87     | CB\*     |
> | BASE       | COM\_PROJ | 2038 | \*0.86     | CB\*     |
> | BASE       | COM\_PROJ | 2039 | \*0.85     | CB\*     |
> | BASE       | COM\_PROJ | 2040 | \*0.84     | CB\*     |
> | BASE       | COM\_PROJ | 2041 | \*0.84     | CB\*     |
> | BASE       | COM\_PROJ | 2042 | \*0.83     | CB\*     |
> | BASE       | COM\_PROJ | 2043 | \*0.83     | CB\*     |
> | BASE       | COM\_PROJ | 2044 | \*0.82     | CB\*     |
> | BASE       | COM\_PROJ | 2045 | \*0.81     | CB\*     |
> | BASE       | COM\_PROJ | 2046 | \*0.81     | CB\*     |
> | BASE       | COM\_PROJ | 2047 | \*0.8      | CB\*     |
> | BASE       | COM\_PROJ | 2048 | \*0.79     | CB\*     |
> | BASE       | COM\_PROJ | 2049 | \*0.79     | CB\*     |
> | BASE       | COM\_PROJ | 2050 | \*0.78     | CB\*     |
> 

> Table 2: Example of a "heavy" update table

## An alternative to UPD tables

You can get the seed values via a FILL-R table, and prepare a DINS (or
even INS) table with transformed values. The table shown below will
write COM\_PROJ values for qualifying demands on a sheet “Demandupdate”.

> 
> 
> | \~TFM\_FILL-R:w=Demandupdate;hcol=region |           |                  |      |            |
> | ---------------------------------------- | --------- | ---------------- | ---- | ---------- |
> | Sourcescen                               | Attribute | CSET\_CN         | Year | AllRegions |
> | BASE                                     | COM\_PROJ | RBn\*,Rbe\*,Cb\* |      | \*1        |
> 

> Table 3: FILL-R table to pull values to be updated

The output of the FILL-R table above is shown below.

> 
> 
> | scenario | attribute | process | commodity     | lim\_type | time\_slice | year | commodity\_group | currency | stage | sow | ACT  | NSW  | NT   | QLD  | SA   | TAS  | VIC  | WA   |
> | -------- | --------- | ------- | ------------- | --------- | ----------- | ---- | ---------------- | -------- | ----- | --- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
> | BASE     | COM\_PROJ | \-      | CB\_Age\_Care | \-        | \-          | 2015 | \-               | \-       | \-    | \-  | 0.08 | 1.6  | 0.05 | 1    | 0.35 | 0.11 | 1.26 | 0.54 |
> | BASE     | COM\_PROJ | \-      | CB\_Age\_Care | \-        | \-          | 2016 | \-               | \-       | \-    | \-  | 0.09 | 1.63 | 0.05 | 1.04 | 0.37 | 0.11 | 1.27 | 0.57 |
> | BASE     | COM\_PROJ | \-      | CB\_Age\_Care | \-        | \-          | 2017 | \-               | \-       | \-    | \-  | 0.09 | 1.67 | 0.05 | 1.07 | 0.38 | 0.11 | 1.3  | 0.59 |
> | BASE     | COM\_PROJ | \-      | CB\_Age\_Care | \-        | \-          | 2018 | \-               | \-       | \-    | \-  | 0.09 | 1.71 | 0.06 | 1.1  | 0.38 | 0.12 | 1.34 | 0.61 |
> | BASE     | COM\_PROJ | \-      | CB\_Age\_Care | \-        | \-          | 2019 | \-               | \-       | \-    | \-  | 0.09 | 1.75 | 0.06 | 1.13 | 0.39 | 0.12 | 1.38 | 0.64 |
> | BASE     | COM\_PROJ | \-      | CB\_Age\_Care | \-        | \-          | 2020 | \-               | \-       | \-    | \-  | 0.1  | 1.8  | 0.06 | 1.17 | 0.4  | 0.12 | 1.42 | 0.66 |
> | BASE     | COM\_PROJ | \-      | CB\_Age\_Care | \-        | \-          | 2021 | \-               | \-       | \-    | \-  | 0.1  | 1.85 | 0.06 | 1.21 | 0.41 | 0.12 | 1.47 | 0.69 |
> | BASE     | COM\_PROJ | \-      | CB\_Age\_Care | \-        | \-          | 2022 | \-               | \-       | \-    | \-  | 0.1  | 1.91 | 0.06 | 1.26 | 0.42 | 0.13 | 1.52 | 0.72 |
> | BASE     | COM\_PROJ | \-      | CB\_Age\_Care | \-        | \-          | 2023 | \-               | \-       | \-    | \-  | 0.11 | 1.97 | 0.07 | 1.31 | 0.44 | 0.13 | 1.58 | 0.76 |
> | BASE     | COM\_PROJ | \-      | CB\_Age\_Care | \-        | \-          | 2024 | \-               | \-       | \-    | \-  | 0.11 | 2.05 | 0.07 | 1.37 | 0.45 | 0.13 | 1.65 | 0.8  |
> | BASE     | COM\_PROJ | \-      | CB\_Age\_Care | \-        | \-          | 2025 | \-               | \-       | \-    | \-  | 0.12 | 2.13 | 0.07 | 1.44 | 0.47 | 0.14 | 1.72 | 0.84 |
> | BASE     | COM\_PROJ | \-      | CB\_Age\_Care | \-        | \-          | 2026 | \-               | \-       | \-    | \-  | 0.12 | 2.22 | 0.08 | 1.51 | 0.49 | 0.14 | 1.8  | 0.89 |
> | BASE     | COM\_PROJ | \-      | CB\_Age\_Care | \-        | \-          | 2027 | \-               | \-       | \-    | \-  | 0.13 | 2.35 | 0.08 | 1.61 | 0.52 | 0.15 | 1.91 | 0.95 |
> | BASE     | COM\_PROJ | \-      | CB\_Age\_Care | \-        | \-          | 2028 | \-               | \-       | \-    | \-  | 0.14 | 2.46 | 0.08 | 1.69 | 0.54 | 0.16 | 2.01 | 1.01 |
> | BASE     | COM\_PROJ | \-      | CB\_Age\_Care | \-        | \-          | 2029 | \-               | \-       | \-    | \-  | 0.14 | 2.56 | 0.09 | 1.77 | 0.56 | 0.16 | 2.1  | 1.07 |
> | BASE     | COM\_PROJ | \-      | CB\_Age\_Care | \-        | \-          | 2030 | \-               | \-       | \-    | \-  | 0.15 | 2.66 | 0.09 | 1.85 | 0.58 | 0.17 | 2.19 | 1.12 |
> | BASE     | COM\_PROJ | \-      | CB\_Age\_Care | \-        | \-          | 2031 | \-               | \-       | \-    | \-  | 0.16 | 2.76 | 0.1  | 1.93 | 0.6  | 0.17 | 2.28 | 1.18 |
> | BASE     | COM\_PROJ | \-      | CB\_Age\_Care | \-        | \-          | 2032 | \-               | \-       | \-    | \-  | 0.16 | 2.86 | 0.1  | 2.01 | 0.62 | 0.18 | 2.37 | 1.23 |
> | BASE     | COM\_PROJ | \-      | CB\_Age\_Care | \-        | \-          | 2033 | \-               | \-       | \-    | \-  | 0.17 | 2.96 | 0.1  | 2.09 | 0.64 | 0.18 | 2.46 | 1.29 |
> | BASE     | COM\_PROJ | \-      | CB\_Age\_Care | \-        | \-          | 2034 | \-               | \-       | \-    | \-  | 0.17 | 3.05 | 0.11 | 2.16 | 0.66 | 0.19 | 2.54 | 1.34 |
> 

> Table 4: Output of the FILL-R table (Cell A1 of sheet Demandupdate)

The table above, combined with the multipliers (in last column below),
can be used to set up the DINS table shown below.

> 
> 
> |      |  | \~TFM\_DINS |               |      |      |      |      |      |      |      |      |      |  |            |
> | ---- |  | ----------- | ------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |  | ---------- |
> | CB\_ |  | attribute   | CSET\_CN      | year | ACT  | NSW  | NT   | QLD  | SA   | TAS  | VIC  | WA   |  | multiplier |
> | CB\_ |  | COM\_PROJ   | CB\_Age\_Care | 2015 |      |      |      |      |      |      |      |      |  | 0          |
> | CB\_ |  | COM\_PROJ   | CB\_Age\_Care | 2016 |      |      |      |      |      |      |      |      |  | 0          |
> | CB\_ |  | COM\_PROJ   | CB\_Age\_Care | 2017 |      |      |      |      |      |      |      |      |  | 0          |
> | CB\_ |  | COM\_PROJ   | CB\_Age\_Care | 2018 |      |      |      |      |      |      |      |      |  | 0          |
> | CB\_ |  | COM\_PROJ   | CB\_Age\_Care | 2019 |      |      |      |      |      |      |      |      |  | 0          |
> | CB\_ |  | COM\_PROJ   | CB\_Age\_Care | 2020 |      |      |      |      |      |      |      |      |  | 1          |
> | CB\_ |  | COM\_PROJ   | CB\_Age\_Care | 2021 | 0.1  | 1.81 | 0.06 | 1.19 | 0.4  | 0.12 | 1.44 | 0.68 |  | 0.98       |
> | CB\_ |  | COM\_PROJ   | CB\_Age\_Care | 2022 | 0.1  | 1.85 | 0.06 | 1.22 | 0.41 | 0.12 | 1.48 | 0.7  |  | 0.97       |
> | CB\_ |  | COM\_PROJ   | CB\_Age\_Care | 2023 | 0.1  | 1.89 | 0.06 | 1.26 | 0.42 | 0.12 | 1.51 | 0.73 |  | 0.96       |
> | CB\_ |  | COM\_PROJ   | CB\_Age\_Care | 2024 | 0.11 | 1.96 | 0.07 | 1.32 | 0.43 | 0.13 | 1.58 | 0.77 |  | 0.96       |
> | CB\_ |  | COM\_PROJ   | CB\_Age\_Care | 2025 | 0.11 | 2.02 | 0.07 | 1.37 | 0.45 | 0.13 | 1.64 | 0.8  |  | 0.95       |
> | CB\_ |  | COM\_PROJ   | CB\_Age\_Care | 2026 | 0.12 | 2.11 | 0.07 | 1.43 | 0.46 | 0.14 | 1.71 | 0.85 |  | 0.95       |
> | CB\_ |  | COM\_PROJ   | CB\_Age\_Care | 2027 | 0.12 | 2.21 | 0.08 | 1.51 | 0.48 | 0.14 | 1.8  | 0.9  |  | 0.94       |
> | CB\_ |  | COM\_PROJ   | CB\_Age\_Care | 2028 | 0.13 | 2.31 | 0.08 | 1.59 | 0.51 | 0.15 | 1.89 | 0.95 |  | 0.94       |
> | CB\_ |  | COM\_PROJ   | CB\_Age\_Care | 2029 | 0.13 | 2.38 | 0.08 | 1.65 | 0.52 | 0.15 | 1.95 | 0.99 |  | 0.93       |
> | CB\_ |  | COM\_PROJ   | CB\_Age\_Care | 2030 | 0.14 | 2.48 | 0.09 | 1.72 | 0.54 | 0.16 | 2.04 | 1.04 |  | 0.93       |
> | CB\_ |  | COM\_PROJ   | CB\_Age\_Care | 2031 | 0.14 | 2.54 | 0.09 | 1.78 | 0.55 | 0.16 | 2.1  | 1.08 |  | 0.92       |
> | CB\_ |  | COM\_PROJ   | CB\_Age\_Care | 2032 | 0.15 | 2.6  | 0.09 | 1.83 | 0.56 | 0.16 | 2.15 | 1.12 |  | 0.91       |
> | CB\_ |  | COM\_PROJ   | CB\_Age\_Care | 2033 | 0.15 | 2.66 | 0.09 | 1.88 | 0.57 | 0.16 | 2.21 | 1.16 |  | 0.9        |
> | CB\_ |  | COM\_PROJ   | CB\_Age\_Care | 2034 | 0.16 | 2.74 | 0.1  | 1.95 | 0.59 | 0.17 | 2.29 | 1.21 |  | 0.9        |
> 

> Table 5: DINS table with updated values

The combination of FILL-R and DINS takes a fraction of the time that the
original UPD took.
