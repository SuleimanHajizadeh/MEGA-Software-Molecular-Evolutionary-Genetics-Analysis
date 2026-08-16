---
title: MEGA12 (Molecular Evolutionary Genetics Analysis)
type: entity
category: software
tags: [software, bioinformatics, phylogenetics, sequence-alignment, tree-building]
created: 2026-08-17
updated: 2026-08-17
sources: ["[[COL1A1_Vertebrate_Phylogenetics_Dataset]]"]
---

# MEGA 12 (*Molecular Evolutionary Genetics Analysis*)

## Overview
**MEGA** (Molecular Evolutionary Genetics Analysis) is a comprehensive suite of statistical analysis tools for molecular phylogenetics, evolutionary rate testing, and sequence alignment.

## Core Capabilities
- **Multiple Sequence Alignment**: Embedded **MUSCLE** (Multiple Sequence Comparison by Log-Expectation) for progressive sequence alignment.
- **Model Selection (ModelTest)**: Evaluates 24+ nucleotide/amino acid substitution models using Bayesian Information Criterion (BIC) and Akaike Information Criterion (AIC).
- **Tree Inference**:
  - Maximum Likelihood (ML) with bootstrap resampling (e.g. 1000 replicates).
  - Neighbor-Joining (NJ) with evolutionary distance metrics (Kimura 2-Parameter, Jukes-Cantor).
- **Divergence Time Estimation**: Implementation of [[Molecular_Clock_RelTime|RelTime]], a computationally fast non-Bayesian method for dating evolutionary divergences without requiring strict clock assumptions.

## Related Entities & Concepts
- Gene Case Study: [[COL1A1]]
- Output Visualizer: [[ITOL]]
- Methodology: [[Phylogenetic_Reconstruction]]
- Evolutionary Metrics: [[Substitution_Models]]
