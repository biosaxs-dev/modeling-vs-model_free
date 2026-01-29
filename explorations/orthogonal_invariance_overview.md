# Orthogonal Invariance: Research Overview

**Purpose**: Quick-start guide to the orthogonal invariance research journey  
**For Full Details**: See [orthogonal_invariance_journey.md](orthogonal_invariance_journey.md)  
**Created**: January 28, 2026  
**Last Updated**: January 28, 2026

---

## 📖 What This Is About

> **Note on Notation**: This document uses the matrix factorization convention $M = PC$ (not $M = CP^T$), consistent with the JOSS paper. See [NOTATION_CONVENTION.md](../NOTATION_CONVENTION.md) for complete details on dimensions, physical interpretation, and rationale.

> **Prerequisites**: Familiarity with orthogonal matrices and transformation ambiguity is helpful. **New to this?** Start with [Matrix Transformations Tutorial](matrix_transformations_tutorial.ipynb) - a visual guide building from 2D examples to factorization concepts.

### The Starting Problem: Underdeterminedness

When decomposing time-resolved scattering data $M$ into scattering profiles ($P$) and elution curves ($C$):

$$M = PC$$

> **Note**: Throughout this document, $M = PC$ and related equalities represent optimization problems (finding $P$ and $C$ that minimize $\|M - PC\|^2$ plus regularization terms) rather than exact equalities. This is implicit in the discussion but important for understanding the practical context. See [NOTATION_CONVENTION.md](../NOTATION_CONVENTION.md) for details.

This equation is **underdetermined** - infinitely many solutions exist. Any invertible transformation matrix $R$ gives an equally valid solution:

$$M = PC = (PR)(R^{-1}C) = P'C'$$

**Question 1**: Among infinite possibilities, which solution is "correct"?

### The Hope: Can Regularization Select One Solution?

"Model-free" methods use **smoothness regularization** to prefer physically reasonable solutions:

$$\text{minimize: } \|M - PC\|^2 + \lambda\|D^2P\|^2$$

The hope: Smoothness penalty $\|D^2P\|^2$ will favor the true solution and eliminate ambiguity.

**Question 2**: Does smoothness regularization provide uniqueness?

### The Critical Discovery: Orthogonal Invariance

**Stage 1 Discovery** (the "aha!" moment): Smoothness regularization is **orthogonally invariant**:

$$\|D^2P\|^2 = \|D^2(PR)\|^2 \quad \text{for orthogonal } R$$

**What this means**: If $P$ has smoothness penalty $S$, then $PR$ (rotated/permuted version) has the **exact same** penalty $S$.

**Question 3**: If smoothness treats all orthogonal transformations equally, how can it select ONE solution?

### The Answer: It Can't (Fundamental Limitation)

This is the core insight driving the entire research journey:

1. **Mathematical proof** (Stage 2): Invariance holds for ALL differential operators $D^k$
2. **Empirical confirmation** (Stages 3, 5, 9): 0% success in practice across multiple optimizers
3. **Deep mechanism** (Stages 6-8): Operator design, objective structure create multiple minima
4. **Conclusion**: Fixed-form invariant regularization → multiple comparable solutions → no uniqueness

**Why "Orthogonal Invariance" Matters**: It's not an abstract property - it's the **mathematical reason** why regularization alone fails. Understanding this logical chain is essential:

```
   Underdetermined Problem           Proposed Solution              Critical Discovery
   M = PC has ∞ solutions      →    Use smoothness penalty    →    But it's invariant!
   M = (PR)(R⁻¹C) also valid        λ||D²P||² to select one       ||D²P||² = ||D²(PR)||²
   
          ↓                                  ↓                              ↓
   
   Need: Select ONE solution         Hope: Penalize "bad" R         Reality: Treats all R equally
   
          ↓                                  ↓                              ↓
   
        Can it work?             ←─────────  NO  ───────────→    Invariance → No distinction
                                                                  → Can't provide uniqueness
```

