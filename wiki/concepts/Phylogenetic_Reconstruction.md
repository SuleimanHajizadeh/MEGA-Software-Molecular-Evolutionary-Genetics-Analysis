---
title: Phylogenetic Reconstruction
type: concept
category: methodology
tags: [phylogenetics, bioinformatics, maximum-likelihood, neighbor-joining, alignment]
created: 2026-08-17
updated: 2026-08-17
sources: ["[[COL1A1_Vertebrate_Phylogenetics_Dataset]]"]
---

# Phylogenetic Reconstruction

## Overview
**Phylogenetic Reconstruction** is the process of inferring evolutionary relationships, branch lengths, and ancestral divergence events among biological taxa using molecular sequence data (DNA, RNA, or amino acids).

## Standard Workflow

```
Raw Sequences (FASTA) 
   │
   ▼
[Step 1] Multiple Sequence Alignment (MUSCLE / Clustal)
   │
   ▼
[Step 2] Evolutionary Model Selection (BIC / AIC in ModelTest)
   │
   ▼
[Step 3] Tree Topology Inference (Maximum Likelihood / Neighbor-Joining)
   │
   ▼
[Step 4] Statistical Validation (Non-parametric Bootstrapping)
   │
   ▼
[Step 5] Molecular Clock & Timetree Calibration (RelTime)
   │
   ▼
[Step 6] Visualization & Annotation (ITOL)
```

## Key Inference Paradigms
1. **Maximum Likelihood (ML)**: Evaluates the statistical probability of observing the alignment given a specific tree topology and substitution model parameterization (e.g. [[Substitution_Models|GTR+G+I]]).
2. **Distance-Matrix Methods (Neighbor-Joining)**: Computes pairwise evolutionary distances (e.g., Kimura 2-Parameter, Jukes-Cantor) and progressively clusters neighbors.
3. **Statistical Validation**: Bootstrapping (500–1000 replicates) to calculate percentage confidence for each interior clade/node.

## Related
- Software: [[MEGA12]], [[ITOL]]
- Models: [[Substitution_Models]]
- Dating: [[Molecular_Clock_RelTime]]
- Case Study: [[COL1A1]]
