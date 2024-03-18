from Bio import SeqIO
import argparse

def main():
    parser = argparse.ArgumentParser(description='Filter sequences based on length.')
    parser.add_argument('input_file', help='input FASTA file')
    parser.add_argument('output_file', help='output FASTA file')
    parser.add_argument('min_len', type=int, help='minimum sequence length')
    args = parser.parse_args()

    input_handle = open(args.input_file, 'r')
    output_handle = open(args.output_file, 'w')
    output_seqs = []

    for record in SeqIO.parse(input_handle, 'fasta'):
        if len(record.seq) >= args.min_len:
            output_seqs.append(record)

    SeqIO.write(output_seqs, output_handle, 'fasta')

    input_handle.close()
    output_handle.close()

    print(f'Kept {len(output_seqs)} sequences')
    print(f'Sequences written to output file {args.output_file}')

if __name__ == '__main__':
    main()