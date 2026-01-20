# EFA Limitations as Documented by Its Inventors

**Purpose**: Systematic extraction of limitations acknowledged by EFA inventors in their foundational papers.

**Relevance**: REGALS employs EFA as Stage 1, therefore inheriting these documented limitations.

---

## Source 1: Maeder & Zilian (1988) - Original EFA Paper

**Full Citation**: Maeder, M. and Zilian, A., 1988. Evolving factor analysis, a new multivariate technique in chromatography. *Chemometrics and Intelligent Laboratory Systems*, 3: 205-213.

### Section: CONCLUSIONS (pp. 211-213)

#### Limitation 1: Baseline Problems

**Quote** (p. 211):
> "It is essential to have a correct baseline [26]. Sloping baselines as well as flat baselines above or below zero simulate additional factors and therefore confuse the evolving factors analysis."

**Context**: 
- Single-beam diode-array detectors cause instabilities (light source flicker and drift)
- Solvent gradients cause drifting baseline due to changing refractive index
- Cannot be circumvented even with double-beam instruments

**Impact**:
- False factors detected
- Rank estimation becomes unreliable
- EFA confusion/failure

---

#### Limitation 2: Noise Sensitivity

**Quote** (p. 211):
> "Another characteristic problem is the noise which is unavoidably contained in any measurement."

**Quote** (p. 211):
> "The detectability of minor components in a peak cluster and the ability of discrimination between components with either very similar absorption spectra or concentration profiles obviously are strongly correlated with the noise level."

**Context**:
- Standard deviation in their example: ~3×10⁻⁴
- Noise level is instrument-dependent and cannot be improved by the chemist
- No simple general rules for detectability and discrimination power

**Impact**:
- Minor component detection limited
- Discrimination between similar components difficult
- Results highly instrument-dependent

---

#### Limitation 3: Tailing (Most Serious Problem)

**Quote** (p. 211):
> "(3) On the chromatographic side, **tailing seems to be the most serious difficulty** [26,27] and every possible effort has to be made to reduce this problem."

**Context** (p. 210):
> "The backward analysis (dotted lines and arrows) is impeded by severe tailing of the elution profiles... The tailing of the other compounds however is not detected correctly (the individual chromatograms of the compounds are known to show tailing)."

**Quote** (p. 210):
> "Tailing seems to be a nasty problem, not only in preparative chromatography, where subsequent components are polluted by the tails of the earlier ones, but also the attempts of deconvolution of overlapping peaks are severely hampered."

**Impact**:
- Concentration windows incorrectly determined in backward EFA
- Cannot detect true endpoint of elution
- Deconvolution severely hampered
- Affects both detection and quantification

---

#### Limitation 4: No Quantification Without External Calibration

**Quote** (p. 212):
> "As soon as a compound is identified and the molar absorptivities are known, a quantitative analysis can be accomplished."

**Quote** (p. 212):
> "It has to be pointed out again, that a quantitative analysis is only possible with the knowledge of the molar absorptivity at least at one wavelength. **EFA produces only the shapes and not the absolute heights of the spectra and profiles.**"

**Context**:
- Arbitrary rotation matrix means no absolute quantification
- Only relative profiles obtainable
- Requires external calibration for quantitative work

**Impact**:
- Not truly "automatic" - requires additional calibration
- Cannot provide quantitative results standalone

---

#### Limitation 5: Scope and Applicability Remain to be Investigated

**Quote** (p. 212):
> "Important questions remain to be investigated. The similarity of retention times and absorption spectra, the relative concentrations and the noise level of the instrument are all highly correlating factors which define the limits of the analysis. **Computer simulations have to be carried out and compared with extensive series of real experiments.**"

**Impact**:
- Limits not fully understood even by inventors
- Need for systematic study of failure conditions
- Uncertainty about practical applicability

---

## Source 2: Keller & Massart (1991) - EFA Tutorial

**Full Citation**: Keller, H.R. and Massart, D.L., 1992. Evolving factor analysis. *Chemometrics and Intelligent Laboratory Systems*, 12: 209-224.

### Section: 5. POSSIBLE LIMITATIONS (pp. 222-223)

#### Limitation 6: Rank Inflation from Instrumental Nonlinearities

**Quote** (p. 222):
> "Although DAD is generally considered to measure the complete spectrum simultaneously, strictly speaking this is not true. Even if the time needed to scan a spectrum is very short, typically 10-50 ms, this can lead to **nonlinearities in the system**, as has been demonstrated elsewhere [22]."

