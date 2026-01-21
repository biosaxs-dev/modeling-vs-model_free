# Revised EFA Limitation Verification Plan

**Date**: January 21, 2026  
**Context**: After reviewing the REGALS mathematical analysis, we've consolidated the 10 original limitations into 3-4 fundamental ones.

---

## Problem with Original 10 Limitations

**Redundancy identified:**
- Limitations 1, 6, 7, 8, 9 all describe **rank inflation** (same problem, different manifestations)
- Limitation 4 conflates two separate issues:
  - Scale ambiguity → Just measurement units (not a real limitation)
  - Rotation ambiguity → The fundamental problem
- Limitation 10 overlaps with Limitation 3 (both about FIFO)

**Mathematical insight from REGALS analysis:**
The fundamental problems are about the **constraint hierarchy** needed to resolve underdeterminedness:
- Level 1-2: Rotation/mixing ambiguity
- Real data: Rank inflation
- Chromatographic: FIFO assumption violations
- Signal quality: Resolution and noise limits

---

## Revised Core Limitations

### 1. ✅ FIFO Assumption Violation (VERIFIED)

**Notebook**: `limitation_3_tailing_effects.ipynb` (15 cells, fully executed)

**What it shows**:
- Forward/backward EFA assumes First-In-First-Out elution
- Fails even for ideal Gaussian peaks with sufficient overlap
- Produces negative window widths (mathematical impossibility)
- Component 3 appears at frame 60 but "disappears" at frame 51

**Key finding**: FIFO is not just a tailing problem - it's fundamental to overlapping components

**Inventor quote** (Maeder 1988, p. 211):
> "tailing seems to be the most serious difficulty"

**Status**: ✅ Complete - Critical discovery made

---

### 2. ⏳ Rotation/Mixing Ambiguity (TO BE REVISED)

**Current notebook**: `limitation_4_no_quantification.ipynb` (needs revision)

**What needs to change**:
- **Remove**: Focus on scale ambiguity $(αP, C/α)$ ← This is just measurement units
- **Add**: Focus on rotation ambiguity $(PR, R^{-1}C)$ ← This is the real problem
- **Demonstrate**: 
  - Multiple factorizations give identical data fit
  - Components are arbitrary linear combinations
  - Non-negativity constraint needed to resolve
  - Even then, permutation ambiguity may persist

**Mathematical basis** (from REGALS_analysis_summary.md):
- Level 1: Any invertible matrix $R$ gives identical fit
- Level 2: Smoothness reduces to orthogonal $B$ only
- Level 3: Non-negativity almost eliminates continuous ambiguity
- Level 4: Discrete permutation may persist (5-50% of cases)

**Inventor quote** (Maeder 1988, p. 212):
> "Arbitrary rotation matrix means no absolute quantification"

**Keller quote** (1991, p. 216):
> "The concentration profiles are only determined up to a rotation"

**Target**: Demonstrate why REGALS needs non-negativity (Level 3) - this is inherited from EFA's fundamental ambiguity

**Status**: ⏳ Needs revision to focus on rotation, not scale

---

### 3. ⏳ Rank Inflation (TO BE CREATED)

**Planned notebook**: `limitation_rank_inflation.ipynb`

**What to demonstrate**:
- Generate 2-component synthetic data
- Add realistic artifacts:
  - Baseline drift (constant offset)
  - Instrumental noise
  - Heteroscedastic noise (signal-dependent)
- Show singular value spectrum with/without artifacts
- Count "significant" singular values → more than 2!
- Demonstrate gap between true rank (2) and detected rank (3-5)

**Key insight**: Real-world data ALWAYS has higher rank than true components

**Inventor quotes**:

Keller & Massart (1991, p. 223):
> "the rank of the data matrix will be higher than the number of underlying chemical species"

Gerritsen et al. (referenced):
> "in real world applications the number of PCs needed to describe a given system is higher than the number of underlying analytes"

**Causes to demonstrate**:
1. Baseline drift/slope
2. Noise (heteroscedastic)
3. Instrumental artifacts
4. Non-simultaneous measurements

