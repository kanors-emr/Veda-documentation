# Trade

Tags for inter-regional trade — the TradeLinks family for declaring trade links, `~TFM_AVA` / `~TFM_AVA-C` for technology and commodity availability across regions, `~ReplicateInRegions` for cloning content across regions, and `~FI_Process_Trades` for per-trade-process metadata.

## Trade Links

Veda models inter-regional trade through dedicated TradeLinks files.
The following tags work together to describe trade between regions.

### ~Tradelinks

The primary trade-links input, given as a **region-by-region matrix**.
Rows and columns are regions; cell entries identify which commodities
are traded between the pair. Concise when many region pairs trade the
same commodities; switch to `~Tradelinks_DINS` when each link needs
its own row-level parameters.

### ~Tradelinks_DINS

The fully-enumerated (Direct Insert) form of trade-link declarations.
Each row identifies a single trade link explicitly — origin region,
destination region, commodity (and optionally process) — and carries
the parameter values directly.

### ~Tradelinks_Desc

Adds short and long descriptions to the trade links defined via
`~Tradelinks_DINS` (per `scentype_taglist`: "description of trade links
that are defined in DINS"). Pure metadata.


## Technology and commodity availability

### ~TFM_AVA

Indicates **availability of technologies across regions**. The
columns are one process filter column (typically `process` or
`PSET_PN`), the `AllRegions` default-flag column, then **one column
per individual region**. Cells carry `0` (unavailable) or `1`
(available).

Real example from `SubRES_H2-Production_Trans.xlsx :: AVA`:

| **~TFM_AVA** | **PSET_PN** | **AllRegions** | **GBL** |
| --- | --- | --- | --- |
| | `*` | 1 | 0 |

This row says: every process matching `*` (i.e. all H2-production
processes in this SubRES) is available in `AllRegions = 1` (default
yes), except `GBL = 0` (excluded from the global region). Add more
columns for other regions where the default needs to be overridden.

### ~TFM_AVA-C

The commodity-side analogue of `~TFM_AVA`. Uses commodity filter
columns (`cset_set`, `cset_cn`, `cset_cd`) plus the same `allregions`
+ per-region column layout to indicate availability of commodities.

### ~ReplicateInRegions

Enumerates per-region replications of processes — useful when a SubRES
template introduces a generic process that needs to be cloned with
region-specific identifiers (e.g. ISO codes) and metadata.

Real example from `SubRes_B-NewTechs_Trans.xlsx :: TechSelection`:

| **~ReplicateInRegions** | **Region** | **incode** | **indesc** | **Process** |
| --- | --- | --- | --- | --- |
| | Africa_North | DZA | Algeria - [Export] | LNG_New-Export |

The columns: `Region` (model region), `incode` (an ISO/country code or
similar identifier to plug into the cloned process name), `indesc`
(description), `Process` (the template process to clone).


## Trade-process linkage

### ~FI_Process_Trades

Augments the `TradeLinks` files with per-trade-process data. Where
`~Tradelinks` and `~Tradelinks_DINS` declare which commodities flow
between which regions, `~FI_Process_Trades` lets process-specific
data (such as the trade process's own attributes) be attached to
those links.
