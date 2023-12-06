


# Import packages
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.io

import os
os.chdir("/mnt/arrakis/courses/bmes477/lab4")


# Define Histogram Parameters
BIN_SIZE = 0.001  # 1 ms
X_MIN = -0.1      # -100 ms
X_MAX = 0.1       # 100 ms

# Calculate the edges of the bins
BIN_EDGES = np.arange(X_MIN, X_MAX + BIN_SIZE, BIN_SIZE)


def generate_psth(ts, ref):
    """Generate a Peristimulus Time Histogram (PSTH)
    Args:
        ts  (np.ndarray): Spike times for a neuron (s)
        ref (np.ndarray): Reference events for a whisker (s)
    Return:
        psth_counts(np.ndarray): the probability of spikes in each bin.
    """

    global BIN_EDGES

    # Initialize list to hold counts for each bin
    psth_counts = np.zeros(len(BIN_EDGES) - 1, dtype=int)

    # Iterate over each stimulus time
    for ref_k in ref:
        # calculate distance from stimulus to all spike times
        d = ts - ref_k

        # calculate number of spikes in each bin
        counts, _ = np.histogram(d, bins=BIN_EDGES)

        # add counts to psth_counts (sum counts from each stimulus)
        psth_counts += counts
    
    # calculate probability of spikes in each bin
    psth_probs = psth_counts / len(ref)

    return psth_probs


def plot_psth(psth):
    """Plot a Peristimulus Time Histogram
    Args:
        psth(pd.DataFrame): Data frame containing neuron, location and psth data
    """

    global BIN_EDGES, BIN_SIZE

    fig, axes = plt.subplots(2, 2, figsize=(6, 4))
    axes = axes.flatten()

    for i, row in psth_data.iterrows():
        ax = axes[i]
        neuron, location, psth_probs = row

        bin_centers = (BIN_EDGES[:-1] + BIN_EDGES[1:]) / 2

        ax.bar(bin_centers, psth_probs, width=BIN_SIZE, align='center', color='#ff5c5c')
        
        ax.spines[['top', 'right']].set_visible(False)

        if i in [2, 3]:  ax.set_xlabel('Time Relative to Stimulus (s)', fontsize=10.5)
        if i in [0, 2]:  ax.set_ylabel('Spike Probability', fontsize=10.5)
        ax.set_title(f"{neuron} - {location}")
        
        ax.set_xlim(-0.1, 0.1)
        ax.set_ylim(0, 0.55)
        ax.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5])

    plt.tight_layout()


def calculate_BA(psth_probs, pre_stim_window=(-0.1, -0.005)):
    """Calculate Background Activity
    Args:
        psth_probs(np.ndarray): Probability of spikes in each bin
        pre_stim_window(tuple): Time window to calculate BA
    Returns:
        ba(float): Background activity
        sd(float): Standard deviation of BA
    """

    global BIN_EDGES

    # find bin indices that correspond to the pre-stimulus window
    pre_stim_bins = np.where(
        (BIN_EDGES >= pre_stim_window[0]) & (BIN_EDGES < pre_stim_window[1])
    )[0]

    # calculate BA and SD of BA
    ba = np.mean(psth_probs[pre_stim_bins[:-1]])
    sd = np.std(psth_probs[pre_stim_bins[:-1]])

    return ba, sd


def find_significant_responses(psth_probs, threshold, post_stim_window=(0.005, 0.09)):
    """Find significant responses in a PSTH and extract neurophysiological measures 
    Args:
        psth_probs(np.ndarray): Probability of spikes in each bin
        threshold(float): Threshold for significant responses
        post_stim_window(tuple): Time window to search for significant responses
    Returns:
        dict: Neurophysiological measures
    """

    global BIN_EDGES

    # Find bins that correspond to the post-stimulus window
    post_stim_bins = np.where(
        (BIN_EDGES[:-1] >= post_stim_window[0]) & (BIN_EDGES[:-1] < post_stim_window[1])
    )[0]

    # Initialize variables to store measures
    fsb, lsb, pl, pr = None, None, None, 0
    consecutive_bins = 0   # number of consecutive bins over threshold

    # iterate through bins to find fsb and lsb
    found_fsb = False
    for i in post_stim_bins:
        if psth_probs[i] > threshold:
            if consecutive_bins == 0 and not found_fsb:  # first significant bin
                fsb = i
            consecutive_bins += 1

            # update lsb
            lsb = i

            # update pr
            if psth_probs[i] > pr:
                pr = psth_probs[i]
                pl = BIN_EDGES[i]
        else:
            if consecutive_bins > 2:
                # found significant response
                found_fsb = True
            else:
                # reset consecutive_bins
                consecutive_bins = 0
    
    # special case: fsb == lsb -> no significant response
    if fsb == lsb:
        pr, pl, fsb, lsb = np.nan, np.nan, np.nan, np.nan
    
    # calculate measures if significant response was found
    if fsb is not None and lsb is not None and consecutive_bins > 2:
        # response magnitude
        rm = np.sum(psth_probs[fsb:lsb+1])

        # first significant bin latency
        fbl = BIN_EDGES[fsb]

        # last significant bin latency
        lbl = BIN_EDGES[lsb]
    else:
        # if no significant response
        rm, fbl, lbl = np.nan, np.nan, np.nan
    
    return {
        "RM": rm,
        "PR": pr,
        "FBL": fbl,
        "LBL": lbl,
        "PL": pl
    }


if __name__ == "__main__":

    # Load PSTH.mat file
    data = scipy.io.loadmat('PSTH.mat')['PSTHdata'][0]
    data = [d.reshape(-1) for d in data]

    # Extract variables
    ts = {k:v for k, v in zip(['neuron 1', 'neuron 2'], data[:2])}  # spike times
    ref = {k:v for k, v in zip(['location 1', 'location 2'], data[2:])} # reference events

    # compute psth for each neuron and whisker location
    psth_data = []
    for n in ts.keys():
        for l in ref.keys():
            psth_data.append({
                'neuron': n,
                'location': l,
                'psth_probs': generate_psth(ts[n], ref[l])
            })

    # Convert to pandas dataframe
    psth_data = pd.DataFrame(psth_data)

    # Plot PSTH
    plot_psth(psth_data);

    # calculate BA for each neuron-location pair
    for index, row in psth_data.iterrows():
        ba, sd = calculate_BA(row['psth_probs'])
        psth_data.at[index, 'ba'] = ba
        psth_data.at[index, 'sd'] = sd

    # compute the threshold for each neuron-location pair
    psth_data['threshold'] = psth_data['ba'] + 3 * psth_data['sd']

    # find significant responses for each neuron-location pair
    for index, row in psth_data.iterrows():
        measures = find_significant_responses(row['psth_probs'], row['threshold'])

        for k, v in measures.items():
            psth_data.at[index, k] = v

    (psth_data[['neuron', 'location', 'RM', 'PR', 'FBL', 'LBL', 'PL']]
        .rename(columns={
            'neuron': 'Neuron', 'location': 'Location',
            'FBL': 'FBL (s)', 'LBL': 'LBL (s)', 'PL': 'PL (s)'
        })
        .style
        .hide(axis='index')
        .format('{:.4f}', subset=['RM', 'PR', 'FBL (s)', 'LBL (s)', 'PL (s)']))
