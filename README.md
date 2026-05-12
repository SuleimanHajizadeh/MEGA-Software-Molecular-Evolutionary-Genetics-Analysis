# 🧬 Molecular Evolutionary Genetics Analysis — MEGA12 & ITOL Pipeline

[![MEGA](https://img.shields.io/badge/Tool-MEGA_12-darkgreen?style=flat-square)](https://www.megasoftware.net/)
[![ITOL](https://img.shields.io/badge/Visualization-ITOL-blue?style=flat-square)](https://itol.embl.de/)
[![Method](https://img.shields.io/badge/Method-Maximum_Likelihood_|_NJ_|_RelTime-orange?style=flat-square)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

## 📌 Overview

This repository contains datasets, alignments, analysis configurations (`.mao` templates), and workflow documentation for **molecular evolution and phylogenetics** analyses using **MEGA 12** and **ITOL (Interactive Tree of Life)**.

Key analyses include phylogenetic reconstruction of the **COL1A1 gene** across multiple species, multi-sequence alignment pipelines, and molecular clock (RelTime) dating workflows.

---

## 🗂️ Repository Structure

```
.
├── MEGA_12/               # MEGA12 project files and analysis configs (.mao templates)
├── Mega(experience)/      # Practice datasets and example phylogenetic analyses
├── COL1A1/                # COL1A1 gene multi-species phylogenetics
├── ITOL/                  # Tree visualization exports for ITOL
├── ITOL Task 2/           # Extended ITOL annotation and styling
├── TRO_Seq/               # Raw FASTA / aligned .meg sequence datasets
├── alignment any animals/ # Cross-species multiple sequence alignments
└── README.md
```

---

## 🔬 Methodology

### Phylogenetic Pipeline

| Step | Tool | Method |
|------|------|--------|
| 1. Sequence retrieval | NCBI GenBank / UniProt | FASTA download |
| 2. Multiple Sequence Alignment | MEGA12 — MUSCLE / ClustalW | Progressive alignment |
| 3. Model selection | MEGA12 — BIC/AIC | Substitution model testing |
| 4. Tree construction | MEGA12 | Maximum Likelihood + Bootstrap (1000×) |
| 5. Molecular dating | MEGA12 — RelTime | Relative timetree estimation |
| 6. Tree visualization | ITOL | Annotated, publication-ready trees |

### COL1A1 Gene Analysis

**COL1A1** (*Collagen, type I, alpha 1*) was selected as a model gene for cross-species phylogenetic comparison due to its evolutionary conservation and clinical relevance in connective tissue disorders. Multi-species alignment and ML tree reconstruction reveal deep evolutionary relationships and selective pressure signatures.

---

## ⚙️ MEGA-CC Automation

Batch analyses can be executed with MEGA Command-line (MEGA-CC):

```bash
# Maximum Likelihood tree
megacc -a mao/ml_nucleotide.mao -d TRO_Seq/alignment.meg -o results/ml_output

# RelTime molecular clock
megacc -a mao/reltime.mao -d TRO_Seq/alignment.meg -t input_tree.nwk -o results/timetree
```

---

## 📊 Key Outputs

- **Phylogenetic trees** (`.nwk` Newick format)
- **ITOL-annotated tree exports** — publication-ready visualizations
- **Bootstrap support values** — statistical confidence on tree topology
- **RelTime chronograms** — divergence time estimates
- **Model selection reports** — BIC scores and substitution parameters

---

## 🎓 Academic Context

This repository demonstrates proficiency in **molecular evolution** and **phylogenomics** — core competencies for computational biology research. The MEGA12 + ITOL workflow is standard in evolutionary biology publications.

**Citation:**
> Tamura K., Stecher G., & Kumar S. MEGA X: Molecular Evolutionary Genetics Analysis across computing platforms. *Molecular Biology and Evolution.*

---

**Author:** Suleiman Hajizadeh | Bioinformatician @ IMBB, Azerbaijan
📧 suleyman.hacizade1@gmail.com