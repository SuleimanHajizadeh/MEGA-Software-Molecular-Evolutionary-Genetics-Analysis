---
title: Phylogenetic Reconstruction
type: concept
category: methodology
tags: [phylogenetics, bioinformatics, maximum-likelihood, neighbor-joining, alignment]
created: 2026-08-17
updated: 2026-08-17
sources: ["[[COL1A1_Vertebrate_Phylogenetics_Dataset]]", "[[Phylo_Pipeline_Script]]"]
---

# Phylogenetic Reconstruction

## Overview
**Phylogenetic Reconstruction** is the process of inferring evolutionary relationships, branch lengths, and ancestral divergence events among biological taxa using molecular sequence data (DNA, RNA, or amino acids).

## Standard Workflow

```
Raw Sequences (FASTA / Entrez) 
   │
   ▼
[Step 1] Sequence Alignment (MUSCLE / PairwiseAligner)
   │
   ▼
[Step 2] Distance / Model Selection (JC69, K2P, or ModelTest GTR+G+I)
   │
   ▼
[Step 3] Tree Topology Inference (Maximum Likelihood or Neighbor-Joining)
   │
   ▼
[Step 4] Statistical Validation (Non-parametric Bootstrapping)
   │
   ▼
[Step 5] Molecular Clock & Timetree Calibration (RelTime)
   │
   ▼
[Step 6] Visualization & Annotation (ITOL / Matplotlib)
```

## Key Inference Paradigms
1. **Maximum Likelihood (ML)**: Evaluates the statistical probability of observing the alignment given a specific tree topology and substitution model parameterization (e.g. [[Substitution_Models|GTR+G+I]]).
2. **Distance-Matrix Methods ([[Neighbor_Joining_Algorithm|Neighbor-Joining]])**: Computes [[Pairwise_Evolutionary_Distance|pairwise evolutionary distances (JC69, K2P)]] and iteratively clusters taxa using dynamic $Q$-matrix minimization.
3. **Statistical Validation**: Bootstrapping (500–1000 replicates) to calculate percentage confidence for each interior clade/node.

## Related
- Software & Code: [[MEGA12]], [[ITOL]], [[Phylo_Pipeline_Script]]
- Algorithms & Math: [[Neighbor_Joining_Algorithm]], [[Pairwise_Evolutionary_Distance]]
- Models: [[Substitution_Models]]
- Dating: [[Molecular_Clock_RelTime]]
- Case Study: [[COL1A1]]
