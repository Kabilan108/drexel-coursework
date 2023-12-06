"""
Script for generating results for lab 5

Author:  Tony Kabilan Okeke
  Date:  11.23.2023
"""

# import packages
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.io
import os


def firingrate(ts):
    """Calculate firing rate for a neuron
    Args:
        ts (np.ndarray): Spike times for a neuron (s)
    Return:
        rate (float): Firing rate (spikes/s)
    """
    return len(ts) / (ts[-1] - ts[0])


def autocorrelogram(ts):
    """Generate an autocorrelogram
    Args:
        ts (np.ndarray): Spike times for a neuron (s)
    Return:
        probs (np.ndarray): the probability of spikes in each bin.
    """
    global EDGES
    counts = np.zeros(len(EDGES) - 1, dtype=int)

    for i, k in enumerate(ts):
        d = np.delete(ts, i) - k
        c, _ = np.histogram(d, bins=EDGES)
        counts += c

    return counts / ts.shape[0]


def plot_ac(ac_data):
    """Plot autocorrelograms for each neuron
    Args:
        ac_data (pd.DataFrame): Dataframe containing autocorrelograms
    """

    fig, axes = plt.subplots(1, 2, figsize=(6, 3))

    for ax, row in zip(axes, ac_data.iterrows()):
        neuron, probs = row[1]

        ax.bar(CENTERS, probs, width=BIN_SIZE, align='center', color='#ff5c5c')

        ax.spines[['top', 'right']].set_visible(False)
        ax.set_xlabel('Time Relative to Spike (s)', fontsize=10.5)
        ax.set_title(f"{neuron}")

        if neuron == 'neuron 1':
            ax.set_ylabel('Spike Probability', fontsize=10.5)
        else:
            ax.set_yticklabels([])

        ax.set_ylim(0, 0.02)

    plt.tight_layout()
    fig.savefig('autocorrelograms.png')

    return


def crosscorrelogram(ts1, ts2):
    """Plot cross correlogram between two neurons
    Args:
        ts1 (np.ndarray): Spike times for neuron 1 (s) (reference)
        ts2 (np.ndarray): Spike times for neuron 2 (s)
    """
    global EDGES
    counts = np.zeros(len(EDGES) - 1, dtype=int)

    for i, k in enumerate(ts1):
        d = ts2 - k
        c, _ = np.histogram(d, bins=EDGES)
        counts += c

    probs = counts / ts1.shape[0]

    # plot cross correlogram
    fig, ax = plt.subplots(figsize=(5, 3))

    ax.bar(CENTERS, probs, width=BIN_SIZE, align='center', color='#ff5c5c')

    ax.spines[['top', 'right']].set_visible(False)
    ax.set_xlabel('Time Relative to Spike (s)', fontsize=10.5)
    ax.set_ylabel('Spike Probability', fontsize=10.5)
    ax.set_title('Cross Correlogram')
    ax.set_xticks([-0.1, -0.05, 0, 0.05, 0.1, 0])

    plt.tight_layout()
    fig.savefig('crosscorrelograms.png')

    return probs


if __name__ == '__main__':
    # go to dir with `Correlations.mat`
    os.chdir("/mnt/arrakis/courses/bmes477/lab5")

    # Define Histogram Parameters
    BIN_SIZE = 0.001  # 1 ms
    X_MIN = -0.1      # -100 ms
    X_MAX = 0.1       # 100 ms

    # Calculate the edges of the bins
    EDGES = np.arange(X_MIN, X_MAX + BIN_SIZE, BIN_SIZE)
    CENTERS = (EDGES[:-1] + EDGES[1:]) / 2

    # Load spike times
    data = scipy.io.loadmat('Correlations.mat')
    neuron1 = data['neuron1'][:, 0]
    neuron2 = data['neuron2'][:, 0]

    # Compute firing rates
    for i, n in enumerate([neuron1, neuron2], 1):
        print(f"Firing rate for neuron {i}: {firingrate(n):.2f} spikes/s")

    # Compute autocorrelogram probabilities
    ac_data = []
    for i, n in enumerate([neuron1, neuron2], 1):
        ac_data.append({
            'neuron': f'neuron {i}',
            'ac_probs': autocorrelogram(n)
        })
    ac_data = pd.DataFrame(ac_data)

    # Plot autocorrelograms
    plot_ac(ac_data)

    # Plot cross correlogram
    probs = crosscorrelogram(neuron1, neuron2)

    # extract center bins
    center_bins = np.where((CENTERS >= -0.005) & (CENTERS <= 0.005))[0]
    center_probs = probs[center_bins]

    # calculate expected value
    expected = np.concatenate((probs[:50], probs[-50:]), axis=0).mean()
    print(f"Expected value: {expected:.4f}")

    # bins above and below expected value
    above = np.where(center_probs > expected)[0]
    below = np.where(center_probs < expected)[0]
    print(f"{len(above)} center bins above expected value")
    print(f"{len(below)} center bins below expected value")

    # calculate standard deviation
    std = np.concatenate((probs[:50], probs[-50:]), axis=0).std()

    # calculate thresholds
    thr = (expected - 3 * std, expected + 3 * std)

    # significant bins
    sig = center_probs[(center_probs < thr[0]) | (center_probs > thr[1])]
    print(f"There are {len(sig)} significant bins with probabilities of {sig.round(4)}.")  # noqa: E501

    # lag time
    lag = CENTERS[center_bins][center_probs == center_probs.max()][0] * 1000
    print(f"The lag time between the highest bin and the reference event is {lag:.2f} ms.")  # noqa: E501
