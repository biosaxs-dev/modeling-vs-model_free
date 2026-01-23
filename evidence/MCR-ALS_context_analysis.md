# MCR-ALS Context Analysis: Chemometrics to SAXS

## Purpose
Understand the broader MCR-ALS (Multivariate Curve Resolution - Alternating Least Squares) context from chemometrics and how it applies to SEC-SAXS deconvolution, particularly as the foundation for REGALS.

**Related**: See [historical_development.md](historical_development.md) for the complete historical narrative integrating both EFA and MCR-ALS traditions.

## Sources
- **Jaumot et al. (2004)**: "Application of multivariate resolution methods to the study of biochemical and biophysical processes" - comprehensive review
- **Parker et al. (2018)**: "An endogenous dAMP ligand in Bacillus subtilis class Ib RNR..." - first application of regularized ALS to AEX-SAXS (precursor to REGALS)

---

## MCR-ALS: The General Framework

### Origins (from Jaumot 2004)

**Field**: Analytical chemistry, chemometrics  
**Problem**: Decompose spectroscopic data from evolving mixtures into pure component spectra and concentration profiles  
**Data structure**: Matrix **D** (m × n) where rows = wavelengths/channels, columns = time points/conditions

**Fundamental equation**:
```
D = C · S^T + E
```
- **D**: Experimental data matrix (m × n)
- **C**: Concentration profiles (n × k), k = number of components
- **S^T**: Pure spectra transposed (k × m)
- **E**: Residuals (noise)

### The Rotational Ambiguity Problem (acknowledged 2004)

**Quote from Jaumot**:
> "The solution of Eq. (1) for C and S^T is ambiguous if no additional information is available. In other words, there is a rotational and/or scale (intensity) freedom in the solutions"

**Mathematical statement**:
```
D = C_old · S_old^T = (C_old · T) · (T^-1 · S_old^T) = C_new · S_new^T
```

For ANY non-singular matrix **T**, infinite solutions exist that fit the data equally well.

**Key insight**: This is THE SAME rotation ambiguity problem identified by Maeder (1987) for EFA!

---

## Two Approaches to Resolve Ambiguity

### 1. Hard-Modeling Methods

**Definition**: Apply explicit physicochemical model

**Process**:
1. Postulate model (e.g., equilibrium constants, reaction rates, stoichiometries)
2. Generate initial concentration profiles from model
3. Least squares fit to get pure spectra
4. Refine model parameters iteratively
5. Repeat until residuals acceptable

**Examples**:
- Global analysis with kinetic/thermodynamic models
- Equilibrium studies with known stoichiometry

**Strength**: Reliable solutions when model is correct  
**Weakness**: Requires knowing the model a priori

---

### 2. Soft-Modeling Methods (Self-Modeling)

**Definition**: Do NOT use explicit physicochemical model

**Goal**: "Recovery of the physicochemical model from the data analysis"

**Problem**: Still has rotational ambiguity without constraints!

**Quote from Jaumot**:
> "It is very difficult to recover directly such a model because of the presence of rotational and intensity freedom, which means that many sets of equilibrium or kinetic constants and pure spectra can reproduce the original data set with the same fit quality"

---

## MCR-ALS Algorithm (Classic, from Jaumot 2004)

### Iterative Process:

1. **Initial estimation**: Provide either C or S^T (from EFA, SIMPLISMA, or other method)

2. **Alternating optimization**:
   - If starting with C:
     - Calculate S^T from C (least squares)
     - Apply constraints to S^T (non-negativity, physical meaning)
     - Recalculate C from S^T (least squares)
     - Apply constraints to C (non-negativity, unimodality, closure)
   
3. **Calculate residuals E**

4. **Repeat until convergence**

### Standard Constraints (Soft):
- **Non-negativity**: Concentrations ≥ 0, spectra ≥ 0
- **Unimodality**: Concentration profiles have single peak
- **Closure**: For closed systems, total concentration constant
- **Local rank**: Component present only in certain regions

**Key limitation**: "Soft restraints are rarely sufficient to provide a robust and unique solution on their own" (Jaumot)

---

## Reducing MCR-ALS Ambiguity (Jaumot 2004 Recommendations)

### Strategy 1: Combine with Hard-Modeling
- Use SVD to reduce dimensions, remove noise
- Feed SVD results into global analysis with physicochemical model
- Example: SVD → kinetic model fitting

### Strategy 2: Multi-Experiment Analysis
> "The simultaneous treatment of data matrices corresponding to experiments carried out under different conditions has been shown to reduce dramatically the number of possible solutions"

**Approaches**:
- **Row-wise augmentation**: Same system, different spectroscopies (e.g., absorption + CD)
- **Column-wise augmentation**: Correlated experiments with shared species
- Provides additional constraints through shared components

