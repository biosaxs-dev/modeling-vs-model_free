# R-Centric Analysis Framework
**A Principled Approach to Matrix Factorization Analysis**

> **Why does this framework documentation exist?** This framework was created after hours of confusion caused by an implicit mental model. For the broader lesson about implicit frameworks in scientific collaboration and why making them explicit matters, see [`IMPLICIT_FRAMEWORKS_LESSON.md`](IMPLICIT_FRAMEWORKS_LESSON.md).

---

## The Core Principle

**Every matrix factorization discussion should be framed in terms of transformation matrix R.**

When analyzing any matrix factorization method (M = P·C), always ask:

### Three Key Questions

1. **What R does it assume?**  
   What constraints or structure does the method impose on the transformation matrix R = P_true^(-1)·P?

2. **What R can it find?**  
   What space of transformations can the method explore or discover?

3. **What R ambiguity remains?**  
   What transformation freedom persists even after applying all constraints?

---

## Why R-Centric Analysis?

### The Fundamental Relationship

Given ground truth factorization M = P_true · C_true, any other valid factorization M = P · C is related via:

```
P = P_true · R
C = R^(-1) · C_true
```

where R is the transformation matrix connecting the two factorizations.

### Why Focus on R?

1. **Unifies all factorization discussions**: Scale ambiguity, rotation ambiguity, permutation ambiguity—all are forms of R transformation
2. **Makes implicit explicit**: Forces articulation of what transformations are allowed vs forbidden
3. **Clarifies method differences**: Methods differ in how they constrain R, not just in their algorithms
4. **Reveals modeling choices**: Every constraint on R is an implicit modeling assumption

---

## Concrete Examples

### Method-Specific R Constraints

| Method | R Constraint | Transformation Space | Ambiguity |
|--------|-------------|---------------------|-----------|
| **REGALS** | Smoothness regularization | Orthogonal group O(n) | Continuous orthogonal transformations |
| **EFA** | Sequential elution (FIFO) | Sequential appearance/disappearance | Enforced by physical assumption |
| **Permutations** | Component label swapping | Permutation matrices | Discrete label choices |
| **Unconstrained** | None | All invertible matrices GL(n) | Infinite continuous ambiguity |

### Constraint Hierarchy (4 Levels)

From `explorations/underdeterminedness_exploration.ipynb`:

| Level | Constraints | R Space | Size of Ambiguity |
|-------|------------|---------|-------------------|
| 1 | Data-fit only | All invertible matrices GL(n) | ∞ (continuous) |
| 2 | + Smoothness regularization | Orthogonal transformations O(n) | ∞ (continuous) |
| 3 | + Non-negativity | Restricted orthogonal subset | Small |
| 4 | + Full REGALS constraints | 0 or small discrete set | 0 or discrete |

**Key insight**: Each constraint level further restricts the space of allowed R transformations.

---

## Pedagogical Example: Implicit vs Explicit R

From `explorations/matrix_transformations_tutorial.ipynb`:

### Part 8: Implicit R Visualization
- Shows amplitude-space trajectories during local optimization
- Displays transformed unit squares in amplitude space
- **R is implicit**: Never computed, only visible through its effect on (P, C)
- **Pedagogical challenge**: Hard to see what R is actually doing

### Part 9: Explicit R Computation
- Computes R_t = P_true^† @ P_t at each iteration
- Visualizes R's geometric evolution directly
- **R is explicit**: Shows actual transformation at each step
- **Pedagogical clarity**: Directly answers "What is R doing here?"

**The lesson**: Computing R explicitly rather than inferring from (P,C) trajectories provides immediate clarity about transformation structure.

---

## Application Guidelines

### When Analyzing Any Method

1. **Start with R**: Before discussing algorithms, ask "What R constraints does this method impose?"
2. **Make implicit explicit**: If the paper doesn't mention R, derive it yourself
3. **Compare R spaces**: Methods differ primarily in what R space they explore
4. **Check ambiguity**: After all constraints, what R freedom remains?

### When Writing/Reviewing

- **Replace vague terms**: "Rotation ambiguity" → "Orthogonal transformation ambiguity (R ∈ O(n))"
- **Be precise about spaces**: Specify what mathematical space R lives in
- **Connect to ground truth**: Always frame as transformation from P_true to P
- **Visualize explicitly**: Compute and plot R when possible, don't just infer

### When Teaching

- **Show R explicitly**: Compute R_t trajectories, don't just show (P,C) evolution
- **Build intuition**: Start with 2D/3D examples where R is a simple rotation/reflection
- **Connect to constraints**: Show how each constraint restricts R space
- **Use this framework**: Organize entire discussion around "What is R doing?"

---

## Historical Context

This framework emerged from January 24, 2026 session analyzing matrix_transformations_tutorial.ipynb pedagogical flow. After hours of discussion about why certain visualizations were confusing, the breakthrough came from recognizing:

> **The confusion was about implicit vs explicit R representation.**

Part 8 showed R implicitly (through amplitude trajectories), Part 9 computed R explicitly. The implicit representation created hours of confusion that evaporated once R was made explicit.

**The meta-lesson**: Implicit frameworks (the "implicit R" in our minds) cause communication breakdowns. Making R explicit in analysis prevents this confusion.

---

## Implementation in This Repository

### Initialization Protocol
When starting a new session: "Initialize: modeling-vs-model_free context"
- Reads README.md, ORGANIZATION.md, PROJECT_STATUS.md
- Loads R-centric analysis principle
- Ensures all future work uses this framework

### Documentation Updates
Three key files now organized around R:
1. **PROJECT_STATUS.md**: R-centric principle in initialization section
2. **explorations/REGALS_analysis_summary.md**: Section 0 frames entire analysis around R
3. **explorations/matrix_transformations_tutorial.ipynb**: Pedagogical note about implicit vs explicit R

### Future Work
All method analyses in this repository will:
- Start by asking the three key questions
- Explicitly compute or derive R when analyzing algorithms
- Frame comparisons in terms of R space constraints
- Document R ambiguity clearly

---

## References

**Within this repository**:
- `explorations/matrix_transformations_tutorial.ipynb` - Parts 8-9 (pedagogical example)
- `explorations/underdeterminedness_exploration.ipynb` - 4-level constraint hierarchy
- `explorations/REGALS_analysis_summary.md` - Section 0 (R-centric framework application)
- `PROJECT_STATUS.md` - Session log (Jan 24, 2026)

**Key insight sources**:
- User's hours of exploration (Jan 24, 2026)
- Matrix transformations pedagogical work
- Mathematical constraint hierarchy analysis
- Meta-reflection on implicit mental models

---

**Last Updated**: January 24, 2026  
**Status**: Framework established and integrated across repository
