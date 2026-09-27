# Analytics / event tracking plan

Target: **GoatCounter hosted service** (free for reasonable public usage) plus Google Search Console.

The site already contains `data-goatcounter-click` attributes for many important links. GoatCounter binds click events to these attributes automatically once its script is enabled.

## Core metrics

### Page visits
- `/`
- `/research.html`
- `/publications.html`
- `/software.html`
- `/collaboration.html`
- `/about.html`
- `/cv.html`
- individual research pages
- individual software pages

### Publication events
Use one stable event name per link, e.g.
- `doi-mct-2026`
- `doi-patterns-2026`
- `doi-ats-2025`
- `arxiv-dobler-2026`

### Software events
- `software-cran-covcortest`
- `software-github-covcortest`
- `software-github-hyposhrink`
- `software-doi-hyposhrink`
- later: `software-cran-hdrm`
- later: `software-github-hdrm`

### Profile / contact events
- `profile-google-scholar`
- `profile-orcid`
- `profile-github`
- `profile-cv`
- `contact-email-home`
- `contact-email-collaboration`
- `affiliation-tu-dortmund`
- `affiliation-rwth-aachen`

## Launch steps

1. Create the GoatCounter account manually.
2. Insert the site code in `includes/analytics.html`.
3. Keep GoatCounter's individual-pageview storage at its default/off setting unless there is a specific reason to change it.
4. Test page visits and at least one click event.
5. Do not add Google Analytics; Search Console is sufficient for Google search visibility.
6. Add Search Console verification to `includes/seo.html`.

## Useful questions after launch

- Which research areas receive the most visits?
- Which featured papers lead to DOI/arXiv clicks?
- Which software pages lead to CRAN/GitHub clicks?
- Does the collaboration page generate email clicks?
- Which Google queries and pages generate impressions/clicks in Search Console?
