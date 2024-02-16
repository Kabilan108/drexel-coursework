#!/bin/bash
#
#SBATCH --mail-user=your_email@drexel.edu
#SBATCH --account=bio331534Prj
#SBATCH --nodes=1
#SBATCH --time=00:15:00
#SBATCH --mem=24G
#SBATCH --partition=def

module load ncbi-blast/2.13.0

makeblastdb -in sequence.fasta -dbtype 'prot'
