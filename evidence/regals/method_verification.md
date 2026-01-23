# REGALS Method Verification

## Purpose
Verify claims about REGALS architecture made in [historical_development.md](../historical_development.md) by carefully reading the REGALS paper (Meisburger et al., 2021) and supporting information.

## Sources
- Main paper: "REGALS: a general method to deconvolve X-ray scattering data from evolving mixtures" (2021, Steve P. Meisburger, Da Xu, Nozomi Ando)
- Supporting information: Parameter tables for 4 datasets (BsRNR AEX-SAXS, PheH titration, MsbA time-resolved, CypA T-jump)

## Key Claims to Verify

### Claim 1: "Two-Stage Architecture"
**ORIGINAL CLAIM (from historical_development.md):**
> "REGALS (2021): Two-stage architecture - Stage 1 detects components using SVD (similar to EFA), Stage 2 applies regularization to resolve them"

**VERIFICATION:**
❌ **INCORRECT CHARACTERIZATION** - REGALS does **NOT** have a "two-stage architecture" in the sense of separate detection and resolution stages.

**What REGALS Actually Does:**
1. **Rank determination (K)**: Uses SVD with normalized singular values s'_j = (s_j - M^(1/2)) / N^(1/2). Components with s'_j > 1 are considered signal above noise (based on random matrix theory).

2. **Single iterative optimization**: Uses regularized Alternating Least Squares (REGALS algorithm) that alternates between:
   - Step 1: Optimize SAXS profiles (Y) while holding concentrations (C) fixed
   - Step 2: Optimize concentrations (C) while holding SAXS profiles (Y) fixed
   - Repeat until convergence

**Direct Quote from Paper (Section 2.3):**
> "ALS replaces the single nonlinear optimization problem with two linear problems that are solved in an alternating fashion over many iterations."

> "The REGALS algorithm solves equation (14) iteratively using ALS with regularization [Fig. 1(c)]. First, an initial guess is made for the concentration basis parameters (v̂). [...] In the first least-squares step, the SAXS basis functions are optimized while the concentrations are held fixed: û := argmin_u [χ²(u,v̂) + Ψ(u)]. [...] In the second least-squares step, the concentration basis functions are optimized while the SAXS profiles are held fixed: v̂ := argmin_v [χ²(û,v) + Ψ'(v)]."

**Correct Characterization:**
REGALS uses **SVD for rank determination** (similar to EFA), then **regularized ALS for iterative unmixing** of basis vectors. The "two steps" are within each iteration of the optimization, not separate architectural stages.

---

### Claim 2: "Compact Support and FIFO Assumption"
**ORIGINAL CLAIM (from historical_development.md):**
> "Like EFA, assumes compact support (sequential elution) in concentration space"

**VERIFICATION:**
✅ **PARTIALLY CORRECT** - but nuanced:

**What REGALS Actually Does:**
1. **Compact support is OPTIONAL** - can be applied to:
   - Concentration profiles (x_min, x_max range) - for chromatography data
   - SAXS profiles in real space (d_max cutoff for P(r)) - for titration/time-resolved data

2. **Not limited to chromatography**: Works for equilibrium titrations, time-resolved SAXS where concentrations are non-zero everywhere

**Direct Quote from Paper (Introduction):**
> "The models include two types of restraint: smoothness and compact support. In AEX-SAXS, for example, each elution peak is assumed to be non-zero over a particular range (compact support) and the background components are assumed to be smooth."

> "In other cases, such as equilibrium titration and time-resolved SAXS, where concentrations are typically non-zero in all (or nearly all) data frames, the assumption that concentrations have compact support is insufficient. However, compact support can be applied to the SAXS profiles in real space by imposing a maximum particle dimension."

**Key Difference from EFA:**
- EFA: **REQUIRES** compact support (sequential elution windows) to work
- REGALS: **OPTIONALLY uses** compact support, can also use smoothness + boundary conditions instead

**Supporting Information Evidence:**
Table S1 (BsRNR AEX-SAXS): Uses compact support ranges for dimer (730-1270) and monomer (1150-1600)
Table S2 (PheH titration): Uses real-space compact support (d_max) instead of concentration ranges
Table S3 (MsbA time-resolved): Uses real-space compact support (d_max = 70Å, 62Å)
Table S4 (CypA T-jump): Uses both concentration smoothness AND real-space compact support

---

