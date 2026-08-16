---
title: TRO_Seq Vector-Host Epidemiological Dataset
type: source
category: dataset
tags: [dataset, tro-seq, leishmania, trypanosomatida, vector-host, sandfly, epidemiology]
created: 2026-08-17
updated: 2026-08-17
raw_source: "results/col1a1_analysis/TRO_Seq(30).txt"
---

# Source: TRO_Seq Vector-Host Epidemiological Dataset

## Summary
The **TRO_Seq(30)** dataset contains 30 aligned nucleotide sequences of kinetoplastid/trypanosomatid parasites across insect vectors, mammalian reservoir hosts, and human clinical isolates from endemic regions across the Middle East, Mediterranean, Africa, and Central Asia (spanning Palestine, Turkey, Iran, Morocco, Ghana, Afghanistan, Pakistan, Greece, and China between 1998 and 2020).

## Isolate Categories & Host-Vector Transmission Chain

| Category | Representative Taxa | Accessions & Origins |
| :--- | :--- | :--- |
| **Human Clinical Isolates** | *Homo sapiens* | `FN677343` (Palestine 2001), `MG515729` (Turkey 2017), `KU680850` (Iran 2016), `KC145160` (Morocco 2012), `KP335145` (Afghanistan 2014), `MN891722` (Pakistan 2014), `EF095751` (Greece 2006) |
| **Insect Vectors (Sandflies)** | *[[Phlebotomus_sergenti]]*, *Sergentomyia hamoni*, *Sergentomyia dentata* | `EU683617` (West Bank 1998), `HM060588` (Iran 2010), `MT966013` (Palestine 2020), `MW111302` (Palestine 2020), `AB787190` (Ghana 2007) |
| **Mammalian Reservoirs** | *[[Canis_lupus_familiaris|Canis lupus]]*, *Procavia capensis* (Rock hyrax), *Meriones persicus* (Persian jird) | `HM004586` (Iran 2010), `FJ595950` (West Bank 2008), `EU871037` (Iran 2008) |
| **Reptilian Isolates** | *Eremias velox*, *Eremias vermiculata*, *Phrynocephalus axillaris* | `KU194945` (China 2015), `KU194928` (China 2015), `KU194963` (China 2015) |
| **Parasitic Outgroup** | *[[Trypanosomatida|Trypanosoma evasi]]* | `MH997512` (Palestine 2018) |

## Associated Analysis Files in Repo
- Raw sequences: `data/raw/col1a1_sequences/TRO_Seq(30).fas` and `results/col1a1_analysis/TRO_Seq(30).txt`
- Alignment session: `results/col1a1_analysis/TRO_Seq(30).mas`
- Distance matrix: `results/col1a1_analysis/TRO_Seq(session).mdsx`
- Phylogenetic topologies: `TRO_Seq(topology).mtsx`, `TRO_Seq(circular).mtsx`, `TRO_Seq(30).meg`

## Related Graph Nodes
- Entities: [[Homo_sapiens]], [[Phlebotomus_sergenti]], [[Trypanosomatida]], [[MEGA12]]
- Concepts: [[Vector_Host_Phylodynamics]], [[Phylogenetic_Reconstruction]], [[MEGA_File_Formats]]
