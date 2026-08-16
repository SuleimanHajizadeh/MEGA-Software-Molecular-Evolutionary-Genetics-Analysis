---
title: Molecular Clock & RelTime Analysis
type: concept
category: evolutionary-genetics
tags: [molecular-clock, timetree, reltime, divergence-dating, mega12]
created: 2026-08-17
updated: 2026-08-17
sources: ["[[COL1A1_Vertebrate_Phylogenetics_Dataset]]"]
---

# Molecular Clock & RelTime Analysis

## Overview
The **Molecular Clock Hypothesis** posits that DNA and protein sequences evolve at rates that are relatively constant over time among related lineages. Because strict constancy is often violated due to lineage-specific metabolic and generation-time variations, relaxed clock and relative rate methods are used.

## RelTime Method in MEGA
**RelTime** is an algorithmic method implemented in [[MEGA12]] that estimates relative divergence times throughout a phylogenetic tree without:
1. Requiring specific statistical distributions for rate variation among lineages (unlike Bayesian MCMC methods).
2. Assuming a strict global molecular clock.

### Workflow & Calibration
1. **Input**: Maximum Likelihood tree topology with branch lengths.
2. **Calibration Point**: Known fossil or biogeographical constraints (e.g. Eutherian mammal radiation calibration at ~87.5 Mya).
3. **Output**: Dated chronogram / timetree (`.nwk`) with relative or absolute node ages and confidence intervals.

## Related
- Software: [[MEGA12]], [[ITOL]]
- Gene Example: [[COL1A1]]
- Pipeline: [[Phylogenetic_Reconstruction]]
