# REGALS Evidence

## Claims to Validate

**From JOSS paper Research Impact Statement:**
> "REGALS employs a two-stage approach combining EFA with L1 regularization, inheriting EFA's fundamental limitations in overlapping peak scenarios"

## Primary Source

**Paper**: Meisburger, S.P., Xu, D., & Ando, N. (2021). REGALS: a general method to deconvolve X-ray scattering data from evolving mixtures. *IUCrJ*, 8, 225-237.

**DOI**: 10.1107/S2052252521000555

## Supporting Sources (EFA Limitations)

### EFA Invention Paper
**Paper**: Maeder, M. & Zilian, A. (1988). Evolving factor analysis, a new multivariate technique in chromatography. *Chemometrics and Intelligent Laboratory Systems*, 3, 205-213.

**DOI**: 10.1016/0169-7439(88)80051-0

### EFA Tutorial
**Paper**: Keller, H.R. & Massart, D.L. (1991). Evolving factor analysis. *Chemometrics and Intelligent Laboratory Systems*, 12, 209-224.

**DOI**: 10.1016/0169-7439(91)80125-S

## Evidence to Extract

### Two-Stage Process
- [ ] Stage 1: EFA (component detection, window determination)
- [ ] Stage 2: Regularized deconvolution (L1 + smoothness)
- [ ] Section/figure showing this architecture

### EFA Limitations Inherited
From Maeder & Zilian (1988):
- [ ] "Tailing seems to be the most serious difficulty"
- [ ] Baseline sensitivity issues
- [ ] Sequential elution assumption (FIFO)

From Keller & Massart (1991):
- [ ] "Rank of data matrix will be higher than number of underlying chemical species"
- [ ] Rank inflation from instrumental nonlinearities
- [ ] Quantification impossibility without external calibration

### Overlapping Peak Context
- [ ] How REGALS handles overlapping peaks via regularization
- [ ] Limitations that persist despite regularization
- [ ] Comparison to baseline-separated cases

## Validation Notes

*To be filled with specific quotes, method descriptions, and analysis demonstrating the two-stage architecture and inherited limitations.*
