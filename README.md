# Modeling vs Model-Free SEC-SAXS Analysis

This repository documents the comparative analysis of SEC-SAXS decomposition approaches, providing evidence for the **Research Impact Statement** in the Molass Library JOSS paper submission ([#9424](https://github.com/openjournals/joss-reviews/issues/9424)).

## Purpose

**Primary Goal**: To systematically validate claims about documented limitations of existing "model-free" methods (CHROMIXS, EFAMIX, REGALS) and demonstrate how Molass Library's explicit parametric modeling approach addresses these limitations for overlapping chromatographic peak decomposition.

**Scope**: This is an **evidence validation repository**, not a standalone research paper. Core work focuses on extracting and documenting evidence from peer-reviewed literature. Supporting mathematical and algorithmic analyses provide additional context but are not required for JOSS validation.

## Key Questions

1. **CHROMIXS**: Does it defer overlapping peak analysis to other methods as stated?
2. **EFAMIX**: What are the quantified failure thresholds (SNR, peak asymmetry, separation)?
3. **REGALS**: What fundamental limitations does it inherit from EFA (Evolving Factor Analysis)?
4. **Molass Library**: How does explicit parametric modeling widen the scope of tractable cases?

## Repository Organization

This repository separates **core validation work** from **supporting research**:

- **Core Work** (required for JOSS): `evidence/`, `molass/`, `tools/`, `reference_papers/`
- **Supporting Work** (valuable context): `explorations/`, `algorithms/`
- **Future Work** (archived): `archive/`

See [ORGANIZATION.md](ORGANIZATION.md) for detailed breakdown of core vs supporting work, or [PROJECT_STATUS.md](PROJECT_STATUS.md) for progress tracking.

## Status

**Phase**: JOSS validation evidence extraction (in progress)

- ✅ EFA limitations documented and verified (3/10 notebooks complete)
- ✅ Literature analysis complete (4 papers extracted and analyzed)
- ⏳ Method-specific evidence extraction (CHROMIXS, EFAMIX, REGALS) - next priority
- ✅ Supporting mathematical analysis complete (exceeds JOSS needs)
- ✅ Algorithm explorations complete (supporting context)

See [PROJECT_STATUS.md](PROJECT_STATUS.md) for detailed progress tracking and [ORGANIZATION.md](ORGANIZATION.md) for core vs supporting work clarification.
