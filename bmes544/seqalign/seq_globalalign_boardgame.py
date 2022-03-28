# Authors: Tony Kabilan Okeke <tko35@drexel.edu>
# Date: 01.27.2022

# Make necessary imports
from seq_boardgame import seq_boardgame
import numpy as np

def seq_globalalign_boardgame(a: str, b: str, match: int = 5, mismatch: int = -4, gap: int = -5):
  """
  This function takes two DNA sequences a and b and returns the optimal gloabl alignment score.
  This function depends on seq_boardgame()

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

  # Create the scoring matrix
  score_mat = np.zeros( (len(a) + 1, len(b) + 1) )

  # Loop through sequences, assigning match and mismatch scores accordingly
  # The first row and column of the matrix are set to zero
  for i in range( len(a) ) :
    for j in range( len(b) ):
      if a[i] == b[j]:
        score_mat[i+1, j+1] = match
      else:
        score_mat[i+1, j+1] = mismatch

  # Compute the optimal alignmnet score
  score = seq_boardgame(B = score_mat, gap = gap)
  
  return score