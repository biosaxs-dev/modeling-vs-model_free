# EFA Limitations: Verification Notebooks

This directory contains systematic demonstrations of the **limitations of Evolving Factor Analysis (EFA)** as documented by its inventors (Maeder & Zilian 1988, Keller & Massart 1991).

**Purpose**: Provide empirical evidence for the Research Impact Statement in the JOSS submission for the Molass Library, specifically supporting the claim that modeling-based approaches address inherent limitations of EFA-based methods.

---

## 📚 Reference Documentation

- [**EFA_limitations_from_inventors.md**](../EFA_limitations_from_inventors.md) - Detailed documentation with original quotes and citations

---

## 🔬 Verification Notebooks

Each notebook demonstrates one limitation through synthetic and/or real SEC-SAXS data:

### ✅ Limitation 1: Baseline Problems
**Notebook**: [limitation_1_baseline_problems.ipynb](limitation_1_baseline_problems.ipynb)

**What it demonstrates**:
- Constant baseline offsets appear as "extra components" in SVD
- Rank inflation: 3 true components → 4 estimated components
- Why buffer subtraction is mathematically necessary, not optional

**Key finding**: Even small offsets (10% of signal) inflate apparent rank, confirming Maeder & Zilian's warning.

---

### ✅ Limitation 2: Noise Sensitivity
**Notebook**: [limitation_2_noise_sensitivity.ipynb](limitation_2_noise_sensitivity.ipynb)

**What it demonstrates**:
- Minor component detectability degrades with noise
- Eigenvalue gap (σ₃/σ₄) shrinks as SNR decreases
- Real SEC-SAXS data SNR measurements across 4 samples

**Key findings**:
- Real synchrotron data: SNR range 0.1–56.9 (average 16.3)
- Simulation SNR (10–100) is **optimistic** compared to real experiments
- At SNR=10, minor component barely distinguishable from noise

---

### ⏳ Limitation 3: Tailing Effects
**Notebook**: *(planned)* `limitation_3_tailing_effects.ipynb`

**Inventors' quote**: "The problem of tails is one of the most serious difficulties"

**What to demonstrate**:
- Peak tailing destroys FIFO assumption
- Forward/backward EFA give different results
- Concentration window estimates become unreliable

---

### ⏳ Limitation 4: No Quantification Without Calibration
**Notebook**: *(planned)* `limitation_4_calibration_required.ipynb`

**What to demonstrate**:
- EFA provides only "relative" concentrations
- Absolute quantification requires external calibration
- Cannot determine molar ratios from EFA alone

---

### ⏳ Limitation 5: Resolution Limitation
**Notebook**: *(planned)* `limitation_5_resolution_limits.ipynb`

**What to demonstrate**:
- Cannot resolve components that co-elute completely
- Eigenvalue gap disappears for highly overlapping peaks
- Distinction between "2 overlapping components" vs "1 broad component" impossible

---

### ⏳ Limitation 9: Rank Inflation
**Notebook**: *(planned)* `limitation_9_rank_inflation.ipynb`

**What to demonstrate**:
- Noise, tailing, baseline → extra eigenvalues
- Multiple sources of rank overestimation combine
- No reliable automated rank determination

---

### ⏳ Limitation 10: FIFO Assumption Failures
**Notebook**: *(planned)* `limitation_10_fifo_failures.ipynb`

**What to demonstrate**:
- Reversible binding, aggregation → FIFO violated
- EFA window estimation fails
- Re-equilibration during chromatography breaks assumptions

---

## 📊 Data Sources

- **Synthetic data**: Created with known ground truth (3-component Gaussian mixtures)
- **Real data**: Molass Tutorial datasets (SAMPLE1-4) from synchrotron SEC-SAXS (Photon Factory, KEK, Japan)

---

## 🎯 Key Takeaways

1. **EFA limitations are real**: Not theoretical concerns, but observable in controlled experiments
2. **Inventors documented honestly**: Original papers (1988–1991) clearly stated these issues
3. **Real data is harsher**: Synchrotron data SNR (avg 16.3) is worse than typical simulation worst-case (SNR=10)
4. **Baseline correction essential**: Not optional preprocessing, but mathematically necessary
5. **Noise affects minor components**: Detectability "strongly correlated with noise level" (confirmed)

---

## 🔗 Relationship to JOSS Submission

**Research Impact Statement** claims:
> "Molass introduces modeling-based approaches that address inherent limitations of EFA-based methods (EFAMIX, REGALS)"

**These notebooks provide empirical evidence by**:
1. Demonstrating each documented EFA limitation
2. Using both synthetic (controlled) and real (representative) data
3. Quantifying severity (e.g., SNR thresholds, rank inflation magnitude)
4. Establishing baseline for comparison with modeling-based approaches

---

## 📝 Notebook Structure

Each notebook follows this template:
1. **Introduction**: Quote from inventor papers, explain limitation
2. **Demonstration Strategy**: Clear test design
3. **Synthetic Data**: Controlled experiment with known ground truth
4. **Real Data** (when applicable): Measurements from actual SEC-SAXS
5. **Quantitative Analysis**: Metrics, thresholds, statistical summaries
6. **Visual Summary**: Comprehensive figures showing the limitation
7. **Conclusion**: Direct confirmation of inventor claims

---

## 🚀 How to Use

1. **Start with documentation**: Read [EFA_limitations_from_inventors.md](../EFA_limitations_from_inventors.md)
2. **Run notebooks sequentially**: Limitations 1-2 are complete
3. **Reproduce results**: All use fixed random seeds (np.random.seed(42))
4. **Cite appropriately**: Each notebook references original papers

---

## 📖 References

- Maeder, M., & Zilian, A. (1988). Evolving factor analysis, a new multivariate technique in chromatography. *Chemometrics and Intelligent Laboratory Systems*, 3(3), 205–213.
- Keller, H. R., & Massart, D. L. (1991). Evolving factor analysis. *Chemometrics and Intelligent Laboratory Systems*, 12(3), 209–224.
- Tauler, R. (1995). Multivariate curve resolution applied to second order data. *Chemometrics and Intelligent Laboratory Systems*, 30(1), 133–146.

---

## 🛠️ AI-Assisted Maintenance

This modular structure (one notebook per limitation) follows best practices documented in:
- [AI_assisted_maintenance_framework.md](../../AI_assisted_maintenance_framework.md)

**Benefits**:
- **Navigability**: Each notebook is self-contained and discoverable
- **Maintainability**: Changes to one limitation don't affect others
- **Citability**: Can reference specific limitations individually
- **Scalability**: Easy to add new limitations without restructuring

---

**Last Updated**: January 20, 2026  
**Status**: Limitations 1-2 complete, 3-6, 9-10 planned
