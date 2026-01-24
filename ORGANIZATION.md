# Repository Organization: Core vs Supporting Work

**Last Updated**: January 22, 2026  
**Purpose**: Clarify what's required for JOSS validation vs valuable supporting research

---

## Quick Reference

| Directory/File | Purpose | Status | Required for JOSS? |
|----------------|---------|--------|-------------------|
| **evidence/** | Direct validation of JOSS claims | 🚧 In progress | ✅ **YES - CORE** |
| **molass/** | JOSS paper submission | ✅ Complete | ✅ **YES - DELIVERABLE** |
| **tools/** | PDF extraction utilities | ✅ Working | ✅ **YES - UTILITIES** |
| **reference_papers/** | Source PDFs | ✅ Available | ✅ **YES - SOURCES** |
| **explorations/** | Mathematical deep dives | ✅ Complete | ❌ **NO - SUPPORTING** |
| **algorithms/** | Algorithm explorations | ✅ Complete | ❌ **NO - SUPPORTING** |
| **archive/** | Future research + process history | ✅ Archived | ❌ **NO - ARCHIVED** |

---

## Core Work (Required for JOSS Validation)

### 🎯 Primary Goal
Document evidence that existing "model-free" methods (CHROMIXS, EFAMIX, REGALS) have documented limitations for overlapping peak decomposition, which Molass Library addresses.

### 📁 Core Directories

#### `evidence/` - **CRITICAL**
Direct evidence extraction supporting Research Impact Statement claims:

- **efa_original/** ✅ COMPLETE
  - Limitations documented by EFA inventors (Maeder & Zilian 1988, Keller & Massart 1991)
  - Includes verification notebooks demonstrating limitations
  - Status: 3 of 10 limitations verified with notebooks
  
- **chromixs/** ⏳ TO DO
  - Evidence that CHROMIXS defers overlapping peak analysis
  - Target: Direct quotes from Panjkovich & Svergun (2018)
  
- **efamix/** ⏳ TO DO
  - Quantified failure thresholds (SNR, peak asymmetry, separation)
  - Target: Specific values from Konarev et al. (2021)
  
- **regals/** ⏳ TO DO
  - Two-stage architecture documentation
  - EFA limitation inheritance
  - Target: Method description from Meisburger et al. (2021)

#### `molass/` - **DELIVERABLE**
- `paper.md` - JOSS submission manuscript
- `paper.bib` - Citations

#### `tools/` - **UTILITIES**
- PDF extraction scripts
- Extracted text from papers (ready for evidence extraction)

#### `reference_papers/` - **SOURCES**
- Original PDFs of cited papers

---

## Supporting Work (Valuable but Not Required)

### 📊 Mathematical Foundations: `explorations/`

**Purpose**: Rigorous mathematical analysis exceeding JOSS validation needs

**Status**: ✅ Complete (January 17-22, 2026)

**Contents**:
1. **underdeterminedness_exploration.ipynb** - 4-level constraint hierarchy proof
2. **permutation_ambiguity_examples.ipynb** - Discrete ambiguity risk quantification (5-50%)
3. **smoothness_orthogonal_invariance_proof.ipynb** - Rigorous proof for D^k operators
4. **REGALS_analysis_summary.md** - Comprehensive mathematical critique

**Why Supporting?**
- Provides deep theoretical foundation
- Exceeds what JOSS reviewers require
- Demonstrates expertise but not necessary for validation
- May support future research publications

**Value**: Strengthens understanding of "model-free" claims and mathematical impossibility of assumption-free methods

---

### 🔬 Algorithm Research: `algorithms/`

**Purpose**: Exploration of modern matrix factorization trends (Zhang 2025)

**Status**: ✅ Complete (January 21-22, 2026)

**Contents**:
1. **zhang2025_simple_concept.ipynb** - Pedagogical 3×3 example
2. **zhang2025_joint_optimization_demo.ipynb** - Full demonstration
3. **zhang2025_denoising_comparison.ipynb** - Real SEC-SAXS data analysis
4. **matrix_factorization_trends_2025.md** - Comprehensive analysis and dual-evaluation approach
5. **temp_regals/** - REGALS code verification

**Why Supporting?**
- Explores algorithmic improvements (enhancement, not validation)
- Different scope: future improvements vs current limitations
- Tangential to JOSS validation needs

**Value**: Identifies potential future enhancements, clarifies architectural differences between methods

---

### 📚 Future Research & Process History: `archive/`

**Purpose**: Original broader research project planning + JOSS paper process documentation

**Status**: ✅ Archived (January 20-23, 2026)

**Contents**:
- `discussion_points.md` - Full research paper outline (future work)
- `detailed_approach.md` - 18-week research implementation plan (future work)
- `paper_revision_context.md` - JOSS paper revision rationale (Jan 20, 2026)
- `AI_assisted_maintenance_framework.md` - AI-readiness framework (Jan 20, 2026) → Condensed version now in molass-library/Copilot/
- `README.md` - Archive context

**Why Archived?**
- **Future research**: Original project scope was broader comparative study, postponed for post-JOSS
- **Process history**: Paper revision documents completed and replaced by actionable guide in molass-library

**Value**: 
- Roadmap for potential follow-up research publication after JOSS acceptance
- Historical record of decisions and their rationale

---

## Document Roles

### Core Documents

| Document | Role | Required? |
|----------|------|-----------|
| **README.md** | Repository purpose statement | ✅ YES |
| **PROJECT_STATUS.md** | Progress tracking & session log | ✅ YES |
| **evidence/README.md** | Validation structure overview | ✅ YES |

### Supporting Documents

| DoQUICK_START.md** | Fast orientation guide | ❌ NO (meta) |
| **explorations/README.md** | Mathematical work overview | ❌ NO |
| **algorithms/README.md** | Algorithm exploration overview | ❌ NO |
| **archive/README.md** | Archive context (future work + process history) | ❌ NO
|----------|------|-----------|
| **ORGANIZATION.md** (this file) | Core vs supporting clarification | ❌ NO (meta) |
| **QUICK_START.md** | Fast orientation guide | ❌ NO (meta) |

---

## Work Priorities

### Immediate Priority (JOSS Validation)

1. **Extract CHROMIXS evidence** → `evidence/chromixs/`
2. **Extract EFAMIX thresholds** → `evidence/efamix/`
3. **Document REGALS architecture** → `evidence/regals/`
4. **Complete EFA verification notebooks** (limitations 4-10)
5. **Update JOSS paper if needed** → `molass/paper.md`

**Estimated completion**: 5-10 hours of focused work

### Future Priority (After JOSS Acceptance)

All work in `explorations/`, `algorithms/`, and `archive/` provides foundation for:
- Full research paper (comparative study)
- Simulation studies
- Real data analysis
- Method selection guidance

**Estimated timeline**: 12-18 weeks (per `archive/detailed_approach.md`)

---

## How to Use This Repository

### For JOSS Reviewers/Editors
Focus on:
- `evidence/` - Direct validation of claims
- `molass/paper.md` - The submission
- `README.md` - Purpose statement

Skip:
- `explorations/` - Mathematical deep dives (optional reading)
- `algorithms/` - Algorithm explorations (tangential)
- `archive/` - Future research plans (not relevant to review)

### For Continuation of Work
Always read:
1. `PROJECT_STATUS.md` - Current state, session log, next steps
2. `ORGANIZATION.md` (this file) - What's core vs supporting
3. Relevant directory README - Context for specific area

### For Future Research
The `archive/` directory contains the original research agenda. After JOSS publication, this work can be resumed using:
- Mathematical foundations from `explorations/`
- Algorithm insights from `algorithms/`
- Evidence framework from `evidence/`

---

## Cross-Repository Workflow

### learnsaxs Integration

**Repository relationship**:
- **learnsaxs** (separate repo): Pedagogical SAXS education, pure teaching focus
- **modeling-vs-model_free** (this repo): JOSS validation, research hypothesis testing

**Work organization** (Option C - Split Approach):
- **Physics simulation** → Developed in learnsaxs (pedagogical focus)
- **Method validation** → Done in modeling-vs-model_free (research focus)

**Context transfer policy** (Combination of Options 1 + 4):

When creating notebooks in learnsaxs that support research questions here:

1. **Option 1 - Design Notes**: Create detailed technical specification
   - Example: `SEC-SAXS-DESIGN-NOTES.md` in learnsaxs repo
   - Contains: Physics equations, implementation guidance, success criteria
   - Audience: AI assistants, developers
   
2. **Option 4 - Context Cell**: Add brief context in notebook itself
   - Example: Use `NOTEBOOK-CONTEXT-CELL.md` template
   - Contains: Pedagogical purpose, research motivation link, scope clarification
   - Audience: Notebook users (students, researchers)

**Reference copy workflow**:
- `temp_learnsaxs/` in this repo is .gitignored (not version controlled)
- Copy FROM learnsaxs TO temp_learnsaxs/ as needed for AI context
- Automated in initialization: `Copy-Item -Recurse ..\learnsaxs\* temp_learnsaxs\ -Force`
- Master lives in learnsaxs, reference copy is disposable

**Data flow**:
```
learnsaxs repository:
  └─ Generate synthetic dataset with ground truth
     └─ Export as .npz with metadata
        └─ Copy to modeling-vs-model_free/evidence/synthetic_data/
           └─ Use for method validation notebooks here
```

---

## Summary

**Core = Evidence extraction for JOSS validation**  
**Supporting = Mathematical/algorithmic deep dives exceeding JOSS needs**  
**Archived = Future research beyond current scope**  
**learnsaxs = Separate pedagogical repo (physics simulation, teaching focus)**

This organization ensures focused progress on JOSS validation while preserving valuable supporting work for future use.
