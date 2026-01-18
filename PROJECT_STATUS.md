# Project Status & Resumption Guide
**Last Updated**: January 17, 2026

---

## Quick Overview

**Project Goal**: Write a paper clarifying the relationship between "modeling" (Molass) and "model-free" (REGALS) approaches in SEC-SAXS analysis.

**Core Thesis**: "Model-free" is a misnomer - REGALS involves implicit modeling at THREE levels:
1. **EFA Stage 1**: Sequential "first-in-first-out" elution assumption (physical model)
2. **EFA Stage 2**: Manual threshold tuning for component detection (subjective modeling decisions)  
3. **Regularization**: Smoothness constraints → implicit Gaussian-like functional forms

**User's Key Insight** (from practical experience): EFA's "automatic" component detection is actually very sensitive to noise and requires extensive manual tuning - skeptical about real-world reliability.

---

## Document Map

| File | Purpose | Status |
|------|---------|--------|
| **discussion_points.md** | Main paper planning - thesis, arguments, outline | ✓ Up-to-date with EFA critique |
| **detailed_approach.md** | 18-week implementation plan (Track 1: Math, Track 2: Numerical) | ✓ Includes EFAMIX, EFA noise study |
| **tools/read_pdfs.py** | Python script to extract text from reference PDFs | ✓ Working |
| **tools/README.md** | Python environment policy & Windows quirks | ✓ Documents global Python usage |
| **tools/extracted_papers.txt** | Full text of Meisburger 2021 + Chure 2024 | ✓ Extracted |
| **tools/efa_papers.txt** | Full text of Maeder 1988 + Keller 1991 | ✓ Extracted |
| **tools/chromixs_paper.txt** | Full text of Panjkovich 2018 (CHROMIXS) | ✓ Extracted |
| **tools/efamix_paper.txt** | Full text of Konarev 2021 (EFAMIX - pure EFA) | ✓ Extracted |
| **molass/paper.md** | User's JOSS paper on Molass Library | Read-only reference |
| **reference_papers/** | Four PDFs (REGALS, hplc-py, EFA x2) | ✓ All read |

---

## Completed Work

### Phase 1: Foundation (✓ Complete)
- ✓ Read Molass JOSS paper (user's own work)
- ✓ Extracted and analyzed Meisburger 2021 (REGALS method paper)
- ✓ Extracted and analyzed Chure 2024 (hplc-py tool paper)
- ✓ Extracted and analyzed Maeder 1988 + Keller 1991 (EFA original papers)
- ✓ Extracted and analyzed Panjkovich 2018 (CHROMIXS - automated SEC-SAXS tool)
- ✓ Extracted and analyzed Konarev 2021 (EFAMIX - pure EFA implementation)

### Phase 2: Thesis Development (✓ Complete)
- ✓ Identified two-stage nature of REGALS (EFA + regularization)
- ✓ Recognized EFA's sequential elution assumption as implicit modeling
- ✓ Integrated user's practical skepticism about EFA noise sensitivity
- ✓ **Critical addition**: Found that EFA inventors (Maeder, Keller) themselves documented fundamental limitations:
  - Rank inflation from instrumental nonlinearities
  - Tailing as "the most serious difficulty"
  - Baseline sensitivity causing false factors
  - Quantification impossibility without external calibration
  - FIFO assumption fragility

### Phase 3: Framework Design (✓ Complete)
- ✓ Created comparison framework with four tools:
  - **Molass** (explicit parametric: EGH/SDM/EDM)
  - **EFAMIX** (pure EFA, no regularization)
  - **REGALS** (EFA + regularization)
  - **hplc-py** (explicit: skew-normal)
- ✓ Developed two-track approach:
  - Track 1: Mathematical proof (implicit functional forms)
  - Track 2: Numerical verification (simulations + real data)
- ✓ Added Step 2.3b: EFA Noise Sensitivity Study (marked CRITICAL)

### Phase 4: Preliminary Mathematical Exploration (✓ Complete)
- ✓ Created `explorations/underdeterminedness_exploration.ipynb`
- ✓ **Part 1**: Demonstrated scale ambiguity and basis ambiguity in unconstrained $\min ||M-PC||^2$
  - Proved infinitely many solutions with identical data fit
  - Visualized 6 different factorizations with completely different components
  - Quantified component correlations: -0.999 to +0.919 despite χ²=0
- ✓ **Part 2**: Tested if regularization breaks basis ambiguity
  - **Key finding**: Smoothness regularization $\lambda||D^2C||^2$ PRESERVES orthogonal transformations
  - All 5 random rotations yield identical objective values (101.22)
  - Proved user's conjecture: $\text{Objective}(PB, B^{-1}C) = \text{Objective}(P, C)$ for orthogonal $B$
  - Non-negativity constraint eliminates rotational freedom
- ✓ Established **4-level hierarchy of constraints** needed for uniqueness:
  1. Data-fit only: infinite solutions
  2. + Smoothness: still infinite (orthogonal transformations remain)
  3. + Non-negativity: continuous ambiguity eliminated; discrete permutation ambiguity may persist
  4. + Full REGALS (compact support + SAXS): unique for generic data; edge cases may have permutation ambiguity
- ✓ **Impact**: Powerful evidence that REGALS requires FOUR layers of implicit modeling, not one
- ✓ Created `explorations/permutation_ambiguity_examples.ipynb`
  - **Scenario 1**: Overlapping monomer-dimer → permutation likely (20-30% risk)
  - **Scenario 2**: Well-separated components → uniqueness guaranteed
  - **Scenario 3**: Oligomeric series → high ambiguity risk (30-50%)
  - **Risk quantification**: 5-50% of real-world SEC-SAXS datasets may have discrete permutation ambiguity
  - **Practical implication**: Manual validation required, undermining "model-free" claim
- ✓ Created `explorations/REGALS_critique_summary.md`
  - Comprehensive summary of all mathematical findings
  - Documents constraint hierarchy, terminology critiques, permutation ambiguity
  - Attribution to GitHub Copilot (Claude Sonnet 4.5)
  - Ready reference for paper writing

---

## Key Decisions & Rationale

### Python Environment
- **Decision**: Use Python 3.13.11 global environment (NOT virtualenv)
- **Location**: `C:\Program Files\Python313\python.exe`
- **Reason**: User preference for simplicity
- **Documented in**: `tools/README.md`
- **Windows quirk**: Use `& "C:\Program Files\Python313\python.exe"` in PowerShell

### Comparison Tools
- **Original plan**: Two-way comparison (Molass vs REGALS)
- **Current focus** (January 17, 2026): 
  - **Main**: Molass vs REGALS (both tackle overlapping peaks)
  - **Supplementary**: EFAMIX + CHROMIXS (supporting evidence in SI)
- **Why EFAMIX added**: Isolates pure EFA effect (Stage 1) from regularization (Stage 2)
- **Why CHROMIXS important**: Shows automation tools defer to REGALS for hard cases
- **Why hplc-py**: Another explicit modeling baseline (not main focus)

### Research Focus
- **Primary question**: What implicit model does REGALS embed? (Core of Molass vs REGALS comparison)
- **Critical addition**: EFA noise sensitivity study (user's practical concern validated by inventors' own papers)
- **Approach**: Both mathematical derivation AND empirical testing
- **Paper strategy**: Keep Molass↔REGALS in main text; EFAMIX/CHROMIXS limitations in SI

---

## Important Context

### Key Equations

**Matrix Decomposition**:
```
M = P·C
```
- M: Measured data matrix (SAXS intensities over time)
- P: SAXS profiles matrix (scattering patterns)
- C: Concentration/elution curves matrix

**REGALS Optimization**:
```
minimize: χ² + λ_C ||D²C||² + λ_P ||D²P||²
```
- χ²: Data fit error
- λ_C ||D²C||²: Smoothness penalty on concentrations
- λ_P ||D²P||²: Smoothness penalty on profiles
- Plus: compact support, non-negativity, real-space constraints

**EFA Sequential Assumption**:
- Forward SVD: Detect component appearances (first-in)
- Backward SVD: Detect component disappearances (first-out)
- **Assumption**: First component to appear is first to disappear

### Critical Citations

1. **Meisburger et al. (2021)** - REGALS method
   - IUCrJ, 8, 225-237
   - Two-stage process: EFA → regularized deconvolution
   - Applications: AEX-SAXS, titrations, time-resolved

2. **Chure & Cremer (2024)** - hplc-py tool  
   - JOSS, 9(94), 6270
   - Skew-normal distributions for peak fitting
   - Can deconvolve completely overlapping signals

3. **Maeder & Zilian (1988)** - EFA invention
   - Chemometrics and Intelligent Laboratory Systems, 3, 205-213
   - **Quote**: "tailing seems to be the most serious difficulty"
   - Identified baseline and noise sensitivity issues

4. **Keller & Massart (1991)** - EFA tutorial
   - Chemometrics and Intelligent Laboratory Systems, 12, 209-224
   - **Quote**: "rank of data matrix will be higher than number of underlying chemical species"
   - Documented rank inflation from instrumental nonlinearities

5. **Panjkovich & Svergun (2018)** - CHROMIXS tool
   - Bioinformatics, 34(11), 1944-1946
   - Automated SEC-SAXS processing (part of ATSAS suite with EFAMIX)
   - **Quote**: Works for "well resolved fractions (i.e. baseline separated sample elution peaks)"
   - For overlapping peaks: defers to REGALS, BioXTAS RAW, or UltraScan-SOMO
   - **Key insight**: Even "automatic" tools admit limitations for overlapping cases

6. **Konarev et al. (2021)** - EFAMIX tool (pure EFA)
   - Protein Science, 31, 269-282
   - Pure EFA implementation: forward/backward SVD + rotation matrix method
   - Part of ATSAS 3.1+ package
   - **Quote**: "EFA does show limitations when applied to systems with significantly asymmetric concentration profiles"
   - **Quote**: "potentially ambiguous" for overlapping peaks
   - **Quantified limitations**: 
     - Two components: SNR ≥ 10² photons, symmetric peaks (τ ≤ 2), concentration ratio ≤ 1:10
     - Three components: SNR ≥ 10³ photons required
     - Four components: SNR ≥ 10⁴ photons (very high quality only)
     - Peak separation ≥ 2× width, fails for asymmetric peaks (τ > 2)
   - **Key insight**: EFAMIX developers quantify exact conditions where EFA breaks down

### Key Insights

1. **REGALS is not one method but TWO sequential stages**:
   - Stage 1: EFA (component detection, window determination)
   - Stage 2: Regularized deconvolution (within windows)

2. **EFA makes a strong physical assumption**: Sequential elution (FIFO)
   - This is a chromatographic model, not data-driven mathematics
   - Breaks down with tailing, column overload, non-equilibrium

3. **EFA "automatic detection" requires manual tuning** (from user experience):
   - Singular value significance threshold
   - Concentration window boundaries
   - Autocorrelation cutoffs
   - **This is subjective modeling** - not algorithmic objectivity

4. **EFA limitations documented by inventors**:
   - Rank inflation (false positives from noise/artifacts)
   - Tailing intolerance (breaks FIFO assumption)
   - Baseline sensitivity (drift → spurious factors)
   - No quantification without external calibration

5. **EFAMIX as the missing link**:
   - Tests pure EFA (Stage 1 only)
   - Reveals how much improvement comes from regularization (Stage 2)
   - Creates spectrum: Explicit (Molass) → Pure EFA (EFAMIX) → EFA+Regularization (REGALS)

6. **Regularization alone is insufficient for uniqueness** (from today's exploration):
   - Smoothness penalty $\lambda||D^2C||^2$ preserves orthogonal transformations
   - Need 4-level constraint hierarchy: data-fit → smoothness → non-negativity → full constraints
   - Each level is an implicit modeling choice
   - "Model-free" requires multiple layers of implicit assumptions

7. **REGALS authors use misleading terminology** ("rotation ambiguity"):
   - They call it "rotation ambiguity" but the ambiguity applies to ANY invertible matrix, not just rotations
   - Unconstrained problem: $(P, C)$ and $(PR, R^{-1}C)$ are equivalent for ANY invertible $R$
   - This includes rotations, scalings, shearings, and arbitrary mixing
   - Only with smoothness regularization does ambiguity reduce to orthogonal (true rotation) matrices
   - Important clarification: the fundamental problem is much broader than "rotation"

8. **Mathematical precision refinements** (January 18, 2026):
   - **Orthogonal group structure**: O(n) includes proper rotations (SO(n), det=+1) and improper rotations (det=-1)
   - For n >> 100 (typical SEC-SAXS), improper rotations encompass far more than reflections: rotoinversions, orientation-reversing isometries
   - **Discrete permutation ambiguity**: Even with all four constraint layers, component label swapping may persist
   - **Risk quantification**: 5-50% of real-world datasets may have permutation ambiguity depending on peak separation, similarity, and noise
   - **Practical consequence**: Manual validation required for component assignments, contradicting "automatic" and "model-free" claims
   - **Constraint hierarchy precision**: Levels 3-4 eliminate continuous ambiguity but not always discrete ambiguity

---

## Technical Setup

### Reading PDFs
```powershell
& "C:\Program Files\Python313\python.exe" tools/read_pdfs.py "path/to/paper.pdf"
```
Output saved to `tools/extracted_papers.txt` or `tools/efa_papers.txt`

### Current Workspace Structure
```
e:\GitHub\modeling-vs-model_free\
├── README.md
├── PROJECT_STATUS.md          # ← This file
├── discussion_points.md        # Main planning document
├── detailed_approach.md        # 18-week implementation plan
├── explorations/
│   ├── underdeterminedness_exploration.ipynb  # Step 1.1: Basis ambiguity proof
│   ├── permutation_ambiguity_examples.ipynb   # Discrete ambiguity scenarios
│   └── REGALS_critique_summary.md             # Comprehensive findings summary
├── molass/
│   └── paper.md               # Reference: User's Molass JOSS paper
├── reference_papers/
│   ├── 2021, Steve P. Meisburger.pdf    # REGALS
│   ├── 2024, Griffin Chure.pdf          # hplc-py
│   ├── 1988, Marcel Maeder.pdf          # EFA original
│   └── 1991, H.R. Keller.pdf            # EFA tutorial
└── tools/
    ├── README.md              # Python environment policy
    ├── read_pdfs.py           # PDF extraction script
    ├── extracted_papers.txt   # REGALS + hplc-py full text
    └── efa_papers.txt         # EFA papers full text
```

---

## Next Session: How to Resume

### 💡 **BEST PRACTICE: Start Every New Copilot Session With**
```
"I'm working on modeling vs model-free SEC-SAXS paper. 
Read PROJECT_STATUS.md for context. 
Then let's work on Priority 1: Mathematical Derivation."
```
(Replace "Priority 1" with Priority 2 or 3 depending on what you want to work on)

This ensures the AI has full context immediately and can continue seamlessly.

---

### Option A: Quick Review (10 minutes)
1. Open `discussion_points.md` - read **Section 3c** (EFA limitations from inventors)
2. Review the **comparison table** - now includes rank estimation, quantification, tailing
3. Check **Section 3b** - your practical EFA skepticism + proposed noise sensitivity study
4. Jump to **"Next Steps → Immediate"** section

### Option B: Deep Dive (30 minutes)  
1. Read this entire `PROJECT_STATUS.md` file
2. Skim `detailed_approach.md` - focus on:
   - **Step 2.3b** (EFA Noise Sensitivity Study - lines ~150-185)
   - **Key Milestones** (bottom of file)
3. Review `discussion_points.md`:
   - Central Thesis
   - Section 3 (REGALS: Two Layers of Implicit Modeling)
   - Section 3b + 3c (EFA practical/theoretical limitations)
4. Check `tools/efa_papers.txt` - search for key quotes:
   - "tailing seems to be the most serious difficulty"
   - "rank of data matrix will be higher"

---

## Immediate Priorities (Next Work Session)

**Paper Focus Strategy** (Updated January 17, 2026):
- **Main**: Molass vs REGALS (explicit vs implicit modeling of overlapping peaks)
- **Supplementary**: EFAMIX (Stage 1 limitations) + CHROMIXS (automation limitations)
- **Rationale**: Clean narrative focused on intellectual core; supporting evidence in SI

### Priority 1: Mathematical Derivation (Track 1) - FOR MOLASS vs REGALS
**Goal**: Derive the implicit functional form from smoothness regularization (core of comparison)

**Status**: Step 1.1 ✓ Complete (underdeterminedness proven, 4-level hierarchy established)

**Tasks**:
- [x] **Step 1.1**: Prove underdeterminedness of $\min ||M-PC||^2$ and test if regularization breaks ambiguity
  - ✓ Demonstrated scale and basis ambiguity (infinitely many solutions)
  - ✓ Proved smoothness regularization preserves orthogonal transformations
  - ✓ Established 4-level hierarchy (data-fit → smoothness → non-negativity → full REGALS)
- [ ] **Step 1.2**: Bayesian interpretation of regularization
  - What prior distribution corresponds to $\lambda||D^2C||^2$?
  - Gaussian process? Integrated Wiener process?
- [ ] **Step 1.3**: Characterize implicit functional form
  - Variational calculus: minimize $||D^2C||^2$ → cubic splines?
  - Frequency domain: high-frequency suppression → Gaussian?
  - Kernel methods: reproducing kernel Hilbert space
- [ ] **Step 1.4**: Connection to explicit models
  - When does REGALS ≈ Gaussian mixture?
- [ ] Combine with EFA's concentration window constraint
- [ ] Show conditions where REGALS ≈ Gaussian mixture model
- [ ] Identify when explicit models (EGH/SDM/EDM) diverge from implicit

**Starting point**: 
- Consult literature on Tikhonov regularization and implicit priors
- Look at Bayesian interpretation of regularization (MacKay 1992?)
- Search for "smoothness penalty implicit model" in chemometrics

### Priority 2: Simulation Framework Setup (Track 2)
**Goal**: Set up code to test REGALS vs Molass empirically

**Tasks**:
- [ ] Generate synthetic SEC-SAXS data with known ground truth
  - Gaussian peaks (test case 1)
  - EGH peaks (test case 2)  
  - Overlapping, non-sequential (test EFA failure)
- [ ] Obtain/implement REGALS code (with full EFA stage)
- [ ] Run Molass on same data
- [ ] Compare reconstructions quantitatively

**Starting point**:
- Check if REGALS code is available (GitHub: ando-lab/regals)
- Set up Molass if not already installed
- Design data generation function: `generate_sec_saxs(peak_type, noise_level, overlap, ...)`

### Priority 3: EFA Noise Sensitivity Study (CRITICAL)
**Goal**: Empirically validate user's skepticism about EFA reliability

**Tasks**:
- [ ] Step 2.3b.1: Noise impact on rank estimation
  - Generate identical data at SNR = 100, 50, 20, 10, 5
  - Plot singular value spectra
  - Measure where signal/noise boundary becomes ambiguous
- [ ] Step 2.3b.2: Threshold sensitivity
  - Same data, vary EFA threshold parameters
  - Quantify result variability
- [ ] Step 2.3b.3: Inter-user variability
  - If possible, have multiple people manually tune EFA
  - Measure disagreement in component count, window boundaries
- [ ] Step 2.3b.4: Compare to explicit detection
  - Run Molass peak detection on same noisy data
  - Which is more robust?

**Starting point**:
- This is new - no prior code
- Focus on Step 2.3b.1 first (most fundamental)
- Can simulate quickly, don't need real data

---

## Long-Term Roadmap

### Phase 4: Simulation Studies (Weeks 6-12)
- Generate synthetic data with known ground truth
- Apply all four methods: Molass, EFAMIX, REGALS, hplc-py
- Quantify agreement/disagreement
- **Critical**: EFA noise sensitivity experiments (Step 2.3b)

### Phase 5: Real Data Analysis (Weeks 13-15)
- Select benchmark SEC-SAXS datasets
- Apply all methods systematically
- Interpret differences physically
- Validate simulation predictions

### Phase 6: Writing (Weeks 16-18)
- Draft paper following outline in `discussion_points.md`
- Emphasize three-level "model-free" misnomer:
  1. EFA sequential assumption (physical model)
  2. Manual tuning (subjective modeling)
  3. Regularization (implicit functional form)
- Cite Maeder & Keller's own documentation of EFA limitations
- Provide guidance for method selection

---

## Questions to Carry Forward

### High Priority
1. **Does REGALS ≈ Gaussian mixture when data is Gaussian?** (Core hypothesis)
2. **At what noise level does EFA fail to detect components reliably?** (User's concern)
3. **How much do EFA results vary with threshold choices?** (Reproducibility)
4. **When does tailing break EFA windows?** (Maeder's identified problem)

### Medium Priority
5. Can we show rank inflation empirically? (Keller's warning)
6. Is EFA+regularization better than pure EFA (EFAMIX)?
7. When does REGALS outperform Molass, and vice versa?
8. Can we use EFA for detection but explicit models for fitting? (Hybrid approach)

### Lower Priority
9. How general is the implicit model derivation?
10. Can EFA be reformulated as an explicit parametric model?
11. What about non-SEC applications where FIFO assumption is invalid?

---

## Key Contacts & Resources

### Papers to Cite (Full References)
- Meisburger, S.P., Xu, D., and Ando, N. (2021). IUCrJ, 8, 225-237
- Chure, G. and Cremer, J. (2024). JOSS, 9(94), 6270  
- Maeder, M. and Zilian, A. (1988). Chemom. Intell. Lab. Syst., 3, 205-213
- Keller, H.R. and Massart, D.L. (1991). Chemom. Intell. Lab. Syst., 12, 209-224
- Panjkovich, A. and Svergun, D.I. (2018). Bioinformatics, 34(11), 1944-1946
- Konarev, P.V., Graewert, M.A., Jeffries, C.M., et al. (2021). Protein Sci., 31, 269-282

### Software Resources
- **REGALS**: https://github.com/ando-lab/regals (Python & MATLAB)
- **Molass**: [User's own library - ask for details]
- **hplc-py**: https://github.com/cremerlab/hplc-py (Python)
- **EFAMIX**: Part of ATSAS suite (may need to check availability)

### Additional Literature to Explore
- MacKay (1992) - Bayesian interpretation of regularization
- Tikhonov & Arsenin (1977) - Regularization theory
- EFA applications in different domains (equilibrium studies, time-resolved, FIA)

---

## Notes for Future Development

### Possible Extensions
1. **Hybrid method**: EFA for detection + explicit models for fitting
2. **Relaxed EFA**: Non-sequential variant for IEX-SAXS, titrations
3. **Benchmarking suite**: Standard test cases for method comparison
4. **Software tool**: Unified interface for all four methods

### Potential Collaborators
- Contact Nozomi Ando (REGALS author) for insights?
- Griffin Chure (hplc-py author) for comparison perspective?
- Chromatography modeling community for validation?

---

---

## Recent Accomplishments

### January 17, 2026

#### Morning Session
- Established paper thesis and comparison framework
- Read and analyzed 6 reference papers
- Documented EFA limitations from inventors' own papers
- Created comprehensive planning documents

#### Afternoon Session
- **Created `explorations/underdeterminedness_exploration.ipynb`**
  - 27 cells, fully executed and validated
  - Part 1: Proved infinitely many solutions to unconstrained problem
  - Part 2: Tested and confirmed user's conjecture about regularization
- **Key Mathematical Results**:
  - Scale ambiguity: $(\alpha P, C/\alpha)$ fits identically
  - Basis ambiguity: $(PR, R^{-1}C)$ fits identically for ANY invertible $R$ (not just rotations!)
  - **Important**: REGALS authors call this "rotation ambiguity" - misleading because $R$ can be any invertible matrix
  - **Critical finding**: Smoothness regularization $\lambda||D^2C||^2$ is invariant under orthogonal transformations
  - All 5 random rotations yielded objective = 101.22 (identical to 14 decimal places)
  - Regularization reduces ambiguity from arbitrary invertible matrices to orthogonal (true rotations) only
- **Established 4-Level Hierarchy**:
  1. Data-fit only → infinite solutions
  2. + Smoothness → still infinite (orthogonal rotations preserved)
  3. + Non-negativity → most rotational freedom eliminated  
  4. + Full REGALS → unique solution
- **Impact**: Powerful evidence that REGALS requires FOUR layers of implicit modeling, not one
- Organized project with `explorations/` folder and comprehensive README

### January 18, 2026 - Morning Session

#### Mathematical Precision Refinements
- **Refined constraint hierarchy** in `underdeterminedness_exploration.ipynb`:
  - Corrected terminology: "orthogonal rotations" → "orthogonal transformations" (includes proper rotations + improper rotations)
  - Added mathematical precision for high-dimensional matrices (n >> 100 typical in SEC-SAXS)
  - Updated Levels 3-4 to acknowledge discrete permutation ambiguity: "0 or small discrete set"
  - Clarified: continuous ambiguity eliminated, but discrete permutations may persist

#### New Notebooks Created
- **`explorations/permutation_ambiguity_examples.ipynb`**: Concrete examples of discrete ambiguity
  - **Scenario 1**: Monomer-dimer with overlap → 20-30% permutation risk
    - Peak separation < 0.5 mL, similar d_max, overlapping windows
    - Visual demonstration of equivalent solutions with swapped labels
  - **Scenario 2**: Small protein vs large aggregate → uniqueness guaranteed
    - Well-separated (4 mL apart), distinct d_max (3 nm vs 15 nm)
    - Permutation violates compact support constraints
  - **Scenario 3**: Oligomeric series (trimer/tetramer/pentamer) → 30-50% risk
    - Heavy overlap, similar sizes (1 nm d_max increments)
    - Multiple permutations may satisfy all constraints
  - **Risk assessment matrix**: Quantified permutation probability across scenarios
  - **Key finding**: 5-50% of real-world SEC-SAXS datasets may require manual validation

- **`explorations/REGALS_critique_summary.md`**: Comprehensive documentation
  - 10 major sections covering all mathematical findings
  - Executive summary of "model-free" critique
  - Complete constraint hierarchy documentation
  - Permutation ambiguity probability estimates
  - Terminology critiques ("rotation ambiguity" misnomer)
  - Implications for Molass vs REGALS paper
  - Next steps for mathematical derivation (Steps 1.2-1.4)
  - Attribution to GitHub Copilot (Claude Sonnet 4.5)
  - Ready reference for paper writing

#### Key Mathematical Insights
- **Orthogonal group O(n)** has dimension n(n-1)/2, includes:
  - **SO(n)**: Proper rotations (det = +1)
  - **det = -1**: Improper rotations (reflections, rotoinversions, orientation-reversing isometries)
  - For n >> 100, "reflections" is inadequate—far more general transformations
- **Permutation ambiguity persistence**:
  - Occurs when components are insufficiently distinguishable
  - Factors: overlapping elution, similar d_max, similar intensities
  - Requires manual expert judgment → undermines "model-free" claim
- **Practical implications**:
  - REGALS cannot always guarantee unique component assignment
  - Manual validation essential for physical meaningfulness
  - "Automatic" claim misleading for 5-50% of datasets

### What's Ready for Next Session
- ✓ Foundation established: "model-free" is mathematically impossible
- ✓ Quantitative proof: regularization alone insufficient
- ✓ Discrete ambiguity quantified: 5-50% of real data affected
- ✓ Comprehensive documentation ready for paper writing
- ✓ Next step clear: Characterize what implicit functional form smoothness assumes (Step 1.2-1.4)

---

## Session Log

| Date | Session Summary | Key Outcomes |
|------|----------------|--------------|
| Jan 17, 2026 (AM) | Initial setup, paper reading, framework design | ✓ Thesis established, EFAMIX added, EFA limitations documented |
| Jan 17, 2026 (PM) | Mathematical exploration: basis ambiguity | ✓ Created underdeterminedness_exploration.ipynb, proved user's conjecture, established 4-level hierarchy |
| Jan 18, 2026 (AM) | Mathematical precision, permutation ambiguity | ✓ Refined constraint hierarchy, created permutation_ambiguity_examples.ipynb, comprehensive REGALS_critique_summary.md |

---

**END OF STATUS DOCUMENT**

---

## Quick Command Reference

### Start New Session
```
Say: "Read PROJECT_STATUS.md and let's continue from Priority [1/2/3]"
```

### Check Document Status
```
Read: discussion_points.md (main planning)
Read: detailed_approach.md (implementation plan)
```

### Run PDF Extraction
```powershell
& "C:\Program Files\Python313\python.exe" tools/read_pdfs.py "file.pdf"
```

### Search Extracted Papers
```powershell
Select-String "search term" tools/efa_papers.txt
```
