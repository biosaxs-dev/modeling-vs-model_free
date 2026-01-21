# Citation Dependency Graph: EFA → CHROMIXS → EFAMIX → REGALS

**Purpose**: Map logical dependencies between methods by analyzing what each paper cites and acknowledges.

**Date**: January 21, 2026

---

## Citation Network

```
EFA (1988, 1991)
    ↓
    ├→ CHROMIXS (2018) [No direct EFA citation visible]
    ├→ EFAMIX (2021) [Cites: Maeder 1987, Keller 1991]
    └→ REGALS (2021) [Cites: Maeder 1987]
```

---

## 1. EFA Foundation (1988, 1991)

### Original Papers
- **Maeder & Zilian (1988)**: "Evolving factor analysis, a new multivariate technique in chromatography"
  - *Chemometrics and Intelligent Laboratory Systems*, 3: 205-213
  
- **Keller & Massart (1991)**: "Evolving factor analysis"
  - *Chemometrics and Intelligent Laboratory Systems*, 12: 209-224

### Documented Limitations
1. Baseline problems → spurious factors
2. Noise sensitivity → minor component detection limits
3. **Tailing** (quote: "tailing seems to be the most serious difficulty")
4. No quantification without calibration → arbitrary rotation matrix
5. Rank inflation → "rank of data matrix will be higher than number of underlying chemical species"
6. Sequential elution assumption (FIFO)

---

## 2. CHROMIXS (2018)

### Full Citation
Panjkovich, A. & Svergun, D.I. (2018). "CHROMIXS: Automatic and interactive analysis of chromatography-coupled small-angle X-ray scattering data." *Bioinformatics*, 34(11), 1944–1946.

### What CHROMIXS Cites
**From extracted_papers.txt (lines 166-194):**
- Brookes et al. (2016) - US-SOMO HPLC-SAXS module
- Franke et al. (2017) - ATSAS 2.8 suite
- Hopkins et al. (2017) - BioXTAS RAW
- Jeffries et al. (2016) - Sample preparation
- Vestergaard (2016) - SAXS analysis overview

**No direct EFA citations found in extracted text** (may be in full references not extracted)

### What CHROMIXS Acknowledges

**From SAXS_methods_analysis.md:**
> "Works for 'well resolved fractions (i.e. baseline separated sample elution peaks)'"
>
> "For overlapping peaks: defers to REGALS, BioXTAS RAW, or UltraScan-SOMO"

**Interpretation**: CHROMIXS acknowledges it **cannot handle overlapping peaks** but doesn't explicitly cite EFA limitations as the reason.

---

## 3. EFAMIX (2021)

### Full Citation
Konarev, P.V., Graewert, M.A., Jeffries, C.M., Fukuda, M., Cheremnykh, T.A., Volkov, V.V. & Svergun, D.I. (2021). "EFAMIX, a tool to decompose inline chromatography SAXS data from partially overlapping components." *Protein Science*, 31, 269-282.

### What EFAMIX Cites

**From extracted_papers.txt (lines 1120-1170):**

**EFA original papers:**
- **6. Maeder M. (1987)**. "Evolving factor analysis for the resolution of overlapping chromatographic peaks." *Anal Chem*, 59:527–530.
- **7. Keller HR, Massart DL. (1991)**. "Evolving factor analysis." *Chemo Intellig Lab Syst*, 12:209–224.

**Other deconvolution methods:**
- 4. Tauler (1995) - MCR-ALS
- 5. Jaumot et al. (2004) - Multivariate resolution
- 11-14. Various chemometric SAXS papers (Herranz-Trillo, Bernado)

**Related SEC-SAXS tools:**
- **9. Hopkins et al. (2017)** - BioXTAS RAW
- **10. Tully et al. (2021)** - EFA deconvolution via scatter
- **15. Meisburger et al. (2021)** - REGALS
- **19. Panjkovich & Svergun (2018)** - CHROMIXS

### What EFAMIX Says About EFA

**From extracted_papers.txt (line 261):**
> "based on the evolving factor analysis (EFA)"

**From extracted_papers.txt (line 348):**
> "EFA is a model-free approach for analyzing matrices of..."

