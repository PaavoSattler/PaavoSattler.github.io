# GitHub username cleanup: PSattlerStat → PaavoSattler

The account/repository identity has moved to `PaavoSattler`.

## HypoShrink

The current repository README already uses:

```r
devtools::install_github("PaavoSattler/HypoShrink")
```

The current `DESCRIPTION` should be checked: during preparation, its `URL:` field still contained the old path while `BugReports:` already used the new path.

Desired values:

```text
URL: https://github.com/PaavoSattler/HypoShrink
BugReports: https://github.com/PaavoSattler/HypoShrink/issues
```

## Other places to check

Search editable material for:

```text
PSattlerStat
https://github.com/PSattlerStat
```

Check:
- package DESCRIPTION files
- README files
- CITATION/CITATION.cff files
- Zenodo metadata, where editable
- ORCID external links
- CV
- institutional profiles, if a GitHub link is present

## Published papers

Do not try to edit old published PDFs solely because they contain an old GitHub URL. GitHub normally redirects renamed repository URLs. Prefer updating all material that is still editable.
