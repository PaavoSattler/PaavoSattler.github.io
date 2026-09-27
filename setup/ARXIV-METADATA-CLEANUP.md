# arXiv metadata cleanup

Goal: when an arXiv preprint is later published, keep the arXiv source/PDF unchanged unless there is a real manuscript update, but add **Journal reference** and **Related DOI** metadata.

## Already linked correctly on arXiv

### arXiv:2411.10121
*Quadratic Form based Multiple Contrast Tests for Comparison of Group Means*  
Journal reference and journal DOI are already shown on arXiv:
- Journal of Statistical Planning and Inference 245 (2026), Article 106414
- DOI: `10.1016/j.jspi.2026.106414`

## Candidates to inspect/update in arXiv account

The current public arXiv pages found during preparation did not expose a journal-reference field for these records, even though the works are now published. Verify inside the arXiv account and add journal metadata if missing:

### arXiv:2409.12592
*Choice of the hypothesis matrix for using the Anova-type-statistic*  
Published: Statistics & Probability Letters 219 (2025), 110356  
Journal DOI: `10.1016/j.spl.2025.110356`

### arXiv:2209.04380
*Testing Hypotheses about Correlation Matrices in General MANOVA Designs*  
Published: TEST 33(2)  
Journal DOI: `10.1007/s11749-023-00906-6`

### arXiv:1909.06205
*Testing Hypotheses about Covariance Matrices in General MANOVA Designs*  
Published: Journal of Statistical Planning and Inference 219 (2022), 134–146  
Journal DOI: `10.1016/j.jspi.2021.12.001`

### arXiv:2310.11799
*Testing for patterns and structures in covariance and correlation matrices*  
Published: Journal of Multivariate Analysis 211 (2026), 105517  
Journal DOI: `10.1016/j.jmva.2025.105517`

### arXiv:1706.02592
*Inference For High-Dimensional Split-Plot-Designs: A Unified Approach for Small to Large Numbers of Factor Levels*  
Published: Electronic Journal of Statistics 12(2) (2018), 2743–2805  
Journal DOI: `10.1214/18-EJS1465`

## Current preprints (no journal metadata yet)

- arXiv:2609.07435 — Dobler, Kuhn, Amro & Sattler
- arXiv:2604.06915 — Munko & Sattler
- arXiv:2507.03406 — Sattler & Jedhoff / CovCorTest
- arXiv:2512.17478 — Sattler & Hichert / hdrm

## Rule

Do not upload a new TeX/PDF version solely to add journal metadata. Use arXiv's metadata update for the journal reference and journal DOI.