**Target outcome**: Show that EFA cannot reliably determine true number of components - expert judgment required

**Status**: ⏳ Not started

---

### 4. ⏳ Resolution Limitation (TO BE CREATED)

**Planned notebook**: `limitation_resolution.ipynb`

**What to demonstrate**:
- Generate 2 components with variable separation
- Test cases:
  - Well-separated (Δt = 3σ) → 2 clear singular values
  - Moderate separation (Δt = 2σ) → singular values close
  - Poor separation (Δt = 1σ) → cannot distinguish
  - Complete overlap (Δt = 0) → appears as 1 component
- Show singular value gap disappearing with decreasing separation

**Key insight**: EFA cannot resolve peaks closer than ~1 peak width

**Inventor quote** (Maeder 1988, p. 212):
> "The similarity of retention times and absorption spectra, the relative concentrations and the noise level of the instrument are all highly correlating factors which define the limits of the analysis."

**Target**: Quantify minimum separation required for reliable 2-component detection

**Status**: ⏳ Not started

---

### 5. (Optional) Noise Sensitivity

**Potential notebook**: `limitation_noise_sensitivity.ipynb`

**What to demonstrate**:
- 2-component system with variable noise levels
- Show detection threshold for minor component
- Demonstrate instrument-dependence

**Inventor quote** (Maeder 1988, p. 211):
> "The detectability of minor components in a peak cluster and the ability of discrimination between components with either very similar absorption spectra or concentration profiles obviously are strongly correlated with the noise level."

**Status**: Lower priority - may defer

---

## Summary Document

**File**: `EFA_core_limitations.md`

**Contents**:
1. Introduction - Why 3-4 core limitations, not 10
2. Limitation 1: FIFO Violation
   - Link to limitation_3_tailing_effects.ipynb
   - Inventor quotes
   - Key findings
3. Limitation 2: Rotation Ambiguity
   - Link to revised limitation_4 notebook
   - Connection to REGALS Level 3 (non-negativity)
   - Permutation ambiguity discussion
4. Limitation 3: Rank Inflation
   - Link to limitation_rank_inflation.ipynb
   - All consolidated quotes about rank
   - Practical implications
5. Limitation 4: Resolution
   - Link to limitation_resolution.ipynb
   - Quantitative thresholds
6. Implications for REGALS
   - Stage 1 (EFA) inherits all these limitations
   - Why Stage 2 (regularization) is needed
   - What constraints address which limitations

---

## Priority Order

1. **Revise limitation_4** → Focus on rotation ambiguity (1-2 hours)
2. **Create rank inflation notebook** (1-2 hours)
3. **Create resolution notebook** (1-2 hours)
4. **Write summary document** EFA_core_limitations.md (1 hour)
5. **Optional**: Noise sensitivity notebook

**Total estimated time**: 5-8 hours for core verification

---

## Connection to JOSS Paper

**Research Impact Statement validation**:

Our verification shows that EFA has **fundamental mathematical limitations**:
1. FIFO assumption (fails for overlapping peaks)
2. Rotation ambiguity (requires non-negativity constraint)
3. Rank inflation (cannot determine true component number)
4. Resolution limits (cannot resolve close peaks)

**These are not implementation details** - they are documented by the inventors themselves and have **mathematical roots** in the underdetermined factorization problem.

**REGALS inherits limitations 1, 3, 4 from EFA Stage 1**, and uses regularization (Stage 2) to partially address limitation 2 (rotation ambiguity).

**Molass** avoids EFA entirely, using explicit parametric models to resolve the factorization uniquely.

This provides **clear evidence** for why alternatives to EFA-based approaches are needed.

---

## References

- Maeder & Zilian (1988) - Original EFA paper
- Keller & Massart (1991) - EFA tutorial
- REGALS_analysis_summary.md - Mathematical constraint hierarchy
- underdeterminedness_exploration.ipynb - 4-level constraint proof
- permutation_ambiguity_examples.ipynb - Discrete ambiguity scenarios

---

**End of Plan**
