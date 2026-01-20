# EFA Original Papers - Documented Limitations

This folder contains systematic analysis of limitations documented in the **original EFA (Evolving Factor Analysis) papers** by its inventors (Maeder & Zilian 1988, Keller & Massart 1991).

## Purpose

EFA is not specific to any single method—it's a general technique for analyzing multivariate data with intrinsic order. Multiple methods build upon EFA:

- **EFAMIX**: Pure EFA implementation (Konarev et al., 2021)
- **REGALS**: EFA + regularization (Meisburger et al., 2021)
- **Other methods**: Various implementations in chromatography and equilibrium studies

Because EFA limitations are **inherited by any method using EFA**, this analysis is kept separate from method-specific evidence.

## Contents

### EFA_limitations_from_inventors.md
Systematic extraction of all limitations documented by EFA's inventors in their foundational papers:
- **Maeder & Zilian (1988)**: Original EFA paper
- **Keller & Massart (1991)**: EFA tutorial

**Key findings:**
1. "Tailing seems to be the most serious difficulty" (most serious problem)
2. "Rank of data matrix will be higher than number of underlying chemical species" (systematic rank inflation)
3. Sequential elution assumption (FIFO) required
4. No quantification without external calibration
5. Baseline, noise, and instrumental artifacts cause problems

## Relationship to JOSS Validation

### For REGALS evidence:
REGALS uses EFA as Stage 1 (component detection) → inherits all EFA limitations documented here

### For EFAMIX evidence:
EFAMIX is pure EFA implementation → all limitations apply directly

### For Molass Library justification:
These documented EFA limitations demonstrate why explicit parametric modeling approaches (like Molass) may be advantageous for certain cases, particularly:
- Overlapping peaks with tailing
- Systems where rank estimation is uncertain
- Scenarios requiring quantification

## Source Papers

Both foundational EFA papers are in [reference_papers/](../../reference_papers/):
- `1988, Marcel Maeder.pdf`
- `1991, H.R. Keller.pdf`

Extracted text available in [tools/efa_papers.txt](../../tools/efa_papers.txt)
