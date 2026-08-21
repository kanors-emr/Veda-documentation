# Where to find the logs

## Add-in log

The Excel add-in writes a single log file:

`%LocalAppData%\VEDA\addin.log`

- On a typical Windows account this expands to something like  
  `C:\Users\<YourUserName>\AppData\Local\VEDA\addin.log`
- The file is **auto-truncated** when it grows past about **1 MB**.
- Open it with Notepad or any text editor after reproducing a problem.

## Connection port file

While VEDA 2.0 is running, the assistant API port is stored here:

`%LocalAppData%\VEDA\assistant_api_port.txt`

If this file is missing while you expect VEDA to be up, connection will fail. See [How we connect](how-we-connect.md).

## What to send when reporting an issue

Include as much of the following as you can:

1. What you were doing (command, workbook type, synced or not).
2. Exact error or status text from Excel or the task pane.
3. A copy of `%LocalAppData%\VEDA\addin.log` from after the failure (or the relevant last lines).
4. Whether VEDA 2.0 was running and whether the ribbon showed a model name or `Model: (none)`.
5. Whether `%LocalAppData%\VEDA\assistant_api_port.txt` existed at the time.
