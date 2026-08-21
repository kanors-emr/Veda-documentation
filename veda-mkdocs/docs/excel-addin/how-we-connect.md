# How we connect

## What this is for

The add-in does not talk to the database by itself. It connects to the **local VEDA 2.0** application, which exposes a small assistant API on your machine. Excel uses that link for catalogs, Cell Info, and tag-related lookups.

## How connection works

1. Start **VEDA 2.0** and open (or import) your model.
2. While VEDA is running, it writes a port number to:

   `%LocalAppData%\VEDA\assistant_api_port.txt`

3. The Excel add-in reads that file and connects to VEDA on `127.0.0.1` using that port.
4. When the link is healthy, the ribbon can show the resolved model name (see [How models are linked](how-models-are-linked.md)).

## What “connected” means

- VEDA 2.0 is running.
- The port file exists and points to a live API.
- The add-in can reach VEDA (for example a ping succeeds) and load catalog data when needed.

If VEDA is closed, the port file is missing, or the API is unreachable, features that need the model will fail or show connection messages. See [Troubleshooting](troubleshooting.md) and [Where to find the logs](logs.md).

## Checklist before you work

1. VEDA 2.0 is open.
2. Your model is imported in VEDA.
3. Excel shows a model name on the **VEDA** ribbon (not `Model: (none)`), for a workbook saved under that model’s folders.
4. If something fails, confirm `%LocalAppData%\VEDA\assistant_api_port.txt` exists while VEDA is running.
