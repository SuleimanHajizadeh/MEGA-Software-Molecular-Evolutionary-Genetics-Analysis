#!/usr/bin/env python3
"""
phylo_pipeline.py — Pure-Python Phylogenetic Distance Pipeline
==============================================================
Implements JC69 and Kimura 2-Parameter (K2P) evolutionary distance models
from their mathematical definitions, followed by Neighbor-Joining (NJ) tree
reconstruction — all without any phylogenetics library or MEGA GUI.

Dependencies: biopython, numpy, matplotlib
Usage:
    python phylo_pipeline.py

Output:
    TRO_Seq/col1a1_nj_tree.png  —  Neighbour-Joining tree (matplotlib)

Author : Suleyman Hajizadeh
Purpose: Cambridge MPhil portfolio — demonstrating mathematical implementation
         of core phylogenetic algorithms
"""

import os
import math
import time
import warnings
import logging
import argparse
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from Bio import Entrez, SeqIO
from Bio.Align import PairwiseAligner

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("phylo_pipeline")

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────────────────────────────────────

# Default NCBI email - can be overridden via CLI
DEFAULT_EMAIL = "suleyman.hacizade1@gmail.com"

# COL1A1 RefSeq accessions across 7 species
ACCESSIONS = {
    "Homo_sapiens":        "NM_000088",
    "Pan_troglodytes":     "XM_016944896",
    "Mus_musculus":        "NM_007742",
    "Rattus_norvegicus":   "NM_053304",
    "Gallus_gallus":       "NM_204775",
    "Danio_rerio":         "NM_001004631",
    "Xenopus_tropicalis":  "NM_001016853",
}


OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "TRO_Seq")
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ─────────────────────────────────────────────────────────────────────────────
# 1. SEQUENCE RETRIEVAL
# ─────────────────────────────────────────────────────────────────────────────

def fetch_sequences(accessions: dict, rettype: str = "fasta") -> dict:
    """
    Retrieve nucleotide sequences from NCBI Entrez.

    Parameters
    ----------
    accessions : dict
        Mapping of species_name -> RefSeq accession string.
    rettype : str
        Entrez return type ('fasta' or 'gb').

    Returns
    -------
    dict
        Mapping of species_name -> Bio.SeqRecord object.
    """
    records = {}
    for species, acc in accessions.items():
        logger.info(f"Fetching {species} ({acc}) …")
        try:
            handle = Entrez.efetch(db="nucleotide", id=acc,
                                   rettype=rettype, retmode="text")
            record = SeqIO.read(handle, rettype)
            handle.close()
            records[species] = record
            time.sleep(0.4)          # NCBI rate-limit courtesy pause
        except Exception as exc:
            logger.warning(f"Could not fetch {acc}: {exc}")
    return records


# ─────────────────────────────────────────────────────────────────────────────
# 2. PAIRWISE ALIGNMENT
# ─────────────────────────────────────────────────────────────────────────────

def align_pair(seq_a: str, seq_b: str) -> tuple:
    """
    Perform global pairwise alignment of two nucleotide sequences.

    Uses Biopython PairwiseAligner with standard DNA scoring:
      match=1, mismatch=-1, open gap=-2, extend gap=-0.5.

    Parameters
    ----------
    seq_a, seq_b : str
        Nucleotide sequences as plain strings (ACGT).

    Returns
    -------
    tuple of (str, str)
        The top-scoring aligned sequences (gaps represented as '-').
    """
    aligner = PairwiseAligner()
    aligner.mode = "global"
    aligner.match_score = 1
    aligner.mismatch_score = -1
    aligner.open_gap_score = -2
    aligner.extend_gap_score = -0.5
    alignments = aligner.align(seq_a, seq_b)
    best = next(iter(alignments))
    # Extract aligned strings
    aligned_a = str(best).split("\n")[0]
    aligned_b = str(best).split("\n")[2]
    return aligned_a, aligned_b


