---
title: ITOL Visualizations & Publication Exports
type: source
category: dataset
tags: [dataset, itol, visualizations, vector-trees, svg, pdf, newick]
created: 2026-08-17
updated: 2026-08-17
raw_source: "results/itol_visualizations/"
---

# Source: ITOL Visualizations & Publication Exports

## Summary
The `results/itol_visualizations/` directory stores publication-ready vector and raster visualizations generated via [[ITOL]] (Interactive Tree Of Life) from tree topologies computed in [[MEGA12]].

## File Inventory & Specifications

| File | Format | Description |
| :--- | :--- | :--- |
| `Task 1 Newick Export.nwk` | Newick (`.nwk`) | Topology with branch lengths and node bootstrap support values for Task 1. |
| `Newick Export.nwk` | Newick (`.nwk`) | Unannotated parenthetical tree string for quick web import. |
| `Task 2.svg` | Scalable Vector Graphics | High-resolution publication vector graphic styled with node branch labels, customized branch strokes, and taxon coloring. |
| `Task 2(png).png` | Raster Bitmap | Rendered preview graphic for presentation and report embeds. |
| `Task 2(with ITOL the stylus for the phylogenetic tree).pdf` | PDF Document | Vector document export preserving exact typography and line geometry. |
| `sequence.fasta`, `sequence.meg` | Alignment Matrix | 54 KB multi-sequence dataset underpinning Task 1 & 2 visualizations. |
| `sequence.mdsx`, `sequence.mtsx` | MEGA XML Sessions | Preserved distance matrix and tree topologies. |

## Related Graph Nodes
- Tools: [[ITOL]], [[MEGA12]]
- Concepts: [[Phylogenetic_Reconstruction]], [[MEGA_File_Formats]]
- Datasets: [[COL1A1_Vertebrate_Phylogenetics_Dataset]], [[TRO_Seq_Dataset]]
