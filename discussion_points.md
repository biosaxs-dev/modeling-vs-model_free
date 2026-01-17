# Modeling vs Model-Free Approaches in SEC-SAXS Analysis
## Discussion Points for Paper

---

## Central Thesis

**"Model-free" is a misnomer** - REGALS's approach involves multiple layers of implicit modeling:
1. **EFA (Evolving Factor Analysis)**: Assumes sequential "first-in-first-out" elution
2. **Regularization**: Constrains peak shapes to be smooth and compact (implicitly assumes Gaussian-like functional forms)

**Goal**: Clarify the mathematical relationship between "explicit modeling" (Molass) and "regularized/model-free" (REGALS) approaches, showing they are **different expressions of the same underlying modeling philosophy**.

---

## Context

Comparing four approaches to chromatographic deconvolution:
- **Molass** (explicit modeling): Parametric elution curves (EGH, SDM, EDM)
- **REGALS** (implicit modeling via EFA + regularization): Sequential elution assumption + smoothness constraints
- **EFAMIX** (implicit modeling via EFA only): Sequential elution assumption + rotation
- **hplc-py** (explicit modeling): Skew-normal distributions

All solve: M = P·C (decompose overlapping signals into components)

**Key distinction**: EFAMIX uses only Stage 1 (EFA), while REGALS adds Stage 2 (regularization)

**Note on CHROMIXS** (Panjkovich & Svergun 2018): Part of ATSAS suite (includes EFAMIX). Automates SEC-SAXS processing for **"well resolved fractions (i.e. baseline separated sample elution peaks)"** but for overlapping peaks, "may help in diagnosing and preparing the data for further processing by other programs" like REGALS, BioXTAS RAW, or UltraScan-SOMO. **This admission is significant**: even "automatic" tools acknowledge they need help with overlapping peaks—precisely where EFA claims advantage.

---

## Key Arguments

### 1. Well-Conditioned Data
For well-separated peaks with high signal-to-noise ratio:
- Both explicit and implicit modeling approaches yield similar results
- Choice of method matters less
- **This is not the interesting case**

### 2. Ill-Conditioned and Noisy Data
For overlapping peaks and/or low SNR:
- Decomposition becomes **underdetermined** - infinite possible solutions
- This is where **method choice becomes critical**
- Both approaches constrain the solution space, but differently

### 3. REGALS: Two Layers of Implicit Modeling

**REGALS is not a single approach but a two-stage process:**

#### **Stage 1: EFA (Evolving Factor Analysis)**
- **Purpose**: Determine number of components and their concentration windows
- **Method**: 
  - Forward SVD: progressively add frames from start → detect when components appear
  - Backward SVD: progressively add frames from end → detect when components disappear
  - Match appearance/disappearance to define concentration windows
- **Key Assumption**: **Sequential elution** - "first-in-first-out" pattern
  - Component appearing first will disappear first
  - Derived from chromatography principles
  - **This is a physical model** - not data-driven mathematics!
- **Output**: Concentration windows for each component

#### **Stage 2: Regularized Deconvolution**
Within the EFA-determined windows, apply regularization:
- **Smoothness**: $\lambda_C \|D^2 C\|^2$ on concentration curves
- **Smoothness**: $\lambda_P \|D^2 P\|^2$ on SAXS profiles  
- **Compact support**: $C(t) = 0$ outside determined windows
- **Real-space constraint**: $P(q) \leftrightarrow P(r)$ with $d_{max}$
- **Non-negativity**: $C \geq 0$, $P(r) \geq 0$

**Both stages involve modeling assumptions!**

### 4. Explicit Modeling Approach (Molass, hplc-py)

Single-stage direct parametric fitting:

- **Form**: Direct parametric functions
  - EGH, SDM, EDM from chromatography theory
  - Skew-normal distributions
- **Expression**: $C(t) = \sum_i A_i \cdot f_i(t; \theta_i)$ where $f_i$ is a known functional form
- **Parameters**: Physically interpretable (retention time, peak width, skewness, etc.)
- **Assumption made explicit**: "Peaks have this specific shape"

### 5. The Central Question

**What functional form does REGALS's regularization implicitly assume?**

Hypothesis: The combination of EFA + smoothness regularization may be mathematically equivalent to assuming:
- **EFA component**: Sequential Gaussian-like peaks (smooth appearance/disappearance)
- **Regularization component**: Gaussian-like peak shapes within windows
- **Combined**: Possibly equivalent to fitting constrained Gaussian mixture

