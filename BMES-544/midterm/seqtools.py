#      Author:  Tony Kabilan Okeke <tko35@drexel.edu>, 
#               Ahmet Sacan <ahmetmsacan@gmail.com>
# Description:  This script contains improved versions of the midterm programming solution.
#        Date:  02.14.2022

# Imports
from Bio import Align, pairwise2, SeqIO
from multiprocessing import Pool
from functools import partial
from psutil import cpu_count
from time import time
import numpy as np


# Function Definitions
def swalign_score(a: str, b: str, gap: int, submat: Align.substitution_matrices.Array): 
  """
  Compute optimal local alignment scores using the Dynamic Programming Algorithm.
  This is based on the binf.swalign function provided by Dr. Sacan
  """
  # Determine sequence lengths
  A = len(a)
  B = len(b)

  # Initialize score table
  T = np.zeros((A+1, B+1)).tolist()

  # Loop through first sequence
  for i in range(A):
    # Retrive match scores for ith residue in a
    submat_ai = submat[a[i]]

    # Assign table locations to variables (optimize referencing object location)
    # These variables reference positions in the score table object
    Ti = T[i]
    Tiplus1 = T[i+1]

    # Loop through second sequence
    for j in range(B):
      # Compute score for this cell
      Tiplus1[j+1] = max( 0, Ti[j]+submat_ai[b[j]], Tiplus1[j]+gap, Ti[j+1]+gap )

  # Return the optimal alignment score
  return np.max(T,axis=None)


def getAlign(alignment):
  """
  Retrieve aligned region from Biopython alignment object
  """
  a = alignment.seqA[alignment.start:alignment.end]
  b = alignment.seqB[alignment.start:alignment.end]
  return a,b


def closestpair_parallel(ptns: list, maxtime: int=0):
  """
  This function identifies the closest pair of proteins in a list
  based on their local alignment scores using parallel processing.
  It returns a dictionary containing the indicies of items in the pair,
  as well as the percent identity of the alignment.
  This function also keeps track of how much time is spent on identifying the closest pair.
  """

  # Determine the number of proteins
  N = len(ptns)

  # Remove gap characters (they break pairwise2)
  ptns = [ ptn.strip('-') for ptn in ptns ]

  # Retrieve substitution matrix
  submat = Align.substitution_matrices.load('BLOSUM62')

  # Start timer
  tic = time()
  stopped = False #flag

  # Loop through 0:N-1 proteins
  # The inner loop (pool) will loop through 1:N
  max_score = -np.inf
  numaligns = 0
  for i in range(N-1):
    with Pool(cpu_count()) as pool:
      # Compute alignment scores using parallel processing
      # Partial provides the first unnamed argument and 2 named arguments
      # pool.map() provides the second unnamed argument
      iscores = pool.map(partial(swalign_score,ptns[i], gap=-5, submat=submat), ptns[i+1:])

    # Retrieve maximum score
    ind = np.argmax(iscores)
    score = iscores[ind]

    # Store score if necessary
    if score > max_score:
      max_score = score
      max_ind = [i, i+1  + ind]

    # Count alignment scores computed  
    numaligns += N-i;

    # Timing (score computing in parallel)
    if maxtime != 0 and time()-tic > maxtime:
      print(f"---WARNING: I only processed up to row={i:d}")
      stopped = True
      break;

  # Timing (For loop)
  toc = time()-tic;
  numtotalaligns = N*(N-1)/2;
  print("Completed {:d} of {:.2f} comparisons in {:.2f}secs ({:.2f}mins) ({:.3f}secs per comparison)"\
        .format(numaligns, numtotalaligns, toc, toc/60, toc/numaligns))
  if stopped:
    print("Full comparison would have taken around {:.2f}mins.".format(toc/numaligns * numtotalaligns/60))

  # Compute alignment for most similar pair
  most_similar = list( map(ptns.__getitem__, max_ind) )
  align = pairwise2.align.localds(
    *most_similar, match_dict=submat, open=-5, extend=-5,
    one_alignment_only=True
  )[0]
  aligned_A, aligned_B = getAlign(align)

  # Compute percent identity
  matches = 0
  for i in range(len(aligned_A)):
    if aligned_A[i] == aligned_B[i]:
      matches += 1
  pct_identity = matches / len(aligned_A) * 100

  return max_ind, pct_identity


def closestpair_loops(ptns: list, maxtime: int=0):
  """
  This function identifies the closest pair of proteins in a list
  based on their local alignment scores using parallel processing.
  It returns a dictionary containing the indicies of items in the pair,
  as well as the percent identity of the alignment.
  This function also keeps track of how much time is spent on identifying the closest pair.
  """

  # Determine the number of proteins
  N = len(ptns)

  # Remove gap characters (they break pairwise2)
  ptns = [ ptn.strip('-') for ptn in ptns ]

  # Retrieve substitution matrix
  submat = Align.substitution_matrices.load('BLOSUM62')

  # Start timer
  tic = time()
  stopped = False #flag

  # Loop through 0:N-1 proteins
  # The inner loop (pool) will loop through 1:N
  max_score = -np.inf
  numaligns = 0
  for i in range(N-1):
    for j in range(i+1, N):
      score = swalign_score( ptns[i], ptns[j], -5, submat )

      # Store score if necessary
      if score > max_score:
        max_score = score
        ind = [i, j]

      # Count alignment scores computed  
      numaligns += 1;

      # Timing (score computing in parallel)
      if maxtime != 0 and time()-tic > maxtime:
        print(f"---WARNING: I only processed up to row={i:d}")
        stopped = True
        break;
    if stopped: break

  # Timing (For loop)
  toc = time()-tic;
  numtotalaligns = N*(N-1)/2;
  print("Completed {:d} of {:.2f} comparisons in {:.2f}secs ({:.2f}mins) ({:.3f}secs per comparison)"\
        .format(numaligns, numtotalaligns, toc, toc/60, toc/numaligns))
  if stopped:
    print("Full comparison would have taken around {:.2f}mins.".format(toc/numaligns * numtotalaligns/60))

  # Compute alignment for most similar pair
  most_similar = list( map(ptns.__getitem__, ind) )
  align = pairwise2.align.localds(
    *most_similar, match_dict=submat, open=-5, extend=-5,
    one_alignment_only=True
  )[0]
  aligned_A, aligned_B = getAlign(align)

  # Compute percent identity
  matches = 0
  for i in range(len(aligned_A)):
    if aligned_A[i] == aligned_B[i]:
      matches += 1
  pct_identity = matches / len(aligned_A) * 100

  return ind, pct_identity


def main():
  """
  Defines and Run Test Cases
  """
  # Load protein list
  ptns = [str(fastaptn.seq) for fastaptn in SeqIO.parse('uteroglobin.blastresults.fasta','fasta')]
  
  # Compute Results
  print("\n--- Testing closestpair Functions ---")
  print("\n--- Testing Loop Implementation ---")
  res = closestpair_loops(ptns, maxtime=10)

  print("\n--- Testing Parallelized Implementation ---")
  res = closestpair_parallel(ptns, maxtime=10)

if __name__ == '__main__':
  main()