from Bio import Entrez, SeqIO
import io

# Function to search and download sequences from NCBI
def search_and_download_sequences(query, max_count=3):
    Entrez.email = "example@example.com"  # An email is required by NCBI for using their API

    # Search for the given query in the nucleotide database
    handle = Entrez.esearch(db="nucleotide", term=query, retmax=max_count)
    search_results = Entrez.read(handle)
    handle.close()

    # Fetch the sequence details
    ids = search_results["IdList"]
    sequences = []

    if ids:
        handle = Entrez.efetch(db="nucleotide", id=ids, rettype="fasta", retmode="text")
        raw_data = handle.read()
        handle.close()

        # Parse the data
        for record in SeqIO.parse(io.StringIO(raw_data), "fasta"):
            # Rename the sequence
            description_parts = record.description.split(" ")
            genus_species = "-".join(description_parts[:2])
            accession_number = description_parts[-1].split(".")[0]
            new_name = f"{genus_species}-{accession_number}"
            record.id = new_name
            record.name = new_name
            record.description = new_name
            sequences.append(record)

    return sequences

# Search for alcohol dehydrogenase gene in three different insect species
adh_sequences = []
for insect in ["Drosophila", "Apis", "Anopheles"]:
    adh_sequences.extend(search_and_download_sequences(f"alcohol dehydrogenase {insect}"))

# Check the number of sequences fetched
len(adh_sequences)
