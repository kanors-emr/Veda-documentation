# Topology

The topology says which commodities each process consumes and produces.
It is built by `~FI_T` (in templates) and by trade links. The topology
tags add connections afterwards, from transformation, trade, scenario or
SysSettings files: they attach an **existing** process to an **existing**
commodity as an input or an output. They are processed early, before any
insert or update ([processing order](processing-order.md)), so the new
connections are visible to every later rule, including `pset_ci` /
`pset_co` filters.

All three are processed in `BY_Trans`, `SubRES_*_Trans`, SysSettings,
trade, regular and NSV files, in that order of file types, and in each,
TOPDINS before TOPINS. The catalog also accepts them in generated
parametric files, but they are **not processed** there. The value cell
(`Value`, alias `IO`) holds `IN` or `OUT`.

## ~TFM_TOPINS

The rule-based form. Processes and commodities are selected with the full
[filters](values-and-filters.md#process-and-commodity-filters): wildcards,
comma lists, sets, topology, and the and/or columns.

| ~TFM_TOPINS | | | | |
| --- | --- | --- | --- | --- |
| **pset_ci** | **pset_co** | **pset_pn** | **cset_cn** | **IO** |
| INDNGA | INDELC | EA* | INDBFG | IN |

Every process whose name starts with `EA`, that consumes `INDNGA` and
produces `INDELC`, gets `INDBFG` as an additional input.

## ~TFM_TOPINS-A

A compact form of TOPINS with three columns: process, commodity and
`IN`/`OUT`. Wildcards are allowed.

| ~TFM_TOPINS-A | | |
| --- | --- | --- |
| **process** | **commodity** | **value** |
| EP_HPS* | AuxStoOUT | OUT |

## ~TFM_TOPDINS

The enumerated form, the topology counterpart of
[`~TFM_DINS`](data-tags.md#tfm_dins): one process name and one commodity
name per row, read literally, with a region. It is the fastest way to add
many explicit connections.

| ~TFM_TOPDINS | | | |
| --- | --- | --- | --- |
| **Region** | **pset_pn** | **cset_cn** | **IO** |
| REG1 | tech_bus1 | e_bus1 | IN |
| REG1 | tech_bus2 | e_bus2 | IN |

- A **region is required**, either in a `Region` column or as
  region-named value columns. A table without one stops with an error.
- Unlike every other data tag, TOPDINS takes **one real region per row**:
  it does not expand comma lists or region groups, and does not read a
  region from the tag text.
- Rows whose region, process or commodity does not exist are dropped
  without a message. Tables that deliberately list more combinations than
  exist rely on this.

Use TOPINS or TOPINS-A when the row is a rule; use TOPDINS when it is a
list.
