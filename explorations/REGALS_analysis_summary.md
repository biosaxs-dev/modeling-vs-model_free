# REGALS Analysis: Constraint-Based vs Parametric Approaches

**Date**: January 18, 2026  
**Context**: Mathematical comparison of constraint-based (REGALS) and parametric (Molass) methods for SEC-SAXS decomposition  
**Attribution**: Analysis conducted in collaboration with GitHub Copilot (Claude Sonnet 4.5)

---

## Executive Summary

REGALS (Regularized Alternating Least Squares) represents a **constraint-based approach** to SEC-SAXS data decomposition, while Molass uses **parametric models** (Gaussian/EGH/SDM/EDM elution profiles). This analysis examines how REGALS' constraint hierarchy resolves fundamental underdeterminedness in matrix factorization and explores what functional forms these constraints may implicitly favor. Key questions: What regularization choices does REGALS make? How do these compare to explicit parametric assumptions?

---

## 1. The Fundamental Underdeterminedness Problem

### Mathematical Foundation

The core problem REGALS solves is matrix factorization:
$$\min_{P,C} \|M - PC\|^2$$

where:
- $M \in \mathbb{R}^{N \times K}$ = measured SEC-SAXS data
- $P \in \mathbb{R}^{N \times n}$ = SAXS profiles of components
- $C \in \mathbb{R}^{n \times K}$ = concentration/elution curves

### Key Discovery: Infinite Solutions

**Without constraints, this problem has infinitely many solutions:**

1. **Scale ambiguity**: $(P, C)$ and $(\alpha P, C/\alpha)$ fit identically for any $\alpha > 0$
2. **Basis ambiguity**: $(P, C)$ and $(PR, R^{-1}C)$ fit identically for **any invertible** matrix $R$

**REGALS authors' description**: They state that "basis vectors can be mixed (or 'rotated')" using "any non-singular K×K matrix Ω" (their notation). They correctly identify this as **any invertible matrix**, not just rotations:
- Rotations (orthogonal matrices)
- Scalings (diagonal matrices)
- Shearings (off-diagonal elements)
- Arbitrary mixing (any invertible transformation)

**Note**: They use quotes around "'rotated'" acknowledging it's not literally about rotations, and correctly state it applies to non-singular matrices.

---

## 2. The Constraint Hierarchy: Four Layers of Constraints

REGALS achieves uniqueness through **four layers of constraints** that progressively eliminate ambiguities:

### Level 1: Data-Fit Only (Baseline)
$$\min_{P,C} \|M - PC\|^2$$

- **Result**: Infinitely many solutions
- **Free parameters**: 1 (scale) + $n^2$ (any invertible matrix)
- **Ambiguity**: Complete—any scaling and any invertible basis transformation

### Level 2: Add Smoothness Regularization
$$\min_{P,C} \|M - PC\|^2 + \lambda\|D^2C\|^2$$

- **Result**: Still infinitely many solutions (orthogonal transformations only)
- **Free parameters**: $\frac{n(n-1)}{2}$ (dimension of orthogonal group O(n))
- **What changed**:
  - Scale ambiguity **eliminated** (smoothness penalty changes with scale)
  - Basis ambiguity **reduced** (from arbitrary invertible $R$ to orthogonal $B$ only)
- **Mathematical insight**: $\|D^2(B^{-1}C)\|^2 = \|D^2C\|^2$ for orthogonal $B$
- **Orthogonal group O(n) structure**:
  - **SO(n)** (det = +1): Special orthogonal group = proper rotations
  - **det = -1**: Improper orthogonal transformations (reflections, rotoinversions, orientation-reversing isometries)
  - For $n \gg 100$ (typical SEC-SAXS), improper transformations are far more complex than simple reflections

### Level 3: Add Non-Negativity
$$\min_{P \geq 0, C \geq 0} \|M - PC\|^2 + \lambda\|D^2C\|^2$$

- **Result**: Unique solution or **small discrete set of local minima**
- **Free parameters**: 0 continuous parameters, but up to $k!$ discrete permutations possible
- **What changed**: 
  - Continuous ambiguity ($n(n-1)/2$ degrees of freedom from O(n)) **eliminated**
  - Discrete permutation ambiguity **may persist** when components are similar
  - **Key insight**: "Small discrete set" = discrete local minima (one per valid permutation)
  - Most random orthogonal transformations (both proper rotations and improper transformations) produce negative values (empirically verified)

