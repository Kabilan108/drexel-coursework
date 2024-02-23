# Picotte BLAST Exercise

Author: Tony K Okeke
Date:   02-16-2024


## Notes

- `wk6/data/chitinase-proteins.fst` - searched 'chitinase' in 'Identical Protein Database'
    - input file for analysis
- `mkblastdb.sh` - SLURM job script to create blast database from input fst file
    - run with `sbatch`
    - output:

    ```raw
    Building a new DB, current time: 02/16/2024 14:39:27
    New DB name:   /home/tko35/courses/bio331/wk6/data/chitinase-proteins.fst
    New DB title:  data/chitinase-proteins.fst
    Sequence type: Protein
    Keep MBits: T
    Maximum file size: 3000000000B
    Adding sequences from FASTA; added 105923 sequences in 1.70125 seconds.

    /bin/rm: cannot remove '/local/scratch/9777365': Permission denied
    ```

- use `2_runBLASTP.sh` to run the BLASTsearch
    - `data/chitinase-proteins.fst` should be the `db` arg
    - `data/putative-chitinases.txt` is the input file for the BLASTp search
        - a separate query will be run for each file in the `-query` file
