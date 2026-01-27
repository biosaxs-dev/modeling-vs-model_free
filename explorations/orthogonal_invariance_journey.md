# The Orthogonal Invariance Journey

**Purpose**: Map the conceptual flow from discovery → proof → applicability → experimental testing  
**Created**: January 27, 2026  
**Status**: Active research with decision points for future reconsideration

---

## 🗺️ The Grand Context: Flow of Discoveries

```
   Discovery              Formalization            Practical Test            Deep Question
   (Jan 17)              (Jan 22)                 (Jan 26)                  (Jan 27)
       │                     │                        │                         │
       ▼                     ▼                        ▼                         ▼
underdetermin...  →  smoothness_orthog... → permutation_reliab... → Can invariance +
exploration.ipynb    onal_invariance_      pilot.ipynb               effectiveness
                     proof.ipynb                                      coexist?
                                                                           │
     Smoothness           Proven for all        0% success with            ▼
     preserves            D^k operators         standard smoothness   Ridge test:
     orthogonal           (11 parts)           (empirical surprise)   Parts 11B-11D
     transforms                                                       
     (conjecture)         Added Part 11:        Hybrid solution       Result: No -
                         Practical caveat      (100% success)        fundamental
                         (degeneracy)                                limitation
```

---

## 📍 Stage 1: Discovery (underdeterminedness_exploration.ipynb)

**Location**: Lines 231-249 (Part 2: Mathematical Insight section)  
**Date**: January 17, 2026  
**Status**: ✅ Complete - Foundation established

### What Was Discovered

**The Conjecture**: For smoothness regularization $\lambda\|D^2C\|^2$, if we transform via orthogonal matrix $B$:
$$\|D^2(B^{-1}C)\|_F^2 = \|B^{-1}(D^2C)\|_F^2 = \|D^2C\|_F^2$$

**Key Insight**: Orthogonal transformations preserve the smoothness penalty!

### Mathematical Implications

**Ambiguity Reduction**:
- Level 1 (data-fit only): Full basis ambiguity - any invertible $R \in GL(n)$ works
- Level 2 (+ smoothness): Reduced to orthogonal transformations $B \in O(n)$
- Degrees of freedom: $n^2$ → $\frac{n(n-1)}{2}$

**Why This Matters**:
- Explains why smoothness alone is insufficient for uniqueness
- Shows that REGALS needs **multiple constraint layers**
- Sets up the question: What eliminates the remaining $O(n)$ freedom?

### Files & Evidence

- **Notebook**: [underdeterminedness_exploration.ipynb](underdeterminedness_exploration.ipynb)
  - Part 2, cells starting "Does Regularization Break the Basis Ambiguity?"
  - Lines 344-404: Numerical validation
  - 5 orthogonal transformations tested
  - Result: **All give identical objectives** (std dev ≈ 0)

### Decision Points for Future

❓ **Could test other regularization forms**: $\|D^1C\|^2$, $\|D^3C\|^2$, mixed penalties?  
❓ **Could explore non-quadratic penalties**: How does $L^1$ sparsity affect invariance?

---

## 📍 Stage 2: Rigorous Proof (smoothness_orthogonal_invariance_proof.ipynb)

**Location**: Parts 1-10  
**Date**: January 22, 2026  
**Status**: ✅ Complete - Mathematical foundation proven

### What Was Proven

**Main Theorem**: For any differential operator $D^k$ (not just $D^2$):
$$\|D^kC\|_F^2 \text{ is invariant under orthogonal transformations } R \in O(n)$$

**Generalization Discovery**: The proof works for:
- First derivative: $\|D^1C\|^2$
- Second derivative: $\|D^2C\|^2$ (REGALS uses this)
- Third derivative: $\|D^3C\|^2$
- Any $k$-th derivative: $\|D^kC\|^2$
- Linear combinations: $\alpha\|D^2C\|^2 + \beta\|D^1C\|^2$

### Why $D^2$ Specifically?

**Not unique invariance** - all $D^k$ have this property!

**Selection rationale** (from Part 8):
- $D^1$: Too weak (penalizes slopes, not curvature)
- $D^2$: "Sweet spot" (penalizes wiggles, allows smooth trends)
- $D^3$, $D^4$: Too strong (over-smoothing, physics violations)

Choice is about **regularization quality**, not mathematical uniqueness.

### Numerical Validation

**Method**: 1000-trial Monte Carlo
- Random matrices $R \in O(n)$
- Random concentration profiles $C$
- Test: $|\|D^kRC\| - \|D^kC\|| < 10^{-10}$

**Result**: ✅ All 1000 trials pass at machine precision

### Files & Evidence

