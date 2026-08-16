---
title: Pure-Python Phylogenetic Distance Pipeline (phylo_pipeline.py)
type: source
category: script
tags: [source, python, algorithms, jc69, k2p, neighbor-joining, pure-python, cli]
created: 2026-08-17
updated: 2026-08-17
raw_source: "scripts/phylo_pipeline.py"
---

# Source: Pure-Python Phylogenetic Distance Pipeline

## Summary
[`scripts/phylo_pipeline.py`](file:///Users/macbookairm2/Documents/GitHub/MEGA-Software-Molecular-Evolutionary-Genetics-Analysis/scripts/phylo_pipeline.py) is a standalone Python implementation of core phylogenetic distance estimation and tree reconstruction algorithms authored by Suleyman Hajizadeh for a Cambridge MPhil portfolio. It implements mathematical definitions of [[Pairwise_Evolutionary_Distance|JC69 and K2P]] models and the [[Neighbor_Joining_Algorithm|Saitou–Nei Neighbor-Joining]] method from scratch using only standard scientific libraries (`numpy`, `matplotlib`, `biopython`), bypassing third-party phylogenetics packages or GUI suites like [[MEGA12]].

## Architecture & Pipeline Components

```
1. Entrez Retrieval ──> 2. Pairwise Alignment ──> 3. Substitution Counting
   (Bio.Entrez)            (PairwiseAligner)         (Purines/Pyrimidines: P, Q)
                                                            │
                                                            ▼
6. Dual Output ◄────── 5. Matplotlib Tree & ◄───── 4. Distance Calculation
   (PNG + Terminal)        Distance Heatmap          (JC69 / K2P -> NJ Q-Matrix)
```

### 1. Sequence Retrieval (`fetch_sequences`)
- Connects to NCBI Entrez via `Bio.Entrez.efetch` (with 0.4s rate-limiting pause).
- Targets RefSeq accessions for 7 vertebrate model taxa across ~450 million years of divergence:
  - *Homo sapiens* (`NM_000088`), *Pan troglodytes* (`XM_016944896`), *Mus musculus* (`NM_007742`), *Rattus norvegicus* (`NM_053304`), *Gallus gallus* (`NM_204775`), *Danio rerio* (`NM_001004631`), *Xenopus tropicalis* (`NM_001016853`).

### 2. Pairwise Sequence Alignment & Substitution Categorization
- `align_pair()`: Global dynamic programming alignment via `Bio.Align.PairwiseAligner` (scores: Match $= +1$, Mismatch $= -1$, Gap open $= -2$, Gap extend $= -0.5$).
- `compute_alignment_counts()`: Iterates aligned columns, filters gap positions, and partitions differences into:
  - **Transitions ($P$)**: Purine $\leftrightarrow$ Purine ($A \leftrightarrow G$) or Pyrimidine $\leftrightarrow$ Pyrimidine ($C \leftrightarrow T$).
  - **Transversions ($Q$)**: Purine $\leftrightarrow$ Pyrimidine ($A/G \leftrightarrow C/T$).

### 3. Evolutionary Distance Estimation
- **JC69**: $d = -\frac{3}{4} \ln\left(1 - \frac{4}{3}p_{\text{total}}\right)$
- **K2P**: $d = -\frac{1}{2} \ln(1 - 2P - Q) - \frac{1}{4} \ln(1 - 2Q)$
- Returns `np.inf` if sequence divergence saturates beyond mathematical limits ($p \ge 0.75$ for JC69 or arguments $\le 0$).

### 4. Saitou–Nei Neighbor-Joining (`neighbor_joining`)
- Implements dynamic $Q$-matrix transformation for $n$ taxa:
  $$Q(i,j) = (n-2) D(i,j) - \sum_{k} D(i,k) - \sum_{k} D(j,k)$$
- Identifies pair $(i, j)$ minimizing $Q(i, j)$ and computes individual branch lengths to new node $u$:
  $$d(i, u) = \frac{D(i,j)}{2} + \frac{\sum_k D(i,k) - \sum_k D(j,k)}{2(n-2)}$$
  $$d(j, u) = D(i,j) - d(i, u)$$
- Dynamically reduces distance matrix and iterates until tree resolution.

### 5. Verification Suite (`tests/test_phylo.py`)
- Unit tests validating:
  - Zero-difference identity ($d=0.0$).
  - Expected analytical values for benchmark transition/transversion inputs.
  - Asymptotic saturation checks (infinite limit returns `np.inf`).
  - Correct classification of matches, transitions, transversions, and gap filtering.

## Related Wiki Graph Nodes
- **Entities**: [[COL1A1]], [[MEGA12]], [[ITOL]], [[Homo_sapiens]]
- **Concepts**: [[Neighbor_Joining_Algorithm]], [[Pairwise_Evolutionary_Distance]], [[Phylogenetic_Reconstruction]], [[Substitution_Models]]
