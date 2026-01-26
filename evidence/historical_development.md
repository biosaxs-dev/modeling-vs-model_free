# Historical Development: From EFA Limitations to Modern Solutions

**Purpose**: Trace the historical evolution of problem recognition, quantification, and solution development in SEC-SAXS deconvolution.

**Date**: January 21, 2026

**Key Sources**: 
- [citation_dependency_graph.md](citation_dependency_graph.md)
- [efa_original/EFA_limitations_from_inventors.md](efa_original/EFA_limitations_from_inventors.md)
- [SAXS_methods_analysis.md](SAXS_methods_analysis.md)
- [efa_original/limitation_3_tailing_effects.ipynb](efa_original/limitation_3_tailing_effects.ipynb) (verification)

---

## Executive Summary

The history of SEC-SAXS deconvolution methods reveals **two parallel traditions converging over three decades**:

**Chromatography tradition (EFA lineage)**:
1. **1988-1991**: EFA invented, fundamental limitations documented (rotation ambiguity, FIFO, rank inflation)
2. **2018**: CHROMIXS automated well-separated cases, acknowledged overlap problem
3. **2021**: EFAMIX quantified exactly where EFA fails

**Chemometrics tradition (MCR-ALS lineage)**:
1. **1995-2004**: MCR-ALS developed for multivariate curve resolution, acknowledged same rotation ambiguity
2. **2016**: First application to SEC-SAXS (Meisburger et al.)
3. **2018**: Parker et al. add smoothness regularization for AEX-SAXS

**Convergence**:
4. **2021**: REGALS synthesizes both traditions - MCR-ALS framework + flexible regularization, works beyond chromatography
5. **2026**: Molass provides complementary explicit parametric modeling approach

**Key insight**: The "30-year gap" reflects parallel development in separate scientific communities. EFA (chromatography) and MCR-ALS (chemometrics) independently identified the same rotation ambiguity problem. REGALS (2021) brings these traditions together with modern regularization theory to resolve ambiguity more robustly than soft constraints (MCR) or FIFO assumptions (EFA) alone.

---

## Timeline: Problem Recognition → Solution Evolution

### 1988: EFA Invention and Problem Discovery

**Paper**: Maeder & Zilian (1988), "Evolving factor analysis, a new multivariate technique in chromatography"

**Innovation**: Mathematical framework for component detection using SVD + forward/backward analysis

**Limitations Documented** (pp. 210-212):

1. **"Tailing seems to be the most serious difficulty"** (p. 211)
   - Quote: "The backward analysis is impeded by severe tailing of the elution profiles"
   - Quote: "Tailing seems to be a nasty problem, not only in preparative chromatography... but also the attempts of deconvolution of overlapping peaks are severely hampered"
   - Impact: Cannot correctly determine concentration windows

2. **Baseline Problems** (p. 211)
   - Quote: "Sloping baselines as well as flat baselines above or below zero simulate additional factors and therefore confuse the evolving factors analysis"
   - Impact: False factor detection, rank estimation unreliable

3. **Noise Sensitivity** (p. 211)
   - Quote: "The detectability of minor components in a peak cluster... obviously are strongly correlated with the noise level"
   - Impact: Instrument-dependent performance, no general rules

4. **No Quantification Without Calibration** (p. 212)
   - Quote: "EFA produces only the shapes and not the absolute heights of the spectra and profiles"
   - Context: Arbitrary rotation matrix means relative profiles only
   - Impact: Requires external calibration for quantitative work

5. **Scope Uncertain** (p. 212)
   - Quote: "Important questions remain to be investigated... Computer simulations have to be carried out and compared with extensive series of real experiments"
   - Impact: Inventors acknowledge limits not fully characterized

**Key insight**: **Inventors were remarkably honest** about limitations from the start.

---

### 1991: EFA Tutorial and Rank Inflation

**Paper**: Keller & Massart (1991), "Evolving factor analysis"

**Contribution**: Comprehensive tutorial, practical guidance

**Additional Limitations Documented** (pp. 222-223):

