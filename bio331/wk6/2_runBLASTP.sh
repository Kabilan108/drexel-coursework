#!/bin/bash

#SBATCH --mail-user=tko35@drexel.edu
#SBATCH --account=bio331534Prj
#SBATCH --nodes=1
#SBATCH --time=00:15:00
#SBATCH --mem=24G
#SBATCH --partition=def

module load ncbi-blast/2.13.0

fields='qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore'

blastp \
    -query data/putative-chitinases.txt \
    -db data/chitinase-proteins.fst \
    -outfmt "6 $fields"
    -max_target_seqs 1 \
    -out data/chitinase.blastp.output

(echo "$(echo $fields | sed 's/\ /\t/g')"; cat data/chitinase.blastp.output) > data/chitinase.blastp.tsv
