# 📜 Wiki Operation Log

Chronological, append-only log of all operations performed on the wiki (ingestions, syntheses, lint passes).

---

## [2026-08-17] init | LLM Wiki Architecture Initialized
- **Action**: Initialized the 3-layer LLM Wiki architecture (`raw/`, `wiki/`, `AGENTS.md`).
- **Created**:
  - [[index]]: Master catalog of the wiki.
  - [[COL1A1]]: Primary vertebrate structural gene entity.
  - [[MEGA12]]: Molecular Evolutionary Genetics Analysis software suite entity.
  - [[ITOL]]: Interactive Tree of Life visualization tool entity.
  - [[Phylogenetic_Reconstruction]]: Core methodology concept page.
  - [[Substitution_Models]]: GTR+G+I and nucleotide substitution models concept page.
  - [[Molecular_Clock_RelTime]]: RelTime relative dating concept page.
  - [[COL1A1_Vertebrate_Phylogenetics_Dataset]]: Initial repository dataset source page.
- **Summary**: Seeded foundational knowledge graph nodes from the repository's molecular evolutionary genetics and phylogenetics pipeline.

## [2026-08-17] ingest | Pure-Python Phylogenetic Pipeline (scripts/phylo_pipeline.py)
- **Source**: `scripts/phylo_pipeline.py` & `tests/test_phylo.py`
- **Created**:
  - [[Phylo_Pipeline_Script]]: Source documentation for standalone pipeline CLI, architecture, and verification.
  - [[Neighbor_Joining_Algorithm]]: Mathematical formulation of Saitou & Nei (1987) $Q$-matrix and branch length estimation.
  - [[Pairwise_Evolutionary_Distance]]: Analytical derivations of JC69 and K2P distance models.
- **Updated**:
  - [[Substitution_Models]]: Cross-referenced mathematical derivations and unit test benchmarks.
  - [[Phylogenetic_Reconstruction]]: Linked algorithmic distance methods and workflow steps.
  - [[index]]: Updated concept/source tables and graph metrics.
- **Summary**: Ingested pure-Python implementation of JC69, K2P, and Neighbor-Joining tree construction, extracting mathematical equations, code structures, and test assertions into the knowledge graph.

## [2026-08-17] ingest | Animal Alignments Dataset (data/raw/animal_alignments/animals.meg)
- **Source**: `data/raw/animal_alignments/animals.meg`
- **Created**:
  - [[Animal_Alignments_Dataset]]: Metadata and schema for 10-taxon vertebrate/invertebrate MEGA alignment benchmark.
  - [[Danio_rerio]]: Basal teleost outgroup entity.
  - [[Gallus_gallus]]: Avian / sauropsid sister clade entity.
- **Summary**: Ingested cross-species multi-alignment files and added species-level evolutionary reference nodes.

## [2026-08-17] synthesis | Comparative Phylogenetic Frameworks
- **Created**: [[Comparative_Phylogenetic_Frameworks]]
- **Updated**: [[index]]
- **Summary**: Synthesized algorithmic vs maximum-likelihood trade-offs, structural purifying selection on the COL1A1 locus ($I = 0.318$), transition bias ($\kappa = 2.84$), and divergence timing across the vertebrate tree.
