import re
import argparse
import os

def preprocess_gbk(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        inside_feature = False
        previous_line = ''
        
        for line in infile:
            if line.startswith('FEATURES'):
                inside_feature = True
            elif line.startswith('ORIGIN'):
                inside_feature = False

            if inside_feature:
                if previous_line.strip().startswith('/tmh-'):
                    if line.lstrip().startswith(('/tmh-', '/translation', '/gene', '/product')):
                        # Write the previous line if the next line starts with another feature
                        outfile.write(previous_line)
                    else:
                        # Merge broken line related to /tmh- without adding an extra hyphen
                        line = previous_line.rstrip() + ' ' + line.lstrip()
                    previous_line = ''
                elif line.strip().startswith('/tmh-'):
                    previous_line = line
                    continue

            if previous_line:
                outfile.write(previous_line)
                previous_line = ''

            outfile.write(line)

        # Write any remaining buffered line
        if previous_line:
            outfile.write(previous_line)

def main():
    parser = argparse.ArgumentParser(description="Preprocess a GenBank file by fixing '/tmh' and '/tmh-' lines.")
    parser.add_argument('input_file', help="The input GenBank file to be processed.")
    args = parser.parse_args()

    # Automatically create the output file name
    input_filename = os.path.basename(args.input_file)
    output_filename = f"fixed_{input_filename}"
    
    # Run the preprocessing function
    preprocess_gbk(args.input_file, output_filename)

if __name__ == "__main__":
    main()
