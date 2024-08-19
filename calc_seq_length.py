from Bio import SeqIO
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description='Output the length of each sequence in a multi-FASTA file.')
    parser.add_argument('input_file', help='input FASTA file (.fna, .fasta, etc.)')
    args = parser.parse_args()

    # Ensure the file has a valid extension
    valid_extensions = ['.fna', '.fasta']
    if not any(args.input_file.endswith(ext) for ext in valid_extensions):
        raise ValueError(f"Input file must have one of the following extensions: {', '.join(valid_extensions)}")
    
    input_handle = open(args.input_file, 'r')

    # Parse the sequences and print their lengths
    for record in SeqIO.parse(input_handle, 'fasta'):
        print(f'{record.id}\t{len(record.seq)}')

    input_handle.close()

if __name__ == '__main__':
    main()