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

### 1. `underdeterminedness_exploration.ipynb`
**Status**: ✓ Complete  
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
- Generates: `../basis_ambiguity.png` (6 concentration profiles with identical data fit)
- Generates: `../regularization_ambiguity.png` (6 profiles with identical regularized objective)

**Corresponds to**: Track 1, Step 1.1 in `detailed_approach.md`

---

## Planned Notebooks

### 2. `implicit_functional_form.ipynb` (Planned)
- **Purpose**: Derive what functional form smoothness regularization implies
- **Approaches**:
  - Variational calculus (minimize $\|D^2C\|^2$ → cubic splines)
  - Frequency domain (Fourier transform → low-pass filter → Gaussian?)
  - Bayesian interpretation (regularization → prior distribution)
- **Goal**: Show conditions where REGALS ≈ Gaussian mixture model
- **Corresponds to**: Track 1, Steps 1.2-1.4 in `detailed_approach.md`

### 3. `efa_noise_sensitivity.ipynb` (Planned - CRITICAL!)
- **Purpose**: Quantify practical limitations of EFA's "automatic" component detection
- **Tests**:
  - Noise impact on singular value spectra (SNR = 100, 50, 20, 10, 5)
  - Threshold sensitivity (how much do results change with parameter tuning?)
  - Inter-user variability (simulate conservative vs aggressive threshold choices)
- **Goal**: Identify SNR threshold where EFA becomes unreliable
- **Corresponds to**: Track 2, Step 2.3b in `detailed_approach.md`

### 4. `simulation_studies.ipynb` (Planned)
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
