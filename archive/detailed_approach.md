# Detailed Two-Track Approach
## Mathematical Proof + Numerical Verification

---

## **TRACK 1: Mathematical Proof**

### Goal
Derive the implicit functional form that REGALS's regularization assumes, and establish mathematical equivalence/relationship to explicit parametric models.

### Step 1.1: Formalize the REGALS Problem
**Objective**: Write down the exact optimization problem REGALS solves

- Start with: $\min_{P,C} \|M - PC\|^2 + R(C) + R(P)$
- Identify all regularization terms:
  - Smoothness on $C$: $\lambda_C \|D^2 C\|^2$ (elution curves)
  - Smoothness on $P$: $\lambda_P \|D^2 P\|^2$ (SAXS profiles)
  - Compact support: $C(t) = 0$ for $t > t_{max}$
  - Real-space constraint on $P$: $P(q) \leftrightarrow P(r)$ with $d_{max}$
  - Non-negativity: $C \geq 0$, $P(r) \geq 0$
- **Deliverable**: Precise mathematical statement of REGALS optimization

### Step 1.2: Bayesian Interpretation
**Objective**: Recast regularization as Bayesian prior distributions

- Recognize: $\|M - PC\|^2$ = negative log-likelihood (Gaussian noise)
- Recognize: $\lambda \|D^2 C\|^2$ = negative log-prior
- **Question**: What prior distribution corresponds to smoothness penalty?
  - Gaussian process with specific covariance?
  - Integrated Wiener process?
- **Deliverable**: $R(C) \leftrightarrow p(C|\text{parameters})$

### Step 1.3: Characterize the Implicit Functional Form
**Objective**: Determine what function shapes are favored by smoothness regularization

**Approach A - Variational Calculus**:
- Find functions that minimize $\|D^2 C\|^2$
- These are piecewise cubic splines (minimum curvature)
- Single peak → cubic spline ≈ ?

**Approach B - Frequency Domain**:
- Smoothness penalty = high-frequency suppression
- Fourier transform: $\|D^2 C\|^2 = \int \omega^4 |\hat{C}(\omega)|^2 d\omega$
- Low-pass filter → Gaussian-like in time domain

**Approach C - Kernel Methods**:
- Smoothness prior → reproducing kernel Hilbert space
- Identify the kernel function
- Kernel → basis functions

**Deliverable**: Mathematical characterization of implicit peak shapes

### Step 1.4: Connection to Explicit Models
**Objective**: Show when/how implicit model relates to Gaussian/EGH/SDM/EDM

- **Gaussian**: Is smoothness penalty exactly equivalent to Gaussian basis?
- **EGH**: Under what conditions does implicit model approximate EGH?
- **General**: Derive relationship: explicit model ↔ regularization strength

**Key Questions**:
- Is REGALS ≡ Gaussian with flexible parameters?
- Or: REGALS ⊃ Gaussian (more general)?
- Or: REGALS ⊄ Gaussian (different space)?

**Deliverable**: Theorem or proposition relating implicit/explicit models

### Step 1.5: Real-Space SAXS Constraint
**Objective**: Understand the additional constraint from P(r) with $d_{max}$

- This is beyond just smoothness - adds physical constraint
- Does this change the implicit model for concentration curves?
- Coupling between P and C through M = PC

**Deliverable**: Extended theory including SAXS-specific constraints

---

## **TRACK 2: Numerical Verification**

### Goal
Empirically test theoretical predictions through simulations and real data analysis.

### Step 2.1: Simulation Framework Setup
**Objective**: Create controlled test environment with ground truth

**2.1a: Data Generation**
- Define time grid: $t \in [0, T]$, elution time points
- Define q-space grid: $q \in [q_{min}, q_{max}]$, scattering vector
- Generate true concentration profiles:
  - Case 1: Single Gaussian peak
  - Case 2: Two overlapping Gaussian peaks  
  - Case 3: Single EGH peak
  - Case 4: Single SDM peak
  - Case 5: Complex mixture (2 EGH + 1 SDM)
- Generate true SAXS profiles for each component
- Compute synthetic data: $M = PC$
- Add noise: $M_{obs} = M + \epsilon$, vary SNR levels

**2.1b: Parameter Space**
- Vary peak overlap: 0.5σ, 1σ, 2σ separation
- Vary noise level: SNR = 100, 50, 20, 10, 5
- Vary number of components: 1, 2, 3, 4
- Vary peak shapes: Gaussian, EGH, SDM, EDM

**Deliverable**: Synthetic dataset library with ground truth

### Step 2.2: Implementation
**Objective**: Apply both REGALS and Molass to synthetic data

**2.2a: REGALS Implementation**
- Option 1: Use original MATLAB/Python code from Meisburger et al.
- Option 2: Implement from scratch following their methods
- Key: Use identical regularization parameters across tests

**2.2b: EFAMIX Application**
- Use ATSAS EFAMIX tool (standard implementation)
- Apply with same EFA thresholds as REGALS
- Isolates pure EFA effect (no regularization)

**2.2c: Molass Application**
- Apply Molass with different explicit models:
  - Gaussian (baseline)
  - EGH
  - SDM  
  - EDM
- Use consistent optimization approach

**2.2d: Fair Comparison**
- Same data preprocessing
- Same number of components (known from ground truth for Molass; estimated by EFA for EFAMIX/REGALS)
- Optimize all methods to convergence
- **Three-way comparison**: EFAMIX (EFA only) vs REGALS (EFA + regularization) vs Molass (explicit)

**Deliverable**: Analysis pipeline for all three methods

### Step 2.3: Metrics and Analysis
**Objective**: Quantify agreement between methods and ground truth

