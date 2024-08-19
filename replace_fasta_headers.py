import argparse
from Bio import SeqIO

def replace_fasta_headers(input_fasta, output_fasta, id_map):
    # Read the ID map into a dictionary
    id_dict = {}
    with open(id_map, 'r') as f:
        for line in f:
            old_id, new_id = line.strip().split()
            id_dict[old_id] = new_id

    # Read the input FASTA and write the updated FASTA
    with open(input_fasta, 'r') as infile, open(output_fasta, 'w') as outfile:
        for record in SeqIO.parse(infile, 'fasta'):
            # Replace the header if it exists in the id_dict
            if record.id in id_dict:
                record.id = id_dict[record.id]
                record.description = record.id  # Update the description as well
            SeqIO.write(record, outfile, 'fasta')

    print(f"FASTA headers updated and saved to {output_fasta}")

def main():
    parser = argparse.ArgumentParser(description="Replace FASTA headers based on an ID map.")
    parser.add_argument("input_fasta", help="Path to the input FASTA file.")
    parser.add_argument("output_fasta", help="Path to the output FASTA file.")
    parser.add_argument("id_map", help="Path to the ID map file. Each line should contain an old ID and a new ID separated by whitespace.")
    
    args = parser.parse_args()
    
    replace_fasta_headers(args.input_fasta, args.output_fasta, args.id_map)

if __name__ == "__main__":
    main()
