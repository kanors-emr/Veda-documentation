#################
Deadlock Detected
#################

**Issue**: Deadlock Detected

    The error occurs when mulitple SubRES files are imported together:

    .. image:: images/deadlock_detected.png
        :width: 600

**Workaround **: Go to Tools -> User Optons -> Syncing Options -> Set Threads Count to 1 and press update button.

    After sync is completed, reset the Threads count to -1 or previous value.

    .. note::
        Do this only when you want to sync multiple SubRES files together