If true, this means:
- REGALS is **not truly model-free** - it assumes models at both stages
- The difference from Molass is **explicitness**, not **existence** of modeling
- Both approaches are on a **spectrum of model specification**:
  - **Explicit** (Molass): Fix functional form (EGH/SDM/EDM) upfront
  - **Implicit** (REGALS): Constrain via EFA (sequential) + regularization (smoothness) → effectively Gaussian-like

**Key Insight**: REGALS embeds its models in:
1. The EFA algorithm (sequential elution assumption)
2. The regularization terms (smoothness → implicit functional form)

---

## Comparison of Constraints

### Main Comparison: Molass vs REGALS

**Focus**: Both methods tackle overlapping peaks (the hard problem). Direct contrast between explicit parametric modeling vs implicit regularization.

**Supplementary**: EFAMIX (pure EFA) and CHROMIXS (automated pipeline) provide supporting evidence for limitations of "automatic" approaches.

| Aspect | Molass (Explicit) | EFAMIX (EFA Only) [*Supplement*] | REGALS (EFA + Regularization) |
|--------|------------------|-------------------|-------------------------------|
| **Peak shape** | Parametric (EGH/SDM/EDM) | SVD rotation only | Smoothness regularization → Gaussian-like |
| **Elution order** | Not constrained | EFA enforces first-in-first-out | EFA enforces first-in-first-out |
| **Number of parameters** | Few (amplitude, position, width, skew) | Many (discretized C(t), P(q)) | Many + regularization weights |
| **Flexibility** | Rigid functional form | High (minimal constraints) | Moderate (smooth functions) |
| **Physical basis** | Chromatography theory (explicit) | Sequential elution only | Sequential elution + smoothness |
| **Interpretability** | Direct parameter meaning | Indirect (must interpret profiles) | Indirect (must interpret profiles) |
| **Component detection** | Manual specification (transparent) | "Automatic" via EFA (manual tuning) | "Automatic" via EFA (manual tuning) |
| **Reproducibility** | Same input → same output | Depends on user threshold choices | Depends on thresholds + λ choices |
| **Noise sensitivity** | Moderate (fitting algorithm) | **High**: 2-comp needs SNR≥10²; 3-comp needs ≥10³; 4-comp needs ≥10⁴ (Konarev 2021) | High (SVD) + moderate (regularization) |
| **Rank estimation** | Manual (user specifies N) | Automatic but unreliable (rank inflation from nonlinearities) | Automatic but unreliable (same as EFAMIX) |
| **Quantification** | Requires calibration standards | Relative shapes only - needs external calibration | Relative shapes only - needs external calibration |
| **Tailing tolerance** | Good (parametric forms handle skew) | **Poor**: Fails at τ>2 (Konarev 2021) | Poor (EFA stage affected) |
| **Peak overlap tolerance** | Flexible | **Limited**: Must be ≥2× width, ratio ≤1:10 (Konarev 2021) | Stage 1 limited, Stage 2 improves |
| **Baseline requirements** | Moderate (fitted as parameter) | Strict (sloping baseline → false factors) | Strict (inherited from EFA) |
| **Regularization** | None | None | Smoothness, compact support, non-negativity |

---

## Research Questions for Paper

### 1. Mathematical Equivalence
**Core Question**: What parametric model does EFA + regularization implicitly assume?

- Derive the **implicit functional form** from:
  - EFA's sequential elution assumption
  - Smoothness regularization penalty
- Show conditions under which REGALS ≈ Gaussian peak fitting
- Identify when explicit models (EGH/SDM/EDM) diverge from implicit (Gaussian-like) forms

### 2. Theoretical Relationship

**Bayesian interpretation**:
- EFA = prior on elution order (sequential appearance/disappearance)
- Smoothness regularization = prior on peak shapes
- Combined: What joint prior distribution?

**Functional analysis**:
- What function space does $\lambda \|D^2 C\|^2$ constrain?
- How does EFA's concentration window constraint interact?

### 3. EFA as Implicit Modeling

**Questions**:
- Is the "first-in-first-out" assumption valid for all SEC-SAXS?
- When does EFA fail? (IEX-SAXS, titrations → REGALS claims advantage here)
- Can we relax EFA assumptions and still get unique solutions?

### 3b. EFA's Practical Limitations (Critical!)