6. **Rank Inflation - The Fundamental Problem**
   - Quote: "**the rank of the data matrix will be higher than the number of underlying chemical species**"
   - Quote: "Gerritsen et al. have shown that **in real world applications the number of PCs needed to describe a given system is higher than the number of underlying analytes**"
   - Causes: instrumental nonlinearities, baseline drift, heteroscedasticity, calibration nonlinearity
   - Impact: **Cannot reliably determine true number of components**

7. **Sequential Elution Assumption (FIFO)**
   - Quote: "Assuming that, in a good chromatogram, where the column is not overloaded and where the concentrations of the compounds are similar, **the substance that elutes first also leaves the detector first**" (p. 216)
   - Conditions: Good chromatogram, no overload, similar concentrations
   - Impact: Fails for tailing, overload, very different concentrations

**Key insight**: **Rank inflation is acknowledged as fundamental** - real data always has more singular values than true components.

---

### 1995-2004: Parallel Development - MCR-ALS in Chemometrics

**What was happening**: While EFA remained dominant in chromatography, chemometrics developed general framework

**Paper**: Jaumot et al. (2004), "Application of multivariate resolution methods to the study of biochemical and biophysical processes"

**Key Framework - Multivariate Curve Resolution (MCR-ALS)**:
```
D = C · S^T + E
```
- D: Data matrix (spectra × time points)
- C: Concentration profiles  
- S^T: Pure spectra (transposed)
- E: Residuals

**The Same Rotation Ambiguity** (from Jaumot 2004):
> "The solution of Eq. (1) for C and S^T is ambiguous if no additional information is available. In other words, there is a rotational and/or scale (intensity) freedom in the solutions"

**Mathematical statement**:
```
D = C_old · S_old^T = (C_old · T) · (T^-1 · S_old^T) = C_new · S_new^T
```

**For ANY non-singular matrix T, infinite solutions exist** - the SAME problem Maeder identified in 1987!

**MCR-ALS Solution Approaches**:
1. **Hard-modeling**: Explicit physicochemical models (equilibrium constants, kinetics)
2. **Soft-modeling**: Constraints without explicit model (non-negativity, unimodality, closure)
3. **Combined approaches**: SVD + global analysis

**Critical Quote** (Jaumot 2004):
> "Soft restraints are rarely sufficient to provide a robust and unique solution on their own"

**Applications**: Protein folding, nucleic acid denaturation, ligand binding - but **NOT SAXS** (not mentioned in 2004 review)

**Key insight**: Chemometrics community had sophisticated tools for rotation ambiguity, but SAXS community didn't adopt them until 2016.

---

### 2016-2018: Bridging Communities

**The convergence begins**: Meisburger group applies MCR-ALS to SAXS

**Meisburger et al. (2016)**: "Domain movements upon activation of phenylalanine hydroxylase characterized by crystallography and chromatography-coupled small-angle X-ray scattering"
- First application of MCR-ALS + EFA to SEC-SAXS
- Cited by REGALS as foundation

**Parker et al. (2018)**: "An endogenous dAMP ligand in Bacillus subtilis class Ib RNR..."
- AEX-SAXS deconvolution problem
- Salt gradient creates changing background
- **Innovation**: Add **smoothness regularization** to MCR-ALS
- Quote (SI): "alternating least-squares algorithm, modified to include smoothness regularization applied to the elution peaks"
- Precursor to REGALS

**Why this mattered**: Showed regularization works better than soft constraints alone for SAXS

**Key insight**: The "30-year gap" was actually two parallel tracks converging.

---

### 2018: CHROMIXS - Pragmatic Automation

**Paper**: Panjkovich & Svergun (2018), "CHROMIXS: Automatic and interactive analysis of chromatography-coupled small-angle X-ray scattering data"

**Innovation**: Automated workflow for SEC-SAXS processing

**What it does**:
- Automatic peak detection
- Buffer region identification
- Subtraction for well-resolved peaks
- Integration with ATSAS suite

**Acknowledged Limitations**:
- Quote (from SAXS_methods_analysis.md): "Works for 'well resolved fractions (i.e. baseline separated sample elution peaks)'"
- Quote: "For overlapping peaks: defers to REGALS, BioXTAS RAW, or UltraScan-SOMO"

**Solution Strategy**: **Pragmatic workaround**
- Automate easy cases (well-separated peaks)
- Defer hard cases (overlapping peaks) to other tools
- Acknowledge problem without solving it

