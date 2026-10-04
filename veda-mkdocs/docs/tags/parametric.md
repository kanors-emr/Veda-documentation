# Parametric scenarios

How to drive many model runs from a single file — the `~INPUTCELL` tag, the controller pattern that turns a run index into a set of assumptions, and the range of things that index can be made to control.

## What they are for

A parametric scenario is one workbook that Veda replays many times. Veda
writes a run index into a single designated cell, recalculates the
workbook, and saves the result as a numbered child file. Repeat for every
index in the declared range.

The original motivation is in the name: **parameter fans**. Setting up a
thousand CO<sub>2</sub> price trajectories is a few minutes of work and is
error-free by construction, because there is only ever one copy of the
logic. Put the thousand trajectories on a source sheet, point one formula
at the run index, declare `~InputCell:1-1000`, and sync. Nothing is
copy-pasted, so nothing can be copy-pasted wrong.

The same machinery turns out to be a good way to **manage scenario
experiments generally**, and — because the controls can be made as simple
as you like while the model underneath stays as complex as it needs to be
— a way to **hand a model to someone who should not be editing it**. Both
are covered below.

## The design table is the artefact

In a conventional setup, the dimensional structure of an experiment is
implicit. Case definitions record which scenario files were switched on,
but nothing states *these are my axes, these are their levels, this is the
set of combinations I ran*. That structure lives in file-naming
conventions and in the modeller's memory.

A parametric file states it explicitly, in one table, sitting next to the
data it controls:

| run | co2 | demand | tech cost |
| --- | --- | --- | --- |
| 1 | low | base | P50 |
| 2 | mid | base | P50 |
| 3 | high | base | P50 |
| … | | | |

This is why parametric files are easy to come back to. You are not
reconstructing the design from evidence — you are reading it off. A year
later the controller sheet still answers "what did I actually vary, and
what was held fixed?" in about thirty seconds.

It also keeps **assumptions modular**. The interface between the design
and the data is a single integer, so the two can change independently. New
data vintage? Replace the source sheets; the design is untouched. New
design? Add rows; the data is untouched. In practice this means one
parametric file per project within a model, each a self-contained
generator with its own numbered children, none of them colliding.

!!! tip "Not just factorial designs"

    The design table is a **list of rows**, not a cross-product. A full
    factorial is one way to fill it, but so is a one-at-a-time sensitivity
    screen, a Latin hypercube sample, or a handful of named storylines with
    deliberately correlated settings.

    This matters because the table is also where you record what is *not*
    independent. If two technologies must move together — say a 4-hour and
    an 8-hour battery driven by the same cost percentile — the design table
    is where that judgement gets written down instead of remembered.

## How a parametric file is put together

Five parts, conventionally on a sheet named `controller`.

**1. The range.** A cell holding the run indices to generate, as text:
`1-27`. Keeping it in its own cell means the range is editable in one
obvious place.

**2. The tag.** Built from the range by formula, so the two can never
disagree:

```
B3:  ="~InputCell:"&A1        renders as   ~InputCell:1-27
```

**3. The input cell.** The cell directly beneath the tag. This is the only
thing Veda changes. Seed it with any valid index.

**4. The design table.** One row per run, keyed on the run index, with a
column per dimension.

**5. The resolvers.** Formulas that turn the current index into the
current level for each dimension:

```
C6:  =VLOOKUP($B$4,$B$10:$J$36,C7,FALSE)
C7:  =COLUMN()-1
```

The second formula supplies the column index, so the resolver can be
dragged sideways across all dimensions without editing.

Data sheets elsewhere in the workbook then reference `controller!$C$6`,
`controller!$D$6` and so on.

### ~INPUTCELL

A `ParScen` tag that marks the cell whose value Veda varies across the
parametric runs. The value after the colon declares which run indices to
generate.

| form | generates |
| --- | --- |
| `~InputCell:1-27` | runs 1 through 27 |
| `~InputCell:91-135` | runs 91 through 135 only |
| `~InputCell:5` | run 5 only |

Sub-ranges are useful for regenerating part of a design without redoing
all of it.

!!! warning "Changed from legacy Veda"

    In VEDA_FE a single number was read as the range `1` to that number,
    so `~InputCell: 5` generated runs 1–5. **In Veda2 a single number means
    that index alone.** Write `1-5` for the old behaviour. See
    [Migration from legacy Veda](../migration.md).

## What the input cell can drive

Because everything downstream of the input cell is ordinary spreadsheet
formulas, and because Veda reads the **calculated** workbook, anything in
a sheet that can be written as a formula becomes parametric. That is a
much wider surface than "values in tables".

| lever | how | what it buys |
| --- | --- | --- |
| **Cell values** | formula in the data cell | the obvious one — different numbers per run |
| **Whole tables** | formula produces the tag, or a deactivated form of it | entire blocks of data on or off |
| **Tag content** | formula builds the tag string | change `curr=`, filters, `limtype`, any tag modifier |
| **Column headers** | formula in the header cell | retarget a column — a different year, region, attribute or region group |
| **Columns** | header resolves to a name listed under `~NOpCol` | the column is ignored for that run |
| **Rows** | ignore-character in an index column | the row is skipped for that run |

Two of these deserve notes.

**Deactivating a tag.** Veda matches a tag by looking for `<tag>*` — the
cell must *begin* with the tag name. Anything prefixed to it therefore
switches the table off, and the house convention is to prefix `Deact`:

