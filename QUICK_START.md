# Quick Start Guide

**Purpose**: Fast orientation to repository structure and navigation

---

## 🎯 What is this repository?

**Research Mission**: Investigate the fundamental behavior of SEC-SAXS decomposition methods through mathematical analysis, computational experiments, and literature review to contribute to the SEC-SAXS community's understanding.

**Origin**: This work began as supporting evidence for the Molass Library JOSS paper ([#9424](https://github.com/openjournals/joss-reviews/issues/9424)), but evolved into broader research contributions.

**Current Status**: Mathematical foundations complete; literature evidence extraction in progress

---

## 📁 Directory Guide

```
modeling-vs-model_free/
│
├── 🔬 MATHEMATICAL FOUNDATIONS (Complete)
│   └── explorations/          Original research contributions
│       ├── orthogonal_invariance_overview.md  ⭐ START HERE
│       ├── orthogonal_invariance_journey.md   Full 9-stage narrative
│       ├── matrix_transformations_tutorial.ipynb
│       ├── smoothness_orthogonal_invariance_proof.ipynb
│       ├── discrete_ambiguity_demonstration.ipynb
│       ├── multiple_minima_diagnostic.ipynb
│       ├── problem_informed_Q_design.ipynb (90% breakthrough)
│       └── REGALS_analysis_summary.md
│
├── 📖 LITERATURE EVIDENCE (In Progress)
│   └── evidence/              Documented limitations from papers
│       ├── efa_original/      ✅ EFA limitations verified
│       ├── chromixs/          ⏳ CHROMIXS documentation
│       ├── efamix/            ⏳ EFAMIX thresholds
│       └── regals/            ⏳ REGALS architecture
│
├── 💻 ALGORITHM ANALYSIS (Complete)
│   └── algorithms/            Matrix factorization trends
│       ├── zhang2025_*.ipynb  Zhang 2025 analysis
│       └── temp_regals/       REGALS code verification
│
└── 📚 SUPPORTING MATERIALS
    ├── tools/                 PDF extraction utilities
    ├── reference_papers/      Bibliography (PDFs not in repo)
    ├── molass/                JOSS paper context
    └── archive/               Future research directions
```

---

## 🚀 Getting Started

### 📊 Just want the findings?
- **Start**: [orthogonal_invariance_overview.md](explorations/orthogonal_invariance_overview.md) (~15 min)
- **Deep dive**: Individual notebooks in `explorations/`
- **Summary**: README.md "Major Discoveries" section

### 🔍 Evaluating SEC-SAXS methods?
- **Practical guidance**: README.md "Impact" section
- **Documented limitations**: `evidence/` folder
- **Method comparison**: [REGALS_analysis_summary.md](explorations/REGALS_analysis_summary.md)

### 🧮 Want the mathematical details?
1. **Beginner**: [matrix_transformations_tutorial.ipynb](explorations/matrix_transformations_tutorial.ipynb)
2. **Overview**: [orthogonal_invariance_overview.md](explorations/orthogonal_invariance_overview.md)
3. **Technical**: [orthogonal_invariance_journey.md](explorations/orthogonal_invariance_journey.md)
4. **Reference**: [NOTATION_CONVENTION.md](NOTATION_CONVENTION.md)

### 🔬 Building on this research?
- Review [PROJECT_STATUS.md](PROJECT_STATUS.md) for current state
- Check "How to Cite" in README.md
- See `algorithms/` for implementations

### 📝 Continuing development?
- [PROJECT_STATUS.md](PROJECT_STATUS.md) - Current priorities
- Focus on literature evidence extraction (`evidence/`)
- See "What's Next" section below

---

## ⏭️ What's Next

**Current Focus**: Complete literature evidence documentation

1. **CHROMIXS** - Document limitations for overlapping peaks
   - Source: `tools/chromixs_paper.txt`
   - Target: `evidence/chromixs/`
   
2. **EFAMIX** - Extract quantified failure thresholds (SNR, τ, separation)
   - Source: `tools/efamix_paper.txt`
   - Target: `evidence/efamix/`
   
3. **REGALS** - Document two-stage architecture and EFA dependencies
   - Sources: `tools/extracted_papers.txt`, `tools/efa_papers.txt`
   - Target: `evidence/regals/`

**Then**: Consider preprint/manuscript preparation for broader dissemination

**Estimated Time**: 3-5 hours for evidence extraction

---

## 📊 Progress Summary

### ✅ Complete
- EFA limitations: 3/10 verified with notebooks
- Literature analysis: 4 papers extracted and analyzed  
- Mathematical foundations: Constraint hierarchy, permutation ambiguity, orthogonal invariance
- Algorithm exploration: Zhang 2025 analysis, REGALS code verification

### 🚧 In Progress
- Method-specific evidence extraction (CHROMIXS, EFAMIX, REGALS)
- Remaining EFA limitation notebooks (7 more planned)

### ⏳ To Do
- Synthesize findings for JOSS paper
- Update Research Impact Statement if needed

---

## 📚 Key Documents

| Document | Purpose | Read When |
|----------|---------|-----------|
| **README.md** | Repository overview | First visit |
| **ORGANIZATION.md** | Core vs supporting breakdown | Need structure clarity |
| **PROJECT_STATUS.md** | Detailed progress tracking | Resuming work, checking status |
| **QUICK_START.md** (this file) | Fast orientation | Need quick reference |
| **evidence/README.md** | Core validation structure | Starting evidence extraction |
| **explorations/README.md** | Mathematical work overview | Interested in theory |
| **algorithms/README.md** | Algorithm work overview | Interested in implementations |

---

## 🔗 Quick Links

- **GitHub Repo**: [biosaxs-dev/modeling-vs-model_free](https://github.com/biosaxs-dev/modeling-vs-model_free)
- **JOSS Context**: [Issue #9424](https://github.com/openjournals/joss-reviews/issues/9424)
- **Paper Updates**: [PAPER_UPDATES_SUMMARY.md](PAPER_UPDATES_SUMMARY.md)

---

## 💡 Key Insight

This repository reveals that **"model-free" is a misnomer**:
- All matrix factorization methods make modeling assumptions (proven mathematically)
- The difference is **transparency**: explicit parametric models vs. implicit regularization choices
- Understanding these hidden choices helps practitioners:
  - Select appropriate methods for their data
  - Recognize when results may be unreliable
  - Design better constraints for challenging cases

**Core finding**: Even with mathematically elegant regularization, optimization landscapes can have multiple comparable local minima—necessitating either global search strategies or additional physical constraints (like Molass's Rg-consistency and parametric models).
