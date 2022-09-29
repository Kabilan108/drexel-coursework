# Sequence Similarity

- BLOSUM & PAM Matrix - capture the amount of mutations that occur in nature
- Mutations appear as the virus is being replicated - substitutions, insertions and deletions
- Compatible substitution - favored because amino acids are compatible in their impact on protein structure
- Use sequences from nature to evaluate how compatible sequences from nature are
- To quantify substitutibility (PAM),
    - look at large number of sequences,
    - manually aligh & evaluate how many times a particular mutation occurs.
    - place counts into an observed frequence matrix (PAM)
    - random estimation of frequencies - expected
    - if observed >> expected, amino acid substitution is favorable → log likelihood ratio
        - similar to BLOSUM
    - PAM creates a phylogenetic tree
        - estimation of history
        - only compares sequuences as they appear in the phylogenetic tree
        - Substitutions can only be counted between parent and child nodes on the phylogenetic tree
- BLOSUM takes blocks of sequnences
    - assume every character is replaced in block
    - compares all given sequences → all considered mutations
    - VVAD
    AVAD
    DVAD
    DAAA
        - All sequences are considered possible sources as well as children
        - No difference between original sequence and mutated sequence
        - Assume mutations occur in colums
        - $N_{V\to A} = 4$
        - $N_{A\to A} = 12$
        - Each column: 12 total substitutions
        - Total number of substitutions: 4*12 = 48
        - $S_{AA} = 2\log_2\frac{P_{AA}}{P_A*P_A}$
        - P_AA = observed = N_AA / (4*NAA)
        - P_A = #A/#tot
        - +ve → substitution is favored
        - -ve → substitution is NOT favored
        - frequency of A (q) = #of A / total #
        - pAA = NAA / total possible substitutions
        - sum of q = 1
        - sum of PAA = 1 (pairs of substitutiosn)
    - Need to know some ionformation about the relationship between dna sequences to decide the appropriate blosum matrix to use → theoretical suggestion
    - Common practice - stick to BLOSUM-62 because  it works well for both highly similar and highly divergent sequences

### Comparing sequences:

- **In MATLAB**
    - Add `Dropbox\bmes.ahmet` to MATLAB path
    - Use most mlx file from blackboard
    - `fasta` - files used for storing, sharing sequences
        - they begin with a line describing the protein or dna sequence
        - one or more lines then contain the actual sequence
        - `fasta` files may contain multiple sequences
        - `>` marks the beginning of a sequence
    - self-dot plots - visual indication of what parts of a sequence are repeated
        - [How to create a dotplot of two DNA sequence in python - Stack Overflow](https://stackoverflow.com/questions/40822400/how-to-create-a-dotplot-of-two-dna-sequence-in-python?rq=1)
        - `seqdotplot` in matlab - can be used to compare a sequence with itself or another sequnence
        - a `window_size`  argument is used to smooth out the figure displayed (window of 10 amino acids)
        - `match filter`
        - In a windowsize of 10, every filter, 5 will be matched with a dot
        - cluster of dots → similarity, not by chance
        - Filter out sparse dots → look at window → if window contains less than 5 matches (filter threshold) then dots will be ignored
        - short horizonal lines → short sequence that is repeating multiple times within that segment of the sequence
        - Opposite diagonal - inversion - reversed copy on entiher sequence - sequences run in opposite directions
        - → need to figure it out in `python`
            - → need to create a comparison matrix to generate dotplot
        - Next week → sequence alignment algorithms
            - ALignment - taking a sequence and aligning similar characters with each other
            - gaps inserted for insertion or deletion mutations
            - find ‘best’ pairing of dna nucleotides
        
- Local alignment
    - take 2 sequences and find short highly similar regions between the two sequences
- Global alignment
    - take two sequences in their entirety and compare them
- If two sequences contain mostly the same genetic material → global alignment
- Comparing genomes of two organisms → local alignment because ther might be some subregions that are shared between the two genomes
- If you have two sequences that represent the same or related things - two copies of same genes or genes from homologous species - perform global alignemnt
- If you are comparing long sequences, parts of which can be similar to other things → use local alignment
- searching for sequences → local alignment
- provide `alphabet` to `swalign` and `nwalign` → `aa` for amino acids, `nt` for nucleotides
- Can also specify `scoringmatrix` which allows comparisons of characters to characters
    - eg: get M→W substitution matrix from BLOSU50 or BLOSUM62
    - Amino acid matrix - 20x20, 24x24 to include ambiguous amino acids
    - Nucleotide matrix - 4x4
- Identity calculations
    - use identity matrices as scoring matrix
        - Match = +1
        - No match = -1
        - create your own 24x24 (in MATLAB) matrix
            - +1 along diagonal
            - -1 everywhere else
- Seq alignment score → sum of scores
- a gap score can be specified
    - ‘linear gap model’ → gap open and gap extend will have the same value
        - every gap is scored by the same amount
        - add -8 (default) to score for every gap (Different convention in python - see documentation for specifying gaps - negative number in py vs positive number in matpoab)
        - Matches & No matches → add score from scoring matrix
    - ‘affine gap model’
        - male a distinction for a stretch of gap characters
        - the first one is scored differently
            - the first is scored as a `GapOpenValue`
            - the rest are scored as `ExtendGapValue`
    - matalb will return the alignment as a 3 row character matrix
        - compare 1st row and 3rd row to determine the number of matching positions
        - total score = matches - nomatch - gaps

Python 1st letter - match params

- Use d version of alignment functions to pass custom substitution matrices to matlab
- Use m version to specify the match and mismatch scores
- Use d for PAM scoring matrix

Python 2nd letter - gap penalty

- linear model - s
- affine model - d

In python, substitution matrix is gotten as a dictionary