# Authors: Tony Kabilan Okeke <tko35@drexel.edu>
# Date: 01.27.2022

# Make necessary imports
from Bio.pairwise2 import align

def seq_globalalign_nwalign(a: str, b: str, match: int = 5, mismatch: int = -4, gap: int = -5):
  """
  This function takes two DNA sequences a and b and returns the optimal gloabl alignment score.
  This function depends on Bio.pairwise2.align.globalms

  PARAMETERS
  ----------
  a: str, b: str
    DNA sequences
  match: int
    The score assigned to matching nucleotides
  mismatch: int
    The score assigned to mismatched nucleotides
  gap: int
    The gap penalty
  """

  # Align the sequences using the Needleman-Wunsch Algorithm
  alignment = align.globalms(a, b, match, mismatch, gap, gap)[0]

  # Return score
  return alignment.score