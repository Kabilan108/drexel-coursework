from scipy.spatial.distance import pdist, squareform
import matplotlib.pyplot as plt
import numpy as np
import requests

import warnings
import urllib3

warnings.filterwarnings("ignore", category=urllib3.exceptions.InsecureRequestWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)


def ptn_gethydrogenbondedpairs(
    seq: np.ndarray, locs: np.ndarray, dist: np.ndarray = None
) -> np.ndarray:
    """Finds hydrogen bonded pairs in a RNA sequence.

    :param seq: A 1D numpy array of RNA sequence.
    :param locs: A (n, 3) numpy array of locations.
    :param dist: A (n, n) numpy array of distances.
    :return: A (2, m) numpy array of bond pairs indices (1-indexed)
             1st column is donor, 2nd column is acceptor
    """

    # constants
    MINSEQDIST = 1
    MINDIST = 3
    MAXDIST = 15

    if dist is None:
        dist = squareform(pdist(locs))
    else:
        dist = dist.copy()

    # use upper triangular matrix
    dist[np.tril_indices_from(dist)] = np.inf

    # residues are H-boned if dist between 3-15 angstroms
    dist[dist < MINDIST] = np.inf
    dist[dist > MAXDIST] = np.inf

    # must be at least MINSEQDIST apart
    for i in range(dist.shape[1]):
        dist[i, i + 1 : i + 1 + MINSEQDIST] = np.inf

    # initialize arrays to track H-bond counts and pairs
    bond_counts = np.zeros(len(seq), dtype=int)
    donated = np.ones(len(seq), dtype=int) * -1
    accepted = np.ones(len(seq), dtype=int) * -1
    pairs = []

    while True:
        # find pair with smallest distance;
        min_dist = dist.min()
        if np.isinf(min_dist):
            break
        r, c = np.where(dist == min_dist)

        # if multiple pairs, select the one that appears first
        r, c = np.sort(np.array([r, c]).T, axis=0)[0]

        # each AA can bond with at most 2 others
        if bond_counts[r] < 2 and bond_counts[c] < 2:
            # decide if r or c is the donor or acceptor
            r_is_donor = donated[r] == -1 and seq[r] != "P"
            c_is_donor = donated[c] == -1 and seq[c] != "P"
            r_is_acceptor = accepted[r] == -1
            c_is_acceptor = accepted[c] == -1

            if r_is_donor and c_is_acceptor:
                pairs.append([r + 1, c + 1])  # 1-indexed
                bond_counts[r] += 1
                bond_counts[c] += 1
                donated[r] = c
                accepted[c] = r
                dist[r, c] = np.inf
            elif r_is_acceptor and c_is_donor:
                pairs.append([c + 1, r + 1])  # 1-indexed
                bond_counts[r] += 1
                bond_counts[c] += 1
                donated[c] = r
                accepted[r] = c
                dist[r, c] = np.inf
            else:
                dist[r, c] = np.inf
        else:
            dist[r, c] = np.inf

    return np.array(pairs)[:, [1, 0]]


def ptn_fitness(
    seq: np.ndarray, locs: np.ndarray, dist: np.ndarray = None
) -> tuple[float, dict]:
    """Calculates the fitness of a PTN fold.

    :param seq: A 1D numpy array of RNA sequence.
    :param locs: A (n, 3) numpy array of locations.
    :param dist: A (n, n) numpy array of distances.
    :return: A tuple of (fitness, info) where info is a dictionary of additional info
    """

    if dist is None:
        dist = squareform(pdist(locs))
    else:
        dist = dist.copy()

    N = len(seq)

    # count total h-bonds
    pairs = ptn_gethydrogenbondedpairs(seq, locs, dist)
    n_bonds = pairs.shape[0]

    # triangular matrix
    dist[np.tril_indices_from(dist)] = np.inf

    # consecutive residues
    seqviolations = numseqviolations = 0
    for i in range(N - 1):
        if not (3.7 <= dist[i, i + 1] <= 3.9):
            if dist[i, i + 1] < 3.7:
                seqviolations += 3.7 - dist[i, i + 1]
            else:
                seqviolations += dist[i, i + 1] - 3.9
            numseqviolations += 1

    # non-consecutive residues
    nonseqviolations = numnonseqviolations = 0
    for i in range(N):
        violation_idx = np.where(dist[i, i + 2 :] <= 3)[0]
        numnonseqviolations += violation_idx.shape[0]
        nonseqviolations += (3 - dist[i, i + 2 :][violation_idx]).sum()

    fitness = n_bonds - seqviolations - nonseqviolations
    info = {
        "totalhbonds": n_bonds,
        "numseqviolations": numseqviolations,
        "numnonseqviolations": numnonseqviolations,
        "seqviolations": seqviolations,
        "nonseqviolations": nonseqviolations,
    }

    return fitness, info


def downloadurl(url: str, filename: str) -> None:
    """Downloads a file from the given URL to the given filename.

    :param url: The URL to download from.
    :param filename: The filename to save to.
    """
    try:
        response = requests.get(url, verify=False)
        with open(filename, "w") as file:
            file.write(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {filename}: {e}")


def rna_plot(locs: np.ndarray, pairs: np.ndarray = None) -> None:
    """Plots RNA structure in 3D.

    :param locs: A (n, 3) numpy array of locations.
    :param pairs: A (2, m) numpy array of index pairs to connect with lines.
    """

    def get_ticks(x):
        return np.arange(5 * (int(min(x) // 5)), 5 * (int(max(x) // 5) + 1), 5)

    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111, projection="3d")
    ax.view_init(elev=20, azim=-120)
    ax.grid(False)

    # Plotting the points
    ax.plot(
        locs[:, 0],
        locs[:, 1],
        locs[:, 2],
        color="r",
        linewidth=1.5,
        marker="o",
        markersize=5,
        markerfacecolor="white",
    )

    # Plotting the pairs if provided
    if pairs is not None and pairs.size > 0:
        for i in range(pairs.shape[0]):
            pair_points = locs[pairs[i, :] - 1, :]
            ax.plot(
                pair_points[:, 0],
                pair_points[:, 1],
                pair_points[:, 2],
                color="b",
                linewidth=2,
                marker="o",
                markersize=5,
                markeredgecolor="r",
                markerfacecolor="white",
            )

    # axes ticks
    ax.set_xticks(get_ticks(locs[:, 0]))
    ax.set_yticks(get_ticks(locs[:, 1]))
    ax.set_zticks(get_ticks(locs[:, 2]))
