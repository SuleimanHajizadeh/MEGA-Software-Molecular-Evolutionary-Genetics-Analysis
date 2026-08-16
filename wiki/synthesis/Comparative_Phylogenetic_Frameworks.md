---
title: Comparative Phylogenetic Frameworks — Pure-Python NJ vs MEGA12 ML & RelTime
type: synthesis
category: analysis
tags: [synthesis, comparative-analysis, maximum-likelihood, neighbor-joining, reltime, col1a1, benchmarks]
created: 2026-08-17
updated: 2026-08-17
sources: ["[[Phylo_Pipeline_Script]]", "[[COL1A1_Vertebrate_Phylogenetics_Dataset]]", "[[Animal_Alignments_Dataset]]"]
---

# Comparative Phylogenetic Frameworks: Pure-Python NJ vs. MEGA12 ML & RelTime

## Executive Summary
This synthesis evaluates the trade-offs, methodological congruence, and biological implications between two distinct phylogenetic workflows present in this repository:
1. **Algorithmic Distance-Based Reconstruction** implemented from scratch in pure Python via [[Phylo_Pipeline_Script|phylo_pipeline.py]] using [[Pairwise_Evolutionary_Distance|K2P distance]] and [[Neighbor_Joining_Algorithm|Saitou–Nei Neighbor-Joining]].
2. **Statistical Model-Based Reconstruction & Timetree Inference** implemented in [[MEGA12]] using [[Substitution_Models|GTR+G+I Maximum Likelihood]] and [[Molecular_Clock_RelTime|RelTime relative rate dating]].

---

## 1. Methodological & Computational Comparison

| Dimension | Pure-Python Pipeline (`phylo_pipeline.py`) | MEGA12 Pipeline |
| :--- | :--- | :--- |
| **Primary Method** | [[Neighbor_Joining_Algorithm|Neighbor-Joining (NJ)]] | Maximum Likelihood (ML) + [[Molecular_Clock_RelTime|RelTime]] |
| **Substitution Model** | [[Pairwise_Evolutionary_Distance|Kimura 2-Parameter (K2P)]] | [[Substitution_Models|General Time Reversible + Gamma + Invariant (GTR+G+I)]] |
| **Rate Heterogeneity** | Homogeneous across sites | $\Gamma$-distribution shape $\alpha = 0.412$ |
| **Invariant Sites** | Unmodeled ($I = 0$) | Estimated $I = 0.318$ (31.8% invariant) |
| **Computational Complexity** | $O(n^3)$ analytical calculation | Iterative numerical optimization ($O(\text{iterations} \cdot n \cdot L)$) |
| **Execution Time** | Sub-second runtime | Minutes (due to 1,000 bootstrap replicates) |
| **Visual Output** | Matplotlib dark-theme dual plot (dendrogram + distance heatmap) | Publication-ready [[ITOL]] vector graphics & chronogram |

---

## 2. Biological Insights from the COL1A1 Locus

Analysis of the [[COL1A1]] coding sequence across vertebrates reveals critical biological evolutionary dynamics:

```
[Deep Vertebrate Radiation: ~450 Mya]
     │
     ├── Danio rerio (Teleostei / Basal Outgroup)
     └── Tetrapoda Radiation (~365 Mya)
           │
           ├── Gallus gallus (Sauropsida / Avian)
           └── Mammalia Radiation (~87.5 Mya Calibration)
                 │
                 ├── Rodentia (Mus musculus, Rattus norvegicus)
                 ├── Artiodactyla (Bos taurus)
                 └── Primata (Pan troglodytes, Homo sapiens)
```

1. **Strong Purifying Selection**:
   - The estimated proportion of invariant sites ($I = 0.318$) in [[MEGA12]] ModelTest reflects the rigid structural constraints of the collagen triple helix. The requirement for a Glycine every third residue (`Gly-X-Y`) prevents non-synonymous substitutions in roughly one-third of all codon positions.
2. **Transition Bias**:
   - The transition/transversion ratio ($\kappa = 2.84$) confirms substantial transition bias, justifying the use of [[Pairwise_Evolutionary_Distance|K2P]] over JC69 for distance-based approximations.
3. **Topological Congruence**:
   - Both the fast pure-Python NJ pipeline and the GTR+G+I Maximum Likelihood pipeline recover identical high-level topological branching orders: basal positioning of *[[Danio_rerio]]*, sister divergence of *[[Gallus_gallus]]*, and clean resolution of the mammalian clade (*[[Homo_sapiens]]*, *Pan*, *Mus*, *Rattus*, *Bos*).

---

## 3. Conclusions & Recommendations
- **For Rapid Exploration & Verification**: Use [[Phylo_Pipeline_Script|phylo_pipeline.py]] for instant algorithmic distance matrix computation and headless testing.
- **For Evolutionary Rigor & Publication**: Use [[MEGA12]] ML (GTR+G+I) with 1,000 bootstrap replicates and export Newick trees to [[ITOL]] for annotated circular/linear figures.

## Related
- Entities: [[COL1A1]], [[Homo_sapiens]], [[Danio_rerio]], [[Gallus_gallus]], [[MEGA12]], [[ITOL]]
- Concepts: [[Neighbor_Joining_Algorithm]], [[Pairwise_Evolutionary_Distance]], [[Substitution_Models]], [[Molecular_Clock_RelTime]], [[Phylogenetic_Reconstruction]]
- Sources: [[Phylo_Pipeline_Script]], [[COL1A1_Vertebrate_Phylogenetics_Dataset]], [[Animal_Alignments_Dataset]]
