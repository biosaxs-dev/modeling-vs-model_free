# Permutation Selection Reliability Study
**Research Question**: How Reliable Are Model-Free Constraints at Selecting the Physically Correct Permutation?

**Created**: January 26, 2026  
**Status**: Proposed computational study  
**Context**: Emerged from discrete ambiguity demonstration analysis

---

## Executive Summary

Today's work ([discrete_ambiguity_demonstration.ipynb](discrete_ambiguity_demonstration.ipynb)) revealed that discrete permutation candidates exist due to topological disconnection in the transformation group GL(2). Local optimization finds ONE candidate without exploring alternatives.

**The Critical Question**:
> When discrete permutation alternatives exist, do model-free regularization constraints (smoothness, non-negativity, compact support) naturally prefer the physically correct permutation, or is selection arbitrary?

**Why This Matters**:
- **If reliable** (95%+ correct): Model-free approaches succeed implicitly → validate current practice
- **If unreliable** (inconsistent/wrong): Silent failure risk → need explicit validation or global optimization
- **Determines**: Whether local optimization is sufficient or global search required

---

## Background: The Selection Problem

### What We Know

1. **Discrete permutations exist**: 2-6 typically for 2-3 components
2. **Topologically disconnected**: Cannot reach each other without crossing singularity (det=0)
3. **Energy barriers**: Singularity creates barriers that trap local optimization in one basin
4. **Local optimization**: Finds whichever permutation basin it starts in
5. **Similar objectives**: Multiple candidates may have nearly identical χ², smoothness, etc.

### What We Don't Know

**Question 1 (Frequency)**: How often do multiple permutations satisfy all constraints equally well?
- Rare (5% of datasets)?
- Common (30-50%)?
- Nearly universal (>80%)?

**Question 2 (Selection Bias)**: When alternatives exist, do regularization constraints prefer correct permutation?
- Strongly (correct permutation has consistently better objective)?
- Weakly (small objective difference)?
- Not at all (arbitrary selection based on initialization)?

**Question 3 (Risk)**: What fraction of analyses might find wrong permutation with excellent fit?
- Negligible (<1%)?
- Notable (5-10%)?
- Substantial (>20%)?

---

## Proposed Computational Study

### Part 1: Synthetic Data with Known Ground Truth

**Objective**: Quantify selection reliability in controlled conditions

#### Test Cases

Generate SEC-SAXS data for:

1. **Well-separated peaks** (baseline resolved)
   - Expected: Low ambiguity, high reliability
   - Baseline: establish best-case performance

2. **Moderate overlap** (50% peak-to-peak distance / width)
   - Expected: Some ambiguity, test regularization effectiveness
   - Critical case: typical real-world scenario

3. **Heavy overlap** (30% separation or less)
   - Expected: High ambiguity, stress test
   - Worst case: reveals failure modes

4. **Similar components** (same MW class, similar d_max)
   - Expected: Maximum ambiguity
   - Critical for testing physical distinguishability

5. **Different SNR levels** (100, 50, 20, 10)
   - Expected: Noise affects basin structure
   - Realistic conditions

#### Ground Truth Design

For each test case:
```
True permutation: Component 1 elutes before Component 2
Known: Positions, widths, SAXS profiles, concentrations
```

#### Experimental Protocol

For each test case:

1. **Generate data**: M = P·C + noise with known ground truth

2. **Multiple initializations**: Run REGALS/similar from 20-50 different random starts
   - Random starting profiles
   - Random starting concentrations
   - Perturbed solutions from SVD

3. **Analyze convergence**: 
   - Which permutation did each run find?
   - What are the objective values?
   - Are objectives statistically different?

4. **Calculate reliability metrics**:
   ```
   Consistency = (runs with same permutation) / (total runs)
   Accuracy = (runs with correct permutation) / (total runs)
   Ambiguity = (number of distinct permutations found) / (possible permutations)
   ```

5. **Objective discrimination**:
   ```
   Δχ² = χ²_wrong - χ²_correct
   Δsmooth = smoothness_wrong - smoothness_correct
   Δtotal = objective_wrong - objective_correct
   ```

#### Expected Outcomes & Interpretation

**High Reliability Scenario**:
- Accuracy > 95%
- Δobjective statistically significant (p < 0.01)
- Regularization naturally prefers correct permutation
- **Conclusion**: Local optimization sufficient

