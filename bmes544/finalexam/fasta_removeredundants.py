# Author: Tony Kabilan Okeke <tko35@drexel.edu>
# Date:    03.14.2022

# Imports
from Bio import SeqIO
import numpy as np

# Function definitions
def fasta_removeredundants(file: str, file_out: str, identthreshold: float=0.9):
    """
    Remove Redundant Alignments From Multiple Alignment Results

    This function takes a fasta file containing aligned sequences from ClustalOmega
    and writes a file that contains the non-redundant proteins from the fasta file.
    It removes entries thate are more than 'identthreshold' similar to any prior
    entry in the file.

    Parameters
    ----------
    file: str
        The file containing BLAST results
    file_out: str
        The results file
    identthreshold: float
        Threshold for similarity between sequences
    """

    # Read alignments from file
    alignments = list( SeqIO.parse(file, 'fasta') )
    N = len(alignments)

    # Loop through the alignments
    avoid = []
    for i in range(N-1):
        if i in avoid:
            continue
        
        # Compute percent identities with the rest of the alignments
        a = alignments[i].seq
        identities = []
        for j in range(i+1, N):
            # Compute percent identity
            b = alignments[j].seq
            ident = 0
            for ca,cb in zip(a,b):
                if ca == cb:
                    ident += 1
            identities.append(ident/len(a))
        
        # Get indices of proteins that exceed threshold
        identities = np.array(identities)
        ind = i+1 + np.where(identities > identthreshold)[0]
        avoid.extend(ind.tolist())

    # Filtered sequences to be written to fasta file
    filtered = [ align for (i, align) in enumerate(alignments) if i not in avoid ]

    # Print fraction removed
    print(f"{len(filtered) / len(alignments) * 100:.2f}% of sequences were removed.")
    
    # Store filtered sequences in fasta file
    SeqIO.write(filtered, file_out, 'fasta');

    return filtered