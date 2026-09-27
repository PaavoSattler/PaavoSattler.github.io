# Website maintenance guide

The goal is to avoid editing the same information in many places.

## New publication

1. Add/clean the BibTeX record in `data/publications.bib`.
2. Add website metadata in `data/publication-meta.yml` if it should be featured or linked to research/software.
3. Until publication-list generation is automated, also add the visible entry to `publications.qmd`.
4. Add journal DOI as the primary link; keep arXiv as an additional free-access link where available.
5. If a preprint becomes published, update arXiv journal metadata without changing the old TeX merely for metadata reasons.

## New preprint

1. Add it under Preprints in `publications.qmd`.
2. Add to `data/publications.bib`.
3. Link it from the relevant research page if useful.
4. Add an explicit GoatCounter event to important arXiv links.

## Software update

Update `data/software.yml` plus the relevant `software/*.qmd` page.

For a CRAN release, add:
- CRAN URL
- installation command
- CRAN tracking event

## New research project

Only expose details that are already public or that you deliberately want to disclose. For unpublished work, describe the problem/research direction rather than technical results.

## Profile/photo

Replace the placeholder with the final 4:5 portrait and update the image reference once. Do not redesign the hero around the final photo.

## Collaboration

Keep the focus on research-oriented collaborations:
- applications/extensions of existing methods/software
- integration into broader methodological frameworks
- projects directly connected to research interests

Do not turn the page into a generic statistics-consulting offer.