**Moderate Reliability Scenario**:
- Accuracy 70-95%
- Small but consistent objective difference
- Some risk of wrong permutation
- **Conclusion**: Post-hoc validation recommended

**Low Reliability Scenario**:
- Accuracy < 70%
- No significant objective difference
- Selection essentially random
- **Conclusion**: Global optimization required

---

### Part 2: Real Data Multi-Start Analysis

**Objective**: Test reliability on actual experimental data

#### Dataset Selection

Use diverse SEC-SAXS datasets with:
- Well-characterized systems (known MW, structures)
- Different degrees of overlap
- Published results for comparison

Candidates:
- Molass validation datasets
- REGALS benchmark cases
- SASBDB entries with multi-component systems

#### Experimental Protocol

For each real dataset:

1. **Multi-start optimization**: Run 20+ times from different initializations

2. **Check consistency**:
   - Do all runs give same component assignment?
   - What is the spread in elution order?
   - Are properties (MW, Rg, d_max) consistent?

3. **Validate against prior knowledge**:
   - Do assignments match expected MW order?
   - Are SAXS profiles physically reasonable?
   - Do Guinier/Kratky plots make sense?

4. **Quantify ambiguity indicators**:
   - Objective value spread across runs
   - Component identity swapping frequency
   - Parameter uncertainty from multi-start

#### Expected Outcomes

**Consistent Results**:
- All runs give same permutation
- Properties match expectations
- **Interpretation**: This dataset has clear solution

**Inconsistent Results**:
- Different runs give different permutations
- Multiple solutions with similar objectives
- **Interpretation**: This dataset has selection ambiguity

**Aggregated Analysis**:
```
Ambiguous_fraction = (datasets with inconsistent results) / (total datasets)
```

---

## Connection to Validation Work

### For JOSS Paper

This study would provide:

1. **Quantitative assessment** of selection reliability
   - Not philosophical: empirical data on how often problem occurs

2. **Risk quantification** for practitioners
   - Under what conditions is multi-start recommended?
   - When is post-hoc validation essential?

3. **Method comparison** opportunity
   - Do explicit models (Molass) avoid ambiguity?
   - How does Molass reliability compare to REGALS?

4. **Practical guidance**
   - Workflow recommendations based on data characteristics
   - Validation checklists for component assignments

### For Broader Research Agenda

Beyond JOSS validation:

1. **Algorithm development**: Guides need for global optimization strategies

2. **Regularization design**: Test which constraints are most effective at disambiguation

3. **Uncertainty quantification**: Multi-start provides natural confidence intervals

4. **Benchmark creation**: Establishes test cases for new methods

---

## Implementation Plan

### Phase 1: Synthetic Data Study (2-3 weeks)

**Week 1: Setup**
- Design test case matrix (5 scenarios × 5 SNR levels = 25 conditions)
- Generate synthetic datasets with known ground truth
- Implement automated multi-start wrapper for REGALS

**Week 2: Computation**
- Run 20-50 initializations per test case
- Process results (convergence checking, permutation identification)
- Calculate reliability metrics

**Week 3: Analysis**
- Statistical analysis of objective differences
- Visualization of basins and convergence
- Identify factors affecting reliability

**Deliverable**: Comprehensive synthetic data report

### Phase 2: Real Data Study (2-3 weeks)

**Week 1: Dataset curation**
- Select 10-20 diverse SEC-SAXS datasets
- Document prior knowledge (MW, structures, expectations)
- Establish validation criteria

**Week 2: Multi-start analysis**
- Run 20+ initializations per dataset
- Check consistency and validate
- Compare to published results

**Week 3: Synthesis**
- Aggregate statistics across datasets
- Identify high-risk vs low-risk scenarios
- Develop practical guidelines

**Deliverable**: Real data validation report

### Phase 3: Method Comparison (1-2 weeks)

**Optional but valuable**:
- Apply same protocol to Molass
- Compare reliability metrics
- Document strengths/limitations of each approach

**Deliverable**: Comparative analysis

---

## Success Criteria

### Minimum Success

- **Frequency quantified**: Know how often ambiguity occurs
- **One reliability regime identified**: Document either high or low reliability
- **Practical guidance**: Recommend when multi-start/validation needed

### Full Success

- **All three questions answered**: Frequency, selection bias, risk
- **Both synthetic and real data**: Complete reliability assessment
- **Actionable recommendations**: Clear workflow guidance for practitioners
- **Method comparison**: Molass vs REGALS reliability characterized

