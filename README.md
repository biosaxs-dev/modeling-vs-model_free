# Modeling vs Model-Free SEC-SAXS Analysis

This repository explores the fundamental behavior of SEC-SAXS decomposition methods through mathematical analysis, computational experiments, and literature review. **Our goal is to contribute to the SEC-SAXS community's understanding of when and why different approaches succeed or fail.**

## Purpose

**Research Mission**: To systematically investigate the mathematical foundations, implicit assumptions, and practical limitations of "model-free" matrix factorization methods (CHROMIXS, EFAMIX, REGALS) applied to overlapping chromatographic peaks, and to understand how explicit parametric modeling approaches can address these challenges.

**Scope**: This repository combines:
- **Original mathematical research** on regularization, optimization dynamics, and discrete ambiguity in SEC-SAXS decomposition
- **Computational experiments** validating theoretical insights with realistic data
- **Literature review** documenting known limitations from peer-reviewed sources

**Origin Note**: This work began as supporting evidence for the Molass Library JOSS paper ([#9424](https://github.com/openjournals/joss-reviews/issues/9424)), but evolved into broader research contributions relevant to the entire SEC-SAXS community, regardless of which tools practitioners use.

## Key Research Questions

1. **Mathematical Foundations**: What regularization constraints preserve which transformation ambiguities? How do optimization dynamics depend on objective function design?
2. **Method Behavior**: When do "model-free" approaches reliably recover correct component structures? What causes failure modes?
3. **Documented Limitations**: What do the inventors of EFA, CHROMIXS, EFAMIX, and REGALS say about their methods' applicability ranges?
4. **Practical Guidance**: What hidden modeling choices exist in "model-free" methods? How can practitioners make informed decisions about method selection?
5. **Alternative Approaches**: How do explicit parametric models address the mathematical challenges revealed by this analysis?

## Repository Organization

This repository is organized by research contribution type:

### Mathematical Foundations (`explorations/`)
Original research on regularization theory, optimization dynamics, and discrete ambiguity:
- Orthogonal invariance of smoothness constraints
- Multiple minima landscape characterization  
- Objective function design and operator choice
- Discrete permutation ambiguity and selection reliability
- **Start here**: [orthogonal_invariance_overview.md](explorations/orthogonal_invariance_overview.md) for 9-stage research journey summary

### Literature Evidence (`evidence/`)
Documented limitations from peer-reviewed sources:
- EFA limitations verified through computational experiments
- Method-specific evidence extraction (in progress)
- Historical development and citation analysis

### Algorithm Analysis (`algorithms/`)
Matrix factorization algorithm trends and REGALS code verification

### Supporting Materials
- `tools/`: PDF extraction utilities and extracted papers
- `reference_papers/`: Source materials
- `molass/`: JOSS paper context
- `archive/`: Future research directions

See [PROJECT_STATUS.md](PROJECT_STATUS.md) for detailed progress and [ORGANIZATION.md](ORGANIZATION.md) for complete structure.

## Key Findings & Status

### Major Discoveries ✓
- **Orthogonal invariance**: Smoothness regularization alone preserves infinite transformation families
- **Multiple minima landscape**: Fixed quadratic regularization creates optimization landscapes with many comparable local minima (validated across multiple optimizers)
- **λ-placement paradox**: Where regularization weights enter objective functions dramatically affects optimization success (25% vs 0%)
- **Discrete ambiguity**: Non-negativity constraints create topological barriers leading to permutation ambiguities requiring global search or initialization strategies
- **Frequency-domain breakthrough**: Problem-informed Q-matrix design achieves 90% reliability while maintaining mathematical elegance

### Current Status
- ✅ **Mathematical foundations complete**: 4 comprehensive notebooks + 9-stage research journey documented
- ✅ **EFA limitations verified**: Computational validation of inventor-documented constraints
- ✅ **Algorithm analysis complete**: Matrix factorization trends and code verification
- ⏳ **Method-specific evidence**: Extracting documented limitations from CHROMIXS, EFAMIX, REGALS papers

### Impact
These findings help practitioners understand:
- Why local optimization may fail even with "good" objective functions
- What initialization strategies methods like REGALS require and why
- How seemingly minor design choices (operator selection, Q-matrix structure) affect reliability
- When explicit constraints become necessary beyond generic regularization

### AI-Assisted Research
This research was conducted in close collaboration with **GitHub Copilot** (Claude Sonnet 4.5). The partnership between human domain expertise and AI capabilities enabled:
- Rapid exploration of mathematical concepts and computational experiments
- Systematic documentation of the 9-stage research journey
- Iterative refinement of theoretical insights through interactive dialogue
- Efficient code development and debugging for validation notebooks

**Transparency note**: All mathematical insights, experimental designs, and interpretations reflect the judgment of the human researcher, with AI serving as a collaborative tool for exploration, implementation, and documentation. This methodology aligns with JOSS requirements for AI attribution and provides readers insight into modern research workflows.

## How to Cite

If this work contributes to your research, please cite:

```
Takahashi, M., & Shimizu, N. (2026). Modeling vs Model-Free SEC-SAXS Analysis: 
Mathematical Foundations and Practical Limitations of Matrix Factorization Methods. 
GitHub repository. https://github.com/biosaxs-dev/modeling-vs-model_free
```

**BibTeX:**
```bibtex
@misc{takahashi2026modeling,
  author = {Takahashi, Masatsuyo and Shimizu, Nobutaka},
  title = {Modeling vs Model-Free SEC-SAXS Analysis: Mathematical Foundations 
           and Practical Limitations of Matrix Factorization Methods},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub repository},
  url = {https://github.com/biosaxs-dev/modeling-vs-model_free},
  note = {Research-in-progress with AI assistance (GitHub Copilot)}
}
```

**When to cite:**
- Using mathematical findings (orthogonal invariance, multiple minima landscape, λ-placement effects)
- Implementing frequency-domain Q-matrix design or other regularization strategies
- Discussing initialization requirements for SEC-SAXS decomposition
- Referencing documented method limitations (EFA, CHROMIXS, EFAMIX, REGALS)

**Status**: This is an active research repository with original contributions to SEC-SAXS methodology. A formal manuscript may be submitted for peer review in the future.

---

See [PROJECT_STATUS.md](PROJECT_STATUS.md) for technical details and research chronology.
