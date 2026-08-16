---
title: Cross-Species Animal Alignments Dataset (animals.meg)
type: source
category: dataset
tags: [dataset, animal-alignments, mega-format, cross-species, multiple-sequence-alignment]
created: 2026-08-17
updated: 2026-08-17
raw_source: "data/raw/animal_alignments/animals.meg"
---

# Source: Cross-Species Animal Alignments Dataset

## Summary
The `data/raw/animal_alignments/` directory contains multi-species nucleotide alignment benchmarks stored in native MEGA formats (`.meg`, `.mas`, `.mdsx`, `.mtsx`). It includes 10 taxa spanning Mammalia (*Homo sapiens*, *Canis lupus familiaris*), Reptilia (*Chelonia mydas*), and other vertebrate/invertebrate models across 839 aligned nucleotide positions.

## Format Specifications
- **MEGA Header**: `#MEGA`, `!Title animals;`, `DataType=Nucleotide`, `NSeqs=10 NSites=839`.
- **Character Conventions**: Identical base `.`, Missing data `?`, Alignment indel/gap `-`.
- **Associated MEGA Files**:
  - `animals.mas`: MEGA Alignment Session metadata.
  - `animals.mdsx`: MEGA Distance Session matrix.
  - `animals.mtsx`: MEGA Tree Session topology data.

## Represented Taxa & Case Studies
- *Homo sapiens* (`Homo_sapiens_9QB3_b`)
- *Canis lupus familiaris* (`Canis_lupus_familiaris_DN905699`)
- *Chelonia mydas* (Green sea turtle, `Chelonia_mydas_FI276988`)

## Related Graph Nodes
- Entities: [[Homo_sapiens]], [[MEGA12]]
- Concepts: [[Phylogenetic_Reconstruction]], [[Substitution_Models]], [[Pairwise_Evolutionary_Distance]]