**Context**: Fig. 12 demonstrates how non-simultaneous measurement causes nonlinear relationship between wavelengths, leading to spurious second principal component for a pure compound.

**Impact**:
- Pure compounds appear as multiple components
- Rank overestimation

---

#### Limitation 7: Sloping and Non-Zero Baselines Cause Problems

**Quote** (p. 223):
> "As published by Maeder et al. [7] and confirmed by our own simulation studies, **sloping and non-zero baselines also cause problems**; these effects therefore need to be corrected before EFA based methods can be applied."

**Impact**:
- Preprocessing required
- Cannot be applied directly to raw data
- Pre-correction needed but may introduce new errors

---

#### Limitation 8: Heteroscedasticity and Calibration Nonlinearity

**Quote** (p. 223):
> "Analogously, **heteroscedasticity and calibration curve nonlinearity will also cause problems**. These effects lead to nonlinearities and more PCs will be necessary to describe a given system."

**Impact**:
- Additional false principal components
- Rank overestimation

---

#### Limitation 9: Rank of Data Matrix Higher Than Number of Chemical Species

**Quote** (p. 223):
> "In other words, **the rank of the data matrix will be higher than the number of underlying chemical species**. This has been confirmed by Gerritsen et al. [23]. The authors have shown that **in real world applications the number of PCs needed to describe a given system is higher than the number of underlying analytes**."

**Context**: This is the fundamental practical limitation - systematic rank inflation in real data.

**Impact**:
- Cannot reliably determine number of components
- False positives (detecting components that don't exist)
- Manual intervention required to distinguish true from false factors

---

#### Limitation 10: Requires Sequential Elution Assumption (FIFO)

**Quote** (p. 216, explaining concentration window determination):
> "Assuming that, in a good chromatogram, where the column is not overloaded and where the concentrations of the compounds are similar, **the substance that elutes first also leaves the detector first**, then the concentration window for the first compound starts at time 4 and ends at time 8."

**Context**: This is the fundamental First-In-First-Out (FIFO) assumption of EFA.

**Impact**:
- Fails for:
  - Column overload conditions
  - Very different concentrations
  - Tailing (as noted in Limitation 3)
  - Non-equilibrium chromatography
- Not generally valid for all separation modes

---

## Summary of EFA Limitations

### Categories of Limitations:

1. **Instrumental/Technical**:
   - Baseline drift and instabilities
   - Noise sensitivity
   - Non-simultaneous measurement artifacts
   - Heteroscedasticity

2. **Chromatographic**:
   - Tailing (most serious)
   - Column overload
   - Concentration ratio effects

3. **Fundamental/Mathematical**:
   - Rank inflation (real data always has higher rank than true number of components)
   - No quantification without external calibration
   - Arbitrary rotation matrix
   - Sequential elution assumption (FIFO)

4. **Practical**:
   - Requires preprocessing (baseline correction)
   - Manual validation needed
   - Limits not fully characterized even by inventors
   - Instrument-dependent performance

### Key Takeaway for JOSS Validation:

Since REGALS uses EFA as its Stage 1 (component detection and window determination), it **inherits all these documented limitations**. The inventors themselves acknowledged these are fundamental problems, not merely implementation issues. The statement that "rank of data matrix will be higher than number of underlying chemical species" in real applications is particularly critical, as it means EFA-based methods cannot reliably determine the true number of components without expert intervention.

---

## References from the Papers

[26] P.J. Gemperline, Target transform factor analysis with linear inequality constraints applied to spectroscopic-chromatographic data, Analytical Chemistry, 58 (1986) 2656-2663.

[27] J.K. Strasters, H.A.H. Billiet, L. de Galan, B.G.M. Vandeginste and G. Kateman, Evaluation of peak-recognition techniques in liquid chromatography with photodiode array detection, Journal of Chromatography, 385 (1987) 181-200.

[22] H.R. Keller, D.L. Massart, P. Kiechle and F. Erni, Effect of the scan time on methods based on evolving factor analysis in high-performance liquid chromatography, Analytica Chimica Acta, 256 (1992) 125-131.

[23] M.J.P. Gerritsen, N.M. Faber, M. van Rijn, B.G.M. Vandeginste and G. Kateman, Realistic simulations of HPLC-UV-Vis data for the evaluation of multivariate techniques, Chemometrics and Intelligent Laboratory Systems, 12 (1992) 257-268.