- **Notebook**: [smoothness_orthogonal_invariance_proof.ipynb](smoothness_orthogonal_invariance_proof.ipynb)
  - Parts 1-2: Setup and definitions
  - Parts 3-7: Proof for $D^2$, generalization to $D^k$
  - Part 8: Discussion of why $D^2$ chosen
  - Parts 9-10: Numerical validation (1000 trials)

### Decision Points for Future

❓ **Could formalize necessary/sufficient conditions**: What class of operators has this property?  
❓ **Could explore weighted norms**: Does $\|WD^2C\|^2$ preserve invariance for diagonal $W$?

---

## 📍 Stage 3: Practical Caveat (smoothness_orthogonal_invariance_proof.ipynb, Part 11)

**Location**: Part 11: "Critical Limitation Despite Mathematical Elegance"  
**Date**: January 27, 2026  
**Status**: ✅ Complete - Empirical reality documented

### The Paradox

**Mathematical elegance** (Parts 1-10): Reduces ambiguity to $O(n)$  
**Empirical reality** (pilot study): 0% success rate with standard smoothness

**The Problem**: Orthogonal invariance doesn't prevent **degeneracy**

### Degeneracy Mechanism

**What happens with correlated SAXS profiles** (r = 0.88):

1. **Component 1**: Becomes bimodal (covers both peaks)
   - High curvature: $\|D^2c_1\|^2 = 0.0025$
   - But captures all signal

2. **Component 2**: Becomes flat (vanishes)
   - Zero curvature: $\|D^2c_2\|^2 \approx 0$ (perfect smoothness!)
   - Contributes nothing

3. **Total smoothness**: $0.0025 + 0 = 0.0025$
   - **Lower** than correct solution with two moderate peaks!

**Why smoothness allows this**:
- Sum structure: $\sum_i \|D^2c_i\|^2$ allows one component to vanish
- Flat profile has zero penalty (maximally smooth)
- One complex + one flat < Two moderate

### Empirical Evidence

**From pilot study** ([permutation_reliability_pilot.ipynb](permutation_reliability_pilot.ipynb)):
- Standard smoothness: **0/10 correct** (0%)
- Hybrid (profile-weighted + min-amplitude): **10/10 correct** (100%)

**Conclusion**: Mathematical elegance ≠ Practical effectiveness

### Files & Evidence

- **Part 11 content**: ~200 lines
  - Concrete example (bimodal + flat)
  - Empirical table (0% vs 100%)
  - Mathematical mechanism explanation
  - Practical solutions discussion

### Decision Points for Future

❓ **Could characterize degeneracy conditions**: When does correlation cause failure?  
❓ **Could test profile-weighted smoothness**: Does it break invariance but prevent degeneracy?

---

## 📍 Stage 4: Generalization Theory (Part 11A)

**Location**: Part 11A: "What Smoothness Definitions Have Orthogonal Invariance?"  
**Date**: January 27, 2026  
**Status**: ✅ Complete - General theorem established

### The General Theorem

**Form**: $S(C) = \text{tr}(CQC^T)$ with **fixed** $Q$ matrix

**Theorem**: This form is **necessary and sufficient** for orthogonal invariance.

### Examples That Work (Fixed Q)

✅ **Differential operators**: $Q = (D^k)^T D^k$ for any $k$  
✅ **Linear combinations**: $Q = \alpha(D^2)^T D^2 + \beta(D^1)^T D^1$  
✅ **Spatial weighting**: $Q = (D^2)^T W D^2$ with fixed diagonal $W$  
✅ **Ridge regularization**: $Q = (D^2)^T D^2 + \epsilon I$ ⭐  
✅ **General quadratic**: $Q = L^T L$ for any fixed $L$

### Examples That Don't Work (Q Not Fixed)

❌ **Profile-weighted**: $Q_i = \|p_i\|^2 (D^2)^T D^2$ (weights depend on P)  
❌ **Min-amplitude**: $\sum_i 1/\max(c_i)$ (not quadratic form)  
❌ **Adaptive smoothness**: $Q(C)$ that changes with solution  
❌ **L1 sparsity**: $\sum_i \|c_i\|_1$ (not quadratic)

### The Trade-off Identified

```
Orthogonal Invariance ←→ Degeneracy Prevention
   (Fixed Q matrix)     ║    (Context-dependent)
                        ║
         Can't have both with fixed Q!
```

### Files & Evidence

- **Part 11A content**: ~150 lines
  - General theorem statement and proof
  - 10 examples (5 valid, 5 invalid)
  - Trade-off diagram and discussion
  - Research directions

### Decision Points for Future

❓ **Could prove uniqueness conditions**: Under what conditions does fixed $Q$ + non-negativity guarantee unique solution?  
❓ **Could design optimal Q**: What choice of $Q$ minimizes degeneracy risk?  
⭐ **Ridge as candidate**: Does $Q = (D^2)^T D^2 + \epsilon I$ help? → Leads to Stage 5

