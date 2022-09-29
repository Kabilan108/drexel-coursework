# Authors: Tony Kabilan Okeke <tko35@drexel.edu>
#          Ifeanyi Osuchukwu  <imo27@drexel.edu>
# Date: 02.24.2022

# Imports
from itertools import permutations
from typing import Union
from numpy import Inf
from Bio import SeqIO

# Definitions
def overlap(a: str, b: str) -> dict:
    """
    Determine overlap between strings
    """
    # Loop through a and record overlap start position if any
    overlap_pos = -Inf
    for i in range(len(a)):
        if b.startswith(a[i:]):
            overlap_pos = i
            break

    # If no overlap found, use length of a
    if overlap_pos == -Inf:
        overlap_pos = len(a)
    
    # Determine overlap length
    overlap_len = len(a[overlap_pos:])
    
    # Return overlap position and length
    return {'Pos': overlap_pos, 'Len': overlap_len}

def merge_on_overlap(a: str, b: str) -> dict:
    """
    Merge strings on their overlap
    """
    # Determing start position of overlap
    pos = overlap(a, b)['Pos']

    # Return merged superstring
    return [a[:pos] + b]

def fastq_assemble_greedy( reads: Union[list, str] ) -> list:
    """
    Implementation of the Greedy Sequence Assemble Algorithm.
    
    @param reads: list or str
        List of short strings, or a fasta file containing short reads
    @return
        List of assembled sequences 
    """

    # Parse input if necessary (convert to read)
    if isinstance(reads, str):
        reads = [ str(seq.seq) for seq in SeqIO.parse(reads, 'fastq') ]

    while len(reads) > 1:
        # Loop through (ordered) pairs of strings
        pairs = list( permutations(reads, 2) )

        # Compute overlap for each ordered pair
        overlaps = {pair: overlap(*pair)["Len"] for pair in pairs}

        # Exit loop if there are no overlaps
        if max(overlaps.values()) == 0: break

        # Select pair with maximum overlap (if there are multiple, select based on alphabetic order)
        mx = sorted([ k for k,v in overlaps.items() if v == max(overlaps.values()) ])[0]

        # Merge maximum pair and edit list
        reads = [read for read in reads if read not in mx] + merge_on_overlap(*mx)

    return sorted(reads)