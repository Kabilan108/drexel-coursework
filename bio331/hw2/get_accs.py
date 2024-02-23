
from Bio import SeqIO, Entrez
from rich import print
import sys
import re

Entrez.email = "tonykabilanokeke@gmail.com"

def get_metadata(accession):
    handle = Entrez.efetch(db="nucleotide", id=accession, rettype="gb", retmode="text")
    record = SeqIO.read(handle, "genbank")
    handle.close()
    return {
        "definition": record.description,
        "accession": record.id,
        "organism": record.annotations["organism"],
        "source": record.annotations["source"],
    }


def process_fasta(fasta_path):
    try:
        for seq_record in SeqIO.parse(fasta_path, "fasta"):
            accession = re.match(r'^(.*)\.1', seq_record.id).group(1)
            metadata = get_metadata(accession)
            print(metadata)
    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python get_accs.py <path_to_fasta>")
        sys.exit(1)
    process_fasta(sys.argv[1])

