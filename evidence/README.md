# Evidence for JOSS Research Impact Statement

This directory contains documented evidence supporting the claims made in the Molass Library JOSS paper's Research Impact Statement.

## Structure

### chromixs/
Evidence that CHROMIXS explicitly defers analysis of overlapping chromatographic peaks to "other methods."

**Key claim to validate**: 
> "While CHROMIXS explicitly defers analysis of overlapping chromatographic peaks to 'other methods'" - Panjkovich & Svergun (2018)

### efamix/
Quantified failure thresholds and limitations documented by EFAMIX developers.

**Key claims to validate**:
> "EFAMIX quantifies failure thresholds (signal-to-noise ratio ≥10³ required for three-component separation; peak asymmetry parameter τ≤2; baseline width separation ≥2× for reliable decomposition)" - Konarev et al. (2021)

### regals/
Documentation that REGALS employs a two-stage approach (EFA + regularization) and inherits EFA's fundamental limitations.

**Key claims to validate**:
> "REGALS employs a two-stage approach combining EFA with L1 regularization, inheriting EFA's fundamental limitations in overlapping peak scenarios" - Meisburger et al. (2021); Maeder & Zilian (1988); Keller & Massart (1991)

## Validation Status

- [ ] CHROMIXS claim validated
- [ ] EFAMIX thresholds extracted
- [ ] REGALS two-stage approach documented
- [ ] EFA fundamental limitations documented

## Citation Context

All claims are made in the context of demonstrating that Molass Library addresses documented limitations through explicit parametric modeling (EGH, SDM, EDM) with global optimization constrained by SEC and SAXS theory.
