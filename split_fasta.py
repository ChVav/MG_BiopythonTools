import argparse
import os
from Bio import SeqIO

def split_fasta(input_file, num_subsets):
    records = list(SeqIO.parse(input_file, "fasta"))
    num_records = len(records)
    records_per_subset = num_records // num_subsets
    remainder = num_records % num_subsets

    subset_sizes = [records_per_subset] * num_subsets

    # Distribute any remaining records evenly among subsets
    for i in range(remainder):
        subset_sizes[i] += 1

    base_name, ext = os.path.splitext(input_file)

    # Create and write the subsets
    start = 0
    for subset_num, subset_size in enumerate(subset_sizes):
        end = start + subset_size
        subset_records = records[start:end]
        output_file = f"{base_name}_subset_{subset_num + 1}{ext}"
        SeqIO.write(subset_records, output_file, "fasta")
        start = end

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split a FASTA file into subsets.")
    parser.add_argument("input_file", help="Input FASTA file to be split.")
    parser.add_argument("num_subsets", type=int, help="Number of subsets to create.")
    args = parser.parse_args()

    split_fasta(args.input_file, args.num_subsets)
