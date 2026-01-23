# REGALS Evidence

## Purpose

This folder contains evidence extraction and verification work for REGALS (Regularized Alternating Least Squares) to validate claims made in the JOSS paper Research Impact Statement.

## Contents

### method_verification.md
**Status**: ✅ **Complete** - Detailed verification of REGALS architecture and capabilities

**Key Findings**:
- ❌ **"Two-stage architecture" claim is incorrect** - REGALS uses iterative regularized ALS, not separate detection/resolution stages
- ✅ **Compact support is optional** - REGALS can use multiple regularization strategies (smoothness, d_max, boundary conditions)
- ⚠️ **More general than EFA** - Works for equilibrium titrations and time-resolved experiments, not just chromatography

**Contains**:
- Verification of 4 claims from historical_development.md
- Direct quotes from Meisburger et al. (2021) paper and supporting information
- Parameter tables from 4 datasets (BsRNR AEX-SAXS, PheH titration, MsbA time-resolved, CypA T-jump)
- Corrected characterization of REGALS method
- Implications for JOSS paper narrative

## Related REGALS Content

REGALS content is distributed across three locations based on purpose:

### 1. Evidence Extraction (This Folder) 🎯 CORE
**Path**: `evidence/regals/`
**Purpose**: Validate JOSS paper Research Impact Statement claims
**Contents**: method_verification.md

### 2. Mathematical Analysis 📚 Supporting
**Path**: [`explorations/REGALS_analysis_summary.md`](../../explorations/REGALS_analysis_summary.md)
**Purpose**: Deep mathematical analysis of constraint hierarchy
**Contents**: 4-level proof showing orthogonal invariance → regularization necessity
**Note**: Exceeds JOSS requirements but provides valuable theoretical foundation

### 3. Code Verification 📚 Supporting
**Path**: [`algorithms/temp_regals/`](../../algorithms/temp_regals/)
**Purpose**: Verify REGALS implementation and behavior
**Contents**: 
- `regals.py` - REGALS implementation
- `efa.py` - EFA comparison code
- `nifty.py` - Utilities
- Complete copy of REGALS repository subfolder (.gitignored)

**Documentation**: [code_verification.md](code_verification.md) - Detailed verification of REGALS alternating least squares implementation

## Primary Source

**Paper**: Meisburger, S.P., Xu, D., & Ando, N. (2021). REGALS: a general method to deconvolve X-ray scattering data from evolving mixtures. *IUCrJ*, 8, 225-237.

**DOI**: 10.1107/S2052252521000555

## Status

- ✅ Method architecture verification complete
- ✅ Key claims corrected
- ⏳ JOSS paper narrative update pending (incorporate corrected characterization)
