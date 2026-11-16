# Command line (Veda CLI)

!!! warning "Proposed feature"
    Veda CLI is in development and is not part of a released version of
    Veda 2.0 yet. This page describes what we have built so far; commands
    and options may change. Tell us what you need in the
    [Veda CLI forum thread](https://forum.kanors-emr.org/showthread.php?tid=1627){ target="_blank" rel="noopener noreferrer" }.

## Overview

Veda CLI (`veda.exe`) runs Veda 2.0 jobs from the command line, without
opening the Veda window. Use it to automate repetitive work, run jobs
overnight, or call Veda from your own scripts (batch files, PowerShell,
Python, a scheduler).

| Command | Does the same as | Changes |
| --- | --- | --- |
| `veda sync` | Sync in the Navigator | The model's data in the database |
| `veda solve` | Solve in the Run Manager | DD and run files, GAMS runs, imported results |
| `veda results` | A full refresh of the Results module | Deletes and rebuilds the model's results |

**Requirements**

- A licensed Veda 2.0 installation.
- Veda has been opened at least once on this computer by the same Windows
  user. Veda CLI uses that user's licence, database and settings, so it
  sees the same models and cases you see in Veda, and what it produces
  shows up in Veda as usual.

`veda --help` prints every command and option. Commands and option names
are not case-sensitive.

## veda sync

Reads a model's Excel files into the database, as the Sync button does.

```
veda sync --path <model folder> [options]
veda sync --model <model folder name> [options]
```

| Option | Value | Meaning |
| --- | --- | --- |
| `--path` | folder | Model folder. Needed the first time, when the model is not registered yet; Veda CLI registers it. |
| `--model` | folder name | Model folder name of a registered model. Default: the last folder name of `--path`. |
| `--select` | `all_model` (default), `inconsistent`, `not_imported`, `except_consistent` | Which files to read: every file (the model is not dropped), changed files, new files, or changed + new + error files. Give it once. |
| `--threads` | 1 or more | Thread count for this run. Default: your Veda setting. |
| `--no-parametric` | — | Skip parametric scenarios. |

What it does:

1. Finds the model, or registers it from `--path`. A registered model must
   be at the same path.
2. Reads the model folder. If files are open in Excel, or file names are
   duplicated, it stops and nothing is synced.
3. Picks the files. Deleted files are always removed from the model and
   dependent files are added. On a model's first import every file is
   read, whatever `--select` says.
4. Syncs, writes the SyncLogs workbooks in the model folder as the
   Navigator sync does, and reports the number of tag errors.

Examples:

```
veda sync --path E:\VedaModels\DemoS_010
veda sync --model DemoS_010 --select inconsistent --threads 6
veda sync --model DemoS_010 --select not_imported --no-parametric
```

## veda solve

Solves saved TIMES cases, as Solve in the Run Manager does: writes the DD
and run files, runs GAMS, then reads and imports the results. Anything you
do not give on the command line comes from the model's saved Run Manager
settings.

```
veda solve --model <model folder name> --case <case name> [--case <case name> ...] [options]
```

| Option | Value | Meaning |
| --- | --- | --- |
| `--model` | folder name | Required. Model folder name of a registered model (register it with `veda sync --path` first). |
| `--case` | case name | Required. A saved case to solve. Repeat it for more cases. |
| `--run-type` | `local`, `dd_only` | `local`: write DD files and run GAMS on this computer. `dd_only`: write the DD and run files only. |
| `--study` | folder name, no spaces | Study the results are imported into. |
| `--max-runs` | 1 or more | Cases solved at the same time, limited by your licence. |
| `--rebuild-results` | — | After the solve, rebuild the model's results, as `veda results` does. |

What it does:

1. Checks everything before writing anything: the model, the saved Run
   Manager settings, the cases, GAMS on the PATH (for `local`) and the
   model's TIMES data. Any problem stops it, and nothing is written.
2. Writes the DD files and runs GAMS for each case, showing its case
   folder. A parametric case runs all its runs. Case folders follow the
   Run Manager: `<GAMS work folder>[\<study>][\<case name>]`.
3. Imports the results as the Run Manager does. Only an Optimal, Integer
   solution or Intermediate nonoptimal solve is imported; any other status
   (for example Infeasible) is reported as failed, with its run log.
4. Prints a summary line per run: name, status and case folder.

With `--rebuild-results`, the model's results are rebuilt once after all
cases finish, when at least one case was imported. The rebuild is skipped
for `dd_only`, when the solve was cancelled, or when no case was imported.

Before the first solve of a model, open its Run Manager in Veda once so
that its settings are saved.

Examples:

```
veda solve --model DemoS_011 --case BASE
veda solve --model DemoS_011 --case BASE --case CO2 --study test1 --max-runs 2
veda solve --model DemoS_011 --case BASE --run-type dd_only
veda solve --model DemoS_011 --case BASE --rebuild-results
```

## veda results

Deletes a model's results and builds them again from all your imported
cases. Use it after cases were solved outside Veda, or when the Results
module looks out of date.

```
veda results --model <model folder name>
```

| Option | Value | Meaning |
| --- | --- | --- |
| `--model` | folder name | Required. Model folder name of a registered model. |

The rebuild also reads the model's set-rules and sys-settings files and
prints their messages.

!!! caution "Caution"
    - The model's results are deleted first. If the rebuild fails part
      way, run `veda results` again.
    - Keep the Results module of this model closed in Veda while it runs.
    - Ctrl+C stops it only before the rebuild starts; once started, it
      runs to the end.

Example:

```
veda results --model DemoS_011
```

## Sync and solve in one go

Commands can be chained in a batch file. Here the solve starts only when
the sync succeeded:

```
veda sync --model DemoS_011 --select inconsistent && veda solve --model DemoS_011 --case BASE --rebuild-results
```

## Exit codes

Every command returns an exit code, so a script can check
`%ERRORLEVEL%` (or `$LASTEXITCODE` in PowerShell) and decide what to do
next.

| Code | sync | solve | results |
| --- | --- | --- | --- |
| 0 | Completed, or nothing to sync | Every case solved and imported (`dd_only`: DD written) | Rebuilt |
| 1 | Bad arguments or input; the model was not changed | Bad arguments or input; nothing was written | Bad arguments, or unknown model; nothing changed |
| 2 | Failed after the model started changing; run it again | One or more cases failed, or the results rebuild failed | Rebuild failed; run it again |
| 3 | Cancelled with Ctrl+C | Cancelled; DD writing and GAMS are stopped | Cancelled before the rebuild started |
| 4 | Files open in Excel, or duplicate file names; nothing synced | — | — |
| 5 | Veda is not set up for this user on this computer (licence or registration) | same | same |
| 6 | Completed, but the model has tag errors (see SyncLogs) | With `--rebuild-results`: rebuilt, but the set-rules / sys-settings files reported errors | Rebuilt, but the set-rules / sys-settings files reported errors |

The first Ctrl+C cancels cleanly. A second Ctrl+C ends Veda CLI at once,
and the model or results may be left part way.

## Current limits

- TIMES cases only.
- Run types `local` and `dd_only` only.
- One model per command.

## Troubleshooting

| Message | What to do |
| --- | --- |
| No activated Veda licence for user … | Open Veda on this computer as this user to activate the licence. |
| User … is not registered on computer … | Open Veda once on this computer, then run again. |
| Cannot connect to the Veda database on … | Check that the database server in your Veda settings is running. |
| No model for folder … | Register it first: `veda sync --path <model folder>`. |
| Close these files and run again | Close the listed workbooks in Excel. |
| The Run Manager settings of this model are not saved yet | Open the Run Manager for this model in Veda once. |
| GAMS was not found on the PATH | Install GAMS, or use `--run-type dd_only`. |
| The model has no TIMES sets or base / SubRES data | Sync the model first. |
| N case(s) failed | Read `<case>_run_log.txt` and `<case>.lst` in the case folder shown. |
