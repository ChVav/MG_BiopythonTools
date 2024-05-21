import argparse
import sys
from Bio import SearchIO

def get_significant_hits(hmmsearch_output, evalue_threshold):
    # Parse the hmmsearch output file
    query_results = SearchIO.parse(hmmsearch_output, 'hmmer3-text')

    significant_hits = []

    for query_result in query_results:
        for hit in query_result:
            # Filter hits based on E-value
            if hit.evalue < evalue_threshold:
                significant_hits.append(hit)

    return significant_hits

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Parse hmmsearch output and get significant sequence hits.")
    parser.add_argument('hmmsearch_output', type=argparse.FileType('r'), help="Path to the hmmsearch output file")
    parser.add_argument('output_file', type=argparse.FileType('w'), help="Path to the output file to write significant hit IDs")
    parser.add_argument('--evalue_threshold', type=float, default=0.01, help="E-value threshold for significant hits (default: 0.01)")

    # Parse arguments
    args = parser.parse_args()

    # Get significant hits
    significant_hits = get_significant_hits(args.hmmsearch_output, args.evalue_threshold)

    # Write the significant hit IDs to the output file
    with args.output_file as outfile:
        for hit in significant_hits:
            outfile.write(f'{hit.id}\n')

if __name__ == "__main__":
    main()
