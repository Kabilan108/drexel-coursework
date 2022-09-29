#!/bin/bash

# Get current working directory
CWD=$(pwd)
# Check if $BLASTDB exists
if [ -z ${BLASTDB+x} ]; then
	BLASTDB=$CWD
fi
# Check if $BLASTDB exists
if [ -z ${BLAST+x} ]; then
	# Change this to the location of your BLAST installation
	#BLAST=$HOME/.anaconda3/envs/blast/bin/
	BLAST=$(which blastp)
fi

# Parse and validate inputs and defaults
if [ $# -eq 0 ]; then
	# No inputs
	validInput=0
elif [ $# -eq 1 ]; then
	# Only one input
	query=$1
	out=blast_report.xml
	validInput=1
elif [ $# -eq 2 ]; then
	# Two inputs
	query=$1
	out=$2
	validInput=1
fi

# Query BLAST Database
if [ $validInput -eq 1 ]; then
	# Download pdb database if not already stored
	if [ ! -f "$BLASTDB/pdbaa.tar.gz.md5" ]; then
		cd $BLASTDB; $BLAST/update_blastdb.pl -decompress pdbaa; cd $CWD
	fi
	# Query BLAST and return results in XML format
	if [ -f "$1" ]; then
		$BLAST/blastp -query $query -db pdbaa -outfmt 5 -out $out
	else
		$BLAST/blastp -query <(echo $query) -db pdbaa -outfmt 5 -out $out
	fi
else
	echo "No valid inputs."
fi

# Example use case
# ./blast_pdb_query.sh query_protein.faa ptn_query_report.xml