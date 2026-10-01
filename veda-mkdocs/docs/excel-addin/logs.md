# Where to find the logs

## Add-in log

The Excel add-in writes one log file per day:

`%LocalAppData%\VEDA\addin-yyyy-MM-dd.log`

- On a typical Windows account this expands to something like  
  `C:\Users\<YourUserName>\AppData\Local\VEDA\addin-yyyy-MM-dd.log`
- Open it with Notepad or any text editor after reproducing a problem.

## What to send when reporting an issue

Include as much of the following as you can:

1. What you were doing (command, workbook type, synced or not).
2. Exact error or status text from Excel or the task pane.
3. A copy of the day’s log, `%LocalAppData%\VEDA\addin-yyyy-MM-dd.log`, from after the failure (or the relevant last lines).
4. Whether VEDA 2.0 was running and whether the ribbon showed a model name or `Model: (none)`.