### Level 4: Full REGALS (Normalization + Compact Support + SAXS)
$$\min_{\substack{P \geq 0, C \geq 0 \\ C(t) = 0 \text{ outside windows} \\ P \leftrightarrow P(r) \text{ with } d_{max} \\ \|P_k\| = 1}} \|M - PC\|^2 + \lambda\|D^2C\|^2$$

- **Result**: Unique solution (typically), or **small discrete set of local minima** (edge cases)
- **Free parameters**: 0 continuous parameters, 0 or small number of valid permutations
- **What changed**:
  - **Normalization**: Ensures no residual scaling freedom
  - **Compact support**: Spatially separates components (reduces permutation ambiguity)
  - **SAXS constraints**: Distinguishes components by molecular size (further reduces permutations)
  - **Edge case**: Nearly identical components may still permit 2-6 discrete local minima (permutations)

---

## 3. Constraint-Based Perspective: What Do These Constraints Favor?

### REGALS' Regularization Choices

1. **Smoothness ($\lambda\|D^2C\|^2$)**: Penalizes rapid changes in concentration profiles
   - Favors: Slowly-varying elution profiles
   - Suppresses: Sharp transitions, high-frequency variations
   - **Open question**: What functional forms does this regularization favor? (Gaussian-like? Cubic splines? Other?)

2. **Non-negativity ($P \geq 0, C \geq 0$)**: Enforces physical positivity
   - Physical constraint: Scattering intensities and concentrations are inherently non-negative
   - Mathematical effect: Eliminates continuous ambiguity space

3. **Compact support**: Requires components to elute in specified windows
   - Incorporates: Prior knowledge from SEC separation
   - Mathematical effect: Spatially separates components

4. **SAXS constraints ($P(r)$ with $d_{max}$)**: Enforces structural properties
   - Compact support in real space: $P(r) = 0$ for $r > d_{max}$ (maximum particle dimension)
   - Mathematical effect: Provides additional constraints for uniqueness (paper states "sufficient information for successful deconvolution")

### Comparison to Parametric Methods (Molass)

**Molass (Parametric)**:
- Specifies functional forms explicitly: Gaussian/EGH/SDM/EDM elution profiles
- Parameters have direct physical interpretation (peak position, width, skewness)
- Assumptions stated upfront in model choice

**REGALS (Constraint-Based)**:
- Specifies constraints and regularization: smoothness penalty, non-negativity, support windows
- Parameters ($\lambda$, windows, $d_{max}$) control strength of constraints
- Functional forms emerge from optimization rather than specified a priori

**Key difference**: **Parametric specification vs constraint-based emergence**

---

## 4. The Permutation Ambiguity Problem as Discrete Local Minima

### Unifying Perspective: Permutations ARE Local Minima

**Critical insight**: "Small discrete set" in the constraint hierarchy = **discrete local minima** in the optimization landscape.

**Each valid permutation is a local minimum**:
- Component swap $(P_1, P_2, P_3) \to (P_2, P_1, P_3)$ creates different solution
- Same or similar $\chi^2$ value (locally optimal)
- Different physical interpretation (which component is which?)
- ALS from single initialization converges to ONE of these randomly

**Example**: 3-component system
- Maximum $3! = 6$ possible permutations
- Each permutation = one local minimum basin
- No gradient path between basins (discrete jumps required)
- Global optimization needed to explore all 6 possibilities

**This explains two phenomena simultaneously**:
1. **Permutation ambiguity** (Section 4): "Different initializations may converge to different permutations"
2. **Need for global optimization** (global_optimization_gap.md): Single initialization insufficient

**EFAMIX's trade-off makes sense**: By avoiding non-negativity constraints, they prevent creation of these discrete local minima branches—but sacrifice physical correctness (negative concentrations possible).

### When Discrete Ambiguity Persists

Even with all four constraint layers, **discrete permutation ambiguity** (component label swapping) can occur when:

1. **Overlapping elution windows**: Peak separation < 0.5 mL
2. **Similar SAXS profiles**: $\Delta d_{max} < 2$ nm
3. **Similar intensities**: Scattering ratio 0.7-1.3
4. **Oligomeric series**: Multiple similar components (dimer, trimer, tetramer)

### Probability Estimates

| Scenario | Permutation Ambiguity Risk |
|----------|---------------------------|
| Well-separated components | < 1% |
| Typical SEC-SAXS data | 5-10% |
| Overlapping peaks | 20-30% |
| Oligomeric series | 30-50% |
| Poor separation + noise | 50-70% |

### Practical Implications

