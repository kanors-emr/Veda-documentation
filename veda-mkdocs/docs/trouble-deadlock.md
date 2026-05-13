# Deadlock Detected

> 
> 
> <div class="note">
> 
> <div class="title">
> 
> Note
> 
> </div>
> 
> **This has been resolved in version 2.005.1.1**
> 
> </div>

**Issue**: Deadlock Detected

The error occurs when mulitple SubRES files are imported together:

> ![](images/deadlock_detected.png)

**Workaround**: Go to Tools -\> User Optons -\> Syncing Options -\> Set
Threads Count to 1 and press update button.

After sync is completed, reset the Threads count to -1 or previous
value.

> 
> 
> <div class="note">
> 
> <div class="title">
> 
> Note
> 
> </div>
> 
> Do this only when you want to sync multiple SubRES files together
> 
> </div>
