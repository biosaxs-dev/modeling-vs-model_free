# Global Optimization: A Gap in Model-Free SEC-SAXS Methods

**Date**: January 23, 2026  
**Purpose**: Document the lack of global optimization strategies in current model-free SEC-SAXS decomposition methods  
**Status**: Research finding for future investigation

---

## Executive Summary

Current model-free SEC-SAXS decomposition methods (EFAMIX, REGALS) do not employ systematic global optimization strategies. EFAMIX developers **explicitly state** they avoid non-negativity constraints because they "may lead to several local minima," while REGALS uses Alternating Least Squares (ALS) with guaranteed convergence only to a **local minimum** from a single SVD+EFA initialization. This limitation has been acknowledged in the chromatography literature since 1991 but remains unaddressed in modern SAXS tools.

**Key question**: Could parametric modeling approaches enable practical global optimization due to their finite-dimensional parameter spaces?

---

## 1. Background: The Non-Convex Optimization Landscape

### Matrix Factorization as Non-Convex Problem

SEC-SAXS decomposition requires solving:

$$\min_{P,C} \|M - PC\|^2 + \text{regularization}(P, C)$$

This optimization landscape is:
- **Non-convex**: Multiple local minima exist
- **High-dimensional**: For model-free methods, $P \in \mathbb{R}^{N \times k}$ and $C \in \mathbb{R}^{k \times K}$ where $N \approx 100$, $K \approx 100$, $k = 2$-$5$
- **Constraint-dependent**: Physical constraints (non-negativity, smoothness) create additional local minima

**Mathematical fact**: Non-convex optimization does not guarantee finding the global minimum without systematic search strategies.

---

## 2. EFAMIX: Explicit Avoidance of Constraints

### Direct Quote from Paper

Konarev et al. (2021), *Protein Science*, 31, 269-282:

> "Currently, EFAMIX does not use the nonnegative least-squares method because **the imposed constraints may lead to several local minima in the search**."

**Location**: Page 272, Section 3.1 (Applications to simulated SEC-SAXS data)  
**Full citation**: tools/extracted_papers.txt, line 515

### Interpretation

The EFAMIX developers:
1. **Recognized** the local minima problem explicitly
2. **Chose** to avoid physical constraints (non-negativity) to prevent it
3. **Trade-off**: Sacrificed physical correctness for convergence guarantee

**Result**: EFAMIX solutions may contain unphysical negative concentrations because enforcing $C \geq 0$ would create local minima that their optimizer cannot handle.

### Implications

This is a **fundamental limitation**: 
- Cannot use standard physical constraints without risking local minima
- No systematic strategy to verify solution optimality
- Users must manually validate physical plausibility

---

## 3. REGALS: Local Convergence from Single Initialization

### Algorithm Structure

Meisburger et al. (2021), *IUCrJ*, 8, 225-237:

**Alternating Least Squares (ALS)**:
```
Initialize: P₀, C₀ from SVD + EFA windows
Repeat until convergence:
    P_{i+1} = argmin_P ||M - PC_i||² + regularization(P)  [convex in P]
    C_{i+1} = argmin_C ||M - P_{i+1}C||² + regularization(C)  [convex in C]
```

### Convergence Properties

**What ALS guarantees**: 
- ✅ Convergence to **a** local minimum
- ✅ Each subproblem (fixing P or C) is convex and solvable

**What ALS does NOT guarantee**:
- ❌ Convergence to the **global** minimum
- ❌ Independence from initialization
- ❌ Uniqueness of solution

