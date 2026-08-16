---
title: MEGA File Formats & Architecture (.meg, .mas, .mdsx, .mtsx, .mao)
type: concept
category: bioinformatics-tools
tags: [mega, file-formats, bioinformatics, alignment-session, tree-session, analysis-options]
created: 2026-08-17
updated: 2026-08-17
sources: ["[[COL1A1_Vertebrate_Phylogenetics_Dataset]]", "[[Animal_Alignments_Dataset]]"]
---

# MEGA File Formats & Architecture

## Overview
[[MEGA12]] utilizes a suite of specialized, structured file extensions designed for reproducibility, state persistence, and command-line execution (MEGA-CC / M7CC).

---

## File Format Specifications

| Extension | Format Name | Purpose & Content |
| :--- | :--- | :--- |
| **`.meg`** | MEGA Data File | Core aligned sequence or distance matrix format starting with `#MEGA` header, containing metadata directives (`!Title`, `!Format`, `!Domain=Data;`). |
| **`.mas`** | MEGA Alignment Session | Saves full alignment workspace state, undo history, translation tables, and MUSCLE/Clustal settings. |
| **`.mdsx`** | MEGA Distance Session (XML) | XML-based structured distance matrix storing pairwise evolutionary distances, variance estimates, and model parameters. |
| **`.mtsx`** | MEGA Tree Session (XML) | XML tree workspace containing topology, branch lengths, bootstrap confidence scores, and visual layout properties. |
| **`.mao`** | MEGA Analysis Options | Text configuration file specifying parameters (model, bootstrap count, rates across sites) for automated batch runs in MEGA-CC. |

---

## Structure of a `.meg` File

```text
#MEGA
!Title COL1A1_MultiSpecies;
!Format
   DataType=Nucleotide
   NSeqs=7 NSites=5540
   Identical=. Missing=? Indel=-;

!Domain=Data;
#Homo_sapiens
ATGTTCAGCT TTGTGGACCT CCGGCTCCTG CTCCTCTTAG CGGCC...
#Pan_troglodytes
ATGTTCAGCT TTGTGGACCT CCGGCTCCTG CTCCTCTTAG CGGCC...
```

## Related
- Software: [[MEGA12]]
- Visualizer: [[ITOL]]
- Datasets: [[Animal_Alignments_Dataset]], [[COL1A1_Vertebrate_Phylogenetics_Dataset]]
- Pipeline: [[Phylogenetic_Reconstruction]]
