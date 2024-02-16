#!/bin/bash

#SBATCH --mail-user=tko35@drexel.edu
#SBATCH --account=bio331534Prj
#SBATCH --nodes=1
#SBATCH --time=00:15:00
#SBATCH --mem=24G
#SBATCH --partition=def

module load ncbi-blast/2.13.0

makeblastdb -in data/chitinase-proteins.fst -dbtype 'prot'

