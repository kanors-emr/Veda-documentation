# Veda Conventions

!!! note "Note"

    Veda has made a large number of choices that might appear quite
    arbitrary. Some of them are explained here.

  - Tags like <span class="title-ref">\~FI\_T</span> and
    <span class="title-ref">\~FI\_Process</span> do not support the
    Region dimension in SubRES files
    
      - The vision behind SubRES files is to describe a sub-part of the
        overall RES, like hydrogen production for example, purely as a
        technology repository that can be easily shared across models.
        One would typically use the
        <span class="title-ref">TFM\_AVA</span> tag to control
        availability of technologies across regions and apply regional
        multipliers via <span class="title-ref">TFM\_UPD</span>.

  - SysSettings is imported at the end of each Sync operation
    
      - SysSettings is where you declare the default interpolation
        options.

  - BY\_Trans sees only VT files and SubRES trans files see only their
    own SubRES
    
      - This is to respect an obvious requirement: Start from scratch
        and any partial import of a set of files should produce the same
        output.

  - 'UC\_T' tags are supported only in Scenario files (not in VT,
    SubRES, or Trade)
    
      - <span class="title-ref">VT files</span> don't support
    <span class="title-ref">TFM tags</span>
    
      - <span class="title-ref">TFM tags</span> are most useful when
        they can access a large part of the RES. If they were supported
        in VT files then they would see only the processes that are
        defined in the same VT file. They are supported in
        <span class="title-ref">BY\_Trans</span> instead, where they can
        access all VT files.