**Verification**: See [code_verification.md](regals/code_verification.md#L279)

### Initialization Strategy

**REGALS approach**: Single initialization
1. SVD of $M$ → initial singular vectors
2. EFA analysis → concentration windows
3. These determine $P_0$ and $C_0$

**No discussion in paper** of:
- Trying multiple random initializations
- Sensitivity analysis to starting point
- Comparison of different local minima
- Verification of global optimality

### Implications

Different initializations **may** yield different solutions:
- Permutation ambiguity (component label swapping): 5-50% of datasets (see [REGALS_analysis_summary.md](../explorations/REGALS_analysis_summary.md#L153))
- Different local minima with different $\chi^2$ values
- No systematic way to know if the found solution is optimal

---

## 4. Historical Context: Keller 1991

### Original EFA Paper Acknowledged the Problem

Keller & Massart (1991), *Chemometrics and Intelligent Laboratory Systems*, 12, 209-224:

> "the multidimensional parameter space will have **many local optima** and it is **not a trivial task to localize the global optimum**"

**Location**: tools/efa_papers.txt, lines 54-56  
**Context**: Discussing chromatographic condition optimization (hardware approach)

### Evolution of the Problem

**1991**: Problem recognized in chromatography optimization context  
**2004**: MCR-ALS developed (chemometrics), accepts local convergence  
**2021**: REGALS adopts ALS framework, local convergence accepted  
**2021**: EFAMIX explicitly avoids constraints due to local minima  
**2026**: Problem remains unaddressed in SAXS field

**Pattern**: The local minima problem has been **acknowledged but not solved** for 35 years.

---

## 5. Working Hypothesis: Permutation Ambiguity as Discrete Local Minima

### A Possible Connection (Unvalidated)

**Hypothesis from constraint hierarchy analysis**: The "small discrete set" in Level 3-4 constraints **may represent discrete local minima**.

**Proposed relationship** (not empirically validated):
- Swapping component labels: $(P_1, P_2) \leftrightarrow (P_2, P_1)$
- May create different solution with similar $\chi^2$
- If true, each would be locally optimal (no gradient direction improves objective)
- Would require discrete jump between permutations (not continuous path)

### Two Problems May Be Related

**Previously appeared as separate issues**:
1. **Permutation ambiguity**: 5-50% of datasets have component label uncertainty
2. **Lack of global optimization**: REGALS/EFAMIX use single initialization

**Proposed unified understanding** (speculative): These may be **manifestations of the same underlying problem**
- Permutation ambiguity creates discrete local minima
- Single initialization randomly selects one permutation
- No mechanism to explore other valid permutations
- Global optimization needed to systematically evaluate all possibilities

### Mathematical Structure

**For $k$ components**: Up to $k!$ possible permutations
- 2 components: 2 permutations (potentially 2 local minima)
- 3 components: 6 permutations (potentially 6 local minima)
- 4 components: 24 permutations (potentially 24 local minima)

**Note**: The one-to-one mapping between permutations and local minima is a working hypothesis, not empirically demonstrated.

**Constraints reduce valid permutations**:
- Compact support (different elution windows) → eliminates some permutations
- SAXS profiles (different $d_{max}$) → eliminates more permutations
- Result: Typically 0, 2, or 3-6 valid permutations remain (not full $k!$)

**Optimization landscape**:
- Continuous dimensions: Parameter values within each permutation
- Discrete dimensions: Which permutation (component assignment)
- **Local optimization**: Explores continuous dimensions only
- **Global optimization**: Explores both continuous AND discrete dimensions

### EFAMIX's Trade-off: A Possible Interpretation

Konarev et al. (2021) quote:
> "constraints may lead to several local minima in the search"

**Speculative interpretation**: They may be specifically concerned about **discrete local minima from permutation ambiguity**
- Non-negativity + smoothness → creates permutation branches
- Each valid permutation is a local minimum
- Their optimizer cannot explore multiple branches
- **Solution**: Remove non-negativity → eliminate discrete branches
- **Cost**: Unphysical negative concentrations possible

**Trade-off summary**:
- **EFAMIX choice**: Single global minimum (no permutations) but unphysical solutions
- **REGALS choice**: Physical solutions (non-negativity enforced) but multiple local minima
- **Neither**: Systematic global search across permutations

---

## 6. Speculative Framework: Discrete Oligomerization as Physical Origin

### A Proposed Connection (Requires Validation)

**Hypothesis**: The discrete mathematical structure (permutation ambiguity potentially creating discrete local minima) **may mirror the discrete physical structure** (oligomeric states).

**Established fact - Oligomerization is inherently discrete**:
- Monomer (1×), Dimer (2×), Trimer (3×), Tetramer (4×), Pentamer (5×)
- **Cannot have**: 2.7-mer or 3.4-mer
- Integer multiples of the monomer unit
- **Discrete jumps** between states, not continuous transitions

**Established fact - Permutation ambiguity is inherently discrete**:
- Component 1 = dimer, Component 2 = trimer (Assignment A)
- Component 1 = trimer, Component 2 = dimer (Assignment B)
- **Cannot have**: "60% dimer assignment, 40% trimer assignment"
- **Discrete jumps** between labelings, not continuous interpolation

**Speculative connection**: The mathematics may reflect the physics - Discrete optimization landscape ↔ Discrete biological states. This correlation is suggestive but not proven causal.

### Why Oligomeric Series Are Hardest

From constraint hierarchy analysis, oligomeric series have **highest permutation ambiguity risk** (30-50%).

**Physical similarity within oligomeric series**:
1. **Similar molecular sizes**: $d_{max}$ scales gradually
   - Monomer: ~3 nm
   - Dimer: ~5 nm  
   - Trimer: ~6 nm
   - Tetramer: ~7 nm
   - Small increments, often within measurement uncertainty

2. **Similar shapes**: All built from same monomer building block
   - Same basic structural motif repeated
   - Similar overall geometry (globular, elongated, etc.)

3. **Similar scattering profiles**: Intensity scales with molecular weight
   - $I(q) \propto n \times I_{monomer}(q)$ approximately
   - Shape similarity → profile similarity
   - Hard to distinguish by SAXS alone

4. **Overlapping elution**: Similar hydrodynamic radii
   - $R_h \propto n^{1/3}$ for compact structures
   - Dimer vs. trimer: only ~26% difference in elution volume
   - Heavy overlap in SEC separation

**Mathematical consequence**: Components insufficiently distinguishable → Multiple component assignments equally valid → Multiple discrete local minima

### The Assignment Problem

**If the hypothesis is correct**: Each local minimum would correspond to one oligomer assignment.

**Hypothetical example: 3-peak system (trimer/tetramer/pentamer mixture)**

| Local Minimum | Peak A | Peak B | Peak C | Objective $\chi^2$ |
|---------------|--------|--------|--------|--------------------|
| Assignment 1 | Trimer | Tetramer | Pentamer | 1.05 |
| Assignment 2 | Tetramer | Trimer | Pentamer | 1.07 |
| Assignment 3 | Trimer | Pentamer | Tetramer | 1.12 |

All three are **locally optimal** but represent **different physical interpretations**:
- Which oligomer elutes first?
- What is the molar ratio?
- What is the equilibrium constant?

**Single-initialization optimization** (REGALS, EFAMIX) randomly selects one assignment. **Global optimization** systematically evaluates all valid assignments.

### Why Discrete Nature May Amplify the Problem

**Continuous systems** (e.g., protein conformations):
- Gradual shape changes
- Continuous parameter variations
- Local minima differ by objective function value
- Can rank by goodness-of-fit

**Discrete oligomeric systems** (hypothetically):
- Abrupt identity changes (trimer ≠ tetramer)
- Similar objective function values (all fit data well)
- Cannot rank by $\chi^2$ alone (differences within noise)
- **Requires physical validation**: Which assignment is biologically reasonable?

**Speculative implication**: If the hypothesis is correct, permutation ambiguity in oligomeric series may not just be a mathematical nuisance—it could reflect **genuine physical degeneracy** in the measurement.

### Opportunities for Structure-Aware Modeling

**Current parametric models** (EGH, SDM, EDM):
- Treat each peak independently
- No relationship between components
- Miss oligomeric structure

**Oligomer-aware parametric models** (potential enhancement):
1. **Constrained size relationships**: 
   - $d_{max,n} = f(n) \cdot d_{max,monomer}$
   - Enforce physical scaling laws

2. **Intensity ratios**:
   - $I_n \propto n \cdot I_{monomer}$ 
   - Molecular weight proportionality

3. **Shape similarity constraints**:
   - $P_n(q) \approx S_{n}(q) \cdot P_{monomer}(q)$
   - Structure factor × form factor

4. **Discrete state models**:
   - Explicitly enumerate: "This is 2-mer, 3-mer, 4-mer"
   - Not just "component A, B, C"
   - Encode discrete identity in model

**Advantage**: Reduce permutation ambiguity by encoding physical relationships
- Fewer valid assignments satisfy oligomeric constraints
- Reduce from $k!$ permutations to 1-2 valid oligomer assignments
- Physical knowledge breaks discrete degeneracy

### Why Model-Free Methods Cannot Leverage This

**Matrix factorization treats components as arbitrary vectors**:
- No concept of "this is 3× that"
- No encoding of oligomeric relationships
- Permutation ambiguity is pure mathematical artifact
- Cannot incorporate discrete biological structure

**REGALS regularization** (smoothness, non-negativity, compact support):
- Helps with continuous parameters
- Does not address discrete identity assignment
- Cannot encode "$P_3 \approx 3 \times P_1$"

**Result**: Model-free methods remain vulnerable to permutation ambiguity in oligomeric systems because they cannot leverage the **discrete structure** inherent in oligomerization.

### Research Implications (If Hypothesis Validated)

**Proposed insight**: If the connection is real, when the physical system has discrete structure (oligomerization), the optimization landscape may acquire discrete branches (local minima). This would not be a flaw—it would be an **accurate mathematical representation** of physical degeneracy.

**Three approaches to handle this**:

1. **Ignore it** (current EFAMIX): Remove constraints → eliminate discrete branches
   - Pro: Single global minimum
   - Con: Unphysical solutions (negative concentrations)

2. **Accept it** (current REGALS): Hope initialization lands in "correct" branch
   - Pro: Physical solutions
   - Con: No verification, 30-50% risk of wrong assignment

3. **Embrace it** (structure-aware modeling): Encode discrete structure explicitly
   - Pro: Reduce ambiguity through physical constraints
   - Pro: Global optimization explores remaining discrete possibilities
   - Con: Requires more prior knowledge (oligomeric nature)

**Research question**: Can structure-aware parametric models with global optimization reliably assign oligomeric identities in overlapping SEC-SAXS data?

---

## 7. Comparison: Model-Free vs Parametric Approaches

### Dimensionality Consideration

**Model-free (REGALS)**:
- Parameter count: $N \times k + k \times K$ = $(100 \times 3) + (3 \times 100)$ = 600 parameters
- Constraints: Matrices $P$, $C$ with regularization
- Optimization: High-dimensional non-convex landscape

**Parametric (EGH/SDM/EDM)**:
- Parameter count per peak: 3-5 parameters (position, width, asymmetry)
- For $k$ peaks: $3k$ to $5k$ parameters = 9-15 parameters for 3 peaks
- Constraints: Peak shape functional forms + positivity
- Optimization: Low-dimensional non-convex landscape

**Mathematical implication**: 
- Global optimization methods (basin-hopping, nested sampling, differential evolution) are **computationally tractable** for low-dimensional spaces
- Same methods become **prohibitively expensive** for 600-dimensional spaces

---

## 8. Global Optimization Methods (Background)

### Basin-Hopping Algorithm

**Reference**: Wales & Doye (1997), *J. Phys. Chem. A*, 101, 5111-5116  
**Implementation**: `scipy.optimize.basinhopping`

**Strategy**:
1. Perform local minimization from current point
2. Accept or reject based on Metropolis criterion
3. Apply random perturbation to "hop" to new basin
4. Repeat to explore multiple basins

**Advantage**: Systematically explores multiple local minima (both continuous AND discrete)  
**Discrete exploration**: Random perturbations can "jump" between permutation branches  
**Computational cost**: $O(N_{\text{hops}} \times N_{\text{local}})$  
**Tractability**: Feasible for ~10 parameters, challenging for ~600 parameters

### Nested Sampling

**Reference**: Skilling (2006), *Bayesian Analysis*, 1, 833-859  
**Implementation**: `ultranest` package

**Strategy**:
1. Sample uniformly from parameter space
2. Iteratively replace lowest-likelihood samples
3. Compress volume systematically
4. Calculate Bayesian evidence

**Advantage**: 
- Provides posterior distributions (uncertainty quantification)
- Explores full parameter space systematically
- Avoids mode-hopping failures of MCMC

**Computational cost**: Scales exponentially with dimensionality  
**Tractability**: Feasible for ~10-20 parameters, impractical for ~600 parameters

### Differential Evolution

**Reference**: Storn & Price (1997), *J. Global Optim.*, 11, 341-359  
**Implementation**: `scipy.optimize.differential_evolution`

**Strategy**:
1. Maintain population of candidate solutions
2. Generate trial vectors via mutation and crossover
3. Select based on fitness (objective function value)
4. Evolve population toward global optimum

**Advantage**: Robust, derivative-free, population-based  
**Computational cost**: $O(N_{\text{pop}} \times N_{\text{gen}} \times N_{\text{eval}})$  
**Tractability**: Effective for ~10-30 parameters, struggles beyond ~100 parameters

---

## 9. The Dimensionality Advantage of Parametric Models

### Why Parametric Models Enable Global Optimization

| Aspect | Model-Free (REGALS) | Parametric (EGH/SDM/EDM) |
|--------|---------------------|--------------------------|
| **Parameter count** | ~600 (matrix elements) | ~10-15 (peak parameters) |
| **Basin-hopping** | Impractical | Feasible |
| **Nested sampling** | Impractical | Feasible |
| **Differential evolution** | Marginal | Efficient |
| **Physical interpretation** | Implicit (matrix values) | Explicit (position, width) |
| **Constraint encoding** | Regularization matrices | Functional form + bounds |

**Key insight**: The 40-60× reduction in dimensionality makes systematic global optimization **computationally tractable** for parametric models but **impractical** for model-free matrix factorization.

### Trade-offs

**Parametric advantages**:
- ✅ Global optimization feasible
- ✅ Uncertainty quantification practical
- ✅ Physical interpretation clear

**Parametric limitations**:
- ❌ Assumes specific functional forms (Gaussian-based)
- ❌ May not capture unusual peak shapes
- ❌ Requires choosing appropriate model (EGH vs SDM vs EDM)

**Model-free advantages**:
- ✅ No functional form assumptions
- ✅ Flexible to any peak shape
- ✅ Data-driven decomposition

**Model-free limitations**:
- ❌ Global optimization impractical
- ❌ Rotation ambiguity (requires constraint hierarchy)
- ❌ High-dimensional parameter space

---

## 10. Current Status in the Field (2026)

### What Exists

**EFAMIX**: Avoids constraints → No local minima, but unphysical solutions  
**REGALS**: Single initialization → Accepts local convergence  
**CHROMIXS**: Defers overlapping peaks to other tools  
**BioXTAS RAW**: Automated range-finding avoids overlap

### What's Missing

❌ **No systematic global optimization strategy** in any model-free SAXS tool  
❌ **No uncertainty quantification** for decomposition parameters  
❌ **No sensitivity analysis** to initialization  
❌ **No verification** of solution optimality

### Research Gap

**Fundamental question**: How much does local vs. global optimization matter in practice?

**Needed investigations**:
1. Frequency of multiple local minima in real SEC-SAXS data
2. Magnitude of objective function differences between local minima
3. Physical meaningfulness differences between local solutions
4. Computational cost-benefit analysis of global optimization

---

## 11. Potential Research Directions

### For Model-Free Methods

**Challenge**: 600-dimensional space makes global optimization impractical

**Possible approaches**:
1. **Hybrid initialization**: Use parametric fits to initialize REGALS → better starting point
2. **Multi-start ALS**: Run REGALS from multiple random initializations, compare solutions
3. **Coarse-to-fine**: Optimize low-rank approximation first, refine gradually
4. **Genetic algorithms**: Population-based methods might explore better

**Limitation**: All remain computationally expensive for high-dimensional spaces

### For Parametric Methods

**Advantage**: ~15-parameter space makes global optimization tractable

**Implementable approaches**:
1. **Basin-hopping** (`scipy.optimize.basinhopping`)
   - Systematic exploration of multiple basins
   - Acceptance criterion prevents early trapping
   - Computationally feasible for ~15 parameters

2. **Nested sampling** (`ultranest`)
   - Full posterior distributions for parameters
   - Bayesian evidence for model comparison
   - Uncertainty quantification included

3. **Differential evolution** (`scipy.optimize.differential_evolution`)
   - Population-based global search
   - Robust to initial guesses
   - Parameter-free (self-adaptive)

**Status for Molass**: Implementation in progress (migration from legacy code)

### Hybrid Approaches

**Idea**: Combine strengths of both paradigms

**Example workflow**:
1. Parametric global optimization → identify peaks (position, width)
2. Constrained matrix factorization → refine with flexibility
3. Bayesian model comparison → select best representation

**Research question**: Does two-stage hybrid outperform pure approaches?

### Oligomer-Aware Parametric Models

**Mo2ivation**: Section 6 showed discrete oligomerization creates discrete local minima

**New research direction**: Structure-aware models for oligomeric series

**Key features**:
1. **Constrained scaling relationships**: $d_{max,n} = f(n) \cdot d_{max,monomer}$
2. **Intensity ratios**: $I_n \propto n$ (molecular weight)
3. **Shape constraints**: $P_n(q) \approx S_n(q) \cdot P_{monomer}(q)$
4. **Discrete state enumeration**: Explicitly model as 2-mer, 3-mer, 4-mer

**Advantages**:
- Reduce permutation ambiguity (fewer valid assignments)
- Leverage physical knowledge (oligomeric structure)
- Global optimization explores reduced discrete space

**Research questions**:
- Can oligomeric constraints resolve 30-50% ambiguity cases?
- How much prior knowledge required (monomer structure)?
- Performance vs. generic parametric models?

---

## 11. Relation to JOSS Validation

### This Repository's Purpose

**Core mission**: Document limitations of existing model-free methods to validate JOSS Research Impact Statement

**This document contributes**:
- ✅ Identifies a **documented limitation** (EFAMIX's explicit statement)
- ✅ Characterizes the **nature of the problem** (local vs. global minima)
- ✅ Explains why it's **unaddressed** (computational tractability)
- ✅ 3. Key Takeaways

### Research Findings

1. **EFAMIX explicitly avoids constraints** due to local minima → sacrifices physical correctness
2. **REGALS accepts local convergence** from single initialization → no optimality verification
3. **Permutation ambiguity = discrete local minima**: Each valid permutation is a separate local minimum basin
4. **Discrete mathematics mirrors discrete physics**: Permutation ambiguity reflects discrete oligomeric states
5. **Oligomeric series are hardest**: 30-50% ambiguity risk due to physical similarity of oligomers
6. **Dimensionality gap**: Model-free (~600 params) vs. parametric (~15 params) determines tractability
7
### Appropriate JOSS Framing

**In JOSS paper** (current wording is correct):
> "rigorous global optimization methods that constrain solutions using SEC theory"

**Interpretation**:
- Methods exist in principle (basin-hopping, nested sampling)
- Implementation status: In progress (honest about timeline)
- Claim: Parametric models **enable** this approach (architectural advantage)
- Not claiming: Proven superiority (would require benchmarking = new research)

---

## 12. Key Takeaways

### Established Facts

1. **EFAMIX explicitly avoids constraints** due to local minima → sacrifices physical correctness
2. **REGALS accepts local convergence** from single initialization → no optimality verification
3. **Dimensionality gap**: Model-free (~600 params) vs. parametric (~15 params) determines tractability
4. **35-year problem**: Acknowledged since Keller 1991, unaddressed in modern SAXS tools
5. **Permutation ambiguity exists**: 5-50% of datasets show component label uncertainty
6. **Oligomerization is discrete**: Physical chemistry fact

### Working Hypotheses (Require Validation)

1. **Permutation ambiguity = discrete local minima**: Each valid permutation may be a separate local minimum basin
2. **Discrete oligomerization causes discrete minima**: Physical discreteness may create mathematical discreteness
3. **Oligomeric series are hardest**: 30-50% ambiguity risk may be due to physical similarity creating degenerate assignments

### Scientific Implications

**For model-free methods** (established):
- Current tools provide **a** solution, not proven optimal
- Different initializations may yield different results (5-50% of cases)
- No systematic uncertainty quantification

**If hypothesis is correct** (speculative):
- Each valid permutation would be a separate local minimum
- Single initialization randomly selects one discrete branch
- No exploration of alternative permutations

**For parametric methods**:
- Low dimensionality makes global optimization **computationally feasible**
- Basin-hopping, nested sampling, differential evolution all tractable
- Enables systematic exploration of both continuous AND discrete minima
- Can evaluate all valid permutations systematically
- Enables systematic optimality verification

**Open research question**: 
> "How much does global vs. local optimization improve decomposition quality in practice?"

Answering this requires comparative benchmarking (beyond JOSS scope, future work).

---

## 13. Citations and References

### Primary Sources

1. *5EFAMIX**: Konarev et al. (2021), *Protein Science*, 31, 269-282
   - Quote (p. 272): "constraints may lead to several local minima in the search"
   - Source: [tools/extracted_papers.txt](../tools/extracted_papers.txt), line 515

2. **REGALS**: Meisburger et al. (2021), *IUCrJ*, 8, 225-237
   - ALS algorithm description (Methods section)
   - No discussion of global optimization or multiple initializations

3. **Keller 1991**: Keller & Massart (1991), *Chemom. Intell. Lab. Syst.*, 12, 209-224
   - Quote: "many local optima...not trivial to localize global optimum"
   - Source: [tools/efa_papers.txt](../tools/efa_papers.txt), lines 54-56

### Global Optimization Methods

1. **Basin-hopping**: Wales & Doye (1997), *J. Phys. Chem. A*, 101, 5111-5116
2. **Nested sampling**: Skilling (2006), *Bayesian Analysis*, 1, 833-859
3. **Differential evolution**: Storn & Price (1997), *J. Global Optim.*, 11, 341-359

### Related Analysis

- [REGALS_analysis_summary.md](../explorations/REGALS_analysis_summary.md) - Permutation ambiguity and local minima discussion
- [code_verification.md](regals/code_verification.md) - ALS convergence properties
- [PROJECT_STATUS.md](../PROJECT_STATUS.md) - Research context and timeline

---

## 14. Future Work

### Immediate Next Steps (This Repository)

1. **Validate core hypothesis**: Does permutation ambiguity actually create discrete local minima?
   - Generate SEC-SAXS data with known ground truth
   - Optimize from multiple random initializations
   - Check if different permutations are separate local minima (isolated basins)
   - Quantify barrier height between permutations
   - **Critical**: This empirical test determines if Sections 5-6 are correct

2. **Quantitative demonstration**: Create notebook showing local minima in synthetic data
   - Generate SEC-SAXS data with known 

4. **Oligomer-aware modeling**: Structure-constrained parametric models
   - Implement oligomeric scaling constraints ($d_{max,n} = f(n) \cdot d_{max,1}$)
   - Test on oligomeric series (monomer-dimer-trimer mixtures)
   - Quantify reduction in permutation ambiguity
   - Compare to generic parametric modelsground truth
   - Optimize from multiple random initializations
   - Visualize different local minima, quantify objective function differences
   - **Purpose**: Educational illustration of the problem (not claiming Molass superiority)

2. **Literature expansion**: Check if any SAXS papers discuss global optimization
   - Systematic search for "global optimization" OR "multiple initializations" in SEC-SAXS literature
   - Document if this gap is unique to SAXS or common across chemometrics

### Future Research (Beyond JOSS)

1. **Comparative benchmarking**: REGALS vs. parametric methods with global optimization
   - Controlled synthetic datasets with known ground truth
   - Multiple noise levels, peak overlaps, asymmetries
   - Metrics: accuracy, precision, computational cost
   - **Result**: Quantitative assessment of global optimization benefit

2. **Real data validation**: Apply to challenging SEC-SAXS datasets
   - Oligomeric series (trimer/tetramer/pentamer)
   - Heavy peak overlap (separation < 1 mL)
   - High asymmetry (τ > 2)
   - Cross-validate with orthogonal methods (AUC, mass spec)

3. **Hybrid methods**: Parametric initialization + matrix refinement
   - Use global parametric optimization to find peak positions
   - Initialize REGALS with parametric solutions
   - Compare hybrid vs. pure approaches

---

**END OF DOCUMENT**

---

**Document Status**: Research finding with speculative hypotheses, not for publication  
**Purpose**: Establish scientific foundation for future comparative studies  
**Attribution**: Analysis conducted January 23-24, 2026, with AI assistance (GitHub Copilot, Claude Sonnet 4.5)  
**Note**: Sections 1-4 based on documented facts from peer-reviewed literature. Sections 5-6 present working hypotheses requiring empirical validation. No claims of method superiority without benchmarking.