### Strategy 3: Selective Regions
- Search for conditions where only ONE component exists
- Recover pure spectrum directly
- Use as anchor for full system resolution

---

## Application to SAXS (Missing from Jaumot 2004)

**Note**: The 2004 MCR review mentions various spectroscopies but NOT SAXS:
- Molecular absorption
- Fluorescence  
- Circular dichroism (CD)
- Vibrational CD (VCD)
- NMR
- IR/Raman

**SAXS not mentioned** - likely because:
1. SAXS community slower to adopt chemometric methods
2. SAXS-specific challenges (radiation damage, buffer subtraction)
3. SEC-SAXS coupling relatively new at the time

---

## Parker et al. (2018): Bridging to SAXS

### The AEX-SAXS Problem

**Context**: Study of B. subtilis ribonucleotide reductase  
**Experiment**: Anion-exchange (AEX) chromatography coupled to SAXS  
**Challenge**: Salt gradient creates changing background scattering

**Quote from Supporting Information**:
> "AEX-SAXS data were decomposed into four scattering components: two components represented the changing background due to the NaCl gradient, possibly including its effect on the X-ray window, and two components represented eluting protein species"

### Parker's Solution: Regularized ALS

**Innovation**: Add smoothness regularization to MCR-ALS

**Method** (from SI):
> "The decomposition was performed in MATLAB using the alternating least-squares algorithm, modified to include smoothness regularization applied to the elution peaks"

**Key difference from standard MCR-ALS**:
- Classic MCR: Non-negativity, unimodality constraints
- Parker's method: **Smoothness regularization** (penalize oscillations)

**Rationale**:
- Background scattering must change GRADUALLY with salt gradient
- Regularization function penalizes large oscillations
- Provides additional constraint beyond soft constraints

---

## From Parker (2018) to REGALS (2021)

### Evolution of the Method

**Parker 2018** (AEX-SAXS only):
- Smoothness regularization for background components
- Specific to AEX-SAXS problem
- Custom MATLAB code
- Proof of concept

**Meisburger/REGALS 2021** (general framework):
- Smoothness regularization for BOTH concentrations AND SAXS profiles
- Works for multiple experiment types (AEX, titration, time-resolved, SEC)
- **Flexible constraint framework**: smoothness, compact support, d_max, boundary conditions
- General-purpose software package (MATLAB + Python)

### REGALS = MCR-ALS + Flexible Regularization

**From REGALS paper**:
> "We chose to adapt the alternating least-squares (ALS) algorithm, which is often used in classic MCR"

