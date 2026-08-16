---
title: MEGA12 Example & Practice Benchmark Suite
type: source
category: dataset
tags: [dataset, mega12, benchmarks, practice, chloroplast, rtdt, timetree]
created: 2026-08-17
updated: 2026-08-17
raw_source: "data/practice/MEGA12_examples/"
---

# Source: MEGA12 Example & Practice Benchmark Suite

## Summary
The `data/practice/` directory contains standard benchmark datasets and practice sessions provided with [[MEGA12]] to validate molecular evolutionary algorithms, evolutionary rate tests, calibration models, and RelTime timetrees.

## Major Sub-Suites & Calibration Models

### 1. RelTime with Dated Tips (RTDT)
- Files: `reltime_with_dated_tips_RTDT_alignment.meg` (207 KB), `reltime_with_dated_tips_RTDT_sample_times.txt`, `reltime_with_dated_tips_RTDT_tree.nwk`, `reltime_with_dated_tips_RTDT_outgroup.txt`.
- Purpose: Benchmarking relaxed molecular clock dating when serial sample times / tip dates (e.g. viral isolates collected across decades) serve as calibration constraints instead of internal fossil nodes.

### 2. Mitochondrial DNA (mtCDNA) & Fossil Calibrations
- Files: `mtCDNA.meg`, `mtCDNA.nwk`, `mtCDNACalibration.txt`, `mtCDNACalibrationDensities.txt`, `mtCDNAOutgroup.txt`.
- Purpose: Demonstrating non-Bayesian divergence time estimation with boundary calibration densities on internal nodes.

### 3. Organellar & Gene Family Benchmarks
- `Chloroplast_Martin.meg` (155 KB): Plastid multi-gene evolution across plant lineages.
- `Drosophila_Adh.meg` (15.7 KB): Alcohol dehydrogenase locus for testing neutral theory and Tajima's $D$.
- `HLA-3Seq.meg`: Major Histocompatibility Complex locus testing positive selection and trans-species polymorphism.
- `Crab_rRNA.meg`, `D-loop_Vigilant.meg`: Ribosomal RNA and mitochondrial D-loop hypervariable region evolution.

## Related Graph Nodes
- Software: [[MEGA12]]
- Concepts: [[Molecular_Clock_RelTime]], [[MEGA_File_Formats]], [[Phylogenetic_Reconstruction]]
