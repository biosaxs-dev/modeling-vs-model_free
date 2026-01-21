# Latest Trends in Matrix Factorization Algorithms (2025)

**Purpose**: Document recent algorithmic advances in matrix factorization that may be relevant to SAXS deconvolution

**Date**: January 21, 2026

**Source**: Zhang et al. (2025), "Loss-Minimizing Model Compression via Joint Factorization Optimization"

---

## Executive Summary

While Zhang 2025 targets neural network compression, it introduces a **fundamentally new approach to low-rank matrix factorization** that addresses a problem **highly relevant to SAXS deconvolution**: separating factorization error minimization from performance optimization.

**Key Innovation**: **Joint optimization** of matrix factorization AND final objective function, rather than treating them as separate steps.

**Relevance to SAXS**: The SAME mathematical problem exists in SAXS deconvolution:
- Traditional approach: Minimize ||D - C·S^T||² (factorization error), THEN add constraints
- Zhang 2025 approach: Simultaneously optimize factorization error AND model performance

---

## The Core Problem (Universal to Matrix Factorization)

### Traditional "Two-Stage" Approach

**Stage 1**: Minimize factorization error
```
min ||W - L·R^T||_F²    (or min ||D - C·S^T||² for SAXS)
```

**Stage 2**: Fine-tune/add constraints to improve performance
- In neural networks: fine-tune with training data
- In SAXS (REGALS): add regularization constraints (smoothness, non-negativity)

**Problem**: These stages are **optimized separately** → suboptimal solution

### Zhang 2025 Innovation: Joint Optimization

**Key insight**: Matrix factorization introduces **noise** δ to parameters

For neural networks:
```
Loss_after = Loss_original + Σ(∂Loss/∂w_i · δ_i)
```

**Critical observation**: If gradient and noise are in **opposite directions**:
```
∂Loss/∂w_i · δ_i < 0  →  Loss decreases!
```

**Solution**: Find factorization noise δ that:
1. Satisfies low-rank constraint: ||W - L·R^T|| ≤ ε
2. **Reduces** loss: ∂Loss/∂w_i · δ_i < 0

---

## Mathematical Framework

### Optimization Objective

**Joint objective** (Equation 9 from paper):
```
min_(δ∈Δ) [Loss_after - Loss_original] = (1/m) Σ Σ (∂Loss/∂w_i · δ_i)

subject to:
  (a) ||w - l·r^T||_F ≤ ε    (factorization accuracy)
  (b) 0 < k < NM/(N+M)       (compression condition)
```

**Two algorithms**:
1. **Lossless optimization**: Minimize loss while maintaining compression
2. **Compact optimization**: Maximize compression while maintaining loss

### Key Mathematical Result (Lemma 3)

> "The upper bound of the generalization error decreases with decreasing effective rank. After reducing the effective rank to a certain value, the upper bound will increase as rank decreases further."

**Implication**: There exists an **optimal rank** that balances compression and performance.

---

## Comparison: Zhang 2025 vs. SAXS Methods

### Traditional SVD (EFA, 1988)
```
Objective: min ||D - Σ s_i·u_i·v_i^T||²
Problem: Minimizes reconstruction error, NOT rotation ambiguity
Result: Requires FIFO assumption + manual intervention
```

### MCR-ALS (2004)
```
Objective: min ||D - C·S^T||²  + soft constraints
Constraints: Non-negativity, unimodality, closure
Problem: Soft constraints "rarely sufficient" (Jaumot 2004)
Result: Rotation ambiguity remains
```

### REGALS (2021)
```
Objective: min ||D - C·S^T||²  + λ_C||D²C||² + λ_P||D²P||²
Constraints: Smoothness + non-negativity + compact support/d_max
Innovation: Flexible regularization framework
Result: Resolves rotation ambiguity through constraint hierarchy
```

### Zhang 2025 Paradigm (Applied to SAXS?)
```
Objective: min [Loss(D, C·S^T) - Loss_target]
         = min Σ (∂Loss/∂C · δ_C + ∂Loss/∂S · δ_S)

subject to:
  ||D - C·S^T||² ≤ ε    (factorization accuracy)
  gradient·noise < 0     (loss reduction)
  
Innovation: Joint optimization of factorization AND physical objective
Potential: Could optimize directly for experimental objectives
```

---

## Potential Applications to SAXS Deconvolution

### 1. Direct Physical Objective Optimization

**Current REGALS approach**:
- Minimize reconstruction error: ||D - C·S^T||²
- Add regularization: smoothness, non-negativity, etc.
- Hope this resolves rotation ambiguity

**Zhang 2025 paradigm**:
- Define physical objective: e.g., minimize deviation from expected P(r) properties
- Jointly optimize factorization to achieve physical objective
- Could directly encode physical constraints (e.g., "real-space profiles should be smooth and compact")

### 2. Optimal Rank Determination

