---
title: Vector-Host Phylodynamics & Pathogen Surveillance
type: concept
category: epidemiology
tags: [phylodynamics, epidemiology, pathogen-tracking, vector-host, zoonosis, leishmaniasis]
created: 2026-08-17
updated: 2026-08-17
sources: ["[[TRO_Seq_Dataset]]", "[[Clinical_Bioinformatics_Presentation]]"]
---

# Vector-Host Phylodynamics & Pathogen Surveillance

## Overview
**Phylodynamics** blends phylogenetics, epidemiology, and population genetics to understand how pathogen transmission dynamics, host immune pressures, and vector biogeography shape genetic variation over space and time.

---

## The Vector-Reservoir-Host Model in TRO_Seq

In vector-borne zoonotic diseases like Leishmaniasis, pathogen lineages circulate across three interconnected biological compartments:

```
                  ┌──────────────────────────────┐
                  │   Insect Vector (Sandfly)    │
                  │   [[Phlebotomus_sergenti]]   │
                  └──────────────┬───────────────┘
                                 │
                 ┌───────────────┴───────────────┐
                 │                               │
                 ▼                               ▼
  ┌──────────────────────────────┐  ┌──────────────────────────────┐
  │      Vertebrate Reservoir    │  │       Accidental Host        │
  │ Procavia capensis / Canines  │  │       [[Homo_sapiens]]       │
  └──────────────────────────────┘  └──────────────────────────────┘
```

## Analytical Workflow for Phylodynamic Tracking
1. **Target Locus Sequencing**: High-resolution sequencing of hypervariable ribosomal internal transcribed spacer (ITS) or kinetoplast DNA (kDNA).
2. **Multiple Alignment & Tree Inference**: Generating Maximum Likelihood and Neighbor-Joining topologies via [[MEGA12]] to identify monophyletic geographic lineages vs cross-regional transmission events.
3. **Outbreak Source Attribution**: Determining whether local human clinical cases originate from domestic canine reservoirs, sylvatic rodent/hyrax reservoirs, or introduced strains.

## Related
- Datasets: [[TRO_Seq_Dataset]], [[Clinical_Bioinformatics_Presentation]]
- Entities: [[Phlebotomus_sergenti]], [[Trypanosomatida]], [[Homo_sapiens]], [[MEGA12]]
- Methodology: [[Phylogenetic_Reconstruction]], [[Molecular_Clock_RelTime]]