**Theoretical claim**: Automatic component detection via SVD rank estimation

**Practical reality** (based on experience + EFAMIX paper quantifications):
- **Noise blurs rank estimation**: With even small noise, all singular values are non-zero
- **No clear cutoff**: Where is the boundary between "significant" and "noise"?
- **Manual tuning required**:
  - Threshold for singular value significance
  - Autocorrelation cutoffs
  - Fine-tuning of concentration windows (as RAW tutorial explicitly shows)
- **Subjective decisions**: User judgment replaces algorithmic objectivity

**Quantified from Konarev 2021 (EFAMIX simulations)**:
- **Two components**: Require SNR ≥ 10² photons (high noise threshold)
- **Three components**: Require SNR ≥ 10³ photons (moderate noise only)
- **Four components**: Only work at SNR ≥ 10⁴ photons (exceptional data quality)
- **Peak asymmetry**: EFA assumes symmetric (Gaussian) profiles; fails when τ > 2 (EGH parameter)
- **Overlap distance**: Must be ≥ 2× individual peak width
- **Concentration ratio**: Cannot detect minor component if > 1:10 ratio

**Key insight**: EFA is not "automatic" - it requires human intervention, which means **implicit modeling decisions**. EFAMIX developers quantify exact thresholds where the method breaks.

**Comparison to Molass**:
- Molass: User explicitly specifies number of components upfront (transparent)
- REGALS: Claims automatic detection, but requires manual threshold tuning (opaque)
- **Both require human judgment, but Molass is honest about it**

**Questions to investigate**:
- How sensitive is EFA to noise level? (Now quantified: see above)
- How much do results vary with different threshold choices?
- Can we quantify the "subjectivity" in EFA component detection?
- How much do results vary with different threshold choices?
- Can we quantify the "subjectivity" in EFA component detection?

**CHROMIXS Evidence** (Panjkovich & Svergun 2018):
- Automated SEC-SAXS tool (part of ATSAS suite with EFAMIX)
- **Explicitly limited to baseline-separated peaks**: "well resolved fractions (i.e. baseline separated sample elution peaks)"
- **For overlapping peaks**: Defers to REGALS, BioXTAS RAW, or UltraScan-SOMO
- Uses "quality measure" scoring: accounts for negative intensities, Guinier fit residuals
  - **This is subjective**: What threshold defines "best quality"?
- **Key admission**: Even developers of "automatic" tools recognize limitations for overlapping cases

**EFAMIX Evidence** (Konarev et al. 2021):
- Pure EFA implementation (Stage 1 of REGALS: forward/backward SVD + rotation matrix)
- Part of ATSAS 3.1+, "requires minimal user intervention"
- **Quantified limitations** from simulations:
  - **Noise sensitivity**: Two components require SNR ≥ 10² photons; three components need ≥ 10³; four components only work at ≥ 10⁴
  - **Peak asymmetry**: Works for symmetric (Gaussian) peaks; fails when τ > 2 (EGH asymmetry parameter)
  - **Overlap distance**: Peak separation must be ≥ 2× individual peak width
  - **Concentration ratio**: Cannot detect minor component if ratio > 1:10
- **Quote**: "EFA does show limitations when applied to systems with significantly asymmetric concentration profiles"
- **Quote**: "potentially ambiguous" for overlapping peaks
- **Key insight**: EFAMIX developers provide exact quantitative thresholds where EFA breaks down

### 3c. EFA Limitations Acknowledged by Inventors (Maeder 1988, Keller 1991)

**The creators of EFA themselves identified fundamental limitations**:

#### **1. Rank Inflation Problem (Keller 1991)**
- **Quote**: "the rank of the data matrix will be higher than the number of underlying chemical species"
- **Causes**: Instrumental nonlinearities (DAD scan time, baseline drift, heteroscedasticity, calibration nonlinearity)
- **Result**: EFA can **overestimate** the number of components
- **Implication**: "Automatic" detection is unreliable - false positives are inherent to the method

#### **2. Tailing Problem (Maeder 1988)**
- **Quote**: "tailing seems to be the most serious difficulty"
- **Issue**: Asymmetric peaks break the FIFO assumption
- **Reality**: SEC-SAXS is notorious for tailing due to:
  - Column interactions
  - Sample heterogeneity
  - Flow rate variations
- **Consequence**: EFA's concentration windows become incorrect