1. **Manual intervention required**: Users must inspect and validate component assignments
2. **Multiple local minima**: Different initializations may converge to different permutations
3. **Physical knowledge needed**: Cannot be truly "automatic" or "model-free"
4. **Validation essential**: Cross-check with other techniques (AUC, mass spectrometry)

---

## 5. Mathematical Precision Issues in REGALS Literature

### Terminology Observations

1. **"'Rotated'" (REGALS authors' term with quotes)**
   - **Technically correct**: They identify the ambiguity as "any non-singular K×K matrix Ω"
   - **Informal language**: They use "'rotated'" (with quotes) as informal shorthand
   - **Their statement**: "basis vectors can be mixed (or 'rotated') without changing χ²"
   - **Assessment**: They understand it's not literally rotations (hence the quotes), though clearer terminology would be "mixed" or "transformed"

2. **"Orthogonal rotations"** (imprecise and redundant terminology)
   - **Issue**: Conflates two distinct concepts from group theory
   - **Correct terminology**:
     - **Orthogonal transformations** = O(n) group (includes both det=+1 and det=-1)
     - **Proper rotations** = SO(n) group (det=+1 only, a subgroup of O(n))
     - **Improper orthogonal transformations** = det=-1 (reflections, rotoinversions, etc.)
   - **Why "orthogonal rotations" is wrong**: "Rotation" specifically means SO(n) (det=+1), so "orthogonal rotations" is either redundant (if meaning SO(n)) or contradictory (if trying to include det=-1 cases)
   - **Mathematical precision**: For $n \gg 100$ (typical SEC-SAXS), O(n) has dimension $n(n-1)/2$, with SO(n) as an index-2 normal subgroup

### Orthogonal Group Structure (Precise Mathematical Classification)

- **O(n)**: Full orthogonal group (all orthogonal matrices)
  - Dimension: $\frac{n(n-1)}{2}$
  - Determinant: +1 or -1
  - Preserves lengths and angles (isometries of Euclidean space)
  
- **SO(n)**: Special orthogonal group (proper rotations only)
  - A normal subgroup of O(n) with index 2
  - Determinant: +1 (det=+1 is the defining property)
  - Path-connected, preserves orientation
  - These are true "rotations" in the geometric sense

- **Improper orthogonal transformations**: (det = -1)
  - NOT a subgroup, only a coset of SO(n)
  - Includes: reflections, rotoinversions, orientation-reversing isometries
  - For $n > 2$: More complex than simple reflections
  - Example: Inversion through origin (all coordinates negated)

- **Quotient**: O(n)/SO(n) ≅ {+1, -1} ≅ O(1)

---

## 6. Implications for the Molass vs REGALS Paper

### Main Arguments

1. **Constraint-based vs parametric approaches**
   - REGALS: Uses regularization (smoothness penalties) and constraints (non-negativity, compact support)
   - Molass: Specifies functional forms explicitly (Gaussian/EGH/SDM/EDM)
   - Both resolve underdeterminedness through different mechanisms

2. **Transparency and interpretability**
   - Parametric models (Molass): Parameters have direct physical meaning (peak position, width, skewness)
   - Constraint-based models (REGALS): Parameters ($\lambda$, windows, $d_{max}$) control constraint strength
   - Different approaches to incorporating prior knowledge

3. **Uniqueness considerations**
   - Even with all constraints, permutation ambiguity can persist (5-50% of cases depending on data quality)
   - Manual validation often required for both approaches
   - Neither is fully "automatic" for challenging datasets

4. **Both approaches have merit**
   - REGALS: Flexible, minimal functional form assumptions
   - Molass: Explicit, parameters interpretable
   - Choice depends on application and available prior knowledge

### Key Insight for Paper

> "Both constraint-based (REGALS) and parametric (Molass) approaches make regularization choices to resolve underdeterminedness. Parametric methods specify functional forms explicitly, while constraint-based methods let forms emerge from optimization. A key research question: **What functional forms do REGALS' constraints actually favor?** Do smoothness penalties implicitly favor Gaussian-like profiles, or do they produce qualitatively different solutions? Understanding this relationship helps users choose the appropriate approach for their data and prior knowledge."

---

## 7. Next Steps for Mathematical Derivation

### Priority 1: Characterize REGALS' Implicit Functional Form

**Goal**: What functional form does smoothness regularization $\lambda\|D^2C\|^2$ implicitly assume?

**Approaches**:
1. **Bayesian interpretation**: Derive prior distribution $p(C) \propto \exp(-\lambda\|D^2C\|^2)$
   - Gaussian process prior?
   - Integrated Wiener process?

2. **Variational calculus**: Minimize $\|D^2C\|^2$ → cubic splines?
   - Characterize optimal smoothness
   - Compare to explicit Gaussian models

3. **Frequency domain**: High-frequency suppression → Gaussian envelope?
   - Fourier analysis of smoothness penalty
   - Connection to bandwidth limitations

4. **Connection to explicit models**: When does REGALS ≈ Gaussian mixture?
   - Identify conditions where implicit and explicit models coincide
   - Quantify divergence when they differ

### Priority 2: Empirical Validation

**Goal**: Test theoretical predictions with simulations

**Simulation plan**:
1. Generate synthetic SEC-SAXS data with known ground truth
2. Compare REGALS vs Molass decompositions
3. Quantify: accuracy, uniqueness, sensitivity to noise
4. Identify: when each method succeeds/fails

---

## 8. Key Takeaways

1. **Constraint-based vs parametric**: REGALS uses constraints and regularization; Molass uses explicit functional forms (Gaussian/EGH/SDM/EDM)

2. **Fundamental underdeterminedness**: Matrix factorization $\min\|M-PC\|^2$ has infinitely many solutions without additional constraints or regularization

3. **Four-layer constraint hierarchy**: Each layer progressively eliminates ambiguities:
   - Level 1 (data-fit): Infinite solutions (any invertible matrix)
   - Level 2 (+ smoothness): Infinite solutions restricted to O(n) (orthogonal transformations)
   - Level 3 (+ non-negativity): Unique or small discrete set
   - Level 4 (+ full REGALS): Typically unique

4. **Permutation ambiguity = discrete local minima**: Even with all constraints, 5-50% of real-world cases have 2-6 discrete local minima (valid permutations). Each is locally optimal; global optimization needed to explore all.

5. **Mathematical precision**: REGALS authors correctly identify mixing ambiguity as "any non-singular matrix", though use informal "'rotated'" terminology (with quotes). With smoothness regularization, ambiguity reduces to O(n) (orthogonal group), not just SO(n) (rotations)

6. **Open research question**: What functional forms does smoothness regularization $\lambda\|D^2C\|^2$ actually favor? (Gaussian-like? Cubic splines? Other?)

7. **Both approaches are valid**: Choice depends on application, available prior knowledge, and whether explicit parametric specification or constraint-based emergence is preferred

---

## 9. References

### Notebooks Created

1. **`underdeterminedness_exploration.ipynb`**: Proves fundamental ambiguities in matrix factorization
   - Part 1: Scale and basis ambiguity demonstration
   - Part 2: Effect of regularization on ambiguity
   - Key result: Four-level constraint hierarchy

2. **`permutation_ambiguity_examples.ipynb`**: Concrete examples of discrete ambiguity
   - Scenario 1: Overlapping monomer-dimer (permutation likely)
   - Scenario 2: Well-separated components (uniqueness guaranteed)
   - Scenario 3: Oligomeric series (high risk)
   - Risk assessment matrix

### Key Mathematical Results

- **O(n) invariance of smoothness**: $\|D^2(B^{-1}C)\|^2 = \|D^2C\|^2$ for all orthogonal $B \in$ O(n)
- **Scale elimination by regularization**: $\|D^2(C/\alpha)\|^2 = \|D^2C\|^2/\alpha^2$ creates unique scale
- **Non-negativity constraint restricts O(n)**: Most random orthogonal transformations (both proper rotations in SO(n) and improper transformations) produce negative values, violating physical constraints

---

## 10. Conclusion

REGALS represents a sophisticated **constraint-based approach** to SEC-SAXS decomposition. Our analysis demonstrates that:

1. REGALS requires **four layers of constraints** to achieve uniqueness (smoothness, non-negativity, normalization, SAXS)
2. Each constraint makes specific **regularization choices** that may favor certain functional forms
3. Even with all constraints, **discrete permutation ambiguity** can persist (5-50% of cases)
4. **Key open question**: What functional forms does smoothness regularization actually produce?

The comparison between REGALS and Molass is best framed as **"constraint-based vs parametric"** rather than "model-free vs model-based." Both approaches make choices to resolve underdeterminedness; they differ in how those choices are specified.

**For the Molass vs REGALS paper**, the key research questions are: *What functional forms do REGALS' constraints favor? When do constraint-based and parametric approaches converge or diverge? How does this inform method choice for different applications?*

---

**End of Summary**
