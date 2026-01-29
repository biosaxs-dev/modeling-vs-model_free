# Project Status & Quick Start
**Last Updated**: January 29, 2026

---

## 🎯 What This Repository Is

Research repository investigating the fundamental behavior of SEC-SAXS decomposition methods through mathematical analysis, computational experiments, and literature review.

**Mission**: To contribute to the SEC-SAXS community's understanding of when and why different matrix factorization approaches succeed or fail, revealing the implicit modeling choices in "model-free" methods and how explicit parametric approaches address these challenges.

**Origin**: This work began as supporting evidence for the Molass Library JOSS paper ([#9424](https://github.com/openjournals/joss-reviews/issues/9424)), but evolved into broader research contributions relevant to the entire SEC-SAXS community.

---

## 🚀 Quick Session Initialization

**For AI assistants**: When user says **"Initialize: modeling-vs-model_free context"**

### Read These Core Documents
1. **README.md** - Repository purpose
2. **PROJECT_STATUS.md** (this file) - Current focus
3. **NOTATION_CONVENTION.md** - Matrix factorization notation ($M = PC$)
4. **R_CENTRIC_FRAMEWORK.md** - Analytical framework
5. **explorations/README.md** - Mathematical foundations overview
6. **explorations/orthogonal_invariance_overview.md** ⭐ - Research journey summary (START HERE for context)
7. **explorations/orthogonal_invariance_journey.md** - Full technical details (9 stages)

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

## 🎯 Latest Breakthroughs

### January 29, 2026: Notation Accessibility for Broader Audience

**Motivation**: While $M = PC$ notation is standard and convenient, it can mislead readers unfamiliar with matrix factorization optimization into thinking it represents exact equality rather than an approximation problem.

**Key Improvements**:

**1. NOTATION_CONVENTION.md Enhanced** (Authoritative Reference):
- **Clarified scope**: "Throughout this repository, $M = PC$ and related equalities...are **presented as simple equalities for brevity and accessibility**, but they represent **optimization problems**"
- **Full objective documented**: Methods minimize $\|M - PC\|^2 + \text{regularization terms}$ (smoothness, non-negativity, etc.)
- **Low-rank approximation emphasized**: P and C have much smaller inner dimension (2-3 components) compared to M's full dimensions (hundreds of q-values × frames)
- **Four key implications listed**: Why multiple solutions, initialization strategies, optimization failures, and explicit constraints matter
- **Pedagogical framing**: Explains the notation choice is intentional for accessibility while warning about technical reality

**2. orthogonal_invariance_overview.md Updated**:
- **Single comprehensive note** after first $M = PC$ appearance: "Throughout this document, $M = PC$ and related equalities represent optimization problems...rather than exact equalities. This is implicit in the discussion but important for understanding the practical context."
- **Broader scope**: Covers subsequent transformations like $M = (PR)(R^{-1}C)$ implicitly

**3. molass/paper.md Clarified** (JOSS Submission):
- **After equation (1)**: "Roughly speaking, in practice methods find P and C that minimize $\|M - PC\|^2$ (plus regularization terms) rather than achieving exact equality"
- **"Roughly speaking" qualifier**: Acknowledges full objective includes smoothness, non-negativity, compact support beyond just data fit

**Why This Matters**:
- **Accessibility preserved**: Simple $M = PC$ notation remains for readability
- **Accuracy ensured**: Warnings prevent misunderstanding for general researchers
- **Proper reference hierarchy**: NOTATION_CONVENTION.md is comprehensive, other docs point there for details
- **Community contribution**: Non-specialists (experimental SAXS users, method evaluators) can now understand the approximation framework without getting lost in optimization details

**Philosophy**: Balance "easiness for broader audience" with technical accuracy through strategic warnings rather than cluttering all discussions with full optimization formalism.

**Status**: ✅ Complete - Notation now accessible to general SEC-SAXS community while maintaining technical precision for specialists

---

### January 28, 2026 (Late Evening): Documentation Structure & Notation Standardization

**Major Repository Improvements**: Comprehensive reorganization and standardization for clarity and pedagogical accessibility.

**1. Notation Convention Standardized**:
- **Unified notation**: All documentation now uses $M = PC$ (matches JOSS paper)
- **Previous inconsistency**: Some docs used $M = CP^T$ (transpose convention)
- **New reference**: [NOTATION_CONVENTION.md](NOTATION_CONVENTION.md) created
  - Explains why $M = PC$ is preferred (standard NMF convention, cleaner math)
  - Documents matrix dimensions and physical interpretations
  - $P$ = scattering curves (q-values × components, columns = spectra)
  - $C$ = elution curves (components × frames, rows = time series)
  - Solution: $P = M \cdot C^{+}$ (direct pseudoinverse)

**2. Pedagogical Structure Created**:
- **New**: [orthogonal_invariance_overview.md](explorations/orthogonal_invariance_overview.md)
  - Executive summary table of all 9 stages
  - Narrative summaries without heavy math (~15 min read)
  - Clear JOSS validation takeaways
  - Navigation guide for different reader levels
  - Context restoration for AI/future sessions
- **Enhanced**: [matrix_transformations_tutorial.ipynb](explorations/matrix_transformations_tutorial.ipynb)
  - Added notation notice linking to NOTATION_CONVENTION.md
  - New "Further Reading" section with cross-references
  - New "Quick Reference" section (concepts, formulas, constraint hierarchy)
  - Clear connections: Tutorial parts → Journey stages
- **Updated**: [orthogonal_invariance_journey.md](explorations/orthogonal_invariance_journey.md)
  - Added navigation section at top
  - Links to overview for quick start
  - Guidance on when to read which document

**3. Terminology Precision**:
- **Renamed**: `degeneracy_scope_diagnostic.ipynb` → `multiple_minima_diagnostic.ipynb`
- **Updated throughout**: "Fundamental Limitation Theorem" → "Multiple Minima Conjecture"
  - Acknowledges lack of formal proof (scientific precision)
  - Broader scope: degeneracy, permutation, shift failures (not just degeneracy)
- **All references updated**: PROJECT_STATUS.md, journey.md, overview.md, README.md

**Learning Paths Now Clear**:
```
Level 1: New to orthogonal matrices
   └─→ matrix_transformations_tutorial.ipynb (visual 2D examples)

Level 2: Understand basics, want big picture
   └─→ orthogonal_invariance_overview.md (executive summary)

Level 3: Need full technical details
   └─→ orthogonal_invariance_journey.md (9 stages, proofs)

Reference: Need formulas/notation
   └─→ NOTATION_CONVENTION.md + Tutorial Quick Reference
```

**Why This Matters**:
- **Accessibility**: Different entry points for different expertise levels
- **Consistency**: Single notation convention eliminates confusion
- **Future-proof**: Context restoration guides help AI assistants
- **JOSS ready**: Clear narrative from limitations to Molass solution

**Files Created**:
- `NOTATION_CONVENTION.md` - Standard reference for $M = PC$ convention
- `explorations/orthogonal_invariance_overview.md` - Pedagogical entry point

**Files Enhanced**:
- `matrix_transformations_tutorial.ipynb` - Cross-references + Quick Reference
- `orthogonal_invariance_journey.md` - Navigation section
- `PROJECT_STATUS.md` - References NOTATION_CONVENTION.md

**Status**: ✅ Complete - Repository now has clear structure from beginner to expert

---

### January 28, 2026 (Evening): Stage 8 - Incompatibility Discovery in 3D Design Space

**Critical Negative Result**: Log-additive + frequency Q = **0% success** (incompatible!)

**Research Question**: Does Stage 5's frequency Q breakthrough work with Stage 7's log-additive winner?
- Hypothesis: >50% success (best of both worlds)
- Reality: **0%** - WORSE than log-additive + generic Q (25%)

**Created**: [log_additive_frequency_Q_test.ipynb](explorations/log_additive_frequency_Q_test.ipynb) (Stage 8 first experiment)
- Tests exact frequency Q from Stage 5 with log-additive objective
- 20-trial multi-start, same correlated profiles setup
- Complete failure: all trials stuck at identical poor local minimum

**Three-Dimensional Design Space**:
| Configuration | Success Rate | Finding |
|--------------|--------------|---------|
| Additive + frequency Q | 90% | ✓ Stage 5 breakthrough |
| Log-additive + generic Q | 25% | ✓ Stage 7 winner |
| **Log-additive + frequency Q** | **0%** | ❌ **INCOMPATIBLE** |

**Why This Matters**:

1. **The design space has structure** - not all combinations work:
   - Operator choice (Stage 6-7): Additive vs Log-additive vs Multiplicative
   - Q form (Stage 4): Fixed form theorem $S(C) = \text{tr}(CQC^T)$
   - Q design (Stage 5): Generic vs Frequency vs Spatial vs Ridge
   - **These three dimensions interact** - some combinations incompatible!

2. **Destructive interference mechanism**:
   - Frequency Q designed for linear penalty: $S(C) = \text{tr}(CQC^T)$
   - Log-additive uses logarithmic: $\log(\text{tr}(CQC^T))$
   - Gradient becomes: $\nabla_C = \frac{\lambda}{\text{tr}(CQC^T)} \cdot 2CQ$ (adaptive inverse scaling)
   - Adaptive scaling conflicts with frequency-domain structure Q tries to enforce
   - Result: 0% (worse than 25%) indicates active interference, not just incompatibility

3. **Stage 5's breakthrough is operator-specific, not universal**:
   - Frequency Q worked for **additive** operator (90%)
   - Does NOT work for **log-additive** operator (0%)
   - Need operator-specific Q design principles

**Profound Implications**:

1. **Hidden compatibility constraints**: Even "model-free" choices must respect structural compatibility between operator and regularizer design
2. **Cannot mix-and-match arbitrarily**: Success requires understanding interaction between operator gradient structure and Q geometry
3. **Stages 4-5 need re-examination**: Fixed form theorem and Q design may need adaptation for each operator type

**Open Questions**:
- Why 0% (destructive) rather than 25% (neutral)? What mechanism causes active interference?
- Can frequency Q be adapted for log-space? Or fundamentally incompatible?
- What Q designs ARE compatible with log-additive's adaptive gradients?
- Does fixed form theorem need modification? $S(C) = \text{tr}(CQC^T)$ vs $\text{tr}(\log(C) Q \log(C)^T)$?

**Status**: Critical negative result documented, mechanism investigation needed

**Updated**: [orthogonal_invariance_journey.md](explorations/orthogonal_invariance_journey.md) v1.6 with Stage 8 experimental results  
**New**: [orthogonal_invariance_overview.md](explorations/orthogonal_invariance_overview.md) - Pedagogical entry point

---

### January 28, 2026 (Late Evening): Stage 8 Diagnostic - Multiple Minima Conjecture Refined

**Critical Discovery**: The Multiple Minima Conjecture (Stage 5) is NOT about degenerate solutions being better—it's about a **complex landscape with many local minima of similar quality**!

**Research Question**: Is the conjecture about objective structure (all optimizers affected) or optimization method (ALS-specific)?

**Created**: [multiple_minima_diagnostic.ipynb](explorations/multiple_minima_diagnostic.ipynb)
- Tests whether degenerate solution has LOWER objective value
- Compares Basin-hopping (global optimizer) vs ALS baselines
- Uses realistic SEC-SAXS setup (Guinier-Porod profiles, r≈0.88)
- Tests both additive and log-additive objectives

**Key Findings**:

1. **Hypothesis Test: Degenerate vs True Solution Objectives**
   ```
   Additive:     True = 0.40 << Degenerate = 40.01 (99× better!)
   Log-additive: True = -1.28 < Degenerate = 3.10 (4.4 units better)
   ```
   **→ TRUE solution IS the global optimum, NOT degenerate**

2. **Basin-hopping Results** (Surprising!):
   - Additive + Basin-hopping: **0%** (vs ALS baseline: 35%) ❌
   - Log-additive + Basin-hopping: **0%** (vs ALS baseline: 25%) ❌
   **→ Global optimization performs WORSE than ALS**

3. **Resolution: Multiple Different Local Minima**
   - ALS finds: Degenerate solutions (one flat, one bimodal)
   - Basin-hopping finds: Permuted/shifted solutions (wrong structure)
   - Both types: Similar objectives (0.40-0.44), high error (0.9-1.5)
   **→ The landscape has MANY comparable minima, not just degenerate**

**Refined Understanding of Multiple Minima Conjecture**:

**Original interpretation** (Stage 5): "Fixed Q can't prevent degeneracy because degenerate solution is better"

**Refined understanding** (Diagnostic): "Fixed Q creates complex landscapes with multiple local minima:"
- True solution: obj ≈ 0.40 (global optimum) ✓
- Permuted/shifted: obj ≈ 0.40-0.44 (comparable) ← Basin-hopping finds these
- Degenerate: obj ≈ 40 (much worse) ← ALS sometimes gets trapped

**Critical Insights**:

1. **The problem is MORE subtle than degeneracy**
   - Not "degenerate is better" but "many minima of similar quality"
   - ALS's constrained alternation sometimes helps (35%, 25%)
   - Basin-hopping's freedom can hurt—explores wrong basins (0%)

2. **Conjecture applies broadly to all optimizers**
   - Both ALS and Basin-hopping fail (different failure modes)
   - Neither the degeneracy-specific nor just ALS-specific
   - Fundamental property of objective landscape structure

3. **Validates Molass's explicit constraints approach**
   - Even with: correct global optimum + global optimizer + log-additive
   - Still fails without explicit constraints (0%)
   - Molass's Rg-consistency and parametric models address this
   - **For JOSS**: Conjecture validates why explicit modeling is necessary

**Updated Conjecture Statement**:
> For SEC-SAXS with correlated profiles, objective functions using only fixed quadratic smoothness regularization create optimization landscapes with **multiple local minima (degenerate, permuted, shifted solutions) of comparable objective value**, preventing reliable component recovery regardless of optimization method (ALS or global). This limitation necessitates additional physical constraints for reliable decomposition.

**Implications for JOSS**:
- Objective structure alone insufficient (even when true solution is global optimum)
- Global optimization doesn't automatically solve it (Basin-hopping: 0%)
- Molass's explicit constraints (Rg-consistency, parametric models) address the **multiple minima problem**
- Strongly supports claim that explicit modeling addresses "model-free" limitations

**Status**: Diagnostic complete, conjecture refined, terminology updated throughout repository

---

### January 28, 2026 (Morning): The λ-Placement Paradox - Where Regularization Weight Enters Matters!

**Profound Discovery**: Mathematical equivalence ≠ practical equivalence when λ placement differs between formulations!

**Research Question**: Are Stages 1-5 findings (invariance, degeneracy) operator-specific or fundamental?

**Created**: [objective_operators_invariance_exploration.ipynb](explorations/objective_operators_invariance_exploration.ipynb) (Stage 7)
- 19 cells, 8 major sections, complete multi-start experiments
- Tests 4 operators: Additive (+), Multiplicative (×), Log-additive (log), Max
- 20 trials per operator on correlated profiles (r≈0.88, degeneracy-prone)

**Key Findings**:

1. **Orthogonal Invariance** ✓
   - ALL operators preserve invariance (σ < 10⁻¹⁰)
   - Stages 1-2 mathematical elegance holds universally
   - Reason: f(A,B) preserved for any function f when A and B individually preserved

2. **Degeneracy Behavior** (Multi-Start Experiment, λ=0.1):
   - Additive: **0%** success (worse than Stage 5's 35%!)
   - Multiplicative: **0%** success (balance enforcement FAILED)
   - **Log-additive: 25% success** (CLEAR WINNER) ✓
   - Max: **0%** success (worst-case logic no help)
   - Zero degeneracy across all operators (ALS with L-BFGS-B more stable)

3. **The λ-Placement Paradox** ⚠️ (Critical Mathematical Discovery):
   - While $\min(A \times B) \equiv \min(\log A + \log B)$ mathematically...
   - **Multiplicative**: Implements $A \times \lambda B$ (linear scaling)
   - **Log-additive**: Implements $\log A + \lambda \log B = \log(A \times B^\lambda)$ (power scaling)
   - With λ=0.1 and B=100:
     - Multiplicative: $0.1 \times 100 = 10.0$ (strong penalty)
     - Log-additive: $100^{0.1} = 1.585$ (weak penalty, **6.3× difference**)

4. **Adaptive Gradient Structure Explains Everything**:
   - Multiplicative: $\frac{\partial f}{\partial B} = \lambda A$ (constant, traps in poor minima)
   - Log-additive: $\frac{\partial f}{\partial B} = \frac{\lambda}{B}$ (adaptive inverse scaling)
   - When B large (poor smoothness): Log-additive weakens penalty, allows data-fit focus
   - When B small (good smoothness): Log-additive strengthens penalty, maintains smoothness
   - **This adaptive behavior creates more navigable optimization landscape**

**Profound Implications**:

1. **Hidden modeling choices go deeper than thought**:
   - Not just which regularizer (D² vs D¹)
   - Not just weighting (λ value)
   - Not just combination operator (+ vs ×)
   - **But WHERE λ enters the formula** (linear vs power scaling)

2. **Mathematical equivalence ≠ practical equivalence**:
   - Two formulations mathematically identical (log transforms)
   - BUT different λ placements create vastly different optimization dynamics
   - Success rate: 25% vs 0% (practical difference is massive)

3. **"Model-free" contains cascade of implicit choices**:
   - Stage 6: WHETHER to combine objectives (+ vs separate)
   - Stage 7: HOW to combine (operator choice)
   - **NEW**: HOW λ enters (scaling structure)
   - Each creates different optimization landscape with measurable reliability impact

**Answer to Meta-Question**: Problems are **operator-dependent through gradient structure**, but subtly. The critical factor is adaptive gradient scaling ($1/B$) vs constant/coupled gradients, not just term coupling alone.

**Status**: Complete with surprising discoveries that reveal deep connection between mathematical formulation and optimization behavior

**Updated**: [orthogonal_invariance_journey.md](explorations/orthogonal_invariance_journey.md) now includes Stage 7 with flow diagram showing progression from Stage 6

---

### January 27, 2026 (Evening): Objective Function Combination Rules - Fundamental Modeling Choice

**New Discovery**: The mathematical operator combining terms (+, ×, log) is itself a modeling decision that determines optimization dynamics through gradient structure!

**Key Insight**: Before even choosing WHAT to regularize, methods must choose HOW to combine terms:
- **Addition (+)**: "OR"-like behavior - allows trade-offs between constraints (∂/∂A = 1, independent gradients)
- **Multiplication (×)**: "AND"-like enforcement - forces balance between constraints (∂/∂A = B, coupled gradients)
- **Log-additive**: Also "AND"-like (multiplicative in original space)
- **Max**: Strongest "AND" enforcement - only worst violation matters

**Created**: [objective_combination_rules_exploration.ipynb](explorations/objective_combination_rules_exploration.ipynb)
- 8-part systematic exploration (18 cells including gradient analysis, complete)
- Tests 5 different combination rules on same solutions
- Demonstrates gradient-based trade-off vs balance enforcement explicitly
- Visualizes trade-off surfaces showing different optimization landscapes
- **Critical correction**: Uses gradient analysis (not naive interpretation) to classify operators

**Critical Finding**: Same solution scores VASTLY differently under different operators (range: $10^{-28}$ to $0.31$). For extreme cases:
- Additive prefers balanced solutions (score = 2.0) - but gradients allow trading
- Multiplicative global extremes exist (score = $2 \times 10^{-8}$) - but gradients enforce balance

**Paper Argument Enhanced**: Reveals modeling assumptions at the MOST FUNDAMENTAL level:
1. Not just "which regularizer" (D² vs D¹)
2. Not just "how to weight" (λ value)
3. But "how constraints interact" (gradient structure determines optimization dynamics)
4. **REGALS's additive form allows marginal trade-offs - implicit modeling of constraint interaction**

**Status**: Complete exploration ready for future investigation of how alternative forms change solution landscape and method behavior

**Updated**: [underdeterminedness_exploration.ipynb](explorations/underdeterminedness_exploration.ipynb) Level 2 now explicitly discusses operator choice with correct gradient-based analysis

---

### January 27, 2026 (Afternoon): Problem-Informed Q-Matrix Design SUCCESS ✓✓

**Major Discovery**: Frequency-domain band-pass filtering achieves 90% reliability while maintaining orthogonal invariance!

**Results from problem_informed_Q_design.ipynb**:
- **Baseline** (standard smoothness): 35% success
- **Spatial weighting**: 75% success (γ=0.5)
- **Frequency filtering**: **90% success** (cutoffs 0.05, 0.7) ✓✓
- **Combined spatial+ridge**: 85% success (γ=0.5, ε=0.01) ✓✓

**Key Insight**: Problem-class knowledge (expected peak widths) can be incorporated into fixed Q-matrix design to prevent degeneracy without breaking invariance. The fundamental limitation from Part 11D was due to **generic** ridge, not inherent impossibility.

**Implications**:
1. Trade-off (invariance ↔ effectiveness) CAN be resolved
2. New research direction: Problem-specific Q-matrix design principles
3. Frequency domain outperforms spatial domain for SEC-SAXS
4. Answers Open Research Question #3 with definitive YES

---

### January 26, 2026: From Understanding Discrete Ambiguity → Questioning Selection Reliability

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
├── NOTATION_CONVENTION.md     # 🔑 Matrix factorization notation (M = PC)
├── SESSION_HISTORY.md         # Detailed development log
├── R_CENTRIC_FRAMEWORK.md     # 🔑 Analytical framework
│
├── evidence/                  # 📖 LITERATURE EVIDENCE (in progress)
│   ├── chromixs/              # ⏳ CHROMIXS documented limitations
│   ├── efamix/                # ⏳ EFAMIX quantified thresholds
│   ├── regals/                # ⏳ REGALS architecture and dependencies
│   └── efa_original/          # EFA limitation verifications (1-4 complete)
│
├── explorations/              # 📚 MATHEMATICAL FOUNDATIONS (complete)
│   ├── matrix_transformations_tutorial.ipynb          # 🔑 Visual guide (updated with cross-refs)
│   ├── discrete_ambiguity_demonstration.ipynb         # 🔑 Group theory visualization
│   ├── smoothness_orthogonal_invariance_proof.ipynb   # 🔑 D^k invariance proof
│   ├── underdeterminedness_exploration.ipynb          # Constraint hierarchy
│   ├── permutation_ambiguity_examples.ipynb           # Discrete ambiguity risk
│   ├── objective_combination_rules_exploration.ipynb  # Stage 6: Operator choice (AND vs OR)
│   ├── objective_operators_invariance_exploration.ipynb # Stage 7: λ-placement paradox ✓
│   ├── log_additive_frequency_Q_test.ipynb            # Stage 8: Incompatibility discovery
│   ├── multiple_minima_diagnostic.ipynb               # Stage 9: Conjecture refinement ✓
│   ├── orthogonal_invariance_overview.md              # ⭐ Research summary (START HERE)
│   ├── orthogonal_invariance_journey.md               # 🔬 Full technical narrative (9 stages)
│   ├── operator_logic_clarification.md                # Canonical reference (AND/OR confusion)
│   ├── permutation_reliability_pilot.ipynb            # Selection problem study
│   ├── problem_informed_Q_design.ipynb                # 90% success with frequency filtering ✓✓
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

### Documentation Structure ✓
**January 28, 2026**: Notation standardization and pedagogical structure
- ✓ NOTATION_CONVENTION.md - Standard $M = PC$ reference
- ✓ orthogonal_invariance_overview.md - Pedagogical entry point with executive summary
- ✓ matrix_transformations_tutorial.ipynb - Enhanced with cross-references and quick reference
- ✓ All docs updated to consistent notation (matches JOSS paper)
- ✓ Clear learning paths: Beginner → Overview → Deep dive

**January 29, 2026**: Notation accessibility for broader audience
- ✓ NOTATION_CONVENTION.md - Enhanced with optimization framework explanation, low-rank approximation emphasis, practical implications
- ✓ orthogonal_invariance_overview.md - Added comprehensive note covering all equalities throughout document
- ✓ molass/paper.md - Clarified M=PC represents optimization with regularization terms
- ✓ Philosophy established: Balance brevity/accessibility with technical accuracy through strategic warnings

### Research Journey (9 Stages Complete) ✓
- ✓ Stage 1-2: Discovery and proof of orthogonal invariance
- ✓ Stage 3-5: Multiple Minima Conjecture formulated
- ✓ Stage 6-7: Operator choice investigation (log-additive 25% winner)
- ✓ Stage 8: 3D framework with incompatibility discovery
- ✓ Stage 9: Conjecture refined (applies to all optimizers)

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

### Priority 1: Complete Literature Evidence Documentation

**CHROMIXS** (30 min):
- Extract quotes showing documented limitations for overlapping peaks
- Source: `tools/chromixs_paper.txt`
- Target: `evidence/chromixs/`

**EFAMIX** (45 min):
- Document quantified failure thresholds (SNR, τ, separation)
- Source: `tools/efamix_paper.txt`
- Target: `evidence/efamix/`

**REGALS** (60 min):
- Document two-stage architecture and EFA dependencies
- Extract limitation quotes from inventors
- Sources: `tools/extracted_papers.txt` + `tools/efa_papers.txt`
- Target: `evidence/regals/`

### Priority 2: Synthesis and Dissemination
- Consider preprint/manuscript preparation (bioRxiv/arXiv)
- Update repository documentation for broader accessibility
- Synthesize findings for JOSS review response

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

### Core Documentation (Start Here)
- **NOTATION_CONVENTION.md** 🔑 - Standard $M = PC$ convention explained
- **explorations/orthogonal_invariance_overview.md** ⭐ - Research journey summary (9 stages, RECOMMENDED START)
- **explorations/matrix_transformations_tutorial.ipynb** 📚 - Visual guide for beginners (updated with cross-refs)
- **explorations/orthogonal_invariance_journey.md** 🔬 - Full technical narrative with proofs and experiments

### Session & Development History
- **SESSION_HISTORY.md** - Detailed development log (session-by-session)
- **explorations/README.md** - Complete overview of mathematical notebooks

### Research Notebooks (Stages 6-9)
- **explorations/objective_combination_rules_exploration.ipynb** ✓ (Stage 6) - Operator choice (AND vs OR logic) affects optimization dynamics
- **explorations/objective_operators_invariance_exploration.ipynb** ✓ (Stage 7) - **λ-placement paradox**: Log-additive achieves 25% success via adaptive gradient scaling
- **explorations/log_additive_frequency_Q_test.ipynb** ✓ (Stage 8) - **INCOMPATIBILITY**: Log-additive + frequency Q = 0%
- **explorations/multiple_minima_diagnostic.ipynb** ✓ (Stage 9) - Conjecture refined: applies to all optimizers

### Key Breakthroughs
- **explorations/problem_informed_Q_design.ipynb** ✓✓ - **BREAKTHROUGH**: Frequency-domain Q achieves 90% reliability while maintaining invariance (resolves Open Research Question #3)
- **explorations/operator_logic_clarification.md** - Canonical reference for gradient-based operator analysis

### Repository Organization
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
