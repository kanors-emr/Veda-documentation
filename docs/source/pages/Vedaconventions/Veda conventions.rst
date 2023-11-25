################
Veda Conventions
################
.. note::
    Veda has made a large number of choices that might appear quite arbitrary. Some of them are explained here.

Tags like `~FI_T` and `~FI_Process` do not support the Region dimension in SubRES files
    * The vision behind SubRES files is to describe a sub-part of the overall RES, like hydrogen production for example, purely as a technology repository that can be easily shared across models. One would typically use the `TFM_AVA` tag to control availability of technologies across regions and apply regional multipliers via `TFM_UPD`.

SysSettings is imported at the end of each Sync operation
    * SysSettings is where you declare the default interpolation options.

BY_Trans sees only VT files and SubRES trans files see only their own SubRES
    * This is to respect an obvious requirement: Start from scratch and any partial import of a set of files should produce the same output.

'UC_T' tags are supported only in Scenario files (not in VT, SubRES, or Trade)
    *

'VT files' don't support 'TFM tags'
    *


