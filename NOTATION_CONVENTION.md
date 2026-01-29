# Notation Convention

**Last Updated**: January 28, 2026  
**Status**: Standardized across repository

---

## Matrix Factorization Convention

This repository uses the **same convention as the JOSS paper** (`molass/paper.md`):

$$M = PC$$

**Note on Interpretation**: Throughout this repository, $M = PC$ and related equalities (such as $M = (PR)(R^{-1}C)$ in transformation discussions) are **presented as simple equalities for brevity and accessibility**, but they represent **optimization problems** rather than exact equalities. In practice, methods find $P$ and $C$ that minimize:

$$\|M - PC\|^2 + \text{regularization terms}$$

where regularization terms include smoothness constraints, non-negativity, and other physical constraints. Importantly, this is a **low-rank approximation**: $P$ and $C$ have much smaller inner dimension (number of components, typically 2-3) compared to $M$'s dimensions (hundreds of q-values × frames), meaning we approximate complex data with a small number of underlying components. This approximation framework (rather than exact equality) is implicit in most discussions but critical for understanding:
- Why multiple solutions exist (optimization can find different local minima)
- Why initialization strategies matter (different starting points → different solutions)
- Why optimization can fail (getting stuck in poor local minima)
- Why explicit constraints (like Molass's approach) are necessary to guide optimization

Where:
- **$M$**: Measured data matrix (q-values × frames)
  - Rows: SAXS q-values
  - Columns: Time frames (elution profile)
  
- **$P$**: Scattering curves matrix (q-values × components)
  - **Each column** is one component's SAXS profile
  - Physical interpretation: Basis spectra
  - Dimensions: $n_q \times n_{\text{components}}$
  
- **$C$**: Elution curves matrix (components × frames)
  - **Each row** is one component's elution over time
  - Physical interpretation: Time-dependent coefficients
  - Dimensions: $n_{\text{components}} \times n_{\text{frames}}$

### Least-Squares Solution

$$P = M \cdot C^{+}$$

where $C^{+}$ is the Moore-Penrose pseudoinverse of $C$.

---

## Why This Convention?

### 1. **Standard in Matrix Factorization Literature**
- Matches NMF (Non-negative Matrix Factorization): $V \approx WH$
- Basis vectors in **columns** of left matrix
- Coefficients in **rows** of right matrix

### 2. **Cleaner Mathematics**
- No transpose needed in basic equation
- Direct pseudoinverse solution
- Simpler to implement and understand

### 3. **Physical Intuition**
- **Column of $P$** = One SAXS spectrum (natural: spectrum is vector)
- **Row of $C$** = One time series (natural: sequence is row)

### 4. **Consistency with Molass Implementation**
- Matches actual library code
- Consistent with JOSS paper
- Reduces confusion

---

## Transformation Ambiguity

The underdeterminedness can be expressed as:

$$M = PC = (PR)(R^{-1}C) = P'C'$$

For any invertible transformation $R$:
- $P' = PR$ (transformed scattering curves)
- $C' = R^{-1}C$ (transformed elution curves)

**Orthogonal invariance** means regularization like $\|D^2P\|^2$ satisfies:

$$\|D^2P\|^2 = \|D^2(PR)\|^2 \quad \text{for orthogonal } R$$

---

## Alternative Convention (NOT USED)

Some ALS papers use $M = CP^T$ with:
- $C$: components (q-values × components)
- $P$: populations (frames × components)

**We DO NOT use this notation** because:
- Requires transpose ($P^T$) making equations messier
- Less standard in broader matrix factorization literature
- Inconsistent with Molass paper

---

## Files Updated to This Convention

All research documentation now uses $M = PC$:

- ✅ `molass/paper.md` - JOSS paper (original source)
- ✅ `explorations/orthogonal_invariance_overview.md` - Research summary
- ✅ `explorations/orthogonal_invariance_journey.md` - Full technical narrative
- ✅ All notebooks (where applicable)

---

## For Future Contributions

When adding new documentation or code:
- Use $M = PC$ (not $M = CP^T$)
- $P$ for scattering curves (columns = components)
- $C$ for elution curves (rows = components)
- Solution: $P = M \cdot C^{+}$

This ensures consistency across the repository and with the published JOSS paper.