### Claim 3: "Inherits FIFO Limitation"
**ORIGINAL CLAIM (from historical_development.md):**
> "REGALS inherits the FIFO assumption from compact support, limiting it to well-separated components"

**VERIFICATION:**
⚠️ **NEEDS REVISION** - this conflates two different issues:

1. **When REGALS uses compact support for chromatography**:
   - Yes, user must specify elution ranges (x_min, x_max)
   - This is similar to EFA's windowing but more flexible (can overlap)
   - Still requires some prior knowledge of component locations

2. **When REGALS uses real-space compact support**:
   - Applies d_max constraint to P(r) function
   - NOT related to sequential elution
   - Works for equilibrium mixtures where all components present simultaneously

**Correct Characterization:**
REGALS does NOT fundamentally require FIFO/sequential elution. It CAN use compact support as one type of regularization among others (smoothness, boundary conditions, d_max constraints). For chromatography data, manually specifying concentration ranges still requires some knowledge of component locations, but REGALS is more flexible than EFA.

---

### Claim 4: "Cites Maeder 1987"
**ORIGINAL CLAIM:**
> "REGALS (2021) cites Maeder (1987) in context of MCR-ALS for SEC-SAXS"

**VERIFICATION:**
✅ **CONFIRMED**

**Direct Quote from Paper (Introduction):**
> "One exception is SAXS data collected with in-line size-exclusion chromatography (SEC-SAXS), where MCR-ALS has been combined with evolving factor analysis (EFA) (Maeder, 1987) to separate overlapping elution peaks (Meisburger et al., 2016; Hopkins et al., 2017)."

---

## Summary of Corrections Needed

### Critical Error:
**"Two-stage architecture"** is a mischaracterization. REGALS is NOT:
- Stage 1: Component detection (SVD)
- Stage 2: Regularized resolution

REGALS IS:
- Rank determination: SVD with s'_j > 1 criterion (same as many methods)
- Iterative optimization: Regularized ALS alternating between Y and C within each iteration

### Moderate Revision:
**"Compact support"** characterization needs nuance:
- NOT a fundamental requirement (like in EFA)
- ONE option among multiple regularization strategies
- Can be applied to concentration OR real-space P(r)
- More flexible than EFA

### Minor Clarification:
**"Inherits FIFO limitation"** - overstated
- Only applies when using concentration-space compact support
- Does NOT apply to equilibrium titrations using d_max constraints
- More general than EFA

---

## Updated REGALS Description

**Accurate characterization for historical_development.md:**

> **REGALS (Regularized Alternating Least Squares, 2021, Meisburger et al.):**
> 
> - **Rank determination**: Uses SVD with normalized singular values (s'_j > 1 criterion, similar to EFA and EFAMIX)
> - **Optimization method**: Iterative regularized ALS alternating between SAXS profiles and concentrations
> - **Regularization types**: 
>   - Smoothness (penalize oscillations)
>   - Compact support (optional, for concentration ranges or real-space d_max)
>   - Boundary conditions (zero at edges)
> - **Key innovation**: Flexible regularization framework adaptable to different experiment types (chromatography, titration, time-resolved)
> - **Citations**: Explicitly cites Maeder (1987) for EFA in context of SEC-SAXS
> - **Limitations**: 
>   - When using concentration compact support for chromatography, user must specify approximate elution ranges (similar to EFA windowing but more flexible)
>   - Does NOT fundamentally require sequential elution (FIFO)
>   - Can handle equilibrium mixtures using alternative constraints (d_max, smoothness, boundary conditions)

---

## Implications for Historical Narrative

1. **REGALS is NOT "EFA + regularization"** - it's MCR-ALS + regularization with flexible constraints

2. **REGALS is MORE general than EFA** - works for equilibrium systems, not just chromatography

3. **REGALS still requires user input** - must choose:
   - Number of components K (from SVD)
   - Type of constraints (smoothness, compact support, d_max)
   - Regularization parameters (λ, λ')
   - Concentration ranges (if using compact support)

4. **The fundamental rotation ambiguity remains** - REGALS resolves it using:
   - Regularization (smoothness)
   - Compact support (when applicable)
   - Physical constraints (non-negativity, normalization)
   
   But these are still **assumptions about the solution**, not derivation from first principles

5. **Molass comparison point**: 
   - REGALS: Imposes soft constraints through regularization
   - Molass: Derives constraints from explicit parametric peak models (Gaussian, EGH, etc.)
   
   Both escape the rotation ambiguity, but through different philosophies (regularization vs. parametric modeling)