def compute_alignment_counts(aligned_a: str, aligned_b: str) -> dict:
    """
    Count substitution categories from a pairwise aligned sequence pair.

    Classifies each aligned column into:
      - match         : identical nucleotide
      - transition P  : purine↔purine or pyrimidine↔pyrimidine (A↔G, C↔T)
      - transversion Q: purine↔pyrimidine (A/G ↔ C/T)
      - gap           : at least one '-'

    Parameters
    ----------
    aligned_a, aligned_b : str
        Gap-containing aligned sequences of equal length.

    Returns
    -------
    dict with keys: n_sites, n_transitions (P), n_transversions (Q), p_frac, q_frac
    """
    purines = set("AG")
    pyrimidines = set("CT")
    n_match = n_P = n_Q = n_gap = 0

    for a, b in zip(aligned_a, aligned_b):
        if a == "-" or b == "-":
            n_gap += 1
            continue
        if a == b:
            n_match += 1
        elif (a in purines and b in purines) or (a in pyrimidines and b in pyrimidines):
            n_P += 1      # transition
        else:
            n_Q += 1      # transversion

    n_sites = n_match + n_P + n_Q   # comparable sites only (no gaps)
    p = n_P / n_sites if n_sites > 0 else 0.0
    q = n_Q / n_sites if n_sites > 0 else 0.0
    return dict(n_sites=n_sites, n_P=n_P, n_Q=n_Q, p=p, q=q)


# ─────────────────────────────────────────────────────────────────────────────
# 3. EVOLUTIONARY DISTANCE MODELS
# ─────────────────────────────────────────────────────────────────────────────

def jc69_distance(p_total: float) -> float:
    """
    Jukes-Cantor 69 (JC69) evolutionary distance.

    Assumes equal base frequencies and equal substitution rates across all
    nucleotide pairs. The proportion of all differences (p = (P+Q)) feeds in.

    Mathematical derivation
    -----------------------
    Under the JC69 model the probability of observing a difference at a site
    after evolutionary time t is:

        p(t) = 3/4 [1 - e^(-8/3 * μt)]

    Inverting for d = μt gives:

        d = -3/4 * ln(1 - 4/3 * p)

    Parameters
    ----------
    p_total : float
        Total proportion of differing sites (transitions + transversions).

    Returns
    -------
    float
        JC69 evolutionary distance (expected substitutions per site).
        Returns np.inf if the argument of ln is non-positive.
    """
    arg = 1.0 - (4.0 / 3.0) * p_total
    if arg <= 0:
        return np.inf
    return -0.75 * math.log(arg)


def k2p_distance(p: float, q: float) -> float:
    """
    Kimura 2-Parameter (K2P) evolutionary distance.

    Extends JC69 by using separate rates for transitions (κ·β) and
    transversions (β), where κ is the transition/transversion ratio.

    Mathematical derivation
    -----------------------
    Under K2P, the expected proportions of transitions (P) and transversions (Q)
    at time t are:

        P = 1/4 [1 - 2e^{-4(α+β)t} + e^{-8βt}]  (approx for α >> β)
        Q = 1/2 [1 - e^{-8βt}]

    Inverting both equations and combining gives:

        d = -1/2 * ln(1 - 2P - Q) - 1/4 * ln(1 - 2Q)

    This accounts for the known excess of transitions over transversions in
    biological sequence data.

    Parameters
    ----------
    p : float
        Proportion of transition differences.
    q : float
        Proportion of transversion differences.

    Returns
    -------
    float
        K2P evolutionary distance. Returns np.inf if arguments of ln are ≤ 0.
    """
    w1 = 1.0 - 2.0 * p - q
    w2 = 1.0 - 2.0 * q
    if w1 <= 0 or w2 <= 0:
        return np.inf
    return -0.5 * math.log(w1) - 0.25 * math.log(w2)