#### **3. Baseline Sensitivity (Maeder 1988)**
- **Quote**: "Sloping baselines...simulate additional factors and therefore confuse the evolving factors analysis"
- **Requirement**: "It is essential to have a correct baseline"
- **Problem**: Another source of false component detection
- **Reality**: SEC-SAXS baselines are rarely perfectly flat

#### **4. Quantification Impossibility (Maeder 1988)**
- **Quote**: "quantification is not possible without further knowledge, such as the molar absorption coefficient at least at one wavelength"
- **Meaning**: EFA determines **shapes only, not absolute concentrations**
- **Implication**: REGALS is not truly "automatic" - it needs external calibration data
- **Comparison to Molass**: Both require known standards for absolute quantification

#### **5. FIFO Assumption Fragility (Keller 1991)**
- **Quote**: "the substance that elutes first also leaves the detector first"
- **Breaks down with**:
  - Tailing (as noted above)
  - Column overload
  - Multiple retention mechanisms
  - Non-equilibrium conditions
- **Problem**: Incorrect window assignment → wrong decomposition

**Key Insight**: The **inventors themselves** acknowledged that EFA is sensitive to noise, baselines, tailing, and instrumental artifacts. These are not hypothetical concerns - they are documented limitations by the method's creators.

**Citation**:
- Maeder, M. and Zilian, A. (1988). "Evolving factor analysis, a new multivariate technique in chromatography." *Chemometrics and Intelligent Laboratory Systems*, 3, 205-213.
- Keller, H.R. and Massart, D.L. (1991). "Evolving factor analysis." *Chemometrics and Intelligent Laboratory Systems*, 12, 209-224.
- Panjkovich, A. and Svergun, D.I. (2018). "CHROMIXS: automatic and interactive analysis of chromatography-coupled small-angle X-ray scattering data." *Bioinformatics*, 34(11), 1944-1946.
- Konarev, P.V., Graewert, M.A., Jeffries, C.M., et al. (2021). "EFAMIX, a tool to decompose inline chromatography SAXS data from partially overlapping components." *Protein Science*, 31, 269-282.

### 4. Empirical Validation

Compare explicit vs implicit modeling on:

**Simulated data** with known ground truth:
- True peaks = Gaussian, sequential elution → does REGALS match Molass-Gaussian?
- True peaks = EGH, sequential → does REGALS approximate?
- True peaks = overlapping, non-sequential → where does EFA break?

**Real SEC-SAXS data**:
- When do REGALS and Molass agree?
- When do they diverge, and why?
- Physical interpretation of differences

### 5. Practical Implications

If REGALS ≈ Gaussian + sequential constraint:
- **Advantages of explicit (Molass)**: 
  - Direct parameter interpretation
  - Can fit non-Gaussian shapes (EGH, SDM, EDM)
  - No sequential elution assumption needed
- **Advantages of implicit (REGALS)**: 
  - Flexibility within Gaussian family
  - Automatic component detection via EFA
  - Works for non-chromatographic data (time-resolved, titrations)

---

## Proposed Terminology

Replace "model-free" with more accurate terms:

| Current Term | Proposed Term | Reasoning |
|--------------|---------------|-----------|
| Model-free | **Implicit modeling** | EFA + regularization embed model assumptions |
| Model-based | **Explicit modeling** | Parametric form stated upfront |
| REGALS | **EFA + regularized parametric** | Two-stage implicit modeling |
| Molass | **Constrained parametric** | Domain-specific functional forms |

Both are **modeling approaches**, differing in **how constraints are specified**.

---

## Paper Structure Outline

### Title
"Implicit vs Explicit Modeling in SEC-SAXS Deconvolution: Unveiling the Hidden Assumptions in 'Model-Free' Regularization"

### Abstract
Show that REGALS's "model-free" approach actually involves two layers of implicit modeling: (1) EFA's sequential elution assumption and (2) regularization's implicit Gaussian-like peak shapes. Direct comparison with Molass (explicit parametric) reveals both methods require modeling assumptions - the key difference is transparency. EFAMIX and CHROMIXS provide supplementary evidence that "automatic" approaches have quantified limitations.

### Sections

1. **Introduction**
   - Underdetermined deconvolution in SEC-SAXS
   - The "model-free" claim requires scrutiny
   - Survey: Molass (explicit), EFAMIX (EFA only), REGALS (EFA + regularization), hplc-py (explicit)

