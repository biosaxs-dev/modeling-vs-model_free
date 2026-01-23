# Quick Start Guide

**Purpose**: Fast orientation to repository structure and current priorities

---

## 🎯 What is this repository?

**Primary Goal**: Validate Research Impact Statement claims for Molass Library JOSS paper ([#9424](https://github.com/openjournals/joss-reviews/issues/9424))

**Current Status**: Evidence extraction phase (core validation work in progress)

---

## 📁 Directory Guide

```
modeling-vs-model_free/
│
├── 🎯 CORE WORK (Required for JOSS validation)
│   ├── evidence/              Evidence extraction from papers
│   │   ├── efa_original/      ✅ EFA limitations (3/10 complete)
│   │   ├── chromixs/          ⏳ CHROMIXS deferral evidence
│   │   ├── efamix/            ⏳ EFAMIX thresholds
│   │   └── regals/            ⏳ REGALS architecture
│   ├── molass/                ✅ JOSS paper submission
│   ├── tools/                 ✅ PDF extraction utilities
│   └── reference_papers/      ✅ Source PDFs
│
├── 📚 SUPPORTING WORK (Valuable but not required)
│   ├── explorations/          ✅ Mathematical deep dives
│   │   ├── underdeterminedness_exploration.ipynb
│   │   ├── permutation_ambiguity_examples.ipynb
│   │   ├── smoothness_orthogonal_invariance_proof.ipynb
│   │   └── REGALS_analysis_summary.md
│   └── algorithms/            ✅ Algorithm explorations (Zhang 2025)
│       ├── zhang2025_simple_concept.ipynb
│       ├── zhang2025_joint_optimization_demo.ipynb
│       ├── zhang2025_denoising_comparison.ipynb
│       ├── matrix_factorization_trends_2025.md
│       └── temp_regals/       REGALS code verification
│
└── 📦 FUTURE WORK (Archived)
    └── archive/               ✅ Broader research agenda (post-JOSS)
        ├── discussion_points.md
        └── detailed_approach.md
```

---

## 🚀 Getting Started

### New to this project?
1. Read [README.md](README.md) - Repository purpose
2. Read [ORGANIZATION.md](ORGANIZATION.md) - Core vs supporting work breakdown
3. Read [PROJECT_STATUS.md](PROJECT_STATUS.md) - Detailed status and session log

### Continuing work?
1. Read [PROJECT_STATUS.md](PROJECT_STATUS.md) - "What's Remaining" section
2. Check priority: Focus on 🎯 **CORE** work first
3. See "Immediate Priorities" section for next steps

### Want to understand the math?
- See `explorations/` directory (📚 supporting work)
- Not required for JOSS, but provides rigorous foundations

### Want to understand algorithms?
- See `algorithms/` directory (📚 supporting work)  
- Zhang 2025 analysis and REGALS code verification

---

## ⏭️ Current Priority

**Next Task**: Extract method-specific evidence

1. **CHROMIXS** - Extract quotes showing deferral to other methods
   - Source: `tools/chromixs_paper.txt`
   - Target: `evidence/chromixs/`
   
2. **EFAMIX** - Extract quantified thresholds
   - Source: `tools/efamix_paper.txt`
   - Target: `evidence/efamix/`
   
3. **REGALS** - Document two-stage architecture
   - Sources: `tools/extracted_papers.txt`, `tools/efa_papers.txt`
   - Target: `evidence/regals/`

**Estimated Time**: 3-5 hours of focused extraction work

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

## 🎓 For JOSS Reviewers

Focus on:
- ✅ `evidence/` - Direct validation of claims
- ✅ `molass/paper.md` - The submission itself
- ✅ `README.md` - Purpose statement

Skip (supporting work, not required):
- ❌ `explorations/` - Mathematical deep dives
- ❌ `algorithms/` - Algorithm explorations  
- ❌ `archive/` - Future research plans

---

## 🔗 Quick Links

- **JOSS Issue**: [#9424](https://github.com/openjournals/joss-reviews/issues/9424)
- **GitHub Repo**: [biosaxs-dev/modeling-vs-model_free](https://github.com/biosaxs-dev/modeling-vs-model_free)

---

## 💡 Key Insight

This repository demonstrates that **"model-free" is a misnomer**:
- All methods require modeling assumptions (proven in `explorations/`)
- Difference is **transparency** of assumptions (explicit vs implicit)
- JOSS validation documents the **limitations** that implicit assumptions create
