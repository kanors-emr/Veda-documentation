# Veda 2.0 multilingual MkDocs site — pilot bundle

This bundle is the first pilot of the Veda 2.0 documentation as a multi-lingual MkDocs site, ready to be dropped into
the [`kanors-emr/Veda2.0-Installation`](https://github.com/kanors-emr/Veda2.0-Installation) repo and published to
GitHub Pages.

## What's in here

```
veda-mkdocs-site/
├── mkdocs.yml                    # mkdocs-material + mkdocs-static-i18n config
├── requirements.txt              # build dependencies
├── overrides/
│   └── stylesheets/
│       └── extra.css             # Veda custom styles (table wrap, fonts)
├── docs/
│   ├── index.md                  # English landing page
│   ├── index.{ja,fr,de,es,zh}.md # language stubs (fall back to English)
│   ├── getting-started.md
│   ├── getting-started.{ja,fr,de,es,zh}.md
│   ├── introduction.md
│   ├── introduction.{ja,fr,de,es,zh}.md
│   ├── reports.md
│   ├── reports.{ja,fr,de,es,zh}.md
│   └── images/                   # 20 images referenced by the pilot pages
└── .github/
    └── workflows/
        └── docs.yml              # GitHub Actions: build + deploy to GH Pages on push to master
```

## Three pilot pages

| Page | Source | Status |
|---|---|---|
| Reports | `Veda-documentation/docs/source/pages/Reports.rst` | Converted, hand-tuned, ready |
| Getting Started | `Veda-documentation/docs/source/pages/Getting started.rst` | Converted via pandoc |
| Introduction | `Veda-documentation/docs/source/pages/introduction.rst` | Converted via pandoc |

The remaining 17 pages from `Veda-documentation` are not part of this pilot; they will be migrated in a follow-up.

## Six languages, zero non-English content

The MkDocs config sets up six locales: **English** (default), **日本語** (`ja`), **Français** (`fr`),
**Deutsch** (`de`), **Español** (`es`), **中文** (`zh`).

Only English content lives in the bundle. The `mkdocs-static-i18n` plugin's `fallback_to_default: true` setting means
visitors who pick a non-English language will see the English content until a translator adds the corresponding file.

To translate a page, create a sibling file with the locale suffix:

* English source:    `docs/reports.md`
* Japanese version:  `docs/reports.ja.md`     ← create when ready to translate
* French version:    `docs/reports.fr.md`     ← create when ready to translate
* German version:    `docs/reports.de.md`     ← create when ready to translate
* Spanish version:   `docs/reports.es.md`     ← create when ready to translate
* Chinese version:   `docs/reports.zh.md`     ← create when ready to translate

No config change needed — the plugin picks up the new file on the next build. **Do not** create empty stub files;
the plugin treats empty files as "translated to nothing" rather than as missing, so the fallback won't kick in.

The language switcher appears automatically in the header.

## How to drop this into the install repo

From the install repo's master branch:

```sh
# 1. Copy the bundle into the repo root (preserving the .github folder).
#    The install repo doesn't have docs/, mkdocs.yml, or requirements.txt yet,
#    so this won't conflict with anything except the .github folder.
cp -r veda-mkdocs-site/{docs,mkdocs.yml,requirements.txt,overrides} <repo>/

# .github needs a merge — the existing .github folder may have other workflows
mkdir -p <repo>/.github/workflows
cp veda-mkdocs-site/.github/workflows/docs.yml <repo>/.github/workflows/

# 2. Enable GitHub Pages on the repo
#    Settings → Pages → Source: GitHub Actions

# 3. Commit and push
git add docs mkdocs.yml requirements.txt overrides .github/workflows/docs.yml
git commit -m "Add MkDocs documentation site (pilot: Reports + Getting Started + Introduction)"
git push origin master
```

The first push to `master` will trigger the `.github/workflows/docs.yml` workflow, which builds the site and publishes
it to GitHub Pages. The published URL will be:

> **https://kanors-emr.github.io/Veda2.0-Installation/**

(After the first successful build, GitHub Pages will report the live URL in the repo's Settings → Pages.)

## Local preview

```sh
pip install -r requirements.txt
mkdocs serve
# → http://127.0.0.1:8000
```

## Migration plan for the rest

The rema