---

## 📍 Stage 5: "The Exciting Part" - Testing Ridge Regularization (Parts 11B-11D)

**Location**: Parts 11B, 11C, 11D  
**Date**: January 27, 2026  
**Status**: ✅ Complete - Fundamental limitation discovered

### The Research Question

**Can ridge regularization prevent degeneracy while maintaining invariance?**

Form: $Q = (D^2)^T D^2 + \epsilon I$

**Why this is exciting**:
- If YES → Principled design for "good" invariant regularizers
- If NO → Fundamental limitation theorem (invariance ↔ effectiveness trade-off)

### The Experimental Journey

#### Part 11B: Theoretical Analysis

**Mathematical reasoning**:
1. Ridge term $\epsilon\|C\|_F^2$ penalizes total energy
2. Degenerate solution (bimodal) might need higher amplitude
3. If total energy higher → ridge could prevent degeneracy
4. ✓ Still maintains invariance (fixed $Q$ form)

**Problem identified**:
- Sum structure: $\epsilon(\|c_1\|^2 + \|c_2\|^2)$ still allows imbalance
- Can have $\|c_2\|^2 \approx 0$ while $\|c_1\|^2$ large
- Total energy not necessarily higher for degenerate solution

#### Part 11C: The Paradox

**Initial test** (with P fixed to true values):
- ✅ 100% success at ε = 0 (standard smoothness)
- ✅ 100% success at all ε tested
- ⚠️ **No degeneracy problem observed!**

**Why?** Data constraint $M = P^T C$ with P fixed is too restrictive
- Only optimizing C with known P
- Hard to create degenerate solution that fits data

**With random initialization** (P still fixed):
- ✅ Still 100% success
- ⚠️ **Paradox**: Pilot study showed 0%, this shows 100%!

#### Part 11D: Paradox Solved - The ALS Difference

**Critical discovery**: Pilot study used **ALS** (alternating least squares)
- Optimizes **both P and C** from data
- Allows profiles to adjust
- Creates flexibility for degeneracy

**Fixed P test** (Parts 11B-C):
- ✓ 100% success
- P = P_true (known profiles)
- Only C optimized

**ALS test** (Part 11D, reproducing pilot):
- ✗ 35% success without ridge (65% failure, **100% degeneracy**)
- ⚠️ 70% success with ridge ε=0.1 (marginal improvement)
- ✗ Ridge insufficient (85-100% degeneracy persists)

### The Final Answer

**Ridge regularization maintains invariance but CANNOT fully prevent degeneracy in ALS**

**Why it fails**:
1. Sum structure: $\epsilon\sum_i \|c_i\|^2$ can't distinguish balanced vs unbalanced
2. When P adjusts, degenerate solutions remain energetically favorable
3. Total energy $\|C^{\text{deg}}\|_F^2$ not necessarily higher than $\|C^{\text{true}}\|_F^2$
4. Marginal help (35% → 70%) but **not sufficient** for reliability

### What This Proves

**Fundamental Limitation Theorem** (informal):
> For SEC-SAXS deconvolution with correlated profiles, no fixed quadratic form $S(C) = \text{tr}(CQC^T)$ can simultaneously:
> 1. Maintain orthogonal invariance
> 2. Prevent degeneracy when both P and C are optimized
>
> To prevent degeneracy, must use context-dependent penalties (profile-weighted, min-amplitude).

### Files & Evidence

- **Part 11B**: ~110 lines
  - Theoretical analysis of ridge mechanism
  - Why it might work / why it might fail
  - Other invariant penalties to explore

- **Part 11C**: ~40 lines  
  - Paradox discovery (100% vs 0% success)
  - Tests with fixed P
  - Random initialization experiments

- **Part 11D**: ~230 lines
  - ALS implementation
  - Reproduces pilot study degeneracy (100% degeneracy rate)
  - Ridge marginal improvement (35% → 70%)
  - Final verdict with visualizations

### Decision Points for Future

⭐ **Reconsider ridge approach**: Current conclusion is "insufficient" - could revisit with:
- Different ε values (tested 0.01, 0.1, 1.0 - try larger?)
- Different problem setups (separation, overlap, SNR)
- Theoretical analysis of when ridge would/wouldn't help

⭐ **Explore other invariant penalties**:
- Higher-order mixed: $Q = (D^2)^T D^2 + \alpha(D^1)^T D^1 + \beta I$
- Spatially-weighted: $Q = (D^2)^T W D^2$ with problem-specific $W$
- Graph Laplacian: Natural for time-series data

⭐ **Characterize fundamental limits**:
- Under what conditions CAN fixed $Q$ prevent degeneracy?
- Formal proof of the limitation theorem
- Connection to Bayesian priors (Gaussian assumption too restrictive?)

