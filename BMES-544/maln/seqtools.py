# Authors: Tony Kabilan Okeke <tko35@drexel.edu>
#          Ifeanyi Osuchukwu  <imo27@drexel.edu>
# Date:    02.20.2022

# Imports
from Bio import pairwise2, SeqIO
from multiprocessing import Pool
from psutil import cpu_count
from functools import partial
import numpy as np

# Function definitions
def _nwalign_pct_id(a, b):
    """
    Wrapper for pairwise2.align.globaldx() that can be used by partials()
    Computes global alignment score with free end gaps, and returns percent identity.
    """
    if a.seq != b.seq:
        # Compute alignment and store aligned sequences
        align = pairwise2.align.globalxs(
            a.seq, b.seq, open=-5, extend=-5, penalize_end_gaps=False,
            one_alignment_only=True
        )[0]
        # Store aligned sequences
        a = align.seqA
        b = align.seqB
        denom = align.end - align.start
        # Compute percent identity
        ident = 0
        for i,j in zip(a,b):
            if i == j:
                ident += 1
        p_id = ident/denom
    else:
        p_id = 1

    return p_id

def fasta_removeredundants(file: str, identthreshold: float=0.95):
    """
    Remove Redundant Proteins From BLAST Results (FASTA file)

    This function takes a fasta file containing aligned sequences from BLAST
    and writes a file with the extension 'nonredundant.fasta' that contains
    the non-redundant proteins from the fasta file.
    It removes entries thate are more than 'identthreshold' similar to any prior
    entry in the file.
    Similarity is calculated based on global alignment scores with free end gaps.
    The function returns the fraction of sequences removed.

    Parameters
    ----------
    file: str
        The file containing BLAST results
    identthreshold: float
        Threshold for similarity between sequences
    """

    # Read proteins from file
    ptns = list( SeqIO.parse(file, 'fasta') )
    N = len(ptns)

    # Loop through list of proteins
    avoid = []
    for i in range(N-1):
        if i in avoid:
            continue
        with Pool(cpu_count()) as pool:
            identities = pool.map(partial(_nwalign_pct_id, ptns[i]), ptns[i+1:])

        # Get indices of proteins that exceed threshold
        identities = np.array(identities)
        ind = i+1 + np.where( identities > identthreshold )[0]
        avoid.extend(ind.tolist())
    
    # Filtered sequences to be written to fasta file
    filt_ptns = [ ptn for (i, ptn) in enumerate(ptns) if i not in avoid ]

    # Compute fraction removed
    pct_lost = len(filt_ptns) / len(ptns)

    # Store filtered sequences in fasta file
    file_out = file + '.nonredundant.fasta'
    SeqIO.write(filt_ptns, file_out, 'fasta');

    return pct_lost

def running_mean(x: np.array, N: int):
    """
    This function is used to create values of a moving average.
    It takes a 1D array of values, and a window size as input.
    Returns averaged data
    Credit: https://stackoverflow.com/questions/13728392/moving-average-or-running-mean
    """
    cumsum = np.cumsum( np.insert(x, 0, 0) )
    return (cumsum[N:] - cumsum[:-N]) / float(N)