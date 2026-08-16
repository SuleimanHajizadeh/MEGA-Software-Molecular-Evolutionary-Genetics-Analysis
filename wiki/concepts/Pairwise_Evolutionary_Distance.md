---
title: Pairwise Evolutionary Distance Models (JC69 & K2P)
type: concept
category: evolutionary-genetics
tags: [evolutionary-distance, jc69, k2p, jukes-cantor, kimura, nucleotide-substitution]
created: 2026-08-17
updated: 2026-08-17
sources: ["[[Phylo_Pipeline_Script]]", "[[COL1A1_Vertebrate_Phylogenetics_Dataset]]"]
---

# Pairwise Evolutionary Distance Models

## Overview
When comparing two homologous nucleotide sequences, the observed proportion of differences ($p$-distance) systematically **underestimates** the true number of evolutionary substitutions due to multiple substitutions at the same site ("multiple hits" / homoplasy) and back-mutations. Evolutionary distance models statistically correct for unseen mutations.

---

## 1. Jukes & Cantor (1969) Model — JC69

### Assumptions
- All 4 nucleotide base frequencies are equal: $\pi_A = \pi_T = \pi_C = \pi_G = 0.25$.
- All 12 substitution rates are identical ($\alpha$).

### Mathematical Derivation
The probability of an observed difference at a single site after time $t$ with substitution rate $\mu$ is:
$$p(t) = \frac{3}{4} \left(1 - e^{-\frac{8}{3} \mu t}\right)$$

Inverting this equation for the expected number of substitutions per site ($d = \mu t$):
$$d_{\text{JC69}} = -\frac{3}{4} \ln\left(1 - \frac{4}{3} p\right)$$
where $p = \frac{\text{Transitions } (P) + \text{Transversions } (Q)}{\text{Total non-gap sites}}$.

- **Boundary Condition**: If $p \ge 0.75$, sequences are completely randomized; $d \to \infty$.

---

## 2. Kimura 2-Parameter (1980) Model — K2P

### Biological Rationale
In real biological sequences, **transitions** ($A \leftrightarrow G, C \leftrightarrow T$, which preserve purine/pyrimidine ring geometry) occur at substantially higher rates than **transversions** ($A/G \leftrightarrow C/T$). K2P separates these two substitution classes.

### Formulation
Let:
- $P = \frac{N_{\text{transitions}}}{N_{\text{sites}}}$ (observed transition frequency)
- $Q = \frac{N_{\text{transversions}}}{N_{\text{sites}}}$ (observed transversion frequency)

The corrected evolutionary distance ($d_{\text{K2P}}$) is:
$$d_{\text{K2P}} = -\frac{1}{2} \ln(1 - 2P - Q) - \frac{1}{4} \ln(1 - 2Q)$$

- **Transition/Transversion Ratio**: $\kappa = \frac{P}{Q}$.
- **Boundary Condition**: If $1 - 2P - Q \le 0$ or $1 - 2Q \le 0$, saturation has occurred and $d \to \infty$.

---

## Benchmark Comparison Table

| Property | Observed $p$-distance | JC69 | K2P |
| :--- | :--- | :--- | :--- |
| **Correction for multiple hits** | ❌ No | ✅ Yes | ✅ Yes |
| **Transition/Transversion bias** | ❌ Ignored | ❌ Assumes $1:1$ | ✅ Explicit ($\kappa$) |
| **Parameters** | 0 | 1 | 2 |
| **Code Implementation** | Naive diff count | `jc69_distance()` | `k2p_distance()` |
| **Unit Test Coverage** | - | `test_jc69_standard_val` | `test_k2p_standard_val` |

## Related
- Tree Construction: [[Neighbor_Joining_Algorithm]], [[Phylogenetic_Reconstruction]]
- Complex Models: [[Substitution_Models]] (GTR+G+I)
- Source Implementation: [[Phylo_Pipeline_Script]]
- Dataset: [[COL1A1_Vertebrate_Phylogenetics_Dataset]]
