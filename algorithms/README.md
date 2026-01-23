# Algorithm Explorations

**Status**: ✅ Complete (January 21-22, 2026)  
**Purpose**: Supporting analysis - **NOT required for JOSS validation**  
**Relevance**: Background research on matrix factorization trends

---

## Overview

This directory contains explorations of **matrix factorization algorithms** and their relevance to SEC-SAXS decomposition. While these analyses provide valuable context about modern algorithmic approaches, **they are not directly required for the JOSS Research Impact Statement validation**.

---

## Contents

### Zhang 2025 Analysis

**Paper**: Zhang et al. (2025) "Loss-Minimizing Model Compression via Joint Factorization Optimization"

**Notebooks**:
- **zhang2025_simple_concept.ipynb** - 3×3 pedagogical example demonstrating gradient·noise insight
- **zhang2025_joint_optimization_demo.ipynb** - 100×50 full demonstration showing 1.7% improvement over SVD
- **zhang2025_denoising_comparison.ipynb** - Real SEC-SAXS data comparison (SVD vs joint optimization)

**Documentation**:
- **matrix_factorization_trends_2025.md** - Comprehensive analysis of Zhang 2025 relevance to Molass and REGALS

**Key Finding**: Zhang 2025 critiques two-stage approaches (denoise → optimize). Molass uses this architecture; REGALS avoids it through implicit denoising via IFT regularization. Pragmatic solution: dual-evaluation approach (optimize on clean, validate on noisy).

### REGALS Code Analysis

**Directory**: `temp_regals/`

**Contents**:
- **REGALS_code_verification.md** - Verification that REGALS uses Alternating Least Squares with closed-form solutions
- **regals.py**, **efa.py**, **nifty.py** - Extracted code for analysis

**Purpose**: Understanding REGALS implementation details to support comparisons with Zhang 2025's simultaneous optimization approach.

---

## Relationship to JOSS Validation

### ❌ NOT Core to Validation

These explorations are **tangential** to the main JOSS validation work:
- JOSS requires documenting **existing method limitations** (CHROMIXS, EFAMIX, REGALS)
- These notebooks explore **algorithmic improvements** (Zhang 2025's joint optimization)
- Different scope: validation vs enhancement

### ✅ Valuable Context

While not required, these analyses:
- Demonstrate deep understanding of the field
- Identify potential future improvements for Molass
- Clarify architectural differences between methods
- Support broader research agenda (see `archive/`)

---

## Completion Status

| Item | Status | Notes |
|------|--------|-------|
| Zhang 2025 simple concept | ✅ Complete | Pedagogical 3×3 example |
| Zhang 2025 full demo | ✅ Complete | 100×50 optimization trajectory |
| Zhang 2025 real data | ✅ Complete | SEC-SAXS with smoothness objective |
| REGALS code verification | ✅ Complete | ALS structure confirmed |
| Moore 1980 IFT analysis | ✅ Complete | Understood implicit denoising |
| Dual-evaluation approach | ✅ Documented | Pragmatic solution for Molass |

**Summary**: Algorithm exploration complete. Ready to return to core JOSS validation priorities.

---

## Usage

These notebooks require:
- Python packages: numpy, matplotlib, scipy
- molass_data package (for real SEC-SAXS data in zhang2025_denoising_comparison.ipynb)

Run with global Python 3.13:
```powershell
& "C:\Program Files\Python313\python.exe" -m jupyter notebook
```

---

## See Also

- **Core validation work**: See `../evidence/` directory
- **Mathematical foundations**: See `../explorations/` directory  
- **Future research agenda**: See `../archive/` directory
- **Project status**: See `../PROJECT_STATUS.md`
