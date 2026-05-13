# Tag scope matrix regeneration

`build_tag_matrix.py` regenerates the "Tag scope reference" section
of `docs/veda-tags.md` from the canonical source in
`Veda-PostgreDb/veda_front_end tables and views/VEDA_TIMES_sets-attributes_veda_parameters.xlsx`
(sheet `scentype_taglist`).

## When to re-run

* New tag added or scope changed in the canonical spreadsheet.
* A previously-undocumented tag has now been written up in
  `veda-tags.md` and should be added to the matrix.

## How

```sh
# 1. Add the new tag name to the DOCUMENTED set in build_tag_matrix.py
#    if it's now covered in veda-tags.md.
# 2. If the spreadsheet has no description for that tag, add a short
#    description to DESC_OVERRIDES.
# 3. Regenerate:
python3 scripts/build_tag_matrix.py > /tmp/matrix.md

# 4. Replace the "## Tag scope reference" .. "## Legacy Tags" block in
#    docs/veda-tags.md with the generated /tmp/matrix.md.
```

The script reads only the `scentype_taglist` sheet — adding or
removing rows there is enough to keep the matrix in sync with what
Veda's code actually accepts.
