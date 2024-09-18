import os
import sys
from Bio import SeqIO
import argparse

def parse_gbk_cds2fna(input_gbk, output_fasta):
    """Convert GenBank (.gbk) file to multifasta (.fna) file with nucleotide sequences.
    
    Args:
        input_gbk (str): Path to the input GenBank (.gbk) file.
        output_fasta (str): Path to the output FASTA (.fna) file.
    """
    # Open output file for writing
    with open(output_fasta, "w") as fasta_out:
        # Parse the GenBank file
        for record in SeqIO.parse(input_gbk, "genbank"):
            # Loop through each feature in the GenBank file
            for feature in record.features:
                # Check if the feature is a CDS and contains a locus_tag
                if feature.type == "CDS" and "locus_tag" in feature.qualifiers:
                    # Extract locus_tag and nucleotide sequence
                    locus_tag = feature.qualifiers["locus_tag"][0]
                    sequence = feature.location.extract(record).seq
                    # Write to the output file in FASTA format
                    fasta_out.write(f">{locus_tag}\n{sequence}\n")

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(
        description="Convert a GenBank (.gbk) file to a FASTA (.fna) file with CDS sequences."
    )
    # Positional argument for input GenBank file
    parser.add_argument("input_gbk", help="Path to the input GenBank (.gbk) file")
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Generate output file name by replacing the extension
    input_gbk = args.input_gbk
    output_fasta = os.path.splitext(input_gbk)[0] + "_cds.fna"
    
    # Check if the input file exists
    if not os.path.isfile(input_gbk):
        print(f"Error: File '{input_gbk}' not found.")
        sys.exit(1)
    
    # Call the function to convert GenBank to FASTA
    parse_gbk_cds2fna(input_gbk, output_fasta)
    
    print(f"Conversion complete. Output written to: {output_fasta}")

if __name__ == "__main__":
    main()
