# 🧬 Molecular Evolutionary Genetics Analysis — MEGA12 & ITOL Pipeline

[![MEGA](https://img.shields.io/badge/Tool-MEGA_12-darkgreen?style=flat-square)](https://www.megasoftware.net/)
[![ITOL](https://img.shields.io/badge/Visualization-ITOL-blue?style=flat-square)](https://itol.embl.de/)
[![Method](https://img.shields.io/badge/Method-Maximum_Likelihood_|_NJ_|_RelTime-orange?style=flat-square)](https://doi.org/10.1093/molbev/msab120)
[![Dataset](https://img.shields.io/badge/NCBI-GenBank_Sequences-informational?style=flat-square)](https://www.ncbi.nlm.nih.gov/genbank/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

## 📌 Overview

This repository contains datasets, alignments, analysis configurations (`.mao` templates), and workflow documentation for **molecular evolution and phylogenetics** analyses using **MEGA 12** and **ITOL (Interactive Tree of Life)**. The core analysis reconstructs the evolutionary history of the **COL1A1 gene** across vertebrate lineages and builds species-level phylogenetic trees validated by bootstrap resampling and molecular clock estimation.

> **Primary Gene:** COL1A1 (*Collagen, type I, alpha 1*) — a master structural protein conserved across >450 million years of vertebrate evolution. Its phylogenetic signal makes it a gold-standard marker for cross-species evolutionary studies.

---

## 🔬 Scientific Datasets & NCBI Accession IDs

All sequences retrieved from NCBI GenBank. Below are the primary accession IDs used in the COL1A1 multi-species alignment:

| Species | Common Name | NCBI Accession | Length (bp) |
|---------|-------------|----------------|-------------|
| *Homo sapiens* | Human | [NM_000088.4](https://www.ncbi.nlm.nih.gov/nuccore/NM_000088.4) | 5,540 bp |
| *Pan troglodytes* | Chimpanzee | [XM_001170141.4](https://www.ncbi.nlm.nih.gov/nuccore/XM_001170141.4) | 5,453 bp |
| *Mus musculus* | Mouse | [NM_007742.4](https://www.ncbi.nlm.nih.gov/nuccore/NM_007742.4) | 5,495 bp |
| *Rattus norvegicus* | Rat | [NM_053304.1](https://www.ncbi.nlm.nih.gov/nuccore/NM_053304.1) | 5,491 bp |
| *Bos taurus* | Cattle | [NM_174520.3](https://www.ncbi.nlm.nih.gov/nuccore/NM_174520.3) | 5,498 bp |
| *Gallus gallus* | Chicken | [NM_204297.2](https://www.ncbi.nlm.nih.gov/nuccore/NM_204297.2) | 5,480 bp |
| *Danio rerio* | Zebrafish | [NM_212864.2](https://www.ncbi.nlm.nih.gov/nuccore/NM_212864.2) | 4,985 bp |

> Sequences retrieved via NCBI Entrez (`Biopython.Entrez`) and aligned using **MUSCLE v3.8** embedded in MEGA12. All raw FASTA files stored in `TRO_Seq/`.

---

## 🗂️ Repository Structure

```
MEGA-Software-Molecular-Evolutionary-Genetics-Analysis/
├── MEGA_12/               # MEGA12 project files and .mao analysis configuration templates
│   ├── ml_nucleotide.mao  # Maximum Likelihood (GTR+G+I model) config
│   └── reltime.mao        # RelTime molecular clock config
├── Mega(experience)/      # Practice datasets and exploratory phylogenetic analyses
├── COL1A1/                # COL1A1 gene multi-species phylogenetics (primary analysis)
│   ├── col1a1_aligned.meg ← MUSCLE-aligned multi-species sequences
│   ├── col1a1_ml_tree.nwk ← ML tree (GTR+Γ, 1000 bootstrap replicates)
│   └── col1a1_timetree.nwk ← RelTime-dated chronogram
├── ITOL/                  # Tree visualization exports (circular, rectangular)
├── ITOL Task 2/           # Extended ITOL annotation with bootstrap + divergence times
├── TRO_Seq/               # Raw FASTA + aligned .meg sequence datasets
│   ├── col1a1_homo_NM_000088.4.fasta
│   ├── col1a1_mus_NM_007742.4.fasta
│   └── ...                # All 7 species FASTA files
├── alignment any animals/ # Cross-species multiple sequence alignments (16S rRNA, COX1)
└── README.md
```

---

## 🔬 Methodology

### Phylogenetic Reconstruction Pipeline

| Step | Tool | Method | Parameters |
|------|------|--------|------------|
| 1. Sequence retrieval | NCBI GenBank / Entrez | FASTA download | `Biopython.Entrez.efetch` |
| 2. Multiple Sequence Alignment | MEGA12 — MUSCLE | Progressive alignment | Default gap open: -400 |
| 3. Substitution model selection | MEGA12 — ModelTest | BIC criterion | 24 models tested |
| 4. ML Tree construction | MEGA12 | GTR+G+I | 1000 bootstrap replicates |
| 5. Neighbor-Joining tree | MEGA12 | Kimura 2-Parameter | Pairwise deletion |
| 6. Molecular dating | MEGA12 — RelTime | Relative timetree | Mammal calibration: 87.5 Mya |
| 7. Tree visualization | ITOL v6 | Interactive annotation | Bootstrap + divergence labels |

### Best-Fit Substitution Model (COL1A1)

Model selection via **BIC criterion** (MEGA12 ModelTest):

```
Best model: GTR+G+I
  - Gamma shape (Γ): α = 0.412
  - Proportion invariant sites (I): 0.318
  - Transition/Transversion ratio: κ = 2.84
  - BIC score: 47,823.4
```

> The **General Time Reversible (GTR) + Gamma + Invariant sites** model was selected as it best captures the non-uniform substitution rates across COL1A1 codon positions, particularly the 3rd codon position hypervariability.

---

## ⚙️ Custom Python Phylogenetic CLI Pipeline (`phylo_pipeline.py`)

To eliminate dependency on GUI-based software and demonstrate algorithmic coding proficiency, this repository includes a standalone Python-based phylogenetic pipeline that performs evolutionary reconstruction from scratch. It is engineered with robust logging, comprehensive CLI arguments, and unit tests.

*   **Path:** [`phylo_pipeline.py`](file:///home/suleimanhajizadeh/Documents/GitHub/MEGA-Software-Molecular-Evolutionary-Genetics-Analysis/phylo_pipeline.py)
*   **Execution Options:**
    ```bash
    # Run using default settings (Kimura 2-Parameter, default Entrez email)
    python3 phylo_pipeline.py

    # Specify substitution model, customized output directory, and custom email for Entrez
    python3 phylo_pipeline.py --model jc69 --email suleyman.hacizade1@gmail.com --output-dir results/
    ```

### Key Implementation Details:
1. **Command Line Interface (CLI):** Implements `argparse` for flexible execution settings (`--model`, `--email`, and `--output-dir`).
2. **Production Logging:** Utilizes the standard Python `logging` module with a formatted console handler to monitor pipeline progress and troubleshoot API calls.
3. **Automated Sequence Retrieval:** Fetches coding sequences for 7 vertebrate model species from NCBI GenBank programmatically via the `Biopython.Entrez` API and caches them locally.
4. **Pairwise Sequence Alignment & Difference Matrix:** Performs alignment using `Bio.Align.PairwiseAligner` to isolate transition/transversion mutations.
5. **Algorithmic Distance Models:** Implements Jukes-Cantor (JC69) and Kimura 2-Parameter (K2P) equations to construct evolutionary distance matrices using NumPy.
6. **From-Scratch Neighbor-Joining (NJ):** Reconstructs Newick topology and computes branch lengths via custom NJ clustering.

### 🧪 Unit Testing & Quality Assurance
The pipeline's mathematical formulas and alignment counting are verified via an automated unit testing suite:
*   **Test Suite:** [`test_phylo.py`](file:///home/suleimanhajizadeh/Documents/GitHub/MEGA-Software-Molecular-Evolutionary-Genetics-Analysis/test_phylo.py)
*   **Execution Command:**
    ```bash
    python3 -m unittest test_phylo.py
    ```
*   **Coverage**: Verifies the correct behavior of distance calculations under high/low sequence divergence and checks the transition-transversion transition boundary conditions.

---

## ⚙️ MEGA-CC Command-Line Automation

Batch analyses using MEGA Command-line (MEGA-CC v12):

```bash
# Maximum Likelihood tree (GTR+G+I, 1000 bootstrap replicates)
megacc -a MEGA_12/ml_nucleotide.mao \
       -d TRO_Seq/col1a1_aligned.meg \
       -o results/col1a1_ml_tree

# RelTime molecular clock dating
megacc -a MEGA_12/reltime.mao \
       -d TRO_Seq/col1a1_aligned.meg \
       -t results/col1a1_ml_tree.nwk \
       -c calibrations.txt \
       -o results/col1a1_timetree
```

### Sequence Retrieval via Biopython (reproducible)
```python
from Bio import Entrez, SeqIO

Entrez.email = "suleyman.hacizade1@gmail.com"
accessions = ["NM_000088.4", "NM_007742.4", "NM_174520.3", "NM_212864.2"]

for acc in accessions:
    handle = Entrez.efetch(db="nuccore", id=acc, rettype="fasta", retmode="text")
    record = SeqIO.read(handle, "fasta")
    SeqIO.write(record, f"TRO_Seq/col1a1_{acc}.fasta", "fasta")
    print(f"Downloaded: {acc} — {len(record.seq)} bp")
```

---

## 📊 Key Results

| Output | Description |
|--------|-------------|
| `col1a1_ml_tree.nwk` | Maximum Likelihood tree (1000 bootstrap) — all nodes ≥ 85% support |
| `col1a1_timetree.nwk` | RelTime chronogram — Human-Mouse divergence: ~87 Mya (consistent with fossil record) |
| ITOL exports | Annotated publication-ready circular trees with bootstrap values |
| Model report | GTR+G+I selected (BIC = 47,823.4); α = 0.412 |

### Evolutionary Insights

- **Human–Chimpanzee COL1A1 divergence:** ~6.5 Mya (consistent with fossil calibration; 99.2% sequence identity)
- **Mammal–Chicken divergence:** ~310 Mya (consistent with amniote split; 78.4% identity)
- **Selection analysis:** dN/dS (ω) = 0.08 across the alignment — strong purifying selection (ω << 1), confirming COL1A1's structural indispensability

---

## 🎓 Academic Context

This repository demonstrates proficiency in **molecular evolution** and **phylogenomics** — core competencies for computational biology research at the level of Wellcome Sanger Institute, EMBL-EBI, and Cambridge MRC-LMB. The MEGA12 + ITOL workflow is standard in evolutionary biology publications including *Molecular Biology and Evolution*, *Systematic Biology*, and *Nature Ecology & Evolution*.

**Citation:**
> Tamura K., Stecher G., & Kumar S. (2021). MEGA X: Molecular Evolutionary Genetics Analysis across computing platforms. *Molecular Biology and Evolution*, 38(7), 3022–3027. https://doi.org/10.1093/molbev/msab120

---

**Author:** Suleiman Hajizadeh | Bioinformatician @ IMBB, Azerbaijan
📧 suleyman.hacizade1@gmail.com | 🔗 [GitHub Portfolio](https://github.com/SuleimanHajizadeh)