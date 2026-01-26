# Project Status & Quick Start
**Last Updated**: January 26, 2026

---

## 🎯 What This Repository Is

JOSS validation repository for **Molass Library** paper ([#9424](https://github.com/openjournals/joss-reviews/issues/9424)).

**Mission**: Document that existing "model-free" methods (CHROMIXS, EFAMIX, REGALS) have limitations that Molass addresses through explicit parametric modeling.

---

## 🚀 Quick Session Initialization

**For AI assistants**: When user says **"Initialize: modeling-vs-model_free context"**

### Read These Core Documents
1. **README.md** - Repository purpose
2. **PROJECT_STATUS.md** (this file) - Current focus
3. **R_CENTRIC_FRAMEWORK.md** - Analytical framework
4. **explorations/README.md** - Mathematical foundations overview

### Key Context Framework
- **R-centric analysis**: Frame all matrix factorization in terms of transformation matrix R
- **Three key questions**: What R does it assume? What R can it find? What R ambiguity remains?
- **Application**: Use this framework for analyzing any method's behavior or limitations

---

## 🔑 Key Mathematical Foundations (Complete)

These four notebooks/documents provide rigorous theoretical support:

### 1. [matrix_transformations_tutorial.ipynb](explorations/matrix_transformations_tutorial.ipynb)
**Status**: ✓ Complete (985+ lines, 12 parts)

**What it covers**:
- Parts 1-7: Matrix transformations, rotation matrices, orthogonal groups
- Parts 8-9: Implicit vs explicit R-centric framework (pedagogical breakthrough)
- Part 10: Constraint hierarchy (4-level uniqueness conditions)
- Part 11: Discrete permutation ambiguity introduction
- Part 12: Summary and implications

**Why it matters**: Comprehensive mathematical foundation for understanding all matrix factorization methods.

### 2. [discrete_ambiguity_demonstration.ipynb](explorations/discrete_ambiguity_demonstration.ipynb)
**Status**: ✓ Complete (16 cells, 6 parts)

**What it demonstrates**:
- Group theory explanation of discrete permutations
- GL(2) disconnected components (det>0 vs det<0)
- Singularity barrier visualization (det=0)
- **Dual view**: Parameter space (PCA) + transformation space (matrix heatmaps)

**Key insight**: "Singularity barriers create energy barriers that keep optimization algorithms within one permutation basin."

**Why it matters**: Explains why methods like REGALS find discrete solutions despite connected feasible space.

### 3. [smoothness_orthogonal_invariance_proof.ipynb](explorations/smoothness_orthogonal_invariance_proof.ipynb)
**Status**: ✓ Complete (11 parts, comprehensive proof)

**What it proves**:
- Smoothness regularization ||D^k C||² preserves orthogonal transformations
- **Generalized discovery**: Applies to ALL differential operators D^k (not just D²)
- 1000-trial numerical validation (machine precision)

**Key finding**: D² preferred not for unique invariance, but as "sweet spot" regularization quality.

**Why it matters**: Explains why REGALS needs multiple constraint layers beyond smoothness alone.

### 4. [R_CENTRIC_FRAMEWORK.md](R_CENTRIC_FRAMEWORK.md)
**Status**: ✓ Complete

**What it provides**:
- Unified analytical framework for all matrix factorization analysis
- Three key questions to ask about any method
- Concrete examples: REGALS, EFA, permutations
- Pedagogical foundation from matrix_transformations_tutorial.ipynb

**Why it matters**: Prevents confusion by establishing consistent analytical approach across all work.

---

## 🎯 Today's Breakthrough (January 26, 2026)

### From Understanding Discrete Ambiguity → Questioning Selection Reliability

**Morning**: Repository reorganization
- Moved matrix_transformations_tutorial.ipynb to explorations/
- Streamlined PROJECT_STATUS.md (created SESSION_HISTORY.md for detailed logs)
- Clear focus on 4 key mathematical foundations

**Afternoon**: Critical realization about selection problem
- **Question asked**: After demonstrating discrete permutation candidates exist (separated by singularity barriers), how do model-free methods select the physically correct one?
- **Two possibilities identified**:
  1. **Lucky**: Regularization constraints implicitly prefer correct permutation
  2. **Selection required**: Need global optimization with physical validation
- **Implication**: Local optimization may be structurally insufficient unless regularization "gets lucky"

**New research question formalized**: "How lucky are model-free approaches?"
- Created [permutation_selection_reliability_study.md](explorations/permutation_selection_reliability_study.md)
- Proposes computational study with synthetic + real data
- Tests: Frequency, selection bias, silent failure risk
- Outcome: Quantify when local optimization suffices vs when global search needed

**Updated**: [historical_development.md](evidence/historical_development.md)
- Added "The Selection Problem: A Fundamental Challenge Revealed" section
- Documents that this is empirically testable, not philosophical
- Connects to broader need for validation in model-free methods

**Status**: Pilot study complete with profound findings

**Implementation complete**: [permutation_reliability_pilot.ipynb](explorations/permutation_reliability_pilot.ipynb)
- ✅ Full workflow: synthetic data → SVD → simple ALS → smoothness-regularized ALS
- ✅ Multi-start experiments (10 runs each, 2 methods)
- ✅ Statistical analysis and permutation detection
- ✅ 5 figures generated with comprehensive visualizations

**Key Findings** (simplest test case: 2 components, moderate overlap, SNR=100):

1. **Non-negativity alone (40% success)**:
   - 40% correct order, 60% swapped
   - Objectives IDENTICAL (p=0.88)
   - Pure ambiguity - random initialization determines outcome

2. **Smoothness regularization (10% success, but...)**:
   - Only 10% correct order, 90% swapped (WORSE selection!)
   - BUT objectives DRAMATICALLY different (p<0.0001)
   - Correct solution: objective = 0.000068
   - Swapped solution: objective = 0.329 (4800× WORSE!)
   - t-statistic: -46311 (massive difference)

3. **Critical insight**: Smoothness ENABLES selection but FAILS optimization
   - IF you could evaluate both permutations → easy to pick correct one
   - BUT random initialization → 90% get trapped in wrong basin
   - Swapped permutation is a powerful attractor

4. **Validates REGALS architecture necessity**:
   - EFA initialization essential to avoid wrong basin
   - Two-stage approach not optional - it's structurally required
   - Local optimization insufficient without good starting point

**Implications**: This provides direct computational evidence that model-free methods require careful initialization strategies - exactly the hidden modeling choice your paper argues about!

---

## 📂 Repository Structure

```
c:\Users\takahashi\GitHub\modeling-vs-model_free\
├── README.md                  # Repository purpose
├── PROJECT_STATUS.md          # ← This file (current focus)
├── SESSION_HISTORY.md         # Detailed development log
├── R_CENTRIC_FRAMEWORK.md     # 🔑 Analytical framework
│
├── evidence/                  # 🎯 JOSS VALIDATION (in progress)
│   ├── chromixs/              # ⏳ CHROMIXS deferral evidence
│   ├── efamix/                # ⏳ EFAMIX threshold evidence
│   ├── regals/                # ⏳ REGALS two-stage evidence
│   └── efa_original/          # EFA limitation verifications (1-4 complete)
│
├── explorations/              # 📚 MATHEMATICAL FOUNDATIONS (complete)
│   ├── matrix_transformations_tutorial.ipynb          # 🔑 Comprehensive foundations
│   ├── discrete_ambiguity_demonstration.ipynb         # 🔑 Group theory visualization
│   ├── smoothness_orthogonal_invariance_proof.ipynb   # 🔑 D^k invariance proof
│   ├── underdeterminedness_exploration.ipynb          # Constraint hierarchy
│   ├── permutation_ambiguity_examples.ipynb           # Discrete ambiguity risk
│   ├── REGALS_analysis_summary.md                     # Comprehensive findings
│   └── discrete_structure_propagation_theory.md       # Topological framework
│
├── algorithms/                # Algorithm trend analysis (complete)
│   ├── zhang2025_*.ipynb      # Matrix factorization trends
│   └── temp_regals/           # REGALS code verification
│
├── molass/
│   └── paper.md               # 📄 JOSS SUBMISSION
│
├── tools/
│   ├── read_pdfs.py           # PDF extraction utility
│   ├── extracted_papers.txt   # REGALS + hplc-py
│   ├── efa_papers.txt         # Maeder + Keller
│   └── chromixs_paper.txt     # Panjkovich & Svergun
│
├── reference_papers/          # Source PDFs
└── archive/                   # Original research project (for future)
```

---

## ✅ What's Complete

### Mathematical Foundations (4 Key Files) ✓
- ✓ matrix_transformations_tutorial.ipynb
- ✓ discrete_ambiguity_demonstration.ipynb
- ✓ smoothness_orthogonal_invariance_proof.ipynb
- ✓ R_CENTRIC_FRAMEWORK.md

### EFA Limitations Verified ✓
- ✓ Limitation 1: Baseline problems
- ✓ Limitation 2: Noise sensitivity
- ✓ Limitation 3: Tailing/FIFO violations (critical discovery)
- ✓ Limitation 4: No quantification without calibration

### Literature Extracted ✓
- ✓ All source papers extracted to `tools/`
- ✓ Comprehensive analysis in `evidence/SAXS_methods_analysis.md`

---

## ⏳ What's Next

### Priority 1: Extract Method Evidence (🎯 Core JOSS Validation)

**CHROMIXS** (30 min):
- Extract quotes showing deferral to other methods
- Source: `tools/chromixs_paper.txt`
- Target: `evidence/chromixs/`

**EFAMIX** (45 min):
- Document quantified thresholds (SNR, τ, separation)
- Source: `tools/efamix_paper.txt`
- Target: `evidence/efamix/`

**REGALS** (60 min):
- Document two-stage architecture
- Extract EFA limitation quotes
- Sources: `tools/extracted_papers.txt` + `tools/efa_papers.txt`
- Target: `evidence/regals/`

### Priority 2: Synthesize for JOSS Paper (1-2 hours)
- Review evidence chain
- Update Research Impact Statement if needed
- Ensure citations align with evidence

---

## 🔬 Technical Setup

### Python Environment
```powershell
# Global Python 3.13 (no virtualenv per project policy)
& "C:\Program Files\Python313\python.exe"
```

### PDF Extraction
```powershell
& "C:\Program Files\Python313\python.exe" tools/read_pdfs.py "path/to/paper.pdf"
```

### Running Notebooks
```powershell
& "C:\Program Files\Python313\python.exe" -m jupyter notebook
```

---

## 📚 Essential Context

### Key Equations

**Matrix Decomposition**:
```
M = P·C
```
- M: Measured data (SAXS intensities over time)
- P: SAXS profiles (scattering patterns)
- C: Concentrations (elution curves)

**REGALS Optimization**:
```
minimize: χ² + λ_C ||D²C||² + λ_P ||D²P||²
```
- Data fit + smoothness constraints + non-negativity + compact support

**4-Level Constraint Hierarchy**:
1. Data-fit only → infinite solutions
2. + Smoothness → still infinite (orthogonal freedom)
3. + Non-negativity → eliminates most continuous ambiguity
4. + Full constraints → discrete permutations may remain

### Critical Citations

1. **Meisburger et al. (2021)** - REGALS method (IUCrJ, 8, 225-237)
2. **Konarev et al. (2021)** - EFAMIX tool (Protein Science, 31, 269-282)
3. **Panjkovich & Svergun (2018)** - CHROMIXS tool (Bioinformatics, 34(11), 1944-1946)
4. **Maeder & Zilian (1988)** - EFA invention (Chemom. Intell. Lab. Syst., 3, 205-213)
5. **Keller & Massart (1991)** - EFA tutorial (Chemom. Intell. Lab. Syst., 12, 209-224)

### Key Insights

1. **REGALS is two-stage**: EFA (detection) → Regularization (deconvolution)
2. **EFA assumes FIFO**: First-in-first-out (sequential elution)
3. **Critical finding**: FIFO fails even for ideal Gaussian peaks (not just tailing)
4. **Smoothness alone insufficient**: Preserves orthogonal transformations
5. **Discrete ambiguity persists**: 5-50% of datasets may need manual validation
6. **Topological origin**: Non-negativity creates disconnected parameter space

---

## 📖 Additional Resources

- **SESSION_HISTORY.md** - Detailed development log (session-by-session)
- **explorations/README.md** - Complete overview of mathematical notebooks
- **ORGANIZATION.md** - Repository structure and priorities
- **archive/** - Original research project plans (for future)

---

## 💡 Quick Commands

### Search Papers
```powershell
Select-String "search term" tools/extracted_papers.txt
```

### Check Errors
```powershell
# Within VS Code - get_errors tool will show any issues
```

### Git Status
```powershell
git status
git diff
```

---

**For detailed history**: See SESSION_HISTORY.md  
**For comprehensive analysis**: See explorations/REGALS_analysis_summary.md  
**For framework reference**: See R_CENTRIC_FRAMEWORK.md
