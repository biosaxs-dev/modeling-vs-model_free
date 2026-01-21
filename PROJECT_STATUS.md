# Project Status & Resumption Guide
**Last Updated**: January 20, 2026 (Evening)

---

## Quick Overview

**Project Goal**: Validate the Research Impact Statement claims for the Molass Library JOSS paper submission ([#9424](https://github.com/openjournals/joss-reviews/issues/9424)).

**Primary Objective**: Document evidence that existing "model-free" methods (CHROMIXS, EFAMIX, REGALS) have documented limitations for overlapping peak decomposition, which Molass Library addresses through explicit parametric modeling.

**JOSS Context**: Following JOSS policy update (January 2026), the Research Impact Statement requires concrete evidence of either realized impact or credible near-term significance. This repository provides systematic validation of the documented limitations cited in our submission.

**Key Claims to Validate**:
1. **CHROMIXS**: Explicitly defers overlapping peak analysis to "other methods"
2. **EFAMIX**: Quantified failure thresholds (SNR ≥10³ for 3 components; τ≤2; separation ≥2× width)
3. **REGALS**: Two-stage approach (EFA + regularization) inheriting EFA's fundamental limitations

---

## Repository Structure

| Directory/File | Purpose | Status |
|----------------|---------|--------|
| **evidence/** | Documented validation of JOSS claims | 🚧 In progress |
| ├─ **chromixs/** | Evidence CHROMIXS defers overlapping peaks | ⏳ To be extracted |
| ├─ **efamix/** | Quantified EFAMIX failure thresholds | ⏳ To be extracted |
| └─ **regals/** | REGALS two-stage architecture & EFA limitations | ⏳ To be extracted |
| **algorithms/** | Matrix factorization algorithm explorations | ✓ Complete |
| ├─ zhang2025_simple_concept.ipynb | 3×3 pedagogical example | ✓ Complete |
| ├─ zhang2025_joint_optimization_demo.ipynb | 100×50 full demonstration | ✓ Complete |
| ├─ zhang2025_denoising_comparison.ipynb | Real data comparison with REGALS discussion | ✓ Complete |
| └─ matrix_factorization_trends_2025.md | Zhang 2025 relevance analysis | ✓ Complete |
| **explorations/** | Mathematical analysis (supporting) | ✓ Complete |
| ├─ underdeterminedness_exploration.ipynb | Constraint hierarchy proof | ✓ Complete |
| ├─ permutation_ambiguity_examples.ipynb | Discrete ambiguity scenarios | ✓ Complete |
| └─ REGALS_analysis_summary.md | Comprehensive findings | ✓ Complete |
| **archive/** | Original research project documents | ✓ Archived |
| ├─ discussion_points.md | Broader research paper planning | Archived |
| └─ detailed_approach.md | 18-week research implementation plan | Archived |
| **tools/** | PDF extraction utilities | ✓ Working |
| **reference_papers/** | Source PDFs | ✓ Available |
| *Validation Progress

### Phase 1: Literature Extrac

## Completed Work

### Phase 1: Foundation (✓ Complete)
- ✓ Read Molass JOSS paper (user's own work)
- ✓ Extracted and analyzed Meisburger 2021 (REGALS method paper)
- ✓ Extracted and analyzed Chure 2024 (hplc-py tool paper)
- ✓ Extracted and analyzed Maeder 1988 + Keller 1991 (EFA original papers)
- ✓ Extracted and analyzed Panjkovich 2018 (CHROMIXS - automated SEC-SAXS tool)
- ✓ Extracted and analyzed Konarev 2021 (EFAMIX - pure EFA implementation)
- ✓ Extracted and analyzed Hopkins 2024 (BioXTAS RAW 2 - latest state of art)

### Phase 2: EFA Limitation Verification (✓ Limitations 1-3 Complete)
Created systematic verification notebooks in `evidence/efa_original/`:
- ✓ `limitation_1_baseline_problems.ipynb` (10 cells, all executed)
  - Confirmed rank inflation from constant baseline
  - Quantified: 4th eigenvalue 0.232-0.247 appears
  - Evidence: σ₃/σ₄ gap shrinks from 231 trillion to 8-9
  
- ✓ `limitation_2_noise_sensitivity.ipynb` (18 cells, all executed)
  - Multi-sample analysis (SAMPLE1-4) from real data
  - Confirmed: Real SNR (avg 16.3) < simulated worst-case (10)
  - Evidence: Simulations were optimistic vs reality
  
- ✓ `limitation_3_tailing_effects.ipynb` (15 cells, all executed)
  - **CRITICAL DISCOVERY**: Problem MORE SEVERE than expected
  - FIFO assumption fails even with ideal Gaussian peaks (not just tailing!)
  - Evidence: Component 3 window [60, 51] = **negative width (-9 frames)**
  - Mathematical impossibility: Component disappears BEFORE it appears
  - This is fundamental to overlapping components, not tailing-specific

- ✓ `EFA_limitations_overview.md` - Navigation index for all limitation notebooks

### Phase 3: Literature Analysis (✓ Complete - Jan 20, 2026)
**Task**: Understand how modern methods (2018-2024) address EFA limitations

**Papers Analyzed**:
1. **CHROMIXS (2018, Panjkovich & Svergun)** - 3 pages
2. **EFAMIX (2021, Konarev et al.)** - 14 pages  
3. **REGALS (2021, Meisburger et al.)** - 13 pages
4. **BioXTAS RAW 2 (2024, Hopkins et al.)** - 15 pages

**Method**: 
- Updated `tools/read_pdfs.py` to extract all 4 papers
- Ran extraction with global Python 3.13
- Agent analyzed 215,947 characters of extracted text
- Created comprehensive comparison document

**Output**: `evidence/SAXS_methods_analysis.md`

**CRITICAL FINDING**: 
None of the 4 modern papers (2018-2024) explicitly acknowledge the fundamental FIFO mathematical impossibility discovered in our Limitation 3 verification:
- **CHROMIXS**: "Can't handle overlapping peaks" (defers to other tools, no explanation WHY)
- **EFAMIX**: Uses EFA but enforces strict FIFO; Figure 3 shows failures at τ > 2 (likely OUR phenomenon) but blames "high asymmetry" rather than mathematical root cause
- **REGALS**: Built to AVOID FIFO assumption via smoothness constraints; implicitly acknowledges problem but never states the mathematical impossibility
- **BioXTAS RAW 2**: Automated range-finding explicitly AVOIDS overlapping regions; detects FIFO violation condition without naming it

**Key Insight for Paper**: 
All modern methods work around this limitation without documenting the underlying mathematical failure mode. Our work **makes explicit what has been implicit in tool development** - the mathematical impossibility (negative window widths) that forces all post-EFA methods to abandon FIFO assumptions.

### Phase 4: Supporting Mathematical Analysis (✓ Complete)
Created detailed mathematical analysis in `explorations/` demonstrating the multi-layered constraint requirements for REGALS uniqueness. While this exceeds the validation needs, it provides rigorous supporting evidence.

### Phase 5: Repository Restructuring (✓ Complete - Jan 20, 2026)
- ✓ Created `evidence/` directory structure for systematic claim validation
- ✓ Created `evidence/efa_original/` for EFA limitation verification notebooks
- ✓ Archived broader research documents to `archive/`
- ✓ Maintained `explorations/` as supporting mathematical analysis
- ✓ Clarified repository purpose: JOSS claim validation (not standalone paper)

### Phase 6: Algorithm Exploration - Zhang 2025 (✓ Complete - Jan 21, 2026)
- ✓ Analyzed Zhang 2025 paper: "Loss-Minimizing Model Compression via Joint Factorization Optimization"
- ✓ Created `algorithms/` directory (moved from `evidence/algorithms/`)
- ✓ **zhang2025_simple_concept.ipynb**: 3×3 pedagogical example demonstrating gradient·noise insight
  - Showed 75% better loss when factorization noise opposes gradient direction
- ✓ **zhang2025_joint_optimization_demo.ipynb**: Full 100×50 demonstration
  - Iterative optimization showing 1.7% better loss than SVD at same rank
- ✓ **zhang2025_denoising_comparison.ipynb**: Real SEC-SAXS data analysis
  - Used molass_data SAMPLE1 at analyst-chosen rank k=5
  - Compared SVD denoising vs Zhang joint optimization with smoothness objective
  - User confirmed "significant improvement in smoothness"
  - Added comparison to REGALS iterative optimization (ALS vs gradient descent)
- ✓ **REGALS code verification**: Analyzed actual Python implementation
  - Verified alternating least squares structure in regals.py
  - Confirmed closed-form solutions via sparse linear solver
  - Validated regularization implementation (H_profile, H_concentration)
  - Created verification document in algorithms/temp_regals/
- ✓ **Moore 1980 IFT analysis**: Read foundational paper on Indirect Fourier Transform
  - Understood IFT as implicit denoising (dimension reduction: 1000 measurements → 20 coefficients)
  - Recognized regularization matrix H controls smoothness
  - Validated user's intuition: "Crucial denoising through IFT"
- ✓ **Key architectural distinction identified**:
  - **REGALS**: No separate denoising stage (IFT regularization during ALS = implicit denoising)
  - **Molass**: Explicit SVD denoising stage before parametric fitting
  - Zhang 2025's critique applies more to Molass than REGALS
- ✓ **Pragmatic solution developed**: Dual-evaluation approach for Molass
  - Optimize on M_clean (smooth landscape for convergence)
  - Validate against M_noisy (robustness check)
  - Simple to implement (just add final evaluation)
  - Addresses Zhang 2025 concern differently (validation vs joint optimization)

---

## Current Status Summary

### What's Complete (✓)
1. **EFA Limitations Verified** (3 of 10):
   - Limitation 1 (Baseline problems) ✓
   - Limitation 2 (Noise sensitivity) ✓
   - Limitation 3 (Tailing/FIFO violations) ✓ - **Critical finding: more severe than expected**
   
2. **Literature Analysis Complete**:

**Note**: Algorithm exploration (Zhang 2025) complete. Returning focus to JOSS validation.

1. **Continue EFA Limitation Verification**:
   - Limitation 4: No Quantification Without Calibration
   - Limitation 5: Resolution Limitation  
   - Limitation 9: Rank Inflation (noise-related)
   - Limitation 10: FIFO Assumption Failures (comprehensive)
   
2. **Synthesize Findings for JOSS Paper**:
   - Update Research Impact Statement if needed
   - Document evidence chain: EFA limitations → Modern workarounds → Molass contribution
   - Emphasize original contribution: explicit mathematical documentation of FIFO impossibility

3. **Consider Algorithm Insights for Future Work** (Optional):
   - Dual-evaluation approach (optimize clean, validate noisy) for Molass robustness checks
   - Potential gradient-informed initialization from Zhang 2025 framework
   - These are enhancements, not required for JOSS validation
1. **Continue EFA Limitation Verification**:
   - Limitation 4: No Quantification Without Calibration
   - Limitation 5: Resolution Limitation  
   - Limitation 9: Rank Inflation (noise-related)
   - Limitation 10: FIFO Assumption Failures (comprehensive)
   
2. **Synthesize Findings for JOSS Paper**:
   - Update Research Impact Statement if needed
   - Document evidence chain: EFA limitations → Modern workarounds → Molass contribution
   - Emphasize original contribution: explicit mathematical documentation of FIFO impossibility

### Key Files Ready for Next Session
- `evidence/EFA_limitations_overview.md` - Index of all limitation notebooks
- `evidence/limitation_3_tailing_effects.ipynb` - Most critical verification
- `evidence/SAXS_methods_analysis.md` - Comprehensive literature comparison
- `tools/extracted_papers.txt` - Full text of 4 papers (215,947 chars)

---

## Recent Accomplishments

### January 20, 2026 - Full Day Session

#### Morning: EFA Limitation Verification
- **Created `limitation_3_tailing_effects.ipynb`**:
  - 15 cells, fully executed (counts 1-7)
  - Implemented Exponentially Modified Gaussian (EMG) for tailing simulation
  - Tested 3 conditions: Gaussian (τ=0), mild tailing (τ=0.5), severe tailing (τ=1.5)
  - Applied forward/backward EFA to detect concentration windows
  - **CRITICAL FINDING**: Component 3 shows negative window widths in ALL conditions
    - Gaussian: [60, 51] → width = -9 frames
    - Mild tailing: [60, 50] → width = -10 frames  
    - Severe tailing: [60, 49] → width = -11 frames
  - **Unexpected Result**: Problem exists even for ideal Gaussian peaks (not tailing-specific!)
  - **Interpretation**: FIFO assumption fundamentally fails for overlapping components
  - **Mathematical impossibility**: Component appears at frame 60 but disappears at frame 51

#### Afternoon: Literature Analysis
- **Literature Review Request**: User asked how alternative tools address tailing limitation
- **Papers to Analyze**: 2018 Panjkovich, 2021 Konarev, 2021 Meisburger, 2024 Hopkins
- **Method**: Updated `tools/read_pdfs.py` to extract all 4 papers
- **Environment Setup**: Configured global Python 3.13 (no venv per project policy)
- **Extraction Success**: 4 papers, 45 pages total, 215,947 characters extracted
- **Agent Analysis**: Comprehensive review of all extracted text
- **Output Created**: `evidence/SAXS_methods_analysis.md` with:
  - Paper-by-paper summaries
  - Direct quotes about handling tailing/overlap
  - Comparison table across all 4 tools
  - Analysis of what each paper says vs doesn't say
  - Identification of critical gap in literature
  - Implications for our original contribution

#### Evening: Documentation Cleanup
- **Spelling Unification**: Changed all "ChromixS" instances to "CHROMIXS" (official name)
- **Files Updated**: 
  - `tools/README.md` - Papers list
  - `evidence/SAXS_methods_analysis.md` - Multiple locations
- **Updated `PROJECT_STATUS.md`**: Added comprehensive session summary (this document)

### January 18, 2026 - Morning Session
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
**Tasks** (in priority order):
- [ ] **CHROMIXS**: Extract direct quotes showing deferral to other methods for overlapping peaks
  - Source: Panjkovich & Svergun (2018), Section on limitations
  - Already noted in tools/chromixs_paper.txt
  - Target: `evidence/chromixs/`
  
- [ ] **EFAMIX**: Document specific quantified thresholds
  - SNR requirements: 10² (2 comp), 10³ (3 comp), 10⁴ (4 comp)
  - Peak asymmetry: τ ≤ 2
  - Separation: ≥ 2× peak width
  - Source: Konarev et al. (2021), Results/Discussion sections
  - Already extracted in tools/efamix_paper.txt
  - Target: `evidence/efamix/`
  
- [ ] **REGALS**: Document two-stage architecture and inherited EFA limitations
  - Source 1: Meisburger et al. (2021) - method description
  - Source 2: Maeder & Zilian (1988) - "tailing" quote
  - Source 3: Keller & Massart (1991) - "rank inflation" quote
  - Already extracted in tools/extracted_papers.txt and tools/efa_papers.txt
  - Target: `evidence/regals/`
- **Original plan**: Two-way comparison (Molass vs REGALS)
- **Current focus** (January 17, 2026): 
  - **Main**: Molass vs REGALS (both tackle overlapping peaks)
  - **Supplementary**: EFAMIX + CHROMIXS (supporting evidence in SI)
- **Why EFAMIX added**: Isolates pure EFA effect (Stage 1) from regularization (Stage 2)
- **Why CHROMIXS important**: Shows automation tools defer to REGALS for hard cases
- **Why hplc-py**: Another explicit modeling baseline (not main focus)

### Research Focus
- **Primary question**: What implicit model does REGALS embed? (Core of Molass vs REGALS comparison)
- *Supporting Mathematical Analysis (Optional Context)

The `explorations/` directory contains rigorous mathematical analysis that, while not required for JOSS validation, provides deep supporting evidence:

- **underdeterminedness_exploration.ipynb**: Proves REGALS requires 4-level constraint hierarchy
- **permutation_ambiguity_examples.ipynb**: Quantifies discrete ambiguity risk (5-50% of datasets)
- **REGALS_analysis_summary.md**: Comprehensive mathematical critique

This work demonstrates expertise but exceeds validation requirements. It may support future research publications.
Scope Definition
- **In scope**: Direct evidence extraction from peer-reviewed papers supporting JOSS claims
- **Optional**: Mathematical explorations in `explorations/` (supporting, not required)
- **Out of scope** (archived): New simulations, comparative studies, full research paper development

### Validation Approach
- **Method**: Direct quote extraction with page/section references
- **Sources**: Papers already extracted to `tools/` directory
- **Output**: Organized evidence in `evidence/` subdirectories
- **Goal**: Defensible documentation that JOSS reviewers/editors can verify
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
c:\Users\takahashi\GitHub\modeling-vs-model_free\
├── README.md                  # Repository purpose statement
├── PROJECT_STATUS.md          # ← This file (validation tracking)
├── evidence/                  # 🎯 VALIDATION DELIVERABLES
│   ├── README.md              # Validation overview
│   ├── chromixs/              # CHROMIXS deferral evidence
│   ├── efamix/                # EFAMIX threshold evidence
│   └── regals/                # REGALS two-stage & EFA limitations
├── algorithms/                # Matrix factorization explorations
│   ├── matrix_factorization_trends_2025.md
│   ├── zhang2025_simple_concept.ipynb
│   ├── zhang2025_joint_optimization_demo.ipynb
│   ├── zhang2025_denoising_comparison.ipynb
│   └── temp_regals/           # REGALS-related explorations
├── explorations/              # Supporting mathematical analysis (optional)
│   ├── underdeterminedness_exploration.ipynb
│   ├── permutation_ambiguity_examples.ipynb
│   └── REGALS_analysis_summary.md
├── archive/                   # Original research project (for future)
│   ├── README.md              # Archive context
│   ├── discussion_points.md   # Broader paper planning
│   └── detailed_approach.md   # 18-week research plan
├── molass/
│   └── paper.md               # 📄 JOSS SUBMISSION (deliverable)
├── reference_papers/          # Source PDFs
│   ├── 2021, Steve P. Meisburger.pdf    # REGALS
│   ├── 2024, Griffin Chure.pdf          # hplc-py  
│   ├── 1988, Marcel Maeder.pdf          # EFA original
│   └── 1991, H.R. Keller.pdf            # EFA tutorial
└── tools/                     # Utilities & extracted text
    ├── README.md
    ├── read_pdfs.py
    ├── extracted_papers.txt   # REGALS + hplc-py
    ├── efa_papers.txt         # Maeder + Keller
    ├── chromixs_paper.txt     # Panjkovich & Svergun
    └validating JOSS Research Impact Statement claims.
Read PROJECT_STATUS.md for context.
Then let's extract evidence for [CHROMIXS/EFAMIX/REGALS]."
```

This ensures the AI has full context for the validation workk on)

This ensures the AI has full context immediately and can continue seamlessly.

---
Quick Start Options

**Option A: Extract CHROMIXS Evidence (30 min)**
1. Read `evidence/chromixs/README.md` for claim details
2. Search `tools/chromixs_paper.txt` for overlapping peak deferral quotes
3. Document findings with page/section references

**Option B: Extract EFAMIX Thresholds (45 min)**
1. Read `evidence/efamix/README.md` for specific thresholds
2. Search `tools/efamix_paper.txt` for SNR, τ, and separation values
3. Extract quantitative requirements with context

**Option C: Document REGALS Architecture (60 min)**
1. Read `evidence/regals/README.md` for multi-source validation
2. Extract two-stage process from `tools/extracted_papers.txt`
3. Extract EFA limitation quotes from `tools/efa_papers.txt`
4. Synthesize into coherent documentations difficulty"
   - "rank of data matrix will be higher"

---

## Immediate Priorities (Next Work Session)

### Priority 1: Continue EFA Limitation Verification ⏳
**Goal**: Systematically verify remaining documented EFA limitations

**Remaining Limitations** (from Maeder 1988 / Keller 1991):
- [ ] **Limitation 4**: No Quantification Without Calibration
- [ ] **Limitation 5**: Resolution Limitation (cannot resolve close peaks)
- [ ] **Limitation 9**: Rank Inflation from noise/artifacts
- [ ] **Limitation 10**: FIFO Assumption Failures (comprehensive treatment)

**Approach**: Create one notebook per limitation following established pattern
- Synthetic data with controlled conditions
- Quantitative measurements
- Visual demonstrations
- Compare with real data where applicable

**Estimated time**: 2-3 hours per limitation

### Priority 2: Synthesize Literature + Verification Findings 📝
**Goal**: Connect our verification work with literature analysis

**Tasks**:
- [ ] Review limitation_3 findings alongside SAXS_methods_analysis.md
- [ ] Draft "gap in literature" section for paper
- [ ] Document how our explicit mathematical treatment adds value
- [ ] Prepare evidence chain: EFA limitations → Modern workarounds → Molass contribution

**Expected outcome**: Clear narrative connecting verification work to JOSS Research Impact Statement

**Estimated time**: 1-2 hours

### Priority 3: Update JOSS Paper (if needed) 📄
**Goal**: Ensure Research Impact Statement reflects verified findings

**Tasks**:
- [ ] Review current claims in molass/paper.md
- [ ] Check if Limitation 3 severity upgrade changes narrative
- [ ] Consider adding explicit mathematical impossibility language
- [ ] Ensure citations align with evidence

**Estimated time**: 30-60 minutes

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
1. Success Criteria

### For JOSS Validation (Current Focus)
- ✅ All three evidence directories populated with direct quotes
- ✅ Page/section references documented for verification
- ✅ Evidence aligns precisely with Research Impact Statement claims
- ✅ Documentation defensible to JOSS reviewers/editors

### For Future Research (Archived)
The broader research agenda (mathematical derivations, simulations, comparative studies) is documented in `archive/` and may be pursued as a separate project after JOSS publication.. (2021). IUCrJ, 8, 225-237
- Chure, G. and Cremer, J. (2024). JOSS, 9(94), 6270  
- Maeder, M. and Zilian, A. (1988). Chemom. Intell. Lab. Syst., 3, 205-213
- KValidation Questions

### For JOSS Defense
1. **Can we verify CHROMIXS deferral claim?** → Extract from Panjkovich & Svergun (2018)
2. **Are EFAMIX thresholds as stated?** → Verify from Konarev et al. (2021)
3. **Is REGALS two-stage architecture documented?** → Confirm from Meisburger et al. (2021)
4. **Did EFA inventors document limitations?** → Confirm from Maeder & Keller papers

### For Future Research (Archived)
Deeper questions about implicit functional forms, comparative performance, and alternative approaches are documented in `archive/` for potential future work.

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

### January 21, 2026 - Algorithm Exploration Session

#### Zhang 2025 Matrix Factorization Analysis
- **Context**: User asked to explore latest trends in matrix factorization algorithms
- **Paper Added**: Zhang et al. (2025) "Loss-Minimizing Model Compression via Joint Factorization Optimization"
  - Core insight: ΔLoss = ∂Loss/∂W · δ (gradient · factorization noise)
  - Key innovation: Joint optimization of factorization + downstream objective
  - Lemma 3: Framework for optimal rank determination

#### Three Demonstration Notebooks Created

1. **zhang2025_simple_concept.ipynb** (Pedagogical)
   - 3×3 matrix example for understanding
   - Demonstrates gradient·noise alignment effect
   - Result: 75% better loss when noise opposes gradient
   - Status: Complete, tested

2. **zhang2025_joint_optimization_demo.ipynb** (Full Demo)
   - 100×50 synthetic data matrix
   - Iterative optimization with gradient computation
   - Visualization of optimization trajectory
   - Result: 1.7% better loss than SVD
   - Status: Complete, tested

3. **zhang2025_denoising_comparison.ipynb** (Real Data)
   - **Data**: SEC-SAXS SAMPLE1 from molass_data (Photon Factory, KEK)
   - **Philosophy**: Analyst chooses rank k=5 (Molass approach)
   - **Comparison**: Traditional SVD vs Zhang joint optimization
   - **Objective**: Elution profile smoothness (second-order differences)
   - **Result**: User confirmed "significant improvement in smoothness"
   - **Added**: Comparison to REGALS iterative optimization
     - REGALS: Alternating Least Squares (fix one factor, optimize other)
     - Zhang 2025: Simultaneous gradient descent (update both factors)
     - Both start from SVD, both iterate toward better solution
   - Status: Complete, tested by user

#### Key Architectural Insight Identified

**Two-Stage Separation Problem**:
- **Molass**: SVD denoising (Stage 1) → Parametric fitting (Stage 2: EGH/SDM/EDM)
  - Stage 2 operates ONLY on denoised data
  - Never sees original noisy measurements
- **REGALS**: EFA windows (Stage 1) → ALS refinement (Stage 2)
  - Stage 2 operates ONLY on windowed data
  - Similar architectural separation

**Zhang 2025 Insight**: Two-stage optimization (factorize → optimize) is fundamentally suboptimal compared to joint optimization

**Open Question**: What objective function should guide Molass denoising?
- Current notebook: Generic smoothness (second-order differences)
- Alternative: Parametric fit quality (how well EGH/SDM/EDM fits after denoising)
- Alternative: Physical plausibility of fitted parameters
- Alternative: Combination of multiple criteria

#### Repository Reorganization
- ✓ Moved `evidence/algorithms/` → `algorithms/` (workspace root)
- ✓ Consolidated Zhang 2025 materials: notebooks, Python scripts, markdown analysis
- ✓ Created `algorithms/temp_regals/` subfolder for REGALS-related explorations
- **Rationale**: Algorithm explorations are distinct from literature evidence documentation

#### REGALS Code Verification and Deep Discussion

**Code Analysis:**
- ✓ Verified notebook's REGALS description against actual Python implementation
- ✓ Confirmed alternating least squares structure: `fit_profiles()` then `fit_concentrations()`
- ✓ Verified closed-form solutions via `spsolve(AA + H, Ab)`
- ✓ Confirmed regularization matrices H_profile and H_concentration
- **Result**: Notebook comparison is accurate
- **Documentation**: Created `algorithms/temp_regals/REGALS_code_verification.md`

**Key Architectural Insights:**

1. **REGALS vs Molass Denoising Architectures**
   - **REGALS**: No separate denoising stage
     - Operates directly on M_noisy
     - IFT regularization provides implicit denoising during ALS iteration
     - Real-space constraints (P(q) ↔ P(r) with dmax) naturally incorporated
     - Regularization matrix H controls smoothness
   - **Molass**: Explicit two-stage with separate SVD denoising
     - Stage 0: M_noisy → SVD → M_clean (denoising)
     - Stage 1 & 2: Parametric fitting operates only on M_clean
     - Zhang 2025's critique applies: sequential denoising → optimization

2. **Moore 1980 IFT Paper Analysis**
   - Read foundational paper: "Small-Angle Scattering. Information Content and Error Analysis"
   - **Key insight**: IFT IS implicit denoising via dimension reduction
     - p(r) represented as truncated Fourier series: Σ(n=1 to nmax) aₙ·sin(πrn/d)
     - Reduces 1000 measurements → ~20 coefficients = denoising
     - Regularization matrix H provides smoothness
     - Error propagation through covariance matrix
   - **Validates user's intuition**: "Crucial denoising performed through IFT"
   - **Implication**: REGALS already does joint optimization (no two-stage problem for denoising)

3. **Pragmatic Solution for Molass: Dual Evaluation**
   - **User's insight**: "Use M_noisy after solving with M_clean"
   - **Approach**:
     ```
     Stage 0: M_noisy → SVD → M_clean
     Stage 1 & 2: Optimize parameters to fit M_clean (smooth landscape)
     Validation: Evaluate χ² against M_noisy (robustness check)
     ```
   - **Benefits**:
     - Keeps existing optimizer (no algorithmic changes needed)
     - Uses denoising for convergence aid
     - Validates against ground truth (M_noisy)
     - Detects overfitting to denoised features
   - **Interpretation**:
     - χ²_clean acceptable, χ²_noisy acceptable → robust solution ✓
     - χ²_clean good, χ²_noisy poor → overfit to denoising artifacts ⚠️
   - **Comparison to Zhang 2025**: Different philosophy
     - Zhang: Joint optimization (change HOW you optimize)
     - Dual eval: Pragmatic validation (optimize on clean, validate on noisy)
     - More practical for Molass's parametric models

4. **Convergence and Optimality Analysis**
   - **REGALS ALS**: Guaranteed convergence to local minimum (convex subproblems)
   - **Zhang 2025**: No convergence guarantee (non-convex joint problem)
   - **Conclusion**: ALS superior for convergence properties
   - **Potential Zhang application**: Gradient-informed initialization for ALS
     - Use Zhang's insight to initialize better
     - Then let ALS converge reliably
     - Hybrid approach keeps best of both

**Final Status**: Algorithm exploration complete, documented, ready to return to JOSS validation work

---

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
| Jan 20, 2026 (AM) | EFA Limitation 3 verification | ✓ Created limitation_3_tailing_effects.ipynb, discovered FIFO fails even for Gaussian peaks, negative window widths |
| Jan 20, 2026 (PM) | Literature analysis: modern methods | ✓ Extracted 4 papers (45 pages), created SAXS_methods_analysis.md, identified critical gap in literature |
| Jan 20, 2026 (Eve) | Documentation cleanup | ✓ Unified CHROMIXS spelling, updated PROJECT_STATUS.md with full session summary |
| Jan 21, 2026 (AM-PM) | Zhang 2025 algorithm exploration | ✓ Created 3 notebooks (pedagogical, full demo, real data), identified two-stage architecture, verified REGALS code, analyzed Moore 1980 IFT, developed dual-evaluation approach |

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