**Relation to EFA**: No direct EFA citation in extracted text (3-page paper)

**Key insight**: **First explicit acknowledgment in SAXS literature** that overlapping peaks require different methods.

---

### 2021: EFAMIX - Quantification of Failure Modes

**Paper**: Konarev et al. (2021), "EFAMIX, a tool to decompose inline chromatography SAXS data from partially overlapping components"

**Innovation**: **Pure EFA implementation** for SAXS + systematic testing

**What it does**:
- Forward/backward EFA (Maeder 1987, Keller 1991)
- Rotation matrix method for component extraction
- SVD-based component detection
- Part of ATSAS 3.1+ package

**Citations**:
- **Directly cites Maeder (1987) and Keller (1991)** - acknowledges EFA foundation
- Cites CHROMIXS (2018), REGALS (2021), BioXTAS RAW - aware of alternatives

**Key Contribution**: **Quantified exactly where EFA fails**

From SAXS_methods_analysis.md:
- **Two components**: SNR ≥ 10² photons, symmetric peaks (τ ≤ 2), concentration ratio ≤ 1:10
- **Three components**: SNR ≥ 10³ photons required
- **Four components**: SNR ≥ 10⁴ photons (very high quality only)
- **Peak separation**: ≥ 2× width required
- **Asymmetry limit**: Fails for τ > 2

**Acknowledged Limitations**:
- Quote: "EFA does show limitations when applied to systems with significantly asymmetric concentration profiles"
- Quote: "potentially ambiguous" for overlapping peaks
- Figure 3 shows failures at τ > 2 (likely our FIFO mathematical impossibility!)

**Solution Strategy**: **Document the problem, don't solve it**
- Test pure EFA systematically
- Quantify failure conditions precisely
- Make explicit what was implicit
- Provide thresholds for users to judge applicability

**Key insight**: **EFAMIX makes EFA limitations quantifiable and testable** - no longer vague statements but concrete thresholds.

---

### 2021: REGALS - Synthesis of Two Traditions

**Paper**: Meisburger, Xu & Ando (2021), "REGALS: a general method to deconvolve X-ray scattering data from evolving mixtures"

**Innovation**: **Synthesis of EFA and MCR-ALS traditions** + modern regularization theory

**Explicit acknowledgment** (from paper):
> "We chose to adapt the alternating least-squares (ALS) algorithm, which is often used in classic MCR"

**REGALS = MCR-ALS + Flexible Regularization**, not just "EFA + regularization"