def build_distance_matrix(sequences: dict,
                           model: str = "k2p") -> tuple:
    """
    Compute a pairwise evolutionary distance matrix for all sequence pairs.

    Parameters
    ----------
    sequences : dict
        species_name -> nucleotide string (str).
    model : str
        'jc69' or 'k2p'.

    Returns
    -------
    (labels, matrix) where labels is a list of species names and
    matrix is a numpy float array of shape (n, n).
    """
    labels = list(sequences.keys())
    n = len(labels)
    mat = np.zeros((n, n))

    for i in range(n):
        for j in range(i + 1, n):
            sa = str(sequences[labels[i]].seq)
            sb = str(sequences[labels[j]].seq)
            # Trim to equal length if needed (simple suffix trim)
            min_len = min(len(sa), len(sb))
            sa, sb = sa[:min_len], sb[:min_len]
            aa, ab = align_pair(sa, sb)
            counts = compute_alignment_counts(aa, ab)
            if model == "jc69":
                d = jc69_distance(counts["p"] + counts["q"])
            else:
                d = k2p_distance(counts["p"], counts["q"])
            mat[i, j] = mat[j, i] = d

    return labels, mat


# ─────────────────────────────────────────────────────────────────────────────
# 4. NEIGHBOR-JOINING ALGORITHM (pure NumPy, no phylogenetics library)
# ─────────────────────────────────────────────────────────────────────────────

def neighbor_joining(labels: list, dist_matrix: np.ndarray) -> list:
    """
    Reconstruct a phylogenetic tree using the Neighbor-Joining algorithm.

    Algorithm (Saitou & Nei, 1987)
    --------------------------------
    Given n taxa with distance matrix D (n×n):

    1. Compute the Q-matrix:
           Q[i,j] = (n-2)*D[i,j] - sum_k(D[i,k]) - sum_k(D[j,k])
    2. Find the pair (i,j) minimising Q[i,j].
    3. Compute branch lengths to new node u:
           d(i,u) = D[i,j]/2 + (sum_k D[i,k] - sum_k D[j,k]) / (2*(n-2))
           d(j,u) = D[i,j] - d(i,u)
    4. Update D: for remaining taxa k,
           D[u,k] = (D[i,k] + D[j,k] - D[i,j]) / 2
    5. Remove i, j; add u. Repeat until 2 taxa remain.

    Parameters
    ----------
    labels : list of str
        Taxon names.
    dist_matrix : np.ndarray, shape (n, n)
        Symmetric pairwise distance matrix.

    Returns
    -------
    list of tuples
        Each tuple: (taxon_a, taxon_b, branch_length_a, branch_length_b)
        describing one NJ join event.
    """
    labels = list(labels)          # work on a copy
    D = dist_matrix.copy().astype(float)
    joins = []

    while len(labels) > 2:
        n = len(labels)
        row_sums = D.sum(axis=1)

        # Q-matrix
        Q = np.full((n, n), np.inf)
        for i in range(n):
            for j in range(i + 1, n):
                Q[i, j] = (n - 2) * D[i, j] - row_sums[i] - row_sums[j]
                Q[j, i] = Q[i, j]

        # Find minimum Q (off-diagonal)
        np.fill_diagonal(Q, np.inf)
        idx = np.unravel_index(np.argmin(Q), Q.shape)
        i, j = int(idx[0]), int(idx[1])

        # Branch lengths
        d_ij = D[i, j]
        if n > 2:
            d_iu = d_ij / 2.0 + (row_sums[i] - row_sums[j]) / (2.0 * (n - 2))
        else:
            d_iu = d_ij / 2.0
        d_ju = d_ij - d_iu

        joins.append((labels[i], labels[j], max(d_iu, 0), max(d_ju, 0)))

        # New node distances
        new_label = f"({labels[i]},{labels[j]})"
        new_dists = []
        for k in range(n):
            if k != i and k != j:
                d_ku = (D[i, k] + D[j, k] - d_ij) / 2.0
                new_dists.append(d_ku)

        # Build reduced distance matrix
        remaining = [k for k in range(n) if k != i and k != j]
        m = len(remaining)
        new_D = np.zeros((m + 1, m + 1))
        for a, ri in enumerate(remaining):
            for b, rj in enumerate(remaining):
                new_D[a, b] = D[ri, rj]
            new_D[a, m] = new_D[m, a] = new_dists[a]

        D = new_D
        labels = [labels[k] for k in remaining] + [new_label]

    # Final pair
    if len(labels) == 2:
        joins.append((labels[0], labels[1], D[0, 1] / 2.0, D[0, 1] / 2.0))

    return joins