```
=IF(B4=$C$4, "~TFM_INS-TS: curr=USD22", "Deact~TFM_INS-TS: curr=USD22")
```

This is better than an arbitrary string like `"not this one"`, because the
deactivated form still shows what the table *would* have been.

**Ignoring columns and rows.** `~NOpCol` in
[SysSettings](system-settings.md#nopcol) lists column headers Veda ignores
during tag processing, and it suppresses the sync-log warnings that would
otherwise follow. A header driven by formula can resolve to one of those
names, which takes the column out of play cleanly. For rows, Veda supports
a per-column ignore character; **Model Info → Veda Tags** lists the
character that applies to each column of each tag.

Combining these, a single integer can change what a table says, which
parts of it are read, what it is addressed to, and whether it exists at
all.

## Wiring data to the controller

Two patterns dominate, suited to different kinds of variation.

### Switching blocks by tag presence

Lay out each variant as a complete block side by side and make the tag
conditional, as above. Simple, and the data stays visible as literal
values. The cost is one block per variant per table, which grows quickly
once a dimension has more than a few levels.

### Driving cells by formula

Keep one block per table and compute each cell from a source sheet,
selecting by whatever the controller resolved:

```
=INDEX(src!$B$2:$L$27,
       MATCH(E$7,src!$A$2:$A$27,0),
       MATCH(controller!$D$6,src!$B$1:$L$1,0))
 * controller!$E$6
```

Here the row is picked by year, the column by the resolved level, and the
result scaled by a resolved multiplier. The tag on such a block is
unconditional, because there is only one block.

This handles level swaps and scalar adjustments in the same structure, and
extends to more levels by adding source columns rather than new blocks.

| | blocks + conditional tag | formula-driven |
| --- | --- | --- |
| data visible as values | yes | only after recalculation |
| adding a level | new block per table | new source column |
| scalar multipliers | awkward | natural |
| best for | few levels, literal data | many levels, derived data |

## A parametric file as a cockpit

Once the controls are a few named cells and the machinery sits behind
formulas, the parametric file can become the **sole entry point** for
people who should use the model but not edit it.

A programme lead, a client, or a colleague from another team opens one
workbook. They see a handful of labelled levers — a carbon trajectory, a
demand storyline, a technology cost level — pick a row, and run. They
never open `BY_Trans`, never touch a SubRES template, never see a
transformation table. The full model is underneath, unchanged and
unendangered.

Nothing extra is required to make this work. The controller is a normal
sheet, so the usual spreadsheet affordances apply: data validation for
dropdowns, named levels instead of indices, a description column
explaining what each row means, protected ranges around everything that is
not a control.

!!! note "The cockpit's author owns the envelope"

    Exposing a few controls is also a promise that every setting they allow
    produces a sensible model. Combinations that are incoherent — a demand
    storyline that contradicts the policy assumption, a cost level outside
    what the rest of the model was calibrated for — are no longer caught by
    the person at the controls, because the point of the cockpit is that
    they cannot see that far down. Keep the design table to combinations
    you have reasoned about.

## Scripting, and where this goes further

A script can obviously generate a set of scenario files. Nothing in Veda
prevents it, and for some jobs it is the right tool.

What a script cannot do is keep the design **inside the model**. Scripted
runs leave a model folder full of generated files whose logic lives
somewhere else — in a language, a library stack and an environment that
have to be reproduced before anyone can say how the runs were made, or
change them. A parametric file keeps the design where the data is, in a
format every Veda user can already read and edit, versioned with the model
and inspectable without installing anything.

The generated children help here too: each is a complete copy of the
apparatus with its own state resolved, so a single child file explains both
what it contains and how it was derived.

!!! tip "They compose"

    Scripting still wins at *deriving* data — unit conversions, fitting,
    pulling from external sources, anything with real computation behind it.
    The two combine well: generate the source sheets programmatically, then
    hand-build the controller and the design table. Computation where
    computation belongs, design where people can see it.

## Generated files

Children are written to `SuppXLS/ParScenFiles/` as
`<parent>_0001.xlsx`, `<parent>_0002.xlsx` and so on. Each is a full copy
of the parent with the input cell overwritten and all formulas
recalculated; the formulas themselves are preserved.

These are **generated output**. The documentation for the
[Navigator](../navigator.md) suggests ignoring them in version control:

```
suppxls/ParScenFiles/
```

## Practical notes

**Recalculation is the engine.** Everything downstream of the input cell
is Excel formulas, so a formula error becomes a missing parameter rather
than a crash. After building a parametric file, generate a couple of
children and check their values against something independent before
trusting the whole set.

**Seed the cached values.** A file written programmatically may contain
formulas with no cached results. Open it once in Excel and save, or set
full-calculation-on-load, before the first sync.

**Mind the combinatorics.** The mechanism makes a thousand runs easy; it
does not make a thousand runs informative. A full factorial over
independently-specified uncertainties will usually overstate the joint
spread, because real dimensions are correlated. Deciding how many runs the
question deserves is still a modelling judgement — the design table just
makes it visible.

**Carry the data lineage.** A parametric file preserves the *design*
perfectly, but the source data is frozen inside it. If the inputs came
from somewhere that updates, record the vintage and a checksum on a notes
sheet, or the file will be perfectly readable and impossible to
reproduce.