**Reconstruction Metrics**:
- Data fit: $\|M_{obs} - \hat{P}\hat{C}\|^2$
- Concentration error: $\|C_{true} - \hat{C}\|^2$
- Profile error: $\|P_{true} - \hat{P}\|^2$
- Peak position error: $|t_{peak,true} - t_{peak,est}|$
- Peak area error (quantification accuracy)

**Comparison Metrics** (EFAMIX vs REGALS vs Molass):
- Agreement: $\|C_{EFAMIX} - C_{REGALS}\|^2$, $\|C_{REGALS} - C_{Molass}\|^2$, $\|C_{EFAMIX} - C_{Molass}\|^2$
- Correlation: $\rho$ for all pairs
- Peak parameters: compare amplitudes, widths, positions across all three

**Analysis Questions**:
- When true model = Gaussian, does REGALS ≈ EFAMIX ≈ Molass-Gaussian?
- Does regularization (REGALS) improve over pure EFA (EFAMIX)?
- When true model = EGH, which method performs best?
- As SNR decreases, when do methods diverge?
- **Key question**: Is the regularization stage (REGALS) necessary, or does EFA alone (EFAMIX) suffice?

**Deliverable**: Comprehensive comparison results

### Step 2.3b: EFA Noise Sensitivity Study (CRITICAL!)
**Objective**: Quantify the practical limitations of EFA's "automatic" component detection

**2.3b.1: Noise Impact on Rank Estimation**
- Generate identical data with varying noise levels: SNR = 100, 50, 20, 10, 5
- Apply SVD, plot singular value spectrum
- **Key question**: At what SNR does the "gap" between signal and noise singular values become ambiguous?
- Measure: ratio of Nth to (N+1)th singular value vs SNR

**2.3b.2: Threshold Sensitivity Analysis**
- For same dataset, vary EFA thresholds:
  - Singular value significance cutoff
  - Autocorrelation threshold
  - Gradient threshold for forward/backward EFA
- **Measure reproducibility**: How much does component number change?
- **Measure result sensitivity**: How much do extracted profiles change?

**2.3b.3: Inter-User Variability**
- Simulate different users with different judgment:
  - Conservative: high thresholds (fewer components)
  - Aggressive: low thresholds (more components)
  - Moderate: default thresholds
- Compare resulting decompositions
- **Key metric**: Is there a "gray zone" where component number is ambiguous?

**2.3b.4: Comparison to Explicit Specification**
- Molass: Specify N components directly (no ambiguity)
- REGALS: EFA estimates N components (with uncertainty)
- **Question**: Does the uncertainty in N propagate to uncertainty in profiles?

**Deliverable**: 
- Quantitative assessment of EFA's noise sensitivity
- Identification of SNR threshold where EFA becomes unreliable
- Documentation of "subjectivity" in supposedly automatic detection

### Step 2.4: Parameter Sensitivity Study
**Objective**: Understand how hyperparameters affect implicit modeling

**REGALS Parameters**:
- Vary $\lambda_C$ (smoothness weight): 10^-4 to 10^0
- Vary $d_{max}$ (compact support)
- Study: How does $\lambda$ change the implicit peak shape?

**Molass Parameters**:
- Vary initial guesses
- Test model misspecification (fit Gaussian to EGH data)

**Deliverable**: Sensitivity analysis revealing implicit model dependence

### Step 2.5: Real SEC-SAXS Data Application
**Objective**: Validate findings on experimental data

**Data Selection**:
- Simple case: Well-separated peaks (validation)
- Challenging case: Overlapping peaks (test case)
- Known mixtures: If available, with known composition

**Analysis Protocol**:
1. Apply both REGALS and Molass
2. Compare results:
   - Do they agree on number of components?
   - Do peak positions/areas match?
   - Which gives more physical P(r) functions?
3. Physical interpretation:
   - Are results consistent with known protein sizes?
   - Do elution curves make chromatographic sense?

**Deliverable**: Real-world case studies

---

## Implementation Timeline

### Phase 1: Foundation (Weeks 1-4)
- [ ] Literature review (both tracks)
- [ ] Mathematical formulation (Track 1.1-1.2)
- [ ] Simulation framework setup (Track 2.1)

### Phase 2: Core Analysis (Weeks 5-10)
- [ ] Mathematical derivation (Track 1.3-1.4)
- [ ] Simulation experiments (Track 2.2-2.3)
- [ ] Cross-validation: Do simulations support theory?

### Phase 3: Refinement (Weeks 11-14)
- [ ] Real data analysis (Track 2.5)
- [ ] Complete mathematical proof (Track 1.5)
- [ ] Synthesize findings

### Phase 4: Writing (Weeks 15-18)
- [ ] Draft paper sections
- [ ] Generate figures
- [ ] Iterate based on findings

---

## Key Milestones

**Milestone 1**: Mathematical relationship established (Track 1.3 complete)

**Milestone 2a**: Simulation shows REGALS ≈ Gaussian for Gaussian data (Track 2.3)

**Milestone 2b**: EFA noise sensitivity quantified - establishes practical limits (Track 2.3b)

**Milestone 3**: Both tracks converge - theory predicts simulations (Week 10)

**Milestone 4**: Real data validates theoretical framework (Week 14)

**Milestone 5**: Paper submitted (Week 18)

---

## Coordination Between Tracks

### Theory → Experiment
- Mathematical derivation predicts: "REGALS should match Gaussian when λ = X"
- Simulation tests: Does it actually match at that λ?

### Experiment → Theory
- Simulation finds: "REGALS diverges from Gaussian at high noise"
- Theory explains: "Because additional constraints (non-negativity, compact support) dominate"

### Iterative Refinement
- Theory incomplete → run simulations to explore
- Simulations show unexpected behavior → refine theory
- Converge when both tracks tell consistent story
