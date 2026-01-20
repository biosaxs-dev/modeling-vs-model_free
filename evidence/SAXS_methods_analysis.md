# Analysis of Modern SEC-SAXS Methods: Addressing EFA Tailing/Overlap Limitations

**Date**: 2026-01-20  
**Context**: Verification of EFA limitations from 1988/1991 papers, specifically Limitation 3 (tailing effects causing FIFO violations)

---

## Executive Summary

**CRITICAL FINDING**: None of the 4 modern papers (2018-2024) explicitly acknowledge the fundamental FIFO assumption problem we discovered - where overlapping components create contradictory detection windows (components appearing to disappear BEFORE they appear, i.e., negative window widths).

All four papers work around the limitation without stating the core mathematical issue. Here's what each does:

---

## Paper 1: CHROMIXS (2018, Panjkovich & Svergun)

### Approach to Tailing/Overlap
- **Does NOT use EFA** - uses different method entirely
- Buffer subtraction with automatic selection
- Uses "quality measure" from AUTORG for scoring subtracted curves

### Key Quote on Limitations
> "CHROMIXS allows for a convenient manual or automated reduction of SEC-SAXS runs with **well resolved fractions (i.e. baseline separated sample elution peaks)**. In more intricate cases, CHROMIXS may help in diagnosing and preparing the data for **further processing by other programs**."

### What This Means
- **CHROMIXS acknowledges it can't handle overlap** but doesn't explain WHY
- Punts overlapping peaks to "other programs" (BioXTAS RAW, UltraScan-SOMO)
- Focuses on automated baseline-separated peak detection
- **Does not discuss the underlying mathematical impossibility**

### Limitations Mentioned
- Cannot handle overlapping peaks
- Cannot handle "intricate cases"
- Relies on baseline separation

---

## Paper 2: EFAMIX (2021, Konarev et al.)

### Approach to Tailing/Overlap
- **Explicitly uses EFA** with rotation matrix method
- Major focus: handling the "changing background scattering" in chromatography

### Critical Quote About FIFO/Windows
> "Each component is not present outside its concentration time window, and its concentration is therefore equal to zero. **It is also assumed that the components elute after each other**, that is, the first component present in the system will be the first to disappear, the second component will disappear next, and so on."

### What EFAMIX Does
1. **Enforces strict FIFO ordering** - "first component present will be the first to disappear"
2. Uses "concentration windows" concept
3. Tests with **symmetric Gaussian peaks** in simulations
4. When testing asymmetric (EGH) peaks with "tailing parameter τ":
   - Works for τ ≤ 2 (moderate asymmetry)
   - **FAILS for τ = 5** (high asymmetry)

### Key Limitation Quote
> "For highly overlapping peaks, a decomposition is still possible for a **moderate asymmetry** of the concentration profiles (when the relaxation parameter τ of the EGH function does not exceed the value of 2). At higher profile asymmetries, the component peaks display **significantly overlapping concentration windows leading to systematic deviations** in the EFA results (τ = 5)."

### What They Found (Fig 3)
- **Acknowledges failure mode exists** but doesn't explain WHY mathematically
- Says "overlapping concentration windows" cause "systematic deviations"
- **This is describing the exact problem we found** (negative window widths!) **but without stating it explicitly**
- They blame "high asymmetry" rather than identifying the fundamental FIFO violation

### Does EFAMIX Address Our FIFO Discovery?
**NO** - They observe the failure (systematic deviations when windows overlap) but:
- Don't explain it's a mathematical impossibility
- Don't mention negative window widths
- Frame it as a "limitation of high asymmetry" rather than a fundamental FIFO assumption violation
- **Their Figure 3 (τ=5 row) likely shows the exact phenomenon we discovered!**

### Additional EFAMIX Insights
- Works for IEC-SAXS with **moderate** salt gradients (12%) but fails at 25%
- Uses smoothness regularization on background components
- **Requires nonoverlapping areas in concentration contours for unambiguous separation**

---

## Paper 3: REGALS (2021, Meisburger, Xu & Ando)

### Approach to Tailing/Overlap
- **Goes BEYOND EFA** - does not rely on FIFO assumption
- Uses regularized alternating least squares (ALS)
- **Key innovation**: Can apply constraints in real space via P(r) functions

### Critical Statement About EFA Limitations
> "Often, however, both the scattering curves and physicochemical model are unknown before the experiment is performed and must be inferred from the data themselves... **the challenge is to identify appropriate mathematical tools to incorporate more general physically motivated restraints** that lead to a reliable and accurate model-free separation."

And specifically about EFA:
> "One exception is SAXS data collected with in-line size-exclusion chromatography (SEC-SAXS), where MCR-ALS has been combined with **evolving factor analysis (EFA)** to separate overlapping peaks... **Although the SVD and MCR algorithms are well suited to certain SAXS experiments, they are a poor fit for other more challenging datasets**."