**Key innovations beyond classic MCR-ALS**:
1. **Tikhonov-Miller regularization** (smoothness penalty)
2. **Parametric basis vectors** (simple, smooth, or real-space P(r))
3. **Compact support** (optional, for concentration OR real-space)
4. **Normalized singular values** for rank determination (s'_j > 1)

---

## The Constraint Hierarchy (REGALS vs. MCR-ALS)

### Classic MCR-ALS (Jaumot 2004):
- Level 1: Data fit only → Infinite solutions (rotational ambiguity)
- Level 2: + Non-negativity → Still many solutions
- Level 3: + Unimodality/closure → Reduced solutions but often insufficient

### REGALS (2021):
- Level 1: Data fit only → Infinite solutions
- Level 2: + Smoothness regularization → Orthogonal ambiguity only
- Level 3: + Non-negativity → Almost unique (discrete permutation may persist)
- Level 4: + Compact support/d_max/boundary conditions → Unique for generic data

**Key advance**: **Regularization reduces ambiguity MORE than soft constraints alone**

**Detailed analysis**: See [../explorations/REGALS_analysis_summary.md](../explorations/REGALS_analysis_summary.md) for mathematical proof of the constraint hierarchy.

---

## Comparison: MCR-ALS vs. EFA vs. REGALS

| Feature | Classic MCR-ALS | EFA | REGALS |
|---------|----------------|-----|--------|
| **Rank determination** | SVD or user-specified | SVD + forward/backward | SVD (s'_j > 1 criterion) |
| **Initial guess** | EFA, SIMPLISMA, or user | Forward/backward analysis | SVD or user |
| **Optimization** | Alternating LS | Rotation matrix | Regularized ALS |
| **Constraints** | Non-negativity, unimodality, closure | FIFO windows (implicit) | Smoothness, compact support, d_max, boundary |
| **Regularization** | None (standard) | None | Tikhonov-Miller (smoothness) |
| **Ambiguity resolution** | Soft constraints (often insufficient) | FIFO assumption (restrictive) | Flexible regularization (robust) |
| **Experiment types** | General (multi-spectroscopy) | Chromatography only | Chromatography, titration, time-resolved |

---

## Key Insights

### 1. Rotation Ambiguity is Universal
- Identified by Maeder (EFA, 1987)
- Acknowledged by Jaumot (MCR-ALS, 2004)  
- Addressed by Meisburger (REGALS, 2021)
- **Same problem**, different communities, 34-year span

### 2. Chromatography Connection
**EFA assumption**: Sequential elution (FIFO) provides constraint  
**MCR-ALS recommendation**: Unimodality for chromatography  
**REGALS innovation**: Compact support (optional) OR d_max (for equilibrium)

**Evolution**: From restrictive (FIFO required) to flexible (multiple constraint types)

### 3. The 30-Year Gap Makes Sense
- MCR-ALS community (chemometrics) separate from SAXS community
- Methods existed but weren't applied to SAXS until Parker (2018)
- REGALS (2021) bridges the communities

### 4. What Makes REGALS Different

**Not just MCR-ALS for SAXS** - it's:
- MCR-ALS framework
- + Tikhonov-Miller regularization (from IFT/P(r) methods)
- + Real-space representation (P(r) basis for SAXS profiles)
- + Flexible constraints adapted to experiment type
- + Software implementation for SAXS community

---

## Implications for Historical Narrative

### The True Timeline

**1987-1991**: EFA identifies rotation ambiguity (chromatography context)  
**1995-2004**: MCR-ALS generalizes approach (chemometrics, no SAXS)  
**2016**: Meisburger et al. apply MCR-ALS + EFA to SEC-SAXS (first mention in REGALS paper)  
**2018**: Parker et al. add smoothness regularization for AEX-SAXS  
**2021**: REGALS generalizes regularized MCR-ALS for all SAXS mixture experiments

### Why 30-Year Gap?
1. **Community separation**: Chemometrics ↔ SAXS
2. **SAXS-specific challenges**: Not straightforward to adapt MCR-ALS
3. **SEC-SAXS adoption**: Method needed the experiment type to become common
4. **Regularization insight**: Parker/Meisburger realized smoothness resolves ambiguity better than soft constraints

### REGALS' Place in History

**REGALS is NOT**:
- A new invention of MCR-ALS
- Just EFA with regularization

**REGALS IS**:
- Sophisticated application of established chemometric framework (MCR-ALS)
- + Modern regularization theory (Tikhonov-Miller, Bayesian)
- + SAXS-specific adaptations (P(r) basis, d_max constraints)
- Solving the same rotation ambiguity problem as MCR-ALS/EFA but with more powerful tools

**Verification**: See [regals/method_verification.md](regals/method_verification.md) for detailed verification of REGALS architecture claims.

---

## Updated Understanding for JOSS Paper

### Key Message

> "SEC-SAXS deconvolution methods have converged from two separate traditions: EFA from chromatography (1987) and MCR-ALS from chemometrics (1995-2004). Both identified the same rotation ambiguity problem. REGALS (2021) brings these traditions together, applying MCR-ALS with flexible regularization to resolve ambiguity more robustly than soft constraints (MCR) or FIFO assumptions (EFA) alone."

### Molass Position

**MCR-ALS/REGALS philosophy**: Model-free with regularization  
- Imposes smoothness/compactness through penalties
- Flexible but requires user parameter choices
- Resolves ambiguity through mathematical constraints

**Molass philosophy**: Explicit parametric modeling  
- Imposes peak shape through explicit models (Gaussian/EGH/SDM/EDM)
- Clear physical interpretation
- Resolves ambiguity through model structure

**Relationship**: Complementary approaches, not competing solutions

---

## References

1. **Jaumot et al. (2004)** - Analytical Biochemistry 327:1-13  
   "Application of multivariate resolution methods to the study of biochemical and biophysical processes"

2. **Parker et al. (2018)** - PNAS 115(20):E4594-E4603  
   "An endogenous dAMP ligand in Bacillus subtilis class Ib RNR promotes assembly of a noncanonical dimer for regulation by dATP"
   - Supporting Information contains AEX-SAXS deconvolution methods

3. **Meisburger et al. (2016)** - J. Am. Chem. Soc. 138(20):6506-6516  
   "Domain movements upon activation of phenylalanine hydroxylase..." (first MCR-ALS + EFA for SEC-SAXS, cited by REGALS)

4. **Maeder & Neuhold (2007)** - "Practical Data Analysis in Chemistry"  
   (cited by Parker 2018 for ALS algorithm)

5. **de Juan & Tauler (2003)** - Critical Reviews in Analytical Chemistry 33:1-27  
   "Multivariate curve resolution" (foundational MCR-ALS review, cited by Jaumot and REGALS)

