
from Bio import SeqIO
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Extract a subset of sequences from a FASTA (.fa, .fna, .faa, .fasta) or GenBank file (.gbk, .genbank).")
    parser.add_argument("input_file", help="Input FASTA or GenBank file")
    parser.add_argument("output_file", help="Output file to store extracted sequences")
    parser.add_argument("wanted_ids", help="File containing a list of wanted sequence IDs")

    args = parser.parse_args()

    # Check the file extension to determine the format
    if args.input_file.endswith((".fa",".fna", ".faa", ".fasta")):
        input_format = "fasta"
    elif args.input_file.endswith((".gbk", ".genbank")):
        input_format = "genbank"
    else:
        print("Unsupported file format. Please provide a FASTA (.fa, .fna, .faa, .fasta) or a GenBank file (.gbk, .genbank).")
        sys.exit(1)  # Exit with an error code

    # Load the list of wanted sequence IDs into a set for fast look-up
    with open(args.wanted_ids, "r") as ids_file:
        wanted_ids = set(line.strip() for line in ids_file)

    # Create an index for the input file
    record_index = SeqIO.index(args.input_file, input_format)

    # Write the extracted sequences to the output file
    with open(args.output_file, "w") as output_handle:
        count = 0
        for record_id in record_index:
            record_id_first_part = record_id.split()[0]  # Take only the first part of the ID
            if record_id_first_part in wanted_ids:
                SeqIO.write(record_index[record_id], output_handle, input_format)
                count += 1

    print(f"Extracted {count} sequences to {args.output_file}")

if __name__ == "__main__":
    main()
