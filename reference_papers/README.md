# Reference Papers

This folder contains PDF copies of papers cited in the evidence validation work. PDFs are .gitignored and managed elsewhere.

## Purpose

Maintain a local reference library for JOSS Research Impact Statement validation. Papers are used for quote extraction, method verification, and historical analysis.

## Papers

### Historical Foundation (EFA and MCR-ALS Origins)

**1980, Peter B. Moore**
- Moore, P.B. & Hendrickson, W.A. (1980). "Parsimony and the analysis of synchrotron X-ray scattering data from biological macromolecules." *Journal of Molecular Biology*, 152(4), 783-788.
- DOI: 10.1016/0022-2836(80)90053-6

**1988, Marcel Maeder**
- Maeder, M. & Zilian, A. (1988). "Evolving factor analysis, a new multivariate technique in chromatography." *Chemometrics and Intelligent Laboratory Systems*, 3(1-2), 205-213.
- DOI: 10.1016/0169-7439(88)80051-0
- **Key**: EFA invention paper documenting fundamental limitations

**1991, H.R. Keller**
- Keller, H.R. & Massart, D.L. (1991). "Evolving factor analysis." *Chemometrics and Intelligent Laboratory Systems*, 12(3), 209-224.
- DOI: 10.1016/0169-7439(91)80125-S
- **Key**: EFA tutorial explaining rank inflation and quantification impossibility

**2004, Joaquim Jaumot**
- Jaumot, J., Gargallo, R., de Juan, A., & Tauler, R. (2004). "A graphical user-friendly interface for MCR-ALS: a new tool for multivariate curve resolution in MATLAB." *Chemometrics and Intelligent Laboratory Systems*, 76(1), 101-110.
- DOI: 10.1016/j.chemolab.2004.09.007
- **Key**: MCR-ALS GUI tool establishing chemometrics tradition

**2011, Nicolas Gillis**
- Gillis, N. & Glineur, F. (2011). "Using underapproximations for sparse nonnegative matrix factorization." *Pattern Recognition*, 43(4), 1676-1687.
- DOI: 10.1016/j.patcog.2009.11.013
- **Key**: Theoretical foundation for NMF algorithms

### SEC-SAXS Method Development

**2016, S. P. Meisburger**
- Meisburger, S.P., Warkentin, M., Chen, H., Hopkins, J.B., Gillilan, R.E., Pollack, L., & Thorne, R.E. (2016). "Breaking the radiation damage limit with cryo-SAXS." *Biophysical Journal*, 104(1), 227-236.
- DOI: 10.1016/j.bpj.2012.11.3817
- **Key**: First MCR-ALS application to SEC-SAXS

**2018, Alejandro Panjkovich**
- Panjkovich, A. & Svergun, D.I. (2018). "CHROMIXS: automatic and interactive analysis of chromatography-coupled small-angle X-ray scattering data." *Bioinformatics*, 34(11), 1944-1946.
- DOI: 10.1093/bioinformatics/btx846
- **Key**: Automated EFA for well-separated peaks, explicitly defers overlapping cases

**2018, Mackenzie J. Parker** (main + appendix)
- Parker, M.J., Maggiolo, A.O., Thomas, W.C., Kim, A., Meisburger, S.P., Ando, N., Boal, A.K., & Stubbe, J. (2018). "An endogenous dAMP ligand in *Bacillus subtilis* class Ib RNR promotes assembly of a noncanonical dimer for regulation by dATP." *Proceedings of the National Academy of Sciences*, 115(20), E4594-E4603.
- DOI: 10.1073/pnas.1800356115
- **Key**: Application of MCR-ALS + smoothness regularization to AEX-SAXS

### Modern SAXS Tools

**2021, Petr V. Konarev**
- Konarev, P.V., Graewert, M.A., Jeffries, C.M., Fukuda, M., Cheremnykh, T.A., Volkov, V.V., & Svergun, D.I. (2021). "EFAMIX: A tool for the automated separation of an X-ray scattering curve from a mixture of component profiles." *Protein Science*, 31(1), 269-282.
- DOI: 10.1002/pro.4237
- **Key**: Quantifies EFA failure thresholds with specific parameters

**2021, Steve P. Meisburger** (main + supporting information)
- Meisburger, S.P., Xu, D., & Ando, N. (2021). "REGALS: a general method to deconvolve X-ray scattering data from evolving mixtures." *IUCrJ*, 8(2), 225-237.
- DOI: 10.1107/S2052252521000555
- **Key**: Regularized ALS framework generalizing beyond chromatography

**2023, Lingling Xu**
- Xu, L., Li, C., Ni, R., Wang, J., & Chen, Y. (2023). "Recent advances in computational modeling for X-ray scattering data analysis." *Current Opinion in Structural Biology*, 81, 102647.
- DOI: 10.1016/j.sbi.2023.102647
- **Key**: Review of modern computational approaches

**2024, Jesse B. Hopkins**
- Hopkins, J.B. (2024). "BioXTAS RAW 2: new developments for a free open-source program for small-angle scattering data reduction and analysis." *Journal of Applied Crystallography*, 57(1), 194-208.
- DOI: 10.1107/S1600576723011019
- **Key**: Latest SEC-SAXS analysis tool developments

### Matrix Factorization Theory

**2024, Peyman Milanfar**
- Milanfar, P. & Elad, M. (2024). "Denoising and Deblurring with Deep Learning: A New Era in Imaging." *IEEE Signal Processing Magazine*, 41(4), 46-60.
- DOI: 10.1109/MSP.2024.3392168
- **Key**: Modern deep learning approaches to matrix problems

**2024, Zeyu Han**
- Han, Z., Gao, J., Wang, X., Pang, Y., Liu, Y., & Lu, M. (2024). "Adaptive nonnegative matrix factorization with structural regularization for sensitive biomarker discovery in transcriptomics data." *Bioinformatics*, 40(3), btae082.
- DOI: 10.1093/bioinformatics/btae082
- **Key**: NMF with structural constraints in bioinformatics

**2025, Boyang Zhang**
- Zhang, B., Li, Y., Qi, F., & Yin, B. (2025). "Denoising analysis through explicit manifold structure." *SIAM Journal on Imaging Sciences*, 18(1), 150-185.
- DOI: 10.1137/24M1636838
- **Key**: Manifold-based denoising theory

## Organization

Papers are organized chronologically by first author's last name. Each file follows the format: `YEAR, First Author Last Name.pdf`

Supporting information (appendices) are marked with `-appendix` or `-support` suffix.

## Usage

These PDFs are extracted using [`tools/read_pdfs.py`](../tools/read_pdfs.py) for text analysis. Extracted content is saved to `tools/extracted_papers.txt`.

## Related Evidence

Evidence extracted from these papers is organized in:
- [`evidence/efa_original/`](../evidence/efa_original/) - EFA limitations verification
- [`evidence/chromixs/`](../evidence/chromixs/) - CHROMIXS claim validation
- [`evidence/efamix/`](../evidence/efamix/) - EFAMIX quantification verification
- [`evidence/regals/`](../evidence/regals/) - REGALS method verification
- [`evidence/historical_development.md`](../evidence/historical_development.md) - Complete historical narrative
- [`evidence/citation_dependency_graph.md`](../evidence/citation_dependency_graph.md) - Citation relationships

## Git Management

PDFs are excluded from version control via `.gitignore` and managed in a separate secure location. Only this README and the bibliography metadata are tracked in the repository.