# ─────────────────────────────────────────────────────────────────────────────
# 5. TREE VISUALISATION
# ─────────────────────────────────────────────────────────────────────────────

def plot_nj_tree(joins: list, labels_orig: list, output_path: str,
                 dist_matrix: np.ndarray) -> None:
    """
    Plot the Neighbor-Joining tree as a cladogram (matplotlib).

    Renders a dendrogram-style figure with branch lengths proportional to
    the K2P evolutionary distances, plus a heatmap of the pairwise distance
    matrix for reference.

    Parameters
    ----------
    joins : list
        Output of neighbor_joining().
    labels_orig : list
        Original taxon labels.
    output_path : str
        File path for the saved PNG.
    dist_matrix : np.ndarray
        Pairwise K2P distance matrix for heatmap.
    """
    fig, axes = plt.subplots(1, 2, figsize=(16, 7),
                             gridspec_kw={"width_ratios": [2, 1]})
    fig.patch.set_facecolor("#0d1117")
    for ax in axes:
        ax.set_facecolor("#161b22")

    # ── left: dendrogram (simplified ladder layout) ──
    ax = axes[0]
    y_positions = {sp: i for i, sp in enumerate(labels_orig)}
    colors = plt.cm.tab10(np.linspace(0, 1, len(labels_orig)))
    color_map = {sp: c for sp, c in zip(labels_orig, colors)}

    current_y = len(labels_orig)
    for join in joins:
        a, b, d_a, d_b = join
        # Leaf y from original; internal nodes get new index
        ya = y_positions.get(a, current_y)
        yb = y_positions.get(b, current_y + 1)
        mid_y = (ya + yb) / 2.0

        # Horizontal branch lines
        x_a_start = 0 if a in labels_orig else 0.05
        ax.plot([x_a_start, d_a], [ya, ya],
                color=color_map.get(a, "white"), linewidth=2.5, solid_capstyle="round")
        ax.plot([x_a_start, d_b], [yb, yb],
                color=color_map.get(b, "white"), linewidth=2.5, solid_capstyle="round")
        # Vertical connecting line
        ax.plot([max(d_a, d_b), max(d_a, d_b)], [ya, yb],
                color="#58a6ff", linewidth=1.5, linestyle="--", alpha=0.7)

        new_label = f"({a},{b})"
        y_positions[new_label] = mid_y
        color_map[new_label] = "#58a6ff"
        current_y += 1

    # Species labels
    for sp, y in [(s, y_positions[s]) for s in labels_orig]:
        ax.text(0.001, y, sp.replace("_", " "), color=color_map[sp],
                fontsize=9, va="center", fontstyle="italic",
                fontfamily="DejaVu Sans")

    ax.set_title("COL1A1 Neighbor-Joining Tree\n(K2P distances — implemented from scratch)",
                 color="white", fontsize=13, pad=12)
    ax.set_xlabel("K2P evolutionary distance (substitutions/site)", color="#8b949e")
    ax.tick_params(colors="#8b949e")
    for spine in ax.spines.values():
        spine.set_edgecolor("#30363d")

    # ── right: distance heatmap ──
    ax2 = axes[1]
    n = len(labels_orig)
    clean_labels = [s.replace("_", " ") for s in labels_orig]
    im = ax2.imshow(dist_matrix, cmap="magma_r", aspect="auto",
                    vmin=0, vmax=np.nanmax(dist_matrix[np.isfinite(dist_matrix)]))
    ax2.set_xticks(range(n))
    ax2.set_yticks(range(n))
    ax2.set_xticklabels(clean_labels, rotation=45, ha="right",
                        color="#c9d1d9", fontsize=7.5, fontstyle="italic")
    ax2.set_yticklabels(clean_labels, color="#c9d1d9",
                        fontsize=7.5, fontstyle="italic")
    for i in range(n):
        for j in range(n):
            val = dist_matrix[i, j]
            ax2.text(j, i, f"{val:.3f}" if np.isfinite(val) else "∞",
                     ha="center", va="center", fontsize=6.5,
                     color="white" if val > 0.05 else "#0d1117")
    cbar = fig.colorbar(im, ax=ax2, pad=0.04)
    cbar.set_label("K2P distance", color="#8b949e")
    cbar.ax.yaxis.set_tick_params(color="#8b949e")
    plt.setp(cbar.ax.yaxis.get_ticklabels(), color="#8b949e")
    ax2.set_title("Pairwise K2P Distance Matrix", color="white", fontsize=11, pad=10)
    for spine in ax2.spines.values():
        spine.set_edgecolor("#30363d")

    fig.suptitle("COL1A1 Phylogenetic Analysis — Pure Python Implementation",
                 color="#f0f6fc", fontsize=14, fontweight="bold", y=1.01)
    plt.tight_layout()
    plt.savefig(output_path, dpi=180, bbox_inches="tight",
                facecolor=fig.get_facecolor())
    print(f"  Tree saved: {output_path}")
    plt.close(fig)


