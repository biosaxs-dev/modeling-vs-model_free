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

## Pragmatic Solution: Dual-Evaluation Approach

### Motivation

**Zhang 2025 critique**: Two-stage optimization (denoise → fit) is suboptimal compared to joint optimization

**Challenge for Molass**: Implementing full joint optimization would require major algorithmic changes:
- Rewrite optimizer to simultaneously handle denoising + parametric fitting
- Define joint objective function combining data fit and physical constraints
- No guarantee of convergence (non-convex joint problem)

**Alternative insight**: Use denoising as optimization aid, but validate against ground truth

### The Dual-Evaluation Strategy

**Approach**:
```python
# Current Molass workflow
M_clean = svd_denoise(M_noisy, k=analyst_chosen_rank)  # Stage 0
params = optimize_parametric_model(M_clean)             # Stage 1 & 2

# Proposed addition: Dual evaluation
chi2_clean = evaluate(M_clean, params)   # Optimization objective (existing)
chi2_noisy = evaluate(M_noisy, params)   # Validation check (NEW)
```

**Key principle**: Optimize on denoised data for convergence stability, but validate on original noisy data for robustness

### Benefits

1. **Simple implementation**: No algorithmic changes to optimizer
   - Just add final evaluation step against M_noisy
   - Reuse existing chi-square calculation code

2. **Diagnostic capability**: Two quality metrics provide insight
   - χ²_clean acceptable, χ²_noisy acceptable → Robust solution ✓
   - χ²_clean good, χ²_noisy poor → Overfit to denoising artifacts ⚠️
   - Quantitative ratio (χ²_noisy / χ²_clean) indicates overfitting severity

3. **Conservative validation**: Doesn't overcommit to denoised features
   - SVD may introduce artifacts (truncation effects)
   - Parametric fit might exploit these artifacts
   - M_noisy validation catches this problem

4. **Familiar paradigm**: Similar to machine learning train/test split
   - "Train" on M_clean (smooth optimization landscape)
   - "Test" on M_noisy (real-world performance)
   - Generalization gap = overfitting indicator

### Comparison to Zhang 2025 Joint Optimization

| Aspect | Zhang 2025 | Dual-Evaluation |
|--------|-----------|-----------------|
| **Philosophy** | Change HOW you optimize | Keep optimizer, add validation |
| **Implementation** | Requires algorithm rewrite | Single line of code |
| **Optimization target** | Joint (data + constraints) | Sequential (M_clean then validate) |
| **Convergence** | No guarantee (non-convex) | Same as current (well-tested) |
| **Diagnostic value** | Single metric | Two metrics (clean vs noisy) |
| **Addresses Zhang critique** | Directly (joint optimization) | Indirectly (pragmatic validation) |

### When Dual-Evaluation Detects Problems

**Scenario 1: Overfitting to SVD truncation**
- M_clean has sharp boundaries at chosen rank k
- Parametric model fits these boundaries
- But M_noisy shows these are artifacts
- Result: χ²_clean ≈ 1.0, χ²_noisy >> 1.5 (failure detected)

**Scenario 2: Noise-exploiting parameter values**
- Optimizer finds parameters that "fit" denoising patterns
- E.g., unrealistic skewness matching SVD basis functions
- M_noisy validation reveals poor generalization
- Result: Parameter values suspicious + high χ²_noisy (investigation needed)

**Scenario 3: Robust solution (ideal)**
- Parameters fit M_clean well (smooth optimization)
- Same parameters fit M_noisy acceptably (robust)
- Result: χ²_clean ≈ χ²_noisy ≈ 1.0 (success)

### Architectural Context

**REGALS**: Already avoids this problem
- No separate SVD denoising stage
- Operates directly on M_noisy
- IFT regularization provides implicit denoising during ALS
- Joint optimization already present (data fit + regularization)

**Molass**: Explicit SVD denoising stage
- Stage 0: M_noisy → SVD(k) → M_clean
- Stage 1 & 2: Parametric fitting on M_clean only
- Zhang 2025's critique directly applies
- Dual-evaluation is pragmatic mitigation

### Implementation Example

```python
# In Molass parametric fitting code
def fit_parametric_model(M_noisy, k, model='EGH'):
    # Stage 0: Denoising (existing)
    M_clean = svd_denoise(M_noisy, rank=k)
    
    # Stage 1 & 2: Optimization (existing)
    params = optimize(M_clean, model)
    
    # NEW: Dual evaluation
    chi2_clean = compute_chi2(M_clean, params)
    chi2_noisy = compute_chi2(M_noisy, params)  # Added validation
    
    # Diagnostic
    if chi2_noisy / chi2_clean > 1.5:
        warnings.warn(f"Overfitting detected: χ²_noisy/χ²_clean = {ratio:.2f}")
    
    return params, {'chi2_clean': chi2_clean, 
                   'chi2_noisy': chi2_noisy,
                   'overfitting_ratio': chi2_noisy / chi2_clean}
```

### Research Question Raised

**Open question**: What threshold ratio indicates problematic overfitting?
- Ratio = 1.0: Perfect (parameters generalize perfectly)
- Ratio = 1.2: Acceptable? (slight overfitting to denoising)
- Ratio = 1.5: Concerning? (significant dependence on denoised features)
- Ratio > 2.0: Failure? (parameters exploiting artifacts)

**Empirical investigation needed**: Test on diverse SEC-SAXS datasets to calibrate threshold

### Conclusion

The dual-evaluation approach offers a **pragmatic middle ground**:
- Captures spirit of Zhang 2025's insight (validate against true objective)
- Avoids complexity of full joint optimization
- Provides diagnostic value for practitioners
- Easy to implement in existing Molass codebase

Not a replacement for joint optimization, but a practical validation strategy that addresses the same concern.

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