**Current challenge** (unsolved since 1991):
- Rank inflation: SVD gives too many components
- User must manually choose K
- No principled way to determine "true" rank

**Zhang 2025 approach**:
- Lemma 3: Optimal rank exists that minimizes generalization error
- Could be adapted to find optimal K for SAXS decomposition
- Balance between: fitting data (high K) vs. physical plausibility (low K)

### 3. Lossless Factorization Without Fine-tuning

**Zhang 2025 result**:
- Achieves better performance than original (!) without retraining
- "Lossless compression" - reduces parameters while maintaining/improving performance

**SAXS analogy**:
- Could we find lower-dimensional representations that maintain/improve physical plausibility?
- E.g., 3-component factorization that better satisfies smoothness than 4-component SVD?

---

## Key Differences: Neural Networks vs. SAXS

### What Transfers Well

✓ **Mathematical structure**: Both are matrix factorization problems  
✓ **Gradient concept**: Can define "gradient" as sensitivity of physical constraints  
✓ **Joint optimization**: Factorization accuracy + objective function  
✓ **Optimal rank**: Balance between complexity and performance  

### What's Different

✗ **Training data**: Neural networks have labels; SAXS only has measurements  
✗ **Gradient computation**: Neural networks backpropagate; SAXS needs physical derivatives  
✗ **Objective function**: Neural networks minimize prediction loss; SAXS needs physical plausibility  
✗ **Noise interpretation**: Neural networks tolerate noise if loss decreases; SAXS noise must be physical  

---

## Algorithmic Insights for SAXS

### 1. Two-Stage is Suboptimal

**Zhang 2025 confirms**: Separating factorization from objective optimization is fundamentally suboptimal

**Implication for SAXS**:
- EFA: Optimize SVD, THEN add FIFO → suboptimal
- MCR-ALS: Optimize factorization, THEN add soft constraints → suboptimal
- REGALS: Iterative regularized ALS is better BUT still separates rank determination (SVD) from optimization

### 2. Gradient-Guided Factorization

**Zhang 2025 strategy**: Use gradient information to guide factorization

**SAXS application**:
- Could use sensitivity analysis: how does changing C or S affect physical plausibility?
- E.g., "Which factorization makes P(r) smoothest while fitting data?"

### 3. Constraint as Objective, Not Penalty

**Traditional regularization**: λ·||constraint||² (penalty term)
**Zhang 2025**: Constraint violation must satisfy ε-neighborhood (hard constraint with joint optimization)

**SAXS implication**:
- Instead of penalizing non-smooth profiles, could REQUIRE smoothness in factorization
- Joint optimization finds factorization that inherently satisfies constraints

---

## Relevance to Molass

### What Molass Does Differently

**Molass approach**: Explicit parametric models (Gaussian/EGH/SDM/EDM)
- NOT matrix factorization at all
- Directly models physical peak shapes
- No rotation ambiguity (explicit functional form)

**Zhang 2025 insight**: Even for parametric models, joint optimization matters

**Potential application**:
- Current: Fit peak parameters to minimize ||data - model||²
- Zhang paradigm: Fit peak parameters to minimize (data error + physically implausible parameter combinations)
- E.g., penalize peaks with unphysical skewness or unrealistic widths DURING fitting, not after

### Complementary Approaches

**Model-free (REGALS + Zhang insights)**:
- Flexible, no assumptions about peak shape
- But requires rank determination, regularization choices

**Model-based (Molass + Zhang insights)**:
- Explicit assumptions (Gaussian, etc.)
- Could benefit from joint optimization of peak parameters and physical constraints

---

## Conclusions: Latest Trends

### Algorithmic Trend (2025)

**From**: "Two-stage" factorization + optimization  
**To**: **Joint optimization** of factorization error AND objective function

**Evidence**: Zhang 2025 achieves "lossless" compression (better than original!) without fine-tuning

### Implications for SAXS

1. **Current methods are suboptimal by design**: Separating factorization from physical objectives
2. **Optimal rank determination is possible**: Theoretical framework exists (Lemma 3)
3. **Gradient-guided factorization**: Use physical sensitivities to guide decomposition
4. **Joint optimization paradigm**: Future methods could optimize factorization for physical objectives directly

### Molass Positioning

**Molass already avoids the main problem**: Explicit parametric models don't have rotation ambiguity

**But could benefit from**: Joint optimization of peak parameters and physical constraints

**Complementary**: Model-based (Molass) vs. model-free (REGALS-style + Zhang insights) approaches both valid

---

## References

**Primary Source**:
- Zhang et al. (2025), "Loss-Minimizing Model Compression via Joint Factorization Optimization"

**SAXS Context**:
- EFA: Maeder (1988), Keller (1991)
- MCR-ALS: Jaumot (2004)
- REGALS: Meisburger (2021)
- historical_development.md (this project)

---

**End of Matrix Factorization Trends Analysis**
