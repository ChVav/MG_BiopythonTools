import sys
from Bio import SeqIO
from pathlib import Path

# =====================================
# ARGUMENTS
# =====================================

if len(sys.argv) != 4:
    print("Usage: python extract_species_proteomes.py <combined_proteins.faa> <species_list.txt> <output_folder>")
    sys.exit(1)

input_fasta = sys.argv[1]
species_list = sys.argv[2]
output_dir = Path(sys.argv[3])

output_dir.mkdir(parents=True, exist_ok=True)

# =====================================
# READ SPECIES LIST
# =====================================

with open(species_list) as f:
    species_ids = {
        line.strip()
        for line in f
        if line.strip()
    }

proteomes = {species: [] for species in species_ids}

# =====================================
# EXTRACT PROTEINS
# =====================================

for record in SeqIO.parse(input_fasta, "fasta"):

    # Extract species identifier
    species = record.id.split(".")[0]

    if species in species_ids:
        proteomes[species].append(record)

# =====================================
# WRITE INDIVIDUAL FASTA FILES
# =====================================

for species, records in proteomes.items():

    if not records:
        print(f"WARNING: No sequences found for {species}")
        continue

    output_file = output_dir / f"{species}.faa"

    SeqIO.write(records, output_file, "fasta")

    print(f"{species}: {len(records)} proteins written")

print("\nFinished!")