2. **Theory**
   - Mathematical formulation: M = P·C
   - **EFA: Implicit chromatographic model**
     - Sequential elution assumption
     - Forward/backward SVD analysis
     - Concentration window determination
   - **Regularization: Implicit functional form**
     - Smoothness penalties
     - Bayesian interpretation
     - Derive implicit peak shapes
   - **Explicit modeling: Direct parametric approach**
     - EGH, SDM, EDM models
     - Parameter interpretation

3. **Mathematical Analysis**
   - Derive implicit functional form from smoothness regularization
   - Show relationship: EFA + regularization ↔ Gaussian mixture?
   - Identify conditions where implicit ≈ explicit

4. **Simulations**
   - Generate data with known peak shapes (Gaussian, EGH, SDM)
   - Apply REGALS (with EFA) vs Molass
   - Test hypothesis: REGALS ≈ Gaussian when data is Gaussian
   - Test failure modes: non-sequential elution

5. **Real Data Analysis**
   - Benchmark SEC-SAXS datasets
   - Compare REGALS vs Molass results
   - When do they agree/disagree?
   - Physical interpretation

6. **Discussion**
   - "Model-free" is a misnomer at three levels:
     1. EFA assumes sequential elution (physical model)
     2. EFA requires manual tuning (subjective modeling decisions)
     3. Regularization assumes smoothness (implicit functional form)
   - Theory vs practice: automatic detection claims vs reality
   - Transparency: explicit parameters (Molass) vs hidden assumptions (REGALS)
   - Trade-offs: flexibility vs interpretability vs reproducibility
   - Guidance for method selection

7. **Conclusions**
   - Unified view: all methods involve modeling
   - REGALS = implicit modeling via EFA + regularization
   - Choose based on data characteristics and analysis goals

---

## Next Steps

### Immediate
1. [x] **Literature review**: 
   - **✓ EFA original papers** (Maeder 1988, Keller 1991) - read and documented
   - **✓ CHROMIXS** (Panjkovich 2018) - automated tool limitations for overlapping peaks
   - Bayesian interpretation of regularization
   - Equivalence between regularization and parametric priors
   - Sequential elution in chromatography
   - Additional EFA applications and limitations papers

2. [ ] **Mathematical derivation**:
   - Formalize EFA's sequential assumption
   - What functional form minimizes $\|M - PC\|^2 + \lambda \|D^2 C\|^2$?
   - Combined effect: EFA windows + smoothness → implicit model?

### Medium-term
3. [ ] **Simulation framework**:
   - Implement or obtain REGALS code (including EFA stage)
   - Generate synthetic SEC-SAXS data
   - Compare against Molass with various models

4. [ ] **Real data comparison**:
   - Select benchmark datasets
   - Apply both methods systematically
   - Quantify agreement/divergence

### Long-term
5. [ ] **Write paper** following proposed structure
6. [ ] **Hybrid method?** Combine EFA (for detection) + explicit models (for fitting)?

---

## Open Questions

4. **How noise-sensitive is SVD rank estimation?**
5. **What is the "gray zone" where component number is ambiguous?**
6. **How reproducible are EFA results across different users/threshold choices?**
### About EFA
1. **Is EFA's sequential assumption always valid for SEC-SAXS?**
2. **What happens when elution order is not first-in-first-out?**
3. **Can EFA be reformulated as a parametric model?**
4. **Quantify rank inflation: At what noise level does EFA detect spurious components?** (Keller 1991)
5. **Measure tailing impact: How does peak asymmetry affect window determination?** (Maeder 1988)
6. **Baseline sensitivity: What baseline drift is tolerable before false factors appear?** (Maeder 1988)
7. **Compare EFA vs explicit detection: Which is more reliable in practice?**

### About Regularization
4. **Is smoothness regularization exactly equivalent to Gaussian peaks, or approximately?**
5. **Can we derive the implicit model analytically, or only numerically?**
6. **How do multiple regularization terms interact?**

### About the Combination
7. **Does EFA + smoothness = Gaussian mixture with sequential constraint?**
8. **Are there cases where REGALS truly has no equivalent explicit model?**
9. **When does REGALS outperform Molass, and vice versa?**

### Practical
10. **Can we use EFA for peak detection, then fit explicit models?**
11. **How sensitive are results to EFA window choices?**
12. **What about non-SEC applications (IEX, time-resolved) where EFA assumptions break?**