**Key statement from SAXS_methods_analysis.md:**
> "EFA does show limitations when applied to systems with significantly asymmetric concentration profiles"
>
> "potentially ambiguous" for overlapping peaks

**Quantified thresholds (from SAXS_methods_analysis.md):**
- Two components: SNR ≥ 10² photons, symmetric peaks (τ ≤ 2), concentration ratio ≤ 1:10
- Three components: SNR ≥ 10³ photons required
- Four components: SNR ≥ 10⁴ photons
- Peak separation ≥ 2× width, fails for asymmetric peaks (τ > 2)

**Interpretation**: EFAMIX **explicitly builds on EFA** (cites original papers) and **quantifies exactly where EFA breaks down**.

---

## 4. REGALS (2021)

### Full Citation
Meisburger, S.P., Xu, D. & Ando, N. (2021). "REGALS: a general method to deconvolve X-ray scattering data from evolving mixtures." *IUCrJ*, 8, 225–237.

### What REGALS Cites

**From extracted_papers.txt (lines 2645-2725):**

**EFA paper:**
- **Maeder M. (1987)**. *Anal Chem*, 59:527–530.

**MCR/Chemometrics:**
- Juan & Tauler (2003) - Multivariate curve resolution
- Jaumot et al. (2004, 2015) - MCR methods
- Various chemometric SAXS papers (Blobel 2009, Herranz-Trillo 2017, Ayuso-Tejedor 2011)

**Other tools:**
- Konarev et al. (2003) - ATSAS OLIGOMER
- Hopkins et al. (2017) - BioXTAS RAW

**Mathematical methods:**
- Hansen (2012) - Bayesian methods
- MacKay (1992, 1996) - Bayesian regularization
- Tikhonov regularization (implicit via methods)

### What REGALS Says About Prior Work

**From extracted_papers.txt (lines 1300-1365):**

> "matrix factorization techniques such as singular value decomposition (SVD)"
>
> "to recover the scattering from each component, the basis vectors from SVD must be recombined using prior knowledge"
>
> "multivariate curve resolution or MCR... alternating least-squares (MCR-ALS)"

**Key acknowledgment:**
> "However, to recover the scattering from each component, the basis vectors from SVD must be recombined using prior knowledge about what constitutes a physically valid solution."

**From REGALS_analysis_summary.md:**
- REGALS describes the ambiguity as "basis vectors can be mixed (or 'rotated') without changing χ²"
- States this applies to "any non-singular K×K matrix Ω"
- Uses quotes around "'rotated'" acknowledging informal language

**Interpretation**: REGALS **acknowledges the rotation ambiguity problem** (cites Maeder 1987) and proposes regularization as the solution.

---

## 5. Logical Dependency Analysis

### What Each Method Builds On

**CHROMIXS (2018)**:
- Builds on: Automated data processing workflows
- Acknowledges: Cannot handle overlapping peaks
- Solution: Defer to other tools (REGALS, BioXTAS RAW)
- **Does not explicitly cite EFA limitations**

**EFAMIX (2021)**:
- Builds on: **Pure EFA implementation** (directly cites Maeder & Keller)
- Acknowledges: EFA limitations with asymmetric peaks, overlap
- Solution: **Quantifies exact failure conditions** (SNR, τ, separation thresholds)
- Contribution: **Tests pure EFA** (Stage 1 only, no regularization)
- **Explicitly documents what EFA can and cannot do**

**REGALS (2021)**:
- Builds on: SVD/EFA + MCR-ALS methods (cites Maeder 1987)
- Acknowledges: Rotation ambiguity in SVD factorization
- Solution: **Two-stage architecture**
  - Stage 1: EFA-like component detection
  - Stage 2: **Regularized deconvolution** (smoothness + constraints)
- Contribution: **Adds regularization to resolve rotation ambiguity**

---

## 6. Historical Problem → Solution Evolution

### Timeline of Problem Recognition

**1987-1991: EFA Invented, Limitations Documented**
- Maeder & Keller identify: tailing, baseline, noise, rank inflation, no quantification
- Quote: "tailing seems to be the most serious difficulty"
- Quote: "rank of data matrix will be higher than number of underlying chemical species"

