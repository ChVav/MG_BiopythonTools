
from Bio import SeqIO
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Extract a subset of sequences from a FASTA (.fna, .faa, .fasta) or GenBank file (.gbk, .genbank).")
    parser.add_argument("input_file", help="Input FASTA or GenBank file")
    parser.add_argument("output_file", help="Output file to store extracted sequences")
    parser.add_argument("wanted_ids", help="File containing a list of wanted sequence IDs")
    
    args = parser.parse_args()
    
    # Check the file extension to determine the format
    if args.input_file.endswith((".fna", ".faa", ".fasta")):
        input_format = "fasta"
    elif args.input_file.endswith((".gbk", ".genbank")):
        input_format = "genbank"
    else:
        print("Unsupported file format. Please provide a FASTA (.fna, .faa, .fasta) or a GenBank file (.gbk, .genbank).")
        sys.exit(1)  # Exit with an error code

    # Load the list of wanted sequence IDs
    with open(args.wanted_ids, "r") as ids_file:
        wanted_ids = [line.strip() for line in ids_file]

    # Extract sequences with matching IDs
    extracted_sequences = []
    with open(args.input_file, "r") as input_handle:
        for record in SeqIO.parse(input_handle, input_format):
            if record.id in wanted_ids:
                extracted_sequences.append(record)

    # Write the extracted sequences to the output file
    with open(args.output_file, "w") as output_handle:
        SeqIO.write(extracted_sequences, output_handle, input_format)

    print(f"Extracted {len(extracted_sequences)} sequences to {args.output_file}")

if __name__ == "__main__":
    main()