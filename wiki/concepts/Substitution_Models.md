---
title: Nucleotide Substitution Models
type: concept
category: evolutionary-genetics
tags: [substitution-models, gtr, jc69, k2p, gamma-distribution, invariant-sites]
created: 2026-08-17
updated: 2026-08-17
sources: ["[[COL1A1_Vertebrate_Phylogenetics_Dataset]]"]
---

# Nucleotide Substitution Models

## Overview
**Nucleotide Substitution Models** describe the statistical rates and probabilities of transitions ($A \leftrightarrow G, C \leftrightarrow T$) and transversions ($A,G \leftrightarrow C,T$) occurring over evolutionary time. Selecting the optimal model avoids both underfitting (biased branch lengths) and overfitting (excess parameters).

## Common Models Hierarchy

| Model | Unequal Base Frequencies? | Unequal Transition/Transversion Rates? | Variable Rate Across Sites? |
| :--- | :--- | :--- | :--- |
| **JC69** (Jukes-Cantor) | No (Equal $0.25$) | No ($\alpha = \beta$) | No |
| **K2P** (Kimura 2-Parameter) | No (Equal $0.25$) | Yes ($\kappa = \alpha/\beta$) | No |
| **HKY85** (Hasegawa-Kishino-Yano) | Yes ($f_A, f_T, f_C, f_G$) | Yes ($\kappa = \alpha/\beta$) | No |
| **GTR** (General Time Reversible) | Yes | Yes (6 reversible rate parameters) | No |
| **GTR+G+I** | Yes | Yes | **Yes** ($\Gamma$-distribution shape $\alpha$ + Invariant sites $I$) |

## Best-Fit for COL1A1 Dataset
Model selection via BIC in [[MEGA12]] selected **GTR+G+I**:
- **Gamma shape parameter ($\alpha$)**: $0.412$ (describes rate heterogeneity across codon positions).
- **Proportion of Invariant Sites ($I$)**: $0.318$ (31.8% of sites are under extreme purifying selection).
- **Transition/Transversion ratio ($\kappa$)**: $2.84$.
- **BIC Score**: $47,823.4$.

## Related
- Application: [[Phylogenetic_Reconstruction]]
- Datasets: [[COL1A1]], [[COL1A1_Vertebrate_Phylogenetics_Dataset]]
- Tools: [[MEGA12]]