### What REGALS Does Differently
1. **Doesn't assume compact support in concentration space** (i.e., doesn't require FIFO)
2. Instead applies:
   - Smoothness regularization
   - **Real-space constraints** (P(r) with maximum dimension dmax)
   - Boundary conditions on concentration profiles
3. Can handle:
   - AEX-SAXS (changing buffer background)
   - Titration series
   - Time-resolved data
   - **Cases where components DON'T obey first-in/first-out**

### Key Quote on Why EFA Fails for Complex Data
> "Because this changing background [in AEX-SAXS] **violates certain assumptions of the EFA method**, model-free deconvolution of AEX-SAXS data is not possible with EFA."

> "In SAXS datasets from time-resolved or ligand titration experiments, it is common for components to have **non-zero concentrations in most or all of the measurements**, and **a compact support cannot be assumed in the concentration basis** as in the AEX-SAXS example above."

### Does REGALS Address Our FIFO Discovery?
**YES, implicitly** - REGALS exists because:
- They recognized EFA's "compact support" assumption (= FIFO requirement) breaks down
- They built a method that **doesn't rely on FIFO ordering**
- Their smoothness/real-space constraints provide alternative information

**But they still don't explicitly state**: "When peaks overlap, EFA fails because it tries to assign contradictory start/end points creating negative window widths"

### REGALS Success Cases
- Successfully deconvolves overlapping BSA monomer-dimer peaks
- Handles PheH titration with overlapping conformational states + aggregation
- Works on time-resolved data (MsbA, CypA T-jump)
- **All cases where EFA would fail due to FIFO violations**

---

## Paper 4: BioXTAS RAW 2 (2024, Hopkins)

### Approach to Tailing/Overlap
- **Implements BOTH EFA and REGALS**
- Provides automated buffer/sample range selection
- Baseline correction (linear and integral)

### Key Statements About EFA vs REGALS
> "Though the mathematics are not the same, from a practical point of view [REGALS] can be thought of as **an extension of the previously implemented EFA technique** to more complex conditions where **components are not necessarily entering and exiting the dataset in a strict first-in/first-out approach** like in SEC-SAXS."

> "We still generally **recommend EFA for standard SEC-SAXS data** due to ease of use, but for **more complex data** as listed above [titrations, time-resolved, IEC-SAXS], REGALS is preferred."

> "REGALS can also handle **deconvolution of SEC-SAXS data with a sloping baseline**, something that **EFA tends to fail at**."

### What RAW Does for Automated Analysis
1. **Automated buffer range finding**:
   - Tests for correlations in total intensity (should be flat)
   - Tests profile similarity
   - Checks number of significant singular values (should be 1)
   
2. **Automated sample range finding**:
   - Looks for constant Rg and MW across peak
   - Tests profile similarity
   - **If Rg trends → multiple components → avoid that region**

### Critical Quote About Algorithm Limitations
> "Both the buffer- and sample-range finding algorithms in RAW are simply based on **useful heuristics**. There is **no proven way of always finding valid sample and buffer ranges** – this may not exist – so instead we have devised a set of metrics..."

### Does RAW Address Our FIFO Discovery?
**Indirectly** - The automated range-finding explicitly:
- Checks for "correlations" (trending Rg/MW) across selected regions
- Rejects ranges where Rg is not constant (= overlapping components)
- **This is detecting the FIFO violation condition** without naming it

The algorithm **avoids selecting overlapping regions** because it knows they'll cause problems, but doesn't explain the mathematical reason (negative window widths).

---

## Comparison: How Each Tool Handles The Tailing Problem

| Tool | Year | Uses EFA? | How It Handles Overlap | Acknowledges FIFO Issue? |
|------|------|-----------|------------------------|--------------------------|
| **CHROMIXS** | 2018 | ❌ No | Requires baseline separation; punts to other tools | ❌ No |
| **EFAMIX** | 2021 | ✅ Yes | Enforces FIFO; fails with high asymmetry (τ>2) | ⚠️ Partial - observes failure, doesn't explain why |
| **REGALS** | 2021 | ❌ No | Uses smoothness + real-space constraints instead of FIFO | ⚠️ Implicit - designed to avoid FIFO requirement |
| **RAW 2** | 2024 | ✅ Both | Automated range finding avoids overlap; uses REGALS for complex cases | ⚠️ Implicit - algorithm detects/avoids condition |

---

## Direct Quotes About "Concentration Windows" and Overlap

### EFAMIX on Concentration Windows:
> "The fundamental idea of EFA is to follow the rank of the data matrix A as a function of the number of measurements taken into account... to determine when a component appears/disappears from the system (for SEC- or IEC-SAXS, this defines the points corresponding to the appearance of an extra component in the time frames in the elution peaks)."