---

## Resources Required

### Computational

- REGALS installation and configuration
- Python environment for automation
- Moderate compute (can run locally, ~100-200 CPU hours estimated)

### Data

- Synthetic: Generate using existing tools (learnsaxs utilities)
- Real: Publicly available (SASBDB, literature)

### Time

- Lead researcher: 6-8 weeks full-time equivalent
- Or: 12-16 weeks part-time
- Collaborative: Could be masters/PhD student project

---

## Risks and Mitigations

### Risk 1: REGALS Convergence Issues

**Risk**: Method might not converge reliably from poor initializations

**Mitigation**: 
- Use range of initialization strategies
- Document convergence failures separately
- This itself provides information about robustness

### Risk 2: Interpretation Ambiguity

**Risk**: Unclear how to identify "same" vs "different" permutation in output

**Mitigation**:
- Define quantitative permutation matching criteria
- Use correlation matrices between components
- Manual inspection of subset for validation

### Risk 3: Computational Cost

**Risk**: 20-50 runs × 25 test cases × multiple methods = large compute

**Mitigation**:
- Start with smaller test matrix
- Parallelize across conditions
- Focus on most informative cases first

---

## Open Questions for Discussion

1. **Scope**: Should we include other model-free methods (EFAMIX, MCR-ALS variants)?

2. **Metrics**: Are there better reliability measures than accuracy/consistency?

3. **Validation**: What constitutes "physically correct" for real data without known ground truth?

4. **Publication**: Is this a standalone paper or part of broader method comparison?

5. **Collaboration**: Would REGALS authors be interested in joint study?

---

## Expected Impact

### Scientific Contribution

**First systematic study** of permutation selection reliability in SEC-SAXS deconvolution:
- Quantifies implicit assumption that local optimization suffices
- Provides empirical data on regularization effectiveness
- Identifies conditions requiring additional validation

### Practical Impact

**Actionable guidance** for community:
- When to use multi-start optimization
- How to validate component assignments
- Risk assessment for different data characteristics

### Method Development Impact

**Informs algorithm design**:
- Need for global optimization strategies
- Importance of ambiguity detection
- Role of explicit vs implicit physical constraints

---

## Connection to Four Key Mathematical Foundations

This study directly applies insights from:

1. **[matrix_transformations_tutorial.ipynb](matrix_transformations_tutorial.ipynb)**: Understanding R transformations
   - Provides framework for identifying permutations
   - Explains constraint hierarchy effects

2. **[discrete_ambiguity_demonstration.ipynb](discrete_ambiguity_demonstration.ipynb)**: Topological disconnection
   - Explains WHY multiple basins exist
   - Shows singularity barrier structure

3. **[smoothness_orthogonal_invariance_proof.ipynb](smoothness_orthogonal_invariance_proof.ipynb)**: Regularization properties
   - Tests whether smoothness constraints disambiguate
   - Quantifies regularization effectiveness

4. **[R_CENTRIC_FRAMEWORK.md](../R_CENTRIC_FRAMEWORK.md)**: Analytical approach
   - Provides consistent framework for analysis
   - Guides interpretation of results

---

## Next Steps

**Immediate** (before starting study):
1. Discuss scope and priorities
2. Confirm available resources
3. Establish success criteria

**Near-term** (next 1-2 weeks):
1. Design detailed test case matrix
2. Set up computational infrastructure
3. Generate first batch of synthetic data

**Medium-term** (next 2-3 months):
1. Execute Phase 1 (synthetic)
2. Execute Phase 2 (real data)
3. Optional Phase 3 (method comparison)

**Long-term**:
1. Write up results
2. Integrate into JOSS evidence or separate publication
3. Develop practical guidelines document

---

## Preliminary Hypothesis

Based on today's theoretical analysis, I hypothesize:

**For well-separated peaks** (>1.5× peak width):
- High reliability (>95% accuracy)
- Regularization constraints sufficient
- Local optimization adequate

**For moderate overlap** (0.5-1.5× separation):
- Moderate reliability (70-90% accuracy)
- Depends on component similarity
- Multi-start recommended

**For heavy overlap** (<0.5× separation, similar components):
- Low reliability (<70% accuracy)
- High ambiguity
- Global optimization or explicit validation required

**This study would test these hypotheses empirically.**

---

**Status**: Proposal ready for discussion and refinement

**Next**: Decide on priority, scope, and timeline