❓ **Alternative research direction**:
- Accept that invariance must be broken for reliability
- Characterize "how much" invariance break is needed
- Hybrid approaches: mostly-invariant with targeted breaks

---

## 🎯 Summary: The Complete Arc

### What We've Established

1. **Discovery** (Stage 1): Smoothness regularization has orthogonal invariance
   - Reduces ambiguity from $GL(n)$ to $O(n)$
   - But insufficient for uniqueness

2. **Proof** (Stage 2): Generalized to all differential operators $D^k$
   - Rigorous mathematical foundation
   - Choice of $D^2$ is about quality, not uniqueness

3. **Reality Check** (Stage 3): Empirical failure despite elegance
   - 0% success with standard smoothness
   - Degeneracy mechanism identified (sum structure weakness)

4. **Generalization** (Stage 4): Necessary/sufficient form discovered
   - $S(C) = \text{tr}(CQC^T)$ with fixed $Q$
   - Trade-off identified: invariance ↔ degeneracy prevention

5. **Deep Question** (Stage 5): Can ridge solve it?
   - Tested: $Q = (D^2)^T D^2 + \epsilon I$
   - **Answer: No** - marginal improvement but insufficient
   - **Conclusion**: Fundamental limitation of fixed $Q$ approach

### The Broader Implication

**For JOSS paper argument**:
- Model-free methods require **architectural choices** (ALS, initialization, constraints)
- These choices ARE modeling decisions (hidden vs explicit)
- No "perfect" invariant regularizer exists
- Must choose: mathematical purity OR practical reliability

**For regularization theory**:
- Discovered fundamental limitation of quadratic penalties
- Trade-off between invariance and degeneracy prevention is unavoidable
- Context-dependent penalties necessary for reliability

### Open Research Questions

1. **Can we formally prove the limitation?** 
   - Theorem: "For correlated profiles, no fixed $Q$ prevents degeneracy in ALS"
   - Would need conditions on correlation, overlap, etc.

2. **What's the minimum invariance-break needed?**
   - Profile-weighted works (100% success) but breaks invariance fully
   - Is there a "mostly-invariant" penalty that works?

3. **Can optimal Q be designed problem-specifically?** ✓✓ **ANSWERED: YES** (January 27, 2026)
   - **Result**: Frequency-domain band-pass filtering achieves **90% reliability** while maintaining invariance!
   - See [problem_informed_Q_design.ipynb](problem_informed_Q_design.ipynb) for full analysis
   - Key insight: Generic ridge insufficient (Part 11D), but **problem-informed** Q incorporating expected peak widths succeeds
   - Baseline 35% → Frequency filtering 90% → Trade-off can be resolved!

4. **Bayesian interpretation?**
   - $\text{tr}(CQC^T)$ = Gaussian prior
   - Is Gaussian assumption the real limitation?
   - Explore non-Gaussian priors that maintain some invariance

---

## 📚 Cross-References

### Related Notebooks
- [underdeterminedness_exploration.ipynb](underdeterminedness_exploration.ipynb) - Origin of conjecture
- [smoothness_orthogonal_invariance_proof.ipynb](smoothness_orthogonal_invariance_proof.ipynb) - Full proof + testing
- [permutation_reliability_pilot.ipynb](permutation_reliability_pilot.ipynb) - Empirical context
- [discrete_ambiguity_demonstration.ipynb](discrete_ambiguity_demonstration.ipynb) - Why permutations matter

### Related Documents
- [R_CENTRIC_FRAMEWORK.md](../R_CENTRIC_FRAMEWORK.md) - Analytical framework
- [REGALS_analysis_summary.md](REGALS_analysis_summary.md) - How REGALS addresses this
- [PROJECT_STATUS.md](../PROJECT_STATUS.md) - Current research status

### Key Figures
- underdeterminedness_exploration.ipynb: Figure showing identical objectives across rotations
- smoothness_orthogonal_invariance_proof.ipynb Part 11: Degeneracy mechanism diagram
- smoothness_orthogonal_invariance_proof.ipynb Part 11D: ALS vs Fixed P comparison plots

---

## 📝 Version History

- **v1.1** (January 27, 2026): Research Question #3 answered
  - Added breakthrough result: Frequency-domain Q achieves 90% reliability
  - Links to problem_informed_Q_design.ipynb
  - Confirms trade-off can be resolved with problem-informed Q design
  
- **v1.0** (January 27, 2026): Initial creation
  - Documented complete journey from discovery → testing
  - Marked decision points for future reconsideration
  - Established as living document for research continuity

---

**Last Updated**: January 27, 2026  
**Status**: Active research document  
**Maintainer**: Primary researcher (modeling-vs-model_free project)
