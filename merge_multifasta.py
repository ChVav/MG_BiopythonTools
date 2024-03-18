import os
import argparse
from Bio import SeqIO

def main(input_dir, output_file):
    # Check if the input directory exists
    if not os.path.isdir(input_dir):
        print(f"Error: Directory '{input_dir}' not found.")
        return

    # Initialize a list to store sequences
    combined_sequences = []

    # Loop through all files in the input directory
    for file_name in os.listdir(input_dir):
        # Check if the file is a fasta file
        if file_name.endswith(('.fa','.fna', '.faa', '.fasta')):
            file_path = os.path.join(input_dir, file_name)
            # Read sequences from the fasta file and add them to the list
            with open(file_path, 'r') as fasta_file:
                for record in SeqIO.parse(fasta_file, 'fasta'):
                    combined_sequences.append(record)

    # Write the combined sequences to the output file
    with open(output_file, 'w') as output_handle:
        SeqIO.write(combined_sequences, output_handle, 'fasta')

    print(f"Combined fasta sequences written to '{output_file}'.")

def parse_arguments():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Combine multiple multi-fasta files into one fasta file.")
    parser.add_argument("input_directory", help="Directory containing multi-fasta files (.fa, .fna, .faa, .fasta)")
    parser.add_argument("output_file", help="Output fasta file name")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    main(args.input_directory, args.output_file)


#python merge_multifasta.py /path/to/fasta_files/ combined.fasta
