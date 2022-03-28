# Author: Tony Kabilan Okeke <tko35@drexel.edu>
# Date:   01.27.2022

# Make necessary imports
from typing import Union
import numpy as np

def seq_boardgame(B: Union[list, np.ndarray], gap: int = -5):
  """
    Given a R-by-C game board, with certain weights (money) on each square, you are asked
    to start from the top left corner (r=c=1) and move all the way to the bottom-right 
    corner (r=R, c=C), moving right, down, or diagonal at each step.
    Diagonal moves are free, you collect the money from the cell you arrive in.
    Moving right or down, you pay a gap penalty of $5 and lose the money in the next cell.
    You always collect money in the top-left square.
    ** Assume the top left corner of the board is always 0
    
    PARAMETERS
    ----------
    B: list or np.ndarray (scoring matrix)
      R-by-C numpy array (matrix) containing the amount of money in each cell
    gap: int (gap penalty)
      The penalty paid for right or down moves
  """
  
  # Check input types
  if isinstance(B, list): 
    # Convert list to numpy array
    B = np.array(B)

  # Determine matrix dimensions
  R, C = B.shape
  
  # Initialize dynamic programming table
  S = np.zeros((R,C))

  # Fill dynamic programming table
  for r in range(R):
    for c in range(C):
      if (r,c) == (0,0): # Cell 1 is always 0
        S[r,c] = 0
      elif r == 0: # Fill rest of row 1
        S[r,c] = S[r,c-1] + gap
      elif c == 0: # Fill rest of column 2
        S[r,c] = S[r-1,c] + gap
      else: # Fill interior cells
        S[r,c] = max([ S[r-1,c-1] + B[r,c], S[r-1,c] + gap, S[r,c-1] + gap ])

  # Return value of bottom right cell
  return int(S[r,c])