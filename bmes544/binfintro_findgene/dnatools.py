# Authors: Tony Kabilan Okeke <tko35@drexel.edu>
#          Ifeanyi Osuchukwu <imo27@drexel.edu>
# Date: 01.08.2022

# Make necessary imports
from re import findall
from json import dumps

# Create dictionary to store complementary base pairs
c_base = {"A": "T", "G": "C", "T": "A", "C": "G"}

# Create dictrionary to store genetic code
# Source: https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=tgencodes#SG1
gen_code = {"UUU": "F", "UCU": "S", "UAU": "Y", "UGU": "C", "UUC": "F", "UCC": "S", "UAC": "Y", "UGC": "C",
            "UUA": "L", "UCA": "S", "UAA": "*", "UGA": "*", "UUG": "L", "UCG": "S", "UAG": "*", "UGG": "W",
            "CUU": "L", "CCU": "P", "CAU": "H", "CGU": "R", "CUC": "L", "CCC": "P", "CAC": "H", "CGC": "R",
            "CUA": "L", "CCA": "P", "CAA": "Q", "CGA": "R", "CUG": "L", "CCG": "P", "CAG": "Q", "CGG": "R",
            "AUU": "I", "ACU": "T", "AAU": "N", "AGU": "S", "AUC": "I", "ACC": "T", "AAC": "N", "AGC": "S",
            "AUA": "I", "ACA": "T", "AAA": "K", "AGA": "R", "AUG": "M", "ACG": "T", "AAG": "K", "AGG": "R",
            "GUU": "V", "GCU": "A", "GAU": "D", "GGU": "G", "GUC": "V", "GCC": "A", "GAC": "D", "GGC": "G",
            "GUA": "V", "GCA": "A", "GAA": "E", "GGA": "G", "GUG": "V", "GCG": "A", "GAG": "E", "GGG": "G"}

def pprint(dict):
  """
    Pretty Print Dictionary
    A nicer way to print dictionaries
  """
  return print( dumps(dict, indent = 2) )

def seq_transcribe(dna):
  """
    Transcribe a DNA sequence to mRNA
    This function takes a string containing the coding DNA strand (5'-3') as input
    and returns the noncoding strand (5'-3'), transcribed mRNA (5'-3'), and the
    protein molecule.
    Stop codons are encoded as '*'
  """

  # Determine noncoding (complementary) strand (5' - 3')
  noncode = ''.join( [c_base[base] for base in dna] )[::-1]

  # Determine mRNA sequence
  mrna = dna.replace('T', 'U')

  # Split the mrna into triplet codons ignoring any residues that are not multiples of 3
  codons = [ mrna[i:i+3] for i in range(0, len(mrna), 3) if len(mrna[i:i+3]) == 3 ]

  # Convert codons to proteins based on the genetic code
  ptn = ''.join( [gen_code[codon] for codon in codons] )

  # Retrun non-coding strand, mRNA, and protein sequences
  return {"noncode": noncode, "mrna": mrna, "ptn": ptn}

def seq_findgene(dna):
  """
    Locate and transcribe the longest ORF in a DNA sequence
    This function takes a string containing a single strand of DNA and returns
    thee amino acid sequence of the longest gene it finds within the DNA sequence.
    A 'gene' is defined as a reading fram that starts with the AUG codon, and ends with 
    a stop codon (UAA, UAG, or UGA).UAA
  """

  # Store the given dna sequence and its complement
  dna = [dna, seq_transcribe(dna)['noncode']]

  # Translate each strand into proteins.
  # One protein will be translated for each possible reading frame (3 proteins per strand)
  orfs = [ seq_transcribe(strand[i:])['ptn'] for i in range(0, 3) for strand in dna ]

  # Identify all genes in the orfs
  valid_genes = map(lambda y: findall(r'M\w*[*]', y), orfs)
  valid_genes = [ x for orf in valid_genes for x in orf ] # Flatten list

  # If no genes were found return empty string
  if valid_genes ==[]:
    gene = ""
  else:
    # Select the longest gene
    gene = max(valid_genes, key=len)

  return gene