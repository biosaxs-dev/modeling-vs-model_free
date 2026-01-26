# Explorations: Mathematical & Numerical Investigations

**Status**: ✅ Complete (January 17-22, 2026)  
**Purpose**: Supporting analysis - **NOT required for JOSS validation**  
**Relevance**: Rigorous mathematical foundations exceeding JOSS review needs

---

This folder contains Jupyter notebooks providing **mathematical deep dives** into matrix factorization underdeterminedness, regularization theory, and constraint hierarchies. While this work strengthens theoretical understanding and may support future research publications, **it is not directly required for JOSS Research Impact Statement validation**.

---

## Relationship to JOSS Validation

### ❌ NOT Core to Validation

These mathematical explorations are **supporting work** that exceeds JOSS requirements:
- JOSS requires documenting **existing method limitations** from literature
- These notebooks provide **mathematical proofs** of theoretical foundations
- Different scope: rigorous derivations vs evidence extraction

### ✅ Valuable Context

While not required, these analyses:
- Prove fundamental impossibility of "model-free" claims
- Quantify ambiguity risks (5-50% of datasets)
- Demonstrate expertise and deep understanding
- Provide foundation for future research publications
- Strengthen arguments in JOSS paper (can be cited as supporting evidence)

---

## Current Notebooks

### 1. `matrix_transformations_tutorial.ipynb`
**Status**: ✓ Complete (January 23-24, 2026)  
**Purpose**: Comprehensive mathematical foundation for understanding matrix transformations, rotation matrices, and constraint hierarchies

**Overview**: 12-part tutorial covering fundamental concepts from basic matrix algebra through advanced topics like discrete permutation ambiguity. Originally created to verify EFA limitations, evolved into rigorous mathematical foundations supporting the entire research project.

**Key Parts**:
- Parts 1-7: Matrix transformations, rotation matrices, orthogonal groups
- Parts 8-9: Implicit vs explicit R-centric framework (pedagogical breakthrough)
- Part 10: Constraint hierarchy (4-level uniqueness conditions)
- Part 11: Discrete permutation ambiguity from group theory
- Part 12: Summary and implications

**Complementary Notebook**: Works with `discrete_ambiguity_demonstration.ipynb` to provide dual perspective on group-theoretic permutation structure.

---

### 2. `discrete_ambiguity_demonstration.ipynb`
**Status**: ✓ Complete (January 25-26, 2026)  
**Purpose**: Demonstrate that permutation ambiguity arises from transformation group structure (GL(2) disconnected components), not parameter space geometry

**Overview**: 6-part demonstration showing the "singularity barrier" — continuous transformations between permuted solutions must pass through singular matrices (det=0), creating discrete basins in optimization landscape.

**Key Visualizations**:
- **Part 4**: Determinant tracking showing det evolution: +1 → 0 → -1
- **Part 5**: Dual visualization (parameter space + transformation space)
  - Left: PCA projection showing connected feasible space with interpolation path
  - Right: 5 matrix heatmaps showing transformation evolution through singularity
- Demonstrates three distinct spaces: feasible (CONNECTED), optimization (discrete minima), group GL(2) (DISCONNECTED)

**Breakthrough Insight**: "Singularity barriers create energy barriers that keep optimization algorithms within one permutation basin." This explains why methods like REGALS find discrete solutions despite connected feasible space.

**Complementary Notebook**: Extends `matrix_transformations_tutorial.ipynb` Part 11 with detailed visualization and group theory analysis.

**Led to**: [permutation_selection_reliability_study.md](permutation_selection_reliability_study.md) - Research question arising from this demonstration ("How lucky are model-free approaches at selecting the correct permutation?")

---

### 3. `underdeterminedness_exploration.ipynb`
**Status**: ✓ Complete (January 18, 2026)  
**Purpose**: Demonstrate fundamental ambiguities in matrix factorization and test if regularization resolves them

**Part 1: Unconstrained Problem** (Cells 1-17)
- **Problem**: $\min_{P,C} \|M - PC\|^2$
- **Demonstrates**:
  - Scale ambiguity: $(αP, C/α)$ fits identically for any $α > 0$
  - Basis ambiguity: $(PR, R^{-1}C)$ fits identically for any invertible $R$
  - All transformations achieve $\chi^2 \approx 0$ but yield completely different components
- **Key Finding**: Infinitely many solutions with correlations ranging from -0.999 to +0.919

**Part 2: With Regularization** (Cells 18-27)
- **Problem**: $\min_{P,C} \|M - PC\|^2 + \lambda\|D^2C\|^2$
- **Tests User's Conjecture**: Does $\text{Objective}(PB, B^{-1}C) = \text{Objective}(P, C)$ for orthogonal $B$?
- **Answer**: **YES** - Confirmed both theoretically and numerically!
- **Key Results**:
  - Data-fit term: invariant for ANY invertible $B$ ✓
  - Smoothness term: invariant for orthogonal $B$ ✓
  - All 5 random rotations yield identical objectives (101.22) ✓
  - Non-negativity constraint eliminates most/all rotational freedom ✓

**The 4-Level Hierarchy**:
1. **Data-fit only**: Infinite solutions (scale + arbitrary basis)
2. **+ Smoothness**: Still infinite (scale + orthogonal rotations)
3. **+ Non-negativity**: Most rotational freedom eliminated
4. **+ Full REGALS** (compact support + SAXS constraints): Unique solution

**Impact for Paper**: Powerful evidence that REGALS requires **FOUR layers** of implicit modeling assumptions, not just one!

**Related Files**:
- Generates: `basis_ambiguity.png` (6 concentration profiles with identical data fit)
- Generates: `regularization_ambiguity.png` (6 profiles with identical regularized objective)

**Corresponds to**: Track 1, Step 1.1 in `detailed_approach.md`

---

### 4. `permutation_ambiguity_examples.ipynb`
**Status**: ✓ Complete  
**Purpose**: Quantify the risk of discrete permutation ambiguity in real-world datasets

**Key Finding**: 5-50% of real-world SEC-SAXS datasets may exhibit permutation ambiguity depending on peak separation, similarity, and noise levels.

---

### 5. `smoothness_orthogonal_invariance_proof.ipynb`
**Status**: ✓ Complete (January 22, 2026)  
**Purpose**: Rigorous mathematical proof that smoothness regularization restricts factorization ambiguity to orthogonal group O(n)

**Key Discovery**: Orthogonal invariance applies to ALL differential operators D^k (not just D²):
- D¹ (first derivative) has O(n) invariance
- D² (second derivative) has O(n) invariance  
- D³ and higher also have O(n) invariance
- D² preferred because it penalizes curvature (sweet spot for regularization)

**Mathematical Framework**: 11 parts with formal proof, numerical validation, and comprehensive testing (1000 random orthogonal transformations).

---

### 6. `permutation_selection_reliability_study.md`
**Status**: 🔄 In Progress (January 26, 2026)  
**Purpose**: Quantify how reliably model-free regularization constraints select the physically correct permutation when discrete alternatives exist

**Overview**: Computational study proposal arising from discrete_ambiguity_demonstration.ipynb insights. Tests the critical question: "How lucky are model-free approaches?"

**Research Questions**:
- **Frequency**: How often do multiple permutations satisfy all constraints equally well?
- **Selection bias**: Do regularization constraints naturally prefer the correct permutation?
- **Risk**: What fraction of analyses might find wrong permutation with excellent fit?

**Proposed Approach**:
- **Part 1**: Synthetic data with known ground truth (25 test cases, 20-50 random initializations each)
- **Part 2**: Real data multi-start analysis (10-20 diverse SEC-SAXS datasets)
- **Metrics**: Accuracy, consistency, ambiguity, objective discrimination
- **Timeline**: 6-8 weeks implementation

**Expected Outcomes**:
- **High reliability** (>95%): Local optimization sufficient
- **Moderate reliability** (70-95%): Post-hoc validation recommended
- **Low reliability** (<70%): Global optimization required

**Why it matters**: Transforms philosophical debate (model-free vs model-based) into empirical science with actionable guidance for practitioners.

**Relation to other work**: Direct application of discrete_ambiguity_demonstration insights; tests effectiveness of constraints from underdeterminedness_exploration hierarchy.

---

### 7. `permutation_reliability_pilot.ipynb`
**Status**: ✅ Complete (January 26, 2026)  
**Purpose**: Pilot implementation for Part 1 (Synthetic Data) of permutation_selection_reliability_study.md - test feasibility and discover critical optimization vs selection distinction

**Overview**: Complete workflow from synthetic data generation through multi-start optimization to reliability quantification, using pure Python implementation (no REGALS dependency for initial testing).

**Implementation Details**:
- **Test case**: 2 components, Gaussian profiles, moderate overlap (4σ separation), SNR=100
- **Ground truth**: Known concentration and SAXS profiles
- **Method**: Simple non-negative ALS (Alternating Least Squares)
- **Experiment**: 10 random initializations to detect permutation variability
- **Analysis**: Correlation-based permutation identification, statistical testing

**Key Components**:
- Part 1: Synthetic data generation (M = P^T · C with realistic parameters)
- Part 2: SVD analysis (baseline rank determination)
- Part 3: Simple ALS implementation (clean reference without external dependencies)
- Part 4: Multi-start experiment (test initialization sensitivity)
- Part 5: Statistical analysis and interpretation

