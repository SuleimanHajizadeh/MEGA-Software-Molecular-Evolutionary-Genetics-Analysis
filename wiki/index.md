# 📚 LLM Wiki Catalog (Index)

Welcome to the central knowledge index. This catalog is automatically maintained and organized by category.

---

## 🧬 Entities

| Entity | Category | Description |
| :--- | :--- | :--- |
| [[COL1A1]] | Gene | Collagen Type I Alpha 1 chain; master structural marker across >450M yrs of vertebrate evolution. |
| [[Homo_sapiens]] | Organism | Human terminal node and primate comparative reference genome. |
| [[Pan_troglodytes]] | Organism | Chimpanzee; closest extant sister taxon to humans (~6–7 Mya divergence). |
| [[Mus_musculus]] | Organism | House mouse model organism; fast-evolving mammalian rodent clade. |
| [[Rattus_norvegicus]] | Organism | Brown rat model organism; rodent sister taxon to *Mus musculus* (~12–15 Mya). |
| [[Bos_taurus]] | Organism | Cattle model organism; Laurasiatherian mammalian reference node (~87.5 Mya). |
| [[Gallus_gallus]] | Organism | Chicken model organism; sauropsid/avian sister taxon to mammalian radiation (~310 Mya). |
| [[Xenopus_tropicalis]] | Organism | Western clawed frog; amphibian anamniote bridging teleosts and amniotes (~350 Mya). |
| [[Danio_rerio]] | Organism | Zebrafish model organism; basal vertebrate teleost outgroup (~450 Mya divergence). |
| [[MEGA12]] | Software | Molecular Evolutionary Genetics Analysis suite for alignment, model selection, ML/NJ trees, and RelTime. |
| [[ITOL]] | Software | Interactive Tree Of Life web visualization and tree annotation platform. |

---

## 🔬 Concepts & Methodologies

| Concept | Category | Description |
| :--- | :--- | :--- |
| [[Phylogenetic_Reconstruction]] | Methodology | End-to-end framework from sequence retrieval, alignment, to ML/NJ tree building and bootstrap validation. |
| [[Neighbor_Joining_Algorithm]] | Algorithm | Saitou & Nei (1987) $Q$-matrix bottom-up clustering and dynamic distance matrix reduction. |
| [[Pairwise_Evolutionary_Distance]] | Evolutionary Genetics | Closed-form derivations of JC69 ($1$-parameter) and K2P ($2$-parameter transition/transversion) distances. |
| [[Substitution_Models]] | Evolutionary Genetics | Mathematical models of nucleotide evolution (JC69, K2P, HKY, GTR+G+I) and rate heterogeneity. |
| [[Molecular_Clock_RelTime]] | Evolutionary Genetics | Relative rate molecular clock method for estimating divergence times without strict clock assumptions. |
| [[MEGA_File_Formats]] | Bioinformatics Tools | Specifications for `.meg`, `.mas`, `.mdsx`, `.mtsx`, and `.mao` analysis option formats. |

---

## 📁 Sources

| Source | Type | Summary |
| :--- | :--- | :--- |
| [[COL1A1_Vertebrate_Phylogenetics_Dataset]] | Dataset | Multi-species GenBank dataset across 7 vertebrate taxa analyzed via MUSCLE, ML (GTR+G+I), and RelTime. |
| [[Animal_Alignments_Dataset]] | Dataset | Multi-species 10-taxon animal alignment benchmark in native MEGA formats (`.meg`, `.mas`, `.mdsx`). |
| [[Phylo_Pipeline_Script]] | Code / Script | Pure-Python standalone phylogenetic distance & NJ pipeline (`scripts/phylo_pipeline.py`) with unit tests. |

---

## 💡 Syntheses & Analyses

| Synthesis | Category | Summary |
| :--- | :--- | :--- |
| [[Comparative_Phylogenetic_Frameworks]] | Analysis | Comparative evaluation of pure-Python NJ vs MEGA12 ML (GTR+G+I) and RelTime dating on COL1A1. |

---

## 📊 Maintenance & Graph Stats
- **Total Entities**: 11
- **Total Concepts**: 6
- **Total Sources**: 3
- **Total Syntheses**: 1
- **Last Ingest / Update**: 2026-08-17
- **Changelog**: See [[log]]
