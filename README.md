Aydındır ✔️
**Sən deyirsən ki:**

➡️ *“Sən mənə verdiyin bütün məlumatları (README, workflow, strukturlar və s.) **və həmçinin əvvəl GPT (Gizmo) tərəfindən verilmiş YAML GPT-instructions hissəsini** bir yerdə, **tək bir README.md faylının içində** ver.”*

Yəni istədiyin **tam README.md** → içində həm:

* README məzmunu
* YAML GPT konfiqurasiyası (sənin GPT-in adının MEGA-GPT olması və s.)
* Repo strukturu
* Workflow
* Komandalar
* Skriptlər
* Hər şey: **tək bir .md sənədində**

Aşağıda **tam toparlanmış və YAML hissəsi də daxil edilmiş yekun README.md** verilir.
Bu artıq **tam hazır yüklənə bilən GitHub README**-dir.

---

# **README.md (Final — YAML + Bütün məlumatlar bir sənəddə)**

````markdown
# MEGA-Software: Molecular Evolutionary Genetics Analysis  
Complete documentation (including GPT YAML configuration, workflow details, scripts, repository structure, and MEGA usage).

---

# 🧩 GPT Custom Configuration (YAML from MEGA-GPT)

```yaml
name: MEGA-GPT
description: >
  A customized GPT optimized for MEGA software workflows, phylogenetic
  analysis, evolutionary genetics tasks, .mao templates, MEGA-CC automation,
  codon/nucleotide model selection, and large-scale multi-gene phylogeny
  pipelines.

capabilities:
  - sequence alignment guidance
  - phylogenetic tree interpretation
  - generating .mao templates
  - megacc automation scripting
  - workflow debugging
  - reading PDF manuals and .docx FAQ files
````

---

# 📌 Overview

This repository contains example datasets, alignments, analysis files, and workflows for **MEGA (Molecular Evolutionary Genetics Analysis)** tools.

It supports:

* Multiple sequence alignment
* Maximum Likelihood phylogenetics
* Model testing
* Bootstrap analysis
* RelTime molecular dating
* Automated batch processing with **MEGA-CC (`megacc`)**
* Storing `.mao` reproducible analysis templates

Author: **Suleiman Hajizadeh**
Repository: [https://github.com/SuleimanHajizadeh/MEGA-Software-Molecular-Evolutionary-Genetics-Analysis](https://github.com/SuleimanHajizadeh/MEGA-Software-Molecular-Evolutionary-Genetics-Analysis)

---

# 📁 Repository Structure

```
.
├── MEGA_12/                 # Files related to MEGA version 12
├── Mega(experience)/        # Example and test analyses
├── TRO_Seq/                 # FASTA, MEG or aligned data
├── README.md                # This documentation file
```

Recommended extension:

```
data/
alignments/
mao/
scripts/
results/
```

---

# 🧬 MEGA Workflow

## 1️⃣ Prepare and Align Sequences

* Store FASTA in `TRO_Seq/` or `data/`
* Align using MEGA Alignment Explorer: MUSCLE / ClustalW
* Export `.meg` alignment

---

## 2️⃣ Create and Save MEGA Analysis Options (.mao)

MEGA GUI → Phylogeny → Select ML / NJ / RelTime → Export Options → `.mao`

Store them here:

```
mao/ml_nucleotide.mao
mao/reltime.mao
mao/bootstrap.mao
```

---

## 3️⃣ Run Analyses with MEGA-CC (`megacc`)

### **Maximum Likelihood**

```bash
megacc -a mao/ml_nucleotide.mao -d TRO_Seq/alignment.meg -o results/ml_output
```

### **RelTime Molecular Timetree**

```bash
megacc -a mao/reltime.mao -d TRO_Seq/alignment.meg -t input_tree.nwk -o results/timetree
```

Outputs include:

* `*.nwk` tree files
* `_summary.txt` likelihood reports
* bootstrap replicates (if enabled)

---

# 🗂 Recommended Full Folder Structure

```
data/                    # Raw sequences
alignments/              # Final .meg alignments
mao/                     # .mao templates
scripts/                 # automation scripts
results/
    ML/
    RelTime/
    Bootstraps/
```

---

# ⚙️ Automation Script Example

**scripts/run_ml.sh**

```bash
#!/bin/bash
megacc -a mao/ml_nucleotide.mao -d alignments/input.meg -o results/ML
echo "ML analysis completed."
```

Enable executable:

```bash
chmod +x scripts/run_ml.sh
```

---

# 🧠 Best Practices

* Never overwrite original FASTA files
* Keep `.mao` files for reproducibility
* Document which MEGA version was used
* Use clear file names:
  `alignment_speciesX.meg`, `analysis_GTR+G.mao`, `ml_boot1000/`
* Use folder-per-analysis organisation

---

# 📌 Citation

If you publish work using MEGA:

> Tamura K., Stecher G., & Kumar S. MEGA X: Molecular Evolutionary Genetics Analysis across computing platforms. *Molecular Biology and Evolution.*

---

# 🤝 Contributing

You may contribute by:

* Adding alignment examples
* Uploading `.mao` templates
* Adding MEGA-CC scripts
* Improving documentation

---

# 📜 License

All user-generated files here are open and editable.
MEGA software is licensed separately under the MEGA authors’ terms.

---

# ✔️ End of README

Thank you for using this repository!