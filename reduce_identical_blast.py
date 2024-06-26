import argparse
from Bio import SeqIO

# Function to read in fasta and keep a set of fasta headers from duplicated sequences
# blast results already filtered for 100% identity, with self-blasts and duplicate pairs
def read_fasta_and_blast(fasta_file, blast_results):
    headers = []
    sequences = []
    identical_seqs = set() # data structure with duplicated values automatically removed
    with open(fasta_file, 'r') as file:
        for record in SeqIO.parse(file, 'fasta'):
            headers.append(record.id)
            sequences.append(str(record.seq))
    with open(blast_results, 'r') as file:
        for line in file:
            fields = line.strip().split('\t')
            identical_seqs.update(fields[:2])  # Use update instead of add to add multiple elements
    return headers, sequences, identical_seqs

# Function to create reduced set of sequences and mapping
def create_reduced_set_and_mapping(headers, sequences, identical_seqs, blast_results):
    reduced_headers = []
    reduced_sequences = []
    mapping = {}
    counter = 1
    identical_mapping = {}

    # Create a mapping for identical sequences
    for line in open(blast_results, 'r'):
        fields = line.strip().split('\t')
        if fields[0] in identical_seqs and fields[1] in identical_seqs:
            if fields[0] not in identical_mapping and fields[1] not in identical_mapping:
                identical_mapping[fields[0]] = f'ESV_SSU_{counter}'
                identical_mapping[fields[1]] = f'ESV_SSU_{counter}'
                counter += 1
            elif fields[0] in identical_mapping and fields[1] not in identical_mapping:
                identical_mapping[fields[1]] = identical_mapping.get(fields[0])
            elif fields[1] in identical_mapping and fields[0] not in identical_mapping:
                identical_mapping[fields[0]] = identical_mapping.get(fields[1])

    ## Print the contents of identical_mapping for debugging
    #print("Identical Mapping:")
    #print({k: identical_mapping[k] for k in list(identical_mapping)[:5]})

    # Iterate through headers and sequences
    for header, sequence in zip(headers, sequences):
        if header not in identical_seqs:
            reduced_headers.append(f'ESV_SSU_{counter}')
            reduced_sequences.append(sequence)
            mapping[header] = f'ESV_SSU_{counter}'
            counter += 1
        elif header in identical_seqs and identical_mapping.get(header) not in reduced_headers:
                mapping[header] = identical_mapping.get(header)
                reduced_headers.append(identical_mapping.get(header))
                reduced_sequences.append(sequence)
        elif header in identical_seqs and identical_mapping.get(header) in reduced_headers:
                mapping[header] = identical_mapping.get(header)

    return reduced_headers, reduced_sequences, mapping

# Function to write reduced set of sequences and mapping to files
def write_output(reduced_headers, reduced_sequences, mapping, reduced_fasta, mapping_file):
    with open(reduced_fasta, 'w') as file:
        for header, sequence in zip(reduced_headers, reduced_sequences):
            file.write(f'>{header}\n{sequence}\n')
    with open(mapping_file, 'w') as file:
        for original_header, reduced_header in mapping.items():
            file.write(f'{original_header}\t{reduced_header}\n')

def main():
    parser = argparse.ArgumentParser(description="Process fasta file and its blast results to create a reduced set of sequences.")
    parser.add_argument("fasta_file", help="Path to the input fasta file")
    parser.add_argument("blast_results", help="Path to the blast results file")
    parser.add_argument("reduced_fasta", help="Path to save the reduced fasta file")
    parser.add_argument("mapping_file", help="Path to save the mapping file")
    args = parser.parse_args()

    headers, sequences, identical_seqs = read_fasta_and_blast(args.fasta_file, args.blast_results)
    reduced_headers, reduced_sequences, mapping = create_reduced_set_and_mapping(headers, sequences, identical_seqs, args.blast_results)
    write_output(reduced_headers, reduced_sequences, mapping, args.reduced_fasta, args.mapping_file)

    ## Print for troubleshooting
    #print(list(identical_seqs)[:5]) 
    
if __name__ == "__main__":
    main()