**What it does**:
- **Rank determination**: SVD with normalized singular values (s'_j > 1 criterion, similar to EFA)
  - Uses random matrix theory to detect signal above noise
  - Determines number of components K
  
- **Iterative optimization**: Regularized Alternating Least Squares (REGALS)
  - Alternates between optimizing SAXS profiles (Y) and concentrations (C) within each iteration
  - Not separate "stages" but coupled optimization steps
  
- **Flexible regularization** (applied as needed for experiment type):
  - Smoothness penalties: $\lambda_C ||D^2C||^2$ (concentrations), $\lambda_P ||D^2P||^2$ (profiles)
  - Non-negativity constraints: $P \geq 0, C \geq 0$
  - Compact support (OPTIONAL): concentration ranges for chromatography OR d_max for real-space P(r)
  - Boundary conditions: zero values at specified edges

**Citations**:
- **Cites Maeder (1987)** - acknowledges EFA/SVD foundation
- Cites MCR-ALS methods (Jaumot, Tauler)
- Cites Bayesian regularization (MacKay)

**Acknowledged Problem**:
- Quote (from extracted_papers.txt): "to recover the scattering from each component, the basis vectors from SVD must be recombined using prior knowledge about what constitutes a physically valid solution"
- Describes "basis vectors can be mixed (or 'rotated')" using "any non-singular K×K matrix Ω"
- Acknowledges this is **rotation/mixing ambiguity, not just rotations**

**Solution Strategy**: **Add constraints to resolve ambiguity**

From [REGALS_analysis_summary.md](../explorations/REGALS_analysis_summary.md), the constraint hierarchy:
- **Level 1** (data-fit only): Infinite solutions
- **Level 2** (+ smoothness): Orthogonal ambiguity only  
- **Level 3** (+ non-negativity): Almost unique (discrete permutation may persist)
- **Level 4** (+ full REGALS): Unique for generic data

**What REGALS Solves**:
- ✓ Rotation/mixing ambiguity (via non-negativity + regularization constraints)
- ✓ Better handling of overlapping peaks (via smoothness regularization)
- ✓ Works beyond chromatography (equilibrium titrations, time-resolved experiments)
- ✓ Flexible constraint framework adaptable to different experiment types

**What REGALS Limitations Remain**:
- ⚠ When using concentration compact support for chromatography: user must specify approximate elution ranges (requires prior knowledge)
- ⚠ Rank inflation (SVD-based K determination still susceptible to noise/overlap)
- ⚠ Still requires user choices: K, constraint types, regularization parameters
- ⚠ Does NOT require sequential elution (FIFO) - can handle equilibrium mixtures using d_max constraints instead

**Key insight**: **REGALS is MORE GENERAL than EFA** - not limited to chromatography, uses flexible regularization instead of requiring sequential elution. Addresses rotation ambiguity through constraint hierarchy.

---

## Comparative Analysis: What Each Method Addressed

### Problem Matrix

| Limitation | EFA (1988) | CHROMIXS (2018) | EFAMIX (2021) | REGALS (2021) | Status |
|------------|------------|-----------------|---------------|---------------|---------|
| **Rotation ambiguity** | Identified | Not mentioned | Acknowledged | **Solved** (constraints) | ✓ Resolved |
| **Tailing/FIFO violation** | "Most serious" | Acknowledged | Quantified (τ ≤ 2) | Not required (d_max alternative) | ✓ Avoided |
| **Rank inflation** | Documented | Not mentioned | Quantified | Not addressed (SVD-based) | ✗ Unsolved |
| **Overlapping peaks** | "Severely hampered" | Defers to others | Quantified limits | Improved (smoothness) | ⚠ Partial |
| **Baseline problems** | Identified | Assumes subtraction | Preprocessing | Modeled explicitly | ✓ Improved |
| **Noise sensitivity** | Instrument-dependent | Not discussed | Quantified (SNR) | Regularization helps | ⚠ Partial |
| **Resolution limit** | Mentioned | Not discussed | Tested (2× width) | Smoothness helps | ⚠ Partial |
| **No quantification** | Scale + rotation | Not mentioned | Rotation only | **Solved** (normalization) | ✓ Resolved |

### Key Patterns

1. **Rotation ambiguity**: Identified 1988 → Solved 2021 (REGALS constraints)
2. **FIFO/tailing**: Identified 1988 → Quantified 2021 (EFAMIX) → Avoided 2021 (REGALS d_max alternative)
3. **Rank inflation**: Identified 1991 → Quantified 2021 (EFAMIX) → Still unsolved (all SVD-based methods)
4. **Overlapping peaks**: Identified 1988 → Acknowledged as blocker 2018 → Quantified 2021 → Improved but challenging

---

## The Unsolved Problems (2026)

### 1. FIFO Mathematical Impossibility

**Discovery**: Our [limitation_3_tailing_effects.ipynb](efa_original/limitation_3_tailing_effects.ipynb) (January 2026)

**Finding**: FIFO assumption fails even for ideal Gaussian peaks with sufficient overlap
- Component 3 appears at frame 60 but backward EFA says "disappears" at frame 51
- **Negative window width** = mathematical impossibility
- Not just a tailing problem - fundamental to overlapping components

**Status in modern methods**:
- CHROMIXS: Avoids problem by requiring "baseline separated" peaks
- EFAMIX: Uses FIFO explicitly, documents failure at τ > 2 (likely this phenomenon)
- REGALS: Compact support is OPTIONAL (can use d_max for equilibrium systems instead of sequential elution)

**Gap in literature**: **None of the modern papers explicitly state the mathematical impossibility** - they work around it without documenting the root cause.

**Our contribution**: Makes explicit what has been implicit in tool development.

---

### 2. Rank Inflation

**Status**: Acknowledged since 1991, quantified in 2021, never solved

**Quote (Keller 1991)**: "rank of data matrix will be higher than number of underlying chemical species"

**EFAMIX quantification**: Need SNR 10⁴ for 4 components (unrealistic for most experiments)

**Impact**: **Cannot automatically determine true number of components**
- Expert judgment required
- Manual validation essential
- "Automatic" claims misleading

**Why unsolved**: Fundamental problem - real data has noise, baseline drift, artifacts

---

### 3. Resolution Limits

**Status**: Acknowledged since 1988, quantified (2× peak width), partially improved

**EFAMIX threshold**: Peak separation ≥ 2× width required

**REGALS improvement**: Smoothness regularization may help closer peaks

**But**: Still cannot resolve completely overlapping peaks with similar properties

---

## Historical Narrative: Three Eras

### Era 1: Problem Discovery (1988-1991)

**Characterized by**: Honest documentation of limitations
- Inventors explicitly state what doesn't work
- "Tailing seems to be the most serious difficulty"
- "Rank higher than true components" in real data
- Scope and limits acknowledged as incompletely understood

**Outcome**: EFA widely adopted despite known limitations

---

### Era 2: Pragmatic Workarounds (2018)

**Characterized by**: Acknowledge problems, avoid rather than solve
- CHROMIXS: "Can't handle overlapping peaks" → defer to others
- Automate easy cases, leave hard cases to experts
- First explicit statement in SAXS literature that overlap requires different methods

**Outcome**: Automation for simple cases, manual intervention for complex cases

---

### Era 3: Quantification and Partial Solutions (2021)

**Characterized by**: Systematic testing and regularization approaches

**EFAMIX contribution**:
- Makes EFA limitations **quantifiable** (SNR thresholds, τ limits, separation requirements)
- Tests pure EFA systematically
- Provides users with concrete applicability criteria

**REGALS contribution**:
- **Solves rotation ambiguity** via constraint hierarchy
- **More general than EFA**: works for equilibrium systems, not limited to chromatography
- Improves overlap handling via smoothness regularization
- Flexible constraint framework (compact support, d_max, smoothness, boundary conditions)
- When using concentration compact support for chromatography: user specifies elution ranges (requires prior knowledge)

**Outcome**: Rotation ambiguity solved; rank determination still SVD-based; compact support optional not required

---

## Why These Problems Matter for Your Work

### What REGALS Does and What Molass Does Differently

**REGALS approach**:
- Uses SVD for rank determination (normalized singular values s'_j > 1)
- Iterative regularized ALS with flexible constraints
- For chromatography: can use concentration compact support (user specifies ranges)
- For equilibrium: can use d_max constraints on P(r) instead
- Does NOT fundamentally require sequential elution (FIFO)

**REGALS limitations**:
1. **Rank determination**: SVD-based, susceptible to noise/overlap artifacts
2. **User input required**: must choose K, constraint types, regularization parameters, elution ranges (if using compact support)
3. **Still model-free**: resolves ambiguity through regularization, not explicit physical models

**Molass approach - Explicit parametric models** (Gaussian/EGH/SDM/EDM):
- ✓ **No FIFO assumption**: Each component has independent elution profile
- ✓ **No rank ambiguity**: Number of components specified explicitly
- ✓ **Direct physical interpretation**: Parameters = peak position, width, skewness
- ✓ **Handles arbitrary overlap**: Model can fit completely overlapping peaks
- ✓ **Transparent assumptions**: Functional form chosen explicitly, testable

**Tradeoff**:
- Requires choosing functional form explicitly
- More parameters to fit
- But assumptions are **transparent and testable**

---

## The Literature Gap We Identified

### What Modern Papers Don't Say

**CHROMIXS (2018)**: 
- Says: "Can't handle overlapping peaks"
- Doesn't say: **Why** (no connection to EFA limitations)

**EFAMIX (2021)**:
- Says: "EFA shows limitations with asymmetric profiles"
- Shows: Failures at τ > 2 (Figure 3)
- Doesn't say: Mathematical root cause (FIFO impossibility)

**REGALS (2021)**:
- Says: "Basis vectors can be mixed (or 'rotated')"
- Builds: Constraint hierarchy to resolve rotation ambiguity
- Doesn't say: How to choose K robustly, what regularization parameters mean physically

### Our Contribution

**Making explicit what has been implicit**:
1. FIFO assumption creates **mathematical impossibility** (negative window widths) for overlapping peaks
2. This affects **EFA and EFAMIX fundamentally** - they require sequential elution
3. **REGALS escapes this** by offering d_max constraints for equilibrium systems
4. **SVD-based rank determination** still susceptible to noise/overlap (affects EFA, EFAMIX, REGALS)
5. Explicit parametric models (Molass) **avoid FIFO entirely** by modeling each peak independently

---

## The Selection Problem: A Fundamental Challenge Revealed (January 2026)

### Discovery from Discrete Ambiguity Analysis

Today's work on discrete permutation ambiguity ([discrete_ambiguity_demonstration.ipynb](../explorations/discrete_ambiguity_demonstration.ipynb)) reveals a profound challenge:

**The Problem**:
1. Discrete permutation candidates exist (2-6 typically for 2-3 components)
2. These are **topologically disconnected** (GL(2) components: det>0 vs det<0)
3. Cannot reach each other without crossing singularity (det=0)
4. Local optimization finds ONE candidate (whichever basin it starts in)
5. **All candidates may have nearly identical objective values**

**The Critical Question**:
> **Which permutation corresponds to physical reality?**

### Two Possibilities

**Possibility 1: Lucky by Design**
- Model-free regularization (smoothness, non-negativity, compact support) might **naturally prefer** the physically correct permutation
- If true: method succeeds without being aware of alternatives
- **Requires**: Implicit physical knowledge encoded in constraint choices
- **Problem**: No guarantee, no validation mechanism

**Possibility 2: Selection Required**
- Multiple permutations satisfy ALL constraints equally well
- Optimization finds whichever candidate is in the starting basin
- **Requires**: Additional physical information to select correct one
- **Implies**: Need for **global optimization with physical constraints**

### Why This Matters

**For REGALS and similar methods**:
- **If lucky**: Regularization choices implicitly select correct permutation → success without explicit awareness
- **If unlucky**: Find incorrect permutation with excellent fit → silent failure
- **No distinction**: Both cases look identical from optimization perspective (good χ², smooth profiles, non-negative)

**For explicit parametric models (Molass)**:
- Physical constraints built into model form (peak shapes, elution order expectations)
- Can incorporate prior knowledge explicitly
- Transparent about which permutation is assumed

### The Need for Global Optimization

After today's demonstration, it becomes clear:

**Local optimization is insufficient when discrete candidates exist**, unless:
1. Regularization/constraints implicitly eliminate wrong permutations (lucky), OR
2. Global search with physical validation explicitly selects correct permutation

**Required capabilities**:
- Awareness that multiple permutations exist
- Physical criteria to distinguish them
- Validation against experimental expectations
- Transparent reporting when ambiguity detected

**Currently missing in model-free approaches**:
- No explicit check for alternative permutations
- No reporting when discrete ambiguity exists
- Implicit assumption that local optimum = physical truth
- User must manually validate component assignments

### Implications for Method Development

This reveals a **fundamental limitation of pure local optimization**:

**Quote from today's work**:
> "Singularity barriers create energy barriers that keep optimization algorithms within one permutation basin."

**Consequence**:
- Method finds ONE solution (local minimum in one basin)
- Alternative permutations in other basins remain unexplored
- Physical correctness depends on either:
  - **Luck**: Starting in the right basin
  - **Wisdom**: Constraint choices that eliminate wrong basins
  - **Post-hoc validation**: Expert recognizes incorrect assignment

**What's needed going forward**:
1. **Global optimization** that explores multiple basins
2. **Physical validation** criteria to select among candidates
3. **Ambiguity detection** that warns when discrete alternatives exist
4. **Transparent reporting** of which permutation was selected and why

This is not a criticism of existing methods—it's a **structural challenge** that was implicit in the mathematics but only becomes clear after rigorous analysis of the discrete ambiguity problem.

---

## Conclusions for JOSS Paper

### Historical Arc

**1988 → 2026: Two Traditions Converge**

**Track 1 - Chromatography (EFA tradition)**:
1. **1988**: EFA invented with documented limitations (FIFO, rotation ambiguity, rank inflation)
2. **2018**: CHROMIXS - pragmatic automation (avoid hard cases, well-separated peaks only)
3. **2021**: EFAMIX - quantifies pure EFA limitations systematically

**Track 2 - Chemometrics (MCR-ALS tradition)**:
1. **1995-2004**: MCR-ALS framework developed, same rotation ambiguity acknowledged
2. **2016**: First MCR-ALS + EFA application to SEC-SAXS (Meisburger et al.)
3. **2018**: Parker et al. add smoothness regularization to MCR-ALS for AEX-SAXS

**Convergence**:
4. **2021**: REGALS synthesizes both traditions with flexible regularization framework
   - MCR-ALS alternating optimization + EFA rank determination
   - Tikhonov-Miller regularization (smoothness)
   - Works beyond chromatography (titration, time-resolved)
   - Resolves rotation ambiguity more robustly than soft constraints or FIFO alone

**Remaining challenges**: Rank determination (SVD-based), user parameter choices

5. **2026**: Molass - complementary explicit parametric approach

### Research Impact

**Your work's place in history**:
- Addresses **unsolved problems** from 1988 (overlap handling, transparent assumptions)
- Provides **alternative approach**: explicit parametric models with clear physical interpretation
- **Different philosophy**: Model-based (Molass) vs. model-free regularization (REGALS)
- **Complementary to REGALS**: Where REGALS uses flexible regularization, Molass uses explicit peak models
- **Reveals fundamental challenge**: Discrete permutation ambiguity requires global optimization or physical validation

### Key Message for Reviewers

> "SEC-SAXS deconvolution methods emerged from two parallel scientific traditions: EFA from chromatography (1987) and MCR-ALS from chemometrics (1995-2004). Both independently identified the rotation ambiguity problem. REGALS (2021) synthesized these traditions, applying MCR-ALS with flexible regularization (smoothness, compact support, d_max) to resolve ambiguity more robustly than EFA's FIFO assumptions or MCR's soft constraints alone. REGALS works across experiment types (chromatography, titration, time-resolved) but relies on local optimization that may encounter discrete permutation ambiguity.
>
> Recent mathematical analysis (January 2026) reveals that discrete permutation candidates exist due to topological disconnection in the transformation group GL(2). Local optimization finds ONE candidate without exploring alternatives. This creates a fundamental challenge: selecting the physically correct permutation requires either (1) implicit guidance from regularization choices that naturally prefer the correct solution, or (2) explicit global optimization with physical validation criteria. 
>
> Molass represents a complementary approach: explicit parametric peak models (Gaussian/EGH/SDM/EDM) that provide transparent physical interpretation, independent peak modeling, and direct parameter estimation. The explicit model form allows incorporating physical expectations (peak shapes, elution order) that can guide permutation selection when ambiguity exists."

---

## References for Historical Narrative

### Primary Sources
- Maeder & Zilian (1988) - Original EFA paper
- Keller & Massart (1991) - EFA tutorial
- Jaumot et al. (2004) - MCR-ALS comprehensive review
- Meisburger et al. (2016) - First MCR-ALS + EFA for SEC-SAXS
- Panjkovich & Svergun (2018) - CHROMIXS
- Parker et al. (2018) - Regularized ALS for AEX-SAXS
- Konarev et al. (2021) - EFAMIX  
- Meisburger et al. (2021) - REGALS

### Our Analysis
- [citation_dependency_graph.md](citation_dependency_graph.md) - Who cites whom
- [efa_original/EFA_limitations_from_inventors.md](efa_original/EFA_limitations_from_inventors.md) - Direct quotes from inventors
- [SAXS_methods_analysis.md](SAXS_methods_analysis.md) - Modern methods comparison
- [MCR-ALS_context_analysis.md](MCR-ALS_context_analysis.md) - Chemometrics parallel development and convergence
- [regals/method_verification.md](regals/method_verification.md) - Verified REGALS architecture and constraints
- [efa_original/limitation_3_tailing_effects.ipynb](efa_original/limitation_3_tailing_effects.ipynb) - FIFO mathematical impossibility proof
- [../explorations/REGALS_analysis_summary.md](../explorations/REGALS_analysis_summary.md) - Constraint hierarchy analysis

---

**End of Historical Development Document**