**Implication**: This explains why explicit constraints (like Molass's Rg-consistency) are necessary - they break the symmetry that invariant regularization preserves.

### The Journey

9 stages of discovery (January 17-28, 2026) exploring:
- **Stages 1-2**: Mathematical foundations (proof of invariance for all $D^k$ operators)
- **Stages 3-5**: Practical failures (degeneracy, multiple minima, ridge doesn't fix it)
- **Stages 6-7**: Deep questions (operator choice, gradient structure)
- **Stage 8**: Framework discovery (3D design space with incompatibilities)
- **Stage 9**: Refined understanding (applies to all optimizers, validates explicit modeling)

**Why It Matters for JOSS**: This work provides **theoretical foundation** for why Molass's explicit parametric constraints (Rg-consistency, physical models) are necessary - regularization alone is fundamentally insufficient due to orthogonal invariance.

---

## 📊 Executive Summary

| Stage | Research Question | Key Finding | Impact on JOSS Validation |
|-------|-------------------|-------------|---------------------------|
| **1. Discovery** | Does smoothness preserve rotations? | Yes - orthogonal invariance proven | Reduces ambiguity but insufficient for uniqueness |
| **2. Proof** | Can we generalize mathematically? | Yes - all differential operators $D^k$ | Rigorous foundation established |
| **3. Reality Check** | Does invariance = practical failure? | Yes - 0% success, degeneracy identified | Confirms need for additional constraints |
| **4. Generalization** | What form preserves invariance? | Fixed form: $\text{tr}(CQC^T)$ with trade-offs | Framework for constraint design |
| **5. Ridge Test** | Can ridge regularization fix it? | No - fundamental limitation of fixed $Q$ | Problem-informed design required |
| **6. Operator Logic** | Why additive combination? | Operator encodes gradient dynamics | Most fundamental modeling choice |
| **7. Meta-Analysis** | Are findings operator-specific? | Yes - log-additive achieves 25% (others 0%) | Operator choice critically affects outcome |
| **8. Framework** | Is it really 1D or multi-dimensional? | 3D space: Operator × Q-form × Q-design | Incompatibilities discovered (not all work) |
| **9. Diagnostic** | Does conjecture apply to all optimizers? | Yes - even global optimizers fail (0%) | **Validates Molass's explicit constraints** ✅ |

---

## 🗺️ The Journey in Brief

### Stage 1: Discovery (January 17, 2026)
**Notebook**: [underdeterminedness_exploration.ipynb](../explorations/underdeterminedness_exploration.ipynb)

**Starting Context**: The decomposition $M = PC$ is underdetermined - any transformation $R$ gives $M = (PR)(R^{-1}C)$. This means infinitely many solutions exist. The question: Can smoothness regularization $\lambda\|D^2P\|^2$ eliminate this ambiguity by preferring one solution?

**The Discovery**: While exploring transformation ambiguity, discovered that smoothness regularization has a critical property - it's **orthogonally invariant**:

$$\|D^2(PR)\|^2 = \|D^2P\|^2 \quad \text{for orthogonal } R$$

**What This Means**: If we transform a solution via orthogonal matrix $R$ (rotations, reflections, permutations), the smoothness penalty stays the same. So solutions $P$ and $PR$ are equally smooth.

**Critical Implication**: If smoothness treats all orthogonal transformations equally, it **cannot** distinguish between them → cannot provide uniqueness within the orthogonal subspace $O(n)$.

**Key Insight**: This discovery explains WHY regularization alone might fail - it's invariant to exactly the transformations we hope it would eliminate! This motivated Stages 2-9 to prove, test, and understand this limitation.

---

### Stage 2: Rigorous Proof (January 22, 2026)
**Notebook**: [smoothness_orthogonal_invariance_proof.ipynb](smoothness_orthogonal_invariance_proof.ipynb)

Proved rigorously that orthogonal invariance holds for **all differential operators** $D^k$ (first-order, second-order, etc.), not just $D^2$. This is an 11-part mathematical proof establishing the theoretical foundation.

**Key Insight**: The invariance is fundamental to differential regularization, not specific to our choice of $D^2$.

---

### Stage 3: Practical Caveat (January 22, 2026)
**Notebook**: Part 11 of [smoothness_orthogonal_invariance_proof.ipynb](smoothness_orthogonal_invariance_proof.ipynb)

Tested empirically: Does smoothness alone work in practice? **No** - 0% success rate. ALS with smoothness regularization consistently produces **degenerate solutions** (one flat component, one containing all signal).

**Key Insight**: Mathematical elegance ≠ practical effectiveness. The sum structure allows degeneracy.

---

### Stage 4: Generalization Theory (January 26-27, 2026)
**Notebook**: Part 11A of [smoothness_orthogonal_invariance_proof.ipynb](smoothness_orthogonal_invariance_proof.ipynb)

Characterized the necessary and sufficient form for orthogonally invariant constraints: $S(C) = \text{tr}(CQC^T)$ where $Q$ is a fixed symmetric matrix. This reveals a **fundamental trade-off**:
- Invariance requires fixed $Q$ (same for all transforms)
- Degeneracy prevention needs $Q$ to distinguish components
- These may be incompatible!

**Key Insight**: Design space has inherent constraints - not all goals are simultaneously achievable.

---

### Stage 5: Ridge Regularization Test (January 27, 2026)
**Notebook**: Parts 11B-11D of [smoothness_orthogonal_invariance_proof.ipynb](smoothness_orthogonal_invariance_proof.ipynb)

Tested: Can ridge regularization $Q = (D^2)^TD^2 + \epsilon I$ solve the degeneracy problem while maintaining invariance?

**Answer**: **No** - Ridge marginally improves (5% success) but insufficient. Problem-informed $Q$ designs (frequency-domain weighting) achieve **90% success**.

**Key Insight**: Fixed $Q$ approach has fundamental limitations - domain knowledge required. This led to the **"Multiple Minima Conjecture"**: Fixed-form invariant constraints create optimization landscapes with multiple local minima of comparable quality, preventing convergence to unique solutions.

---

### Stage 6: The Deeper Question (January 27, 2026)
**Notebook**: [objective_combination_rules_exploration.ipynb](objective_combination_rules_exploration.ipynb)

Why do we use additive combination $f(C) = \text{fit}(C) + \lambda \cdot \text{smooth}(C)$? Explored alternatives:
- **Additive** ($A + \lambda B$): Independent gradients, allows trade-offs ("OR"-like logic)
- **Multiplicative** ($A \times \lambda B$): Coupled gradients, requires balance ("AND"-like logic)
- **Log-additive** ($\log A + \lambda \log B$): Adaptive gradients via power scaling
- **Max** ($\max(A, \lambda B)$): Lexicographic priority

**Key Insight**: Operator choice is the **most fundamental modeling decision** - it encodes how constraints interact through gradient structure.

---

### Stage 7: Operator-Dependent Journey (January 28, 2026)
**Notebook**: [objective_operators_invariance_exploration.ipynb](objective_operators_invariance_exploration.ipynb)

Meta-question: Are findings from Stages 1-5 operator-dependent? Tested multiplicative, log-additive, and max operators.

**Results**:
- All operators preserve orthogonal invariance ✓
- Multiplicative: Still 0% (degeneracy persists)
- **Log-additive: 25% success!** (Surprise winner)
- Max: 0%

**Key Discovery**: Mathematical equivalence ≠ practical equivalence. The **λ-placement paradox** - WHERE the regularization parameter enters determines gradient structure:
- Multiplicative $\frac{\partial f}{\partial B} = \lambda A$ (constant, traps in poor minima)
- Log-additive $\frac{\partial f}{\partial B} = \frac{\lambda}{B}$ (adaptive, inverse scaling)

**Key Insight**: Operator choice + λ placement critically affect optimization dynamics.

---

### Stage 8: The Three-Dimensional Framework (January 28, 2026)
**Analysis**: Meta-analysis of Stages 1-7

Critical realization: Stages 4-5 explored $Q$ design for **additive operator only**. The design space is actually **three-dimensional**:

1. **Operator Choice**: Additive vs Multiplicative vs Log-additive vs Max (Stage 6-7)
2. **Q Form**: What mathematical form preserves invariance? (Stage 4)
3. **Q Design**: Specific matrix design - Generic vs Ridge vs Frequency vs Problem-informed (Stage 5)

**First Incompatibility Discovered**: Log-additive + frequency Q = **0% success**
- Worse than log-additive + generic Q (25%)
- While additive + frequency Q = 90%
- Suggests **destructive interference** between adaptive gradients and frequency filtering

**Key Insight**: Not all combinations work - the design space has **structure and incompatibilities**. Stage 5's 90% breakthrough is operator-specific, not universal.

---

### Stage 9: Diagnostic Refinement (January 28, 2026)
**Notebook**: [multiple_minima_diagnostic.ipynb](multiple_minima_diagnostic.ipynb)

Core question: Is the Multiple Minima Conjecture (Stage 5) about objective landscape (affects all optimizers) or optimization method (ALS-specific)? Tested with **Basin-hopping** (global optimizer) instead of ALS.

**Critical Tests**:
1. **Objective Comparison**: Is degenerate solution better?
   - **NO** - True solution has lower objective (0.40 << 40.01)
   - True solution IS the global optimum
   
2. **Basin-hopping + Additive**: Does global optimization help?
   - **NO** - 0% success (vs ALS: 35%)
   - Finds different minima: permuted/shifted (not degenerate)
   
3. **Basin-hopping + Log-additive**: Molass-relevant test?
   - **NO** - 0% success (vs ALS: 25%)
   - Even with correct objective + global optimizer, still fails

**Refined Understanding**:
- True solution is global optimum ✓
- But landscape has **many comparable local minima** (~0.40-0.44 objective)
- Three types: True (global), Permuted/Shifted (Basin-hopping finds), Degenerate (ALS finds)
- **Paradox**: ALS's constrained alternation sometimes helps (25-35%) vs Basin-hopping's freedom (0%)

**Updated Terminology**: "Fundamental Limitation Theorem" → **"Multiple Minima Conjecture"** (acknowledges lack of formal proof)

**Key Insight for JOSS**: Even with:
- ✅ Correct global optimum (true solution is best)
- ✅ Global optimizer (Basin-hopping, not just ALS)
- ✅ Better operator (log-additive, Molass-like)

System **still fails (0%)** without explicit constraints. This **strongly validates Molass's approach**: Rg-consistency + parametric models directly address the multiple minima problem.

---

## 🎯 Key Takeaways for JOSS Validation

### What We've Proven
1. **Invariance Properties**: Smoothness/regularization constraints are orthogonally invariant (mathematical fact)
2. **Practical Limitations**: Invariant constraints alone lead to multiple local minima (empirical finding)
3. **Scope**: Applies to all optimizers (ALS and global), all tested operators (diagnostic confirmation)

### How This Validates Molass

**The Core Argument**:
> "Model-free" approaches using only regularization (smoothness, non-negativity) face a **Multiple Minima Problem**. Even with optimal objective design + global optimization, the landscape contains many comparable solutions. Explicit parametric constraints (Rg-values, physical shape models) directly address this by encoding domain knowledge that breaks the symmetry.

**Supporting Evidence from This Research**:
- **Stage 3**: Pure regularization fails (0%)
- **Stage 5**: Problem-informed Q (frequency-domain) helps for additive (90%) but isn't universal
- **Stage 8**: Operator-specific incompatibilities exist (log-additive + frequency Q = 0%)
- **Stage 9**: Even Basin-hopping + log-additive fails without explicit constraints (0%)

**Molass's Solution**:
- Rg-consistency constraint (physical domain knowledge)
- Parametric shape models (Guinier-Porod, Schulz distributions)
- These break the permutation/rotation symmetry explicitly
- Not just regularization - structural information

### Connection to Reference Methods

This framework helps articulate why existing "model-free" methods have limitations:
- **CHROMIXS**: May face similar multiple minima without sufficient constraints
- **REGALS**: EFA initialization + ALS refinement - still susceptible to local minima
- **EFAMIX**: EFA has known limitations (baseline, noise, tailing) - multiple minima likely factor

---

## 🧭 Navigation Guide

### Which Document Should I Read?

**New to Orthogonal Matrices?** ([Matrix Transformations Tutorial](matrix_transformations_tutorial.ipynb)):
- Visual introduction starting from 2D examples
- Builds intuition: What are rotations? Why do they matter?
- Demonstrates factorization ambiguity concretely
- Includes quick reference formulas
- **Read this first** if terms like "orthogonal invariance" are unfamiliar

**Start Here** (This overview):
- You understand basic matrix concepts
- You want the big picture quickly
- You're preparing JOSS validation arguments
- You need to understand key findings without math details
- You want to see how stages connect

**Go Deep** ([Journey Document](orthogonal_invariance_journey.md)):
- You want full mathematical proofs
- You need experimental details and code snippets
- You're reviewing the research methodology
- You want complete context for each stage
- You need the ASCII flow diagram showing discovery sequence

**For Specific Topics**:
- **Mathematical Foundation**: Journey Stages 1-2, 4
- **Practical Failures**: Journey Stages 3, 5, 9
- **Operator Theory**: Journey Stages 6-7
- **Design Framework**: Journey Stage 8
- **JOSS Arguments**: This overview's "Key Takeaways" section

### Related Documents

- [matrix_transformations_tutorial.ipynb](matrix_transformations_tutorial.ipynb) - Visual introduction to orthogonal matrices (recommended prerequisite)
- [PROJECT_STATUS.md](../PROJECT_STATUS.md) - Latest breakthroughs and quick start
- [explorations/README.md](README.md) - Mathematical foundations overview
- [NOTATION_CONVENTION.md](../NOTATION_CONVENTION.md) - Standard $M = PC$ notation explained
- Individual notebooks linked in each stage above

---

## 📝 Context Restoration Guide

**For Future Sessions**: Start by reading this overview, then consult journey.md for specific stage details.

**Key Files**:
- `matrix_transformations_tutorial.ipynb` - Foundational tutorial (start here if new to orthogonal matrices)
- `orthogonal_invariance_overview.md` (this file) - Entry point for research journey
- `orthogonal_invariance_journey.md` - Full technical narrative (9 stages)
- `multiple_minima_diagnostic.ipynb` - Latest stage (Stage 9)
- `objective_operators_invariance_exploration.ipynb` - Operator analysis (Stage 7)

**Current Status** (January 28, 2026):
- ✅ 9 stages complete
- ✅ Multiple Minima Conjecture refined (applies to all optimizers)
- ✅ 3D framework established (Operator × Q-form × Q-design)
- ⏳ Incompatibility mechanisms (Stage 8) - open research question
- Ready for JOSS validation evidence extraction

**Next Priorities**:
1. Understand log-additive + frequency Q incompatibility mechanism (Stage 8 follow-up)
2. Extract evidence from reference papers (CHROMIXS, EFAMIX, REGALS)
3. Connect Multiple Minima Conjecture to published method limitations
4. Build JOSS validation narrative using this theoretical foundation

---

**Version**: 1.0  
**Contributors**: Research conducted January 17-28, 2026  
**License**: Part of modeling-vs-model_free JOSS validation repository