**2018: CHROMIXS - Practical Workaround**
- Automated for well-separated peaks
- Acknowledges: "Can't handle overlapping peaks"
- Solution: Defer to other methods (doesn't solve the problem)

**2021: EFAMIX - Quantification of Failure Modes**
- Pure EFA implementation
- Contribution: **Quantifies exactly where EFA fails**
  - SNR thresholds: 10² (2 comp) → 10⁴ (4 comp)
  - Asymmetry limit: τ ≤ 2
  - Separation requirement: ≥ 2× peak width
- Shows EFA limitations are **quantifiable** and **severe** for real data

**2021: REGALS - Regularization Solution**
- Acknowledges rotation ambiguity from SVD/EFA
- Solution: **Add Stage 2 regularization**
  - Smoothness penalties
  - Non-negativity constraints
  - Compact support
  - SAXS constraints
- Contribution: **Resolves rotation ambiguity through constraints**

---

## 7. Key Insights for Historical Narrative

### What Problems Were Recognized When?

1. **1988-1991**: EFA inventors identify all core limitations
   - Tailing/FIFO violations
   - Rank inflation
   - Rotation ambiguity (no quantification without calibration)
   - Noise sensitivity

2. **2018**: CHROMIXS acknowledges overlap problem
   - But doesn't explicitly connect to EFA limitations
   - Practical workaround: automate easy cases, defer hard ones

3. **2021**: EFAMIX quantifies EFA failure conditions
   - Makes explicit what was implicit in practice
   - Provides quantitative thresholds

4. **2021**: REGALS addresses rotation ambiguity
   - Cites Maeder (1987)
   - Explicitly describes mixing/rotation problem
   - Proposes regularization as solution

### What Problems Remain Unaddressed?

**From the papers themselves:**

1. **FIFO assumption**: Still present in EFA stage of REGALS
   - REGALS uses compact support windows (implicitly assumes sequential)
   - EFAMIX uses forward/backward EFA (explicitly FIFO)

2. **Rank inflation**: Not explicitly addressed
   - EFAMIX quantifies it
   - REGALS uses SVD but doesn't solve rank determination

3. **Tailing/overlap**: Partially addressed
   - REGALS smoothness regularization may help
   - EFAMIX quantifies limits (τ ≤ 2)
   - But fundamental FIFO problem remains

**This motivates Molass**: Explicit parametric models avoid FIFO assumption entirely

---

## 8. Citation Graph Summary

```
EFA (1988, 1991) - Foundation
  ├── Documented Limitations:
  │   ├── Tailing ("most serious")
  │   ├── Rank inflation (real data > true components)
  │   ├── Rotation ambiguity (arbitrary rotation matrix)
  │   ├── FIFO assumption
  │   └── Noise sensitivity
  │
  ├→ CHROMIXS (2018)
  │   ├── Acknowledges: Can't handle overlapping peaks
  │   ├── Solution: Defer to other tools
  │   └── Citation: No direct EFA citation (in extracted text)
  │
  ├→ EFAMIX (2021)
  │   ├── Cites: Maeder 1987, Keller 1991
  │   ├── Acknowledges: EFA limitations with asymmetry, overlap
  │   ├── Contribution: Quantifies failure conditions
  │   └── Solution: None - pure EFA implementation
  │
  └→ REGALS (2021)
      ├── Cites: Maeder 1987
      ├── Acknowledges: Rotation ambiguity from SVD
      ├── Contribution: Two-stage architecture
      └── Solution: Regularization (smoothness + constraints)
```

### Dependencies

- **CHROMIXS**: Independent automation tool, acknowledges overlap problem
- **EFAMIX**: **Direct descendant** of EFA (pure implementation)
- **REGALS**: **Builds on EFA/SVD** but adds regularization layer
- **Molass**: Addresses limitations REGALS inherits from EFA Stage 1

---

## 9. Next Steps

1. **Verify CHROMIXS full references**: Check if Maeder/Keller cited (not in extracted 3-page text)
2. **Extract specific quotes**: Get exact statements about rotation ambiguity from REGALS
3. **Build historical narrative**: Show evolution from problem recognition → quantification → partial solutions
4. **Identify gaps**: What problems remain unsolved that motivate Molass?

---

**End of Citation Analysis**
