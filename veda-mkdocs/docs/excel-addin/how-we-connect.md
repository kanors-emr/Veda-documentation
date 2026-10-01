# How we connect

## What this is for

The add-in does not talk to the database by itself. It connects to the **local VEDA 2.0** application, which exposes a small assistant API on your machine. Excel uses that link for catalogs, Cell Info, and tag-related lookups.

## How connection works

1. Start **VEDA 2.0** on this machine and open your model.
2. The **Session** line on the **VEDA** ribbon shows **Connected** when Excel can reach that VEDA.
3. The same group shows the model name for the workbook (see [How models are linked](how-models-are-linked.md)).

## What “connected” means

- VEDA 2.0 is running on this machine.
- The ribbon shows **Connected**.

If VEDA is closed, features that need the model fail or show a connection message. See [Troubleshooting](troubleshooting.md) and [Where to find the logs](logs.md).

## Checklist before you work

1. VEDA 2.0 is open.
2. Your model is imported in VEDA.
3. Excel shows **Connected**, and a model name on the **VEDA** ribbon (not `Model: (none)`). Under an imported model folder that name is the file’s model; on a Desktop or unsaved file it is the model open in VEDA ([Files outside the model](files-outside-the-model.md)).

## Session

The **Session** group’s connection control is only the link to VEDA.

| Ribbon | Meaning |
|--------|---------|
| **Connected** (green check) | Excel can reach VEDA 2.0. Click to try again. |
| **Not Connected** (red cross) | No link. Click to try again. |
| **Model: …** or **Model: (none)** | The model name for this workbook |

A failed click shows one of these messages:

- **VEDA 2.0 did not respond in time.** Start VEDA, open a model, wait, then click again.
- **VEDA 2.0 is not reachable on the local API port.** Start VEDA 2.0, open a model, then click again.
- **VEDA 2.0 returned an error on connect.** Check the VEDA log, then click again.
- **Not connected to VEDA 2.0.** Start VEDA 2.0, open a model, then click again.

## Compatibility

A separate ribbon control. It is not the connection status. The line starts with **Version** and the add-in version. While disconnected, that is all it shows. While connected, a second note is added:

| Note | Meaning |
|------|---------|
| **Compatibility: OK** (green check) | This add-in and the running VEDA are a supported pair. |
| **Upgrade add-in →** *version* | Install that add-in version. |
| **Upgrade VEDA →** *version* | This add-in needs that VEDA version. |
| **Compatibility not verified** | The pair could not be checked. |

Hovering the line shows the full mismatch text. The same text is in **About**. A mismatch does not block the other commands.