# ─────────────────────────────────────────────────────────────────────────────
# MAIN PIPELINE
# ─────────────────────────────────────────────────────────────────────────────

def parse_args():
    parser = argparse.ArgumentParser(
        description="COL1A1 Phylogenetic Pipeline - JC69 & K2P Evolutionary Distance Models"
    )
    parser.add_argument(
        "--model",
        choices=["k2p", "jc69"],
        default="k2p",
        help="Evolutionary distance model to use for tree building (default: k2p)"
    )
    parser.add_argument(
        "--email",
        default=DEFAULT_EMAIL,
        help=f"NCBI Entrez email address (default: {DEFAULT_EMAIL})"
    )
    parser.add_argument(
        "--output-dir",
        default=OUTPUT_DIR,
        help=f"Output directory for saved figures (default: {OUTPUT_DIR})"
    )
    return parser.parse_args()


def main():
    """Run the complete phylogenetic analysis pipeline."""
    args = parse_args()
    Entrez.email = args.email

    logger.info("=" * 60)
    logger.info("COL1A1 Phylogenetic Pipeline")
    logger.info(f"Model: {args.model.upper()} | Tree: Neighbour-Joining (pure Python)")
    logger.info("=" * 60)

    # 1. Fetch sequences
    logger.info("Step [1/4]: Fetching COL1A1 sequences from NCBI Entrez …")
    seqs = fetch_sequences(ACCESSIONS)
    if len(seqs) < 3:
        raise RuntimeError("Too few sequences fetched — check internet/NCBI access.")
    logger.info(f"Retrieved {len(seqs)} sequences successfully.")

    # 2. Build distance matrix based on chosen model
    logger.info(f"Step [2/4]: Computing pairwise {args.model.upper()} distances …")
    labels, dist_mat = build_distance_matrix(seqs, model=args.model)
    
    logger.info(f"{args.model.upper()} Distance Matrix:")
    header = f"{'':>22}" + "".join(f"{l[:8]:>10}" for l in labels)
    logger.info(header)
    for i, la in enumerate(labels):
        row = f"{la[:22]:>22}" + "".join(f"{dist_mat[i,j]:>10.4f}" for j in range(len(labels)))
        logger.info(row)

    # 3. Also compute the alternative model for comparison
    alt_model = "jc69" if args.model == "k2p" else "k2p"
    logger.info(f"Step [3/4]: Computing pairwise {alt_model.upper()} distances (for comparison) …")
    _, alt_mat = build_distance_matrix(seqs, model=alt_model)

    # 4. NJ tree
    logger.info("Step [4/4]: Building Neighbour-Joining tree …")
    joins = neighbor_joining(labels, dist_mat)
    logger.info("NJ join sequence:")
    for jn in joins:
        logger.info(f"  Joined: {jn[0][:30]} ↔ {jn[1][:30]} (d={jn[2]:.5f}, {jn[3]:.5f})")

    os.makedirs(args.output_dir, exist_ok=True)
    out_path = os.path.join(args.output_dir, f"col1a1_nj_tree_{args.model}.png")
    
    # Save the output visualization
    fig, axes = plt.subplots(1, 2, figsize=(16, 7),
                             gridspec_kw={"width_ratios": [2, 1]})
    fig.patch.set_facecolor("#0d1117")
    for ax in axes:
        ax.set_facecolor("#161b22")

    # left: dendrogram layout
    ax = axes[0]
    y_positions = {sp: i for i, sp in enumerate(labels)}
    colors = plt.cm.tab10(np.linspace(0, 1, len(labels)))
    color_map = {sp: c for sp, c in zip(labels, colors)}

    current_y = len(labels)
    for join in joins:
        a, b, d_a, d_b = join
        ya = y_positions.get(a, current_y)
        yb = y_positions.get(b, current_y + 1)
        mid_y = (ya + yb) / 2.0

        x_a_start = 0 if a in labels else 0.05
        ax.plot([x_a_start, d_a], [ya, ya],
                color=color_map.get(a, "white"), linewidth=2.5, solid_capstyle="round")
        ax.plot([x_a_start, d_b], [yb, yb],
                color=color_map.get(b, "white"), linewidth=2.5, solid_capstyle="round")
        ax.plot([max(d_a, d_b), max(d_a, d_b)], [ya, yb],
                color="#58a6ff", linewidth=1.5, linestyle="--", alpha=0.7)

        new_label = f"({a},{b})"
        y_positions[new_label] = mid_y
        color_map[new_label] = "#58a6ff"
        current_y += 1

    for sp, y in [(s, y_positions[s]) for s in labels]:
        ax.text(0.001, y, sp.replace("_", " "), color=color_map[sp],
                fontsize=9, va="center", fontstyle="italic",
                fontfamily="DejaVu Sans")

    ax.set_title(f"COL1A1 Neighbor-Joining Tree\n({args.model.upper()} distances — implemented from scratch)",
                 color="white", fontsize=13, pad=12)
    ax.set_xlabel(f"{args.model.upper()} evolutionary distance (substitutions/site)", color="#8b949e")
    ax.tick_params(colors="#8b949e")
    for spine in ax.spines.values():
        spine.set_edgecolor("#30363d")

    # right: distance heatmap
    ax2 = axes[1]
    n = len(labels)
    clean_labels = [s.replace("_", " ") for s in labels]
    im = ax2.imshow(dist_mat, cmap="magma_r", aspect="auto",
                    vmin=0, vmax=np.nanmax(dist_mat[np.isfinite(dist_mat)]))
    ax2.set_xticks(range(n))
    ax2.set_yticks(range(n))
    ax2.set_xticklabels(clean_labels, rotation=45, ha="right",
                        color="#c9d1d9", fontsize=7.5, fontstyle="italic")
    ax2.set_yticklabels(clean_labels, color="#c9d1d9",
                        fontsize=7.5, fontstyle="italic")
    for i in range(n):
        for j in range(n):
            val = dist_mat[i, j]
            ax2.text(j, i, f"{val:.3f}" if np.isfinite(val) else "∞",
                     ha="center", va="center", fontsize=6.5,
                     color="white" if val > 0.05 else "#0d1117")
    cbar = fig.colorbar(im, ax=ax2, pad=0.04)
    cbar.set_label(f"{args.model.upper()} distance", color="#8b949e")
    cbar.ax.yaxis.set_tick_params(color="#8b949e")
    plt.setp(cbar.ax.yaxis.get_ticklabels(), color="#8b949e")
    ax2.set_title(f"Pairwise {args.model.upper()} Distance Matrix", color="white", fontsize=11, pad=10)
    for spine in ax2.spines.values():
        spine.set_edgecolor("#30363d")

    fig.suptitle(f"COL1A1 Phylogenetic Analysis — Pure Python ({args.model.upper()})",
                 color="#f0f6fc", fontsize=14, fontweight="bold", y=1.01)
    plt.tight_layout()
    plt.savefig(out_path, dpi=180, bbox_inches="tight",
                facecolor=fig.get_facecolor())
    logger.info(f"Tree saved to output: {out_path}")
    plt.close(fig)

    logger.info("✅ Pipeline execution completed successfully.")


if __name__ == "__main__":
    main()