> "Taking only the portion of the vectors and matrix C **outside of the concentration window range**, one column of the matrix R can be sequentially restored after the other."

**Translation**: The rotation matrix calculation **requires non-overlapping windows** - this is the FIFO assumption in mathematical form!

### REGALS on Why This Fails:
> "It is known from the literature on chemometric separation of matrices for mixtures that the separation is **unambiguous if there are nonoverlapping areas** in the contours of the component spectra (which is not always the case with SAXS) or in the contours of the concentration profiles (**the EFA principle relies on this**)."

> "Chromatographic separation, as a minimum, provides **nonoverlapping initial sections** of the concentration curves, and this should be sufficient for a successful decomposition."

**Translation**: EFA REQUIRES "nonoverlapping initial sections" = FIFO assumption. When this breaks down (overlapping peaks), EFA fails.

---

## What The Papers DON'T Say (But Should)

None of the papers explicitly state:

1. **The mathematical impossibility**: When two Gaussian peaks overlap, forward EFA detects component B appearing at frame X, while backward EFA detects component A disappearing at frame Y, where Y < X. This creates a **negative window width** (start > end).

2. **Why this happens**: The "concentration window" concept **assumes** each component has a contiguous region where it exists exclusively. Overlapping peaks violate this by definition - there's no frame where A exists without B, or B without A.

3. **The FIFO paradox**: The original EFA theory states "first component to appear is first to disappear." But with tailing, we observe component A tailing into component B's peak → A disappears AFTER B appears → FIFO violation → undefined rotation matrix.

4. **It's not about peak shape**: Our notebook showed this happens even with **ideal Gaussian peaks** when they overlap. It's not a "tailing" problem per se - it's an **overlap** problem that becomes mathematically unresolvable under FIFO assumptions.

---

## Why Don't They State It Explicitly?

Possible reasons:

1. **It's considered "obvious"** in the chemometrics community that EFA requires non-overlapping regions
2. **Legacy knowledge** - the original 1987/1991 papers may have stated it more clearly and later papers assume readers know
3. **Focus on solutions** - papers focus on "here's what works" rather than "here's exactly why the old method fails"
4. **Partial understanding** - EFAMIX observes the failure mode but may not fully understand the mathematical root cause

---

## Conclusion: What We've Discovered vs What They Say

### What We Found (Limitation 3 Notebook):
✅ **Explicit demonstration** that overlapping Gaussian peaks create:
- Forward EFA: Component B appears at frame 26
- Backward EFA: Component A disappears at frame 15
- **Result**: Negative window width = mathematical impossibility
- **This happens even with ideal peaks** (no tailing artifacts)

### What The Papers Say:
- **EFAMIX**: "High asymmetry causes systematic deviations when concentration windows overlap" (observes symptom, not cause)
- **REGALS**: "EFA requires nonoverlapping concentration profiles" (states requirement, doesn't explain failure mode)
- **RAW**: "No proven way to find valid ranges" + algorithm avoids overlapping regions (pragmatic solution, no theory)
- **CHROMIXS**: "Can't handle overlapping peaks" (punts problem elsewhere)

### The Gap:
Nobody in the modern literature **explicitly connects**:
1. Overlapping peaks →
2. Contradictory start/end point detection →
3. Negative window widths →
4. Mathematical impossibility of rotation matrix calculation →
5. **Therefore EFA fundamentally cannot work for overlapping components**

**This is the core insight from our verification work** that apparently has NOT been clearly stated in the modern SEC-SAXS literature, even though all the tools have been designed to work around it!

---

## Implications for Our Paper

We can make a **strong original contribution** by:

1. **Explicitly demonstrating** the FIFO violation with simple overlapping Gaussians
2. **Showing the math** of negative window widths from contradictory forward/backward EFA
3. **Connecting** this to why modern tools (REGALS, etc.) abandon FIFO assumptions
4. **Clarifying** that this isn't about "tailing artifacts" - it's a fundamental consequence of overlap under FIFO constraints

**Quote for paper**: "While modern SEC-SAXS tools acknowledge EFA's limitations with overlapping peaks (Meisburger et al., 2021; Konarev et al., 2021), none explicitly demonstrate that the FIFO assumption creates mathematically contradictory concentration windows - where backward EFA detects a component's disappearance before forward EFA detects its appearance. This fundamental failure mode explains why model-free deconvolution methods have moved away from EFA's compact support assumptions."

---

## Recommendations

1. **Use EFAMIX Figure 3 (τ=5) as supporting evidence** - their systematic deviations are likely showing the same effect
2. **Cite REGALS explicitly** as the solution that abandons FIFO in favor of smoothness constraints
3. **Reference RAW's automated range-finding** as implicit recognition that overlapping regions are problematic
4. **Position our work as**: "Making explicit what has been implicit in method development" - closing the gap between tool design and theoretical understanding