**Outputs**: 5 figures
- `permutation_pilot_ground_truth.png` (4-panel: concentrations, SAXS profiles, clean/noisy data)
- `permutation_pilot_svd.png` (scree plot + cumulative variance)
- `permutation_pilot_als_convergence.png` (error + parameter change)
- `permutation_pilot_als_comparison.png` (4-panel comparison with ground truth)
- `permutation_pilot_multistart_errors.png` (error distribution + scatter)
- `permutation_pilot_smoothness_comparison.png` (4-panel: selection rates, objectives, scatter, summary table)

**Key Results**:
- **Non-negativity**: 40% success, objectives identical (perfect ambiguity)
- **Smoothness (λ=1.0)**: 10% success, correct objective 4800× better (selection works, optimization fails)
- **Critical finding**: Smoothness enables selection but creates optimization trap
- **Validates**: REGALS' EFA initialization is structurally necessary, not just convenient

**Profound Implication**: Distinguishes **selection capability** (can you tell which is better?) from **optimization reliability** (will local search find it?). Smoothness solves the first but exacerbates the second!

**Next Steps**:
1. Test different λ values (does stronger smoothness help or hurt?)
2. Test harder cases (more overlap → likely worse)
3. Document for paper (direct evidence of hidden modeling requirement)
4. Consider: Is global optimization unavoidable for reliable deconvolution?

**Relation to other work**: Provides computational proof for permutation_selection_reliability_study.md research question; transforms philosophical debate into quantified optimization challenge.

---

## Planned Notebooks

### `implicit_functional_form.ipynb` (Planned)
- **Purpose**: Derive what functional form smoothness regularization implies
- **Approaches**:
  - Variational calculus (minimize $\|D^2C\|^2$ → cubic splines)
  - Frequency domain (Fourier transform → low-pass filter → Gaussian?)
  - Bayesian interpretation (regularization → prior distribution)
- **Goal**: Show conditions where REGALS ≈ Gaussian mixture model
- **Corresponds to**: Track 1, Steps 1.2-1.4 in `detailed_approach.md`

### `efa_noise_sensitivity.ipynb` (Planned - CRITICAL!)
- **Purpose**: Quantify practical limitations of EFA's "automatic" component detection
- **Tests**:
  - Noise impact on singular value spectra (SNR = 100, 50, 20, 10, 5)
  - Threshold sensitivity (how much do results change with parameter tuning?)
  - Inter-user variability (simulate conservative vs aggressive threshold choices)
- **Goal**: Identify SNR threshold where EFA becomes unreliable
- **Corresponds to**: Track 2, Step 2.3b in `detailed_approach.md`

### `simulation_studies.ipynb` (Planned)
- **Purpose**: Compare REGALS, EFAMIX, and Molass on synthetic data
- **Test cases**:
  - Gaussian peaks (does REGALS ≈ Molass-Gaussian?)
  - EGH peaks (which method performs best?)
  - Overlapping vs separated peaks
  - Various noise levels (SNR = 100, 50, 20, 10, 5)
- **Metrics**: Reconstruction error, peak position/area accuracy, method agreement
- **Corresponds to**: Track 2, Steps 2.1-2.3 in `detailed_approach.md`

---

## Usage Notes

### Running Notebooks
All notebooks use the **global Python 3.13.11** environment (not virtualenv, per user preference).

**Windows PowerShell**:
```powershell
& "C:\Program Files\Python313\python.exe" -m jupyter notebook
```

### Required Packages
- `numpy` (matrix operations)
- `matplotlib` (visualization)
- `scipy` (SVD, QR decomposition)

### Figures
Notebooks save figures to the parent directory (`../`) for inclusion in documentation/paper.

### Cross-References
- See `../detailed_approach.md` for complete research plan
- See `../PROJECT_STATUS.md` for current progress
- See `../discussion_points.md` for paper outline and arguments

---

## Contributing

When adding new notebooks:
1. Follow naming convention: `descriptive_name_exploration.ipynb`
2. Include markdown cells with:
   - Purpose/goal statement
   - Mathematical setup
   - Key findings summary
3. Save figures to parent directory with descriptive names
4. Update this README with notebook description
5. Update `PROJECT_STATUS.md` with completion status

---

## Key Findings So Far

From `underdeterminedness_exploration.ipynb`:

1. **"Model-free" is mathematically impossible**  
   - Unconstrained $\min \|M-PC\|^2$ has infinitely many solutions
   - Every method MUST make modeling choices to get unique solution

2. **Smoothness regularization alone is insufficient**  
   - Preserves orthogonal transformations → still infinite solutions
   - Need additional constraints (non-negativity, compact support, SAXS) for uniqueness

3. **REGALS uses a 4-layer constraint hierarchy**  
   - Each layer is an implicit modeling assumption
   - Transparency, not existence, differentiates "model-free" from explicit modeling

This sets the foundation for the paper's central argument!
