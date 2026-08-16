---
title: Neighbor-Joining (NJ) Algorithm
type: concept
category: methodology
tags: [neighbor-joining, saitou-nei, phylogenetics, algorithms, distance-matrix, q-matrix]
created: 2026-08-17
updated: 2026-08-17
sources: ["[[Phylo_Pipeline_Script]]", "[[COL1A1_Vertebrate_Phylogenetics_Dataset]]"]
---

# Neighbor-Joining (NJ) Algorithm

## Overview
The **Neighbor-Joining (NJ)** method (Saitou & Nei, 1987; Studier & Keppler, 1988) is a bottom-up clustering algorithm for reconstructing phylogenetic trees from an $n \times n$ pairwise evolutionary distance matrix. Unlike UPGMA, NJ does not assume a constant molecular clock (ultrametricity) and produces additive unrooted trees where branch lengths accurately represent varying evolutionary rates along different lineages.

---

## Step-by-Step Mathematical Formulation

### 1. The $Q$-Matrix (Neighbor Selection Criterion)
For $n$ active taxa with distance matrix $D$:
$$Q(i, j) = (n - 2) D(i, j) - R_i - R_j$$
where $R_i = \sum_{k=1}^n D(i, k)$ and $R_j = \sum_{k=1}^n D(j, k)$ are the net divergence sums of taxa $i$ and $j$ from all other taxa.

The pair $(i, j)$ with the minimum $Q(i, j)$ value represents the closest evolutionary neighbors relative to the rest of the tree.

### 2. Branch Length Computation to New Node $u$
When neighbors $i$ and $j$ are joined into a composite ancestral node $u$:
$$d(i, u) = \frac{1}{2} D(i, j) + \frac{R_i - R_j}{2(n - 2)}$$
$$d(j, u) = D(i, j) - d(i, u)$$

If $R_i = R_j$, the branch splits symmetrically ($D(i,j)/2$). If lineage $i$ has accumulated more mutations than $j$, $d(i, u) > d(j, u)$.

### 3. Distance Matrix Reduction
For every remaining taxon $k \neq i, j$, compute its distance to the new interior node $u$:
$$D(u, k) = \frac{D(i, k) + D(j, k) - D(i, j)}{2}$$

### 4. Iteration
Remove taxa $i$ and $j$ from the matrix, add node $u$, set $n \leftarrow n - 1$, and repeat until only 2 nodes remain. Join the final pair with branch lengths $D(1, 2)/2$.

---

## Algorithmic Complexity & Properties
- **Computational Complexity**: $O(n^3)$ without heuristic optimizations, $O(n^2)$ with fast candidate queues.
- **Additivity**: Guarantees reconstruction of the true tree topology if the distance matrix is additive.
- **Negative Branch Lengths**: Can occasionally occur due to sampling noise in real-world alignments; standard implementations clamp negative lengths to zero.

---

## Implementations in the Repository
- **Pure-Python CLI**: Implemented in [[Phylo_Pipeline_Script|phylo_pipeline.py]] using pure `numpy` matrix slicing.
- **Software Tool**: Implemented natively in [[MEGA12]] with pairwise deletion and bootstrap support.

## Related
- Distance Models: [[Pairwise_Evolutionary_Distance]], [[Substitution_Models]]
- Pipeline: [[Phylogenetic_Reconstruction]]
- Datasets: [[COL1A1]], [[COL1A1_Vertebrate_Phylogenetics_Dataset]]
