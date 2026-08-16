---
title: COL1A1 Vertebrate Phylogenetics Dataset & Repository Benchmark
type: source
category: dataset
tags: [dataset, col1a1, genbank, mega12, itol, vertebrates]
created: 2026-08-17
updated: 2026-08-17
raw_source: "data/raw/col1a1_sequences/"
---

# Source: COL1A1 Vertebrate Phylogenetics Dataset

## Summary
The primary multi-species dataset of the *Collagen Type I Alpha 1* ([[COL1A1]]) gene, compiled from NCBI GenBank. Sequences span 7 representative vertebrate species from Teleostei (*Danio rerio*) through Aves (*Gallus gallus*) to Mammalia (*Homo sapiens*, *Pan troglodytes*, *Mus musculus*, *Rattus norvegicus*, *Bos taurus*).

## Key Information
- **Alignment Tool**: MUSCLE v3.8 (embedded in [[MEGA12]])
- **Aligned Matrix Location**: `results/col1a1_analysis/col1a1_aligned.meg`
- **Output Trees**:
  - Maximum Likelihood: `results/col1a1_analysis/col1a1_ml_tree.nwk` (GTR+G+I, 1000 bootstraps)
  - Timetree: `results/col1a1_analysis/col1a1_timetree.nwk` (RelTime dating)
- **Visualizations**: Publication-ready trees generated for [[ITOL]] in `results/itol_visualizations/`

## Key Entities & Concepts Connected
- Entities: [[COL1A1]], [[MEGA12]], [[ITOL]], [[Homo_sapiens]]
- Concepts: [[Phylogenetic_Reconstruction]], [[Substitution_Models]], [[Molecular_Clock_RelTime]]
