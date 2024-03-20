import argparse
import re
import pandas as pd
from Bio.Blast import NCBIWWW
from Bio import Entrez

# Function to retrieve taxonomy information using Entrez
def get_taxonomy(hit_id):
    try:
        handle = Entrez.efetch(db="nucleotide", id=hit_id, retmode="xml")
        record = Entrez.read(handle)
        taxonomy = record[0]["GBSeq_taxonomy"]
        return taxonomy
    except Exception as e:
        print(f"Error retrieving taxonomy for {hit_id}: {e}")
        return None

# Function to perform BLAST search and parse results
def perform_blast(fasta_file, output_file, output_file2):
    Entrez.email = "myemail@gmail.com"

    # Perform a BLAST search against NCBI nt database 
    result_handle = NCBIWWW.qblast("blastn", "nr", open(fasta_file).read(), format_type="Text", megablast=True)

    # Save the BLAST results to the output file
    with open(output_file, "w") as output:
        output.write(result_handle.read())

    print(f"Results saved to {output_file}")

    # Parse BLAST results
    results = {"Query": [], "Hit_Title": [], "Taxonomy": [], "Identity": [], "Gaps": []}
    current_query = ""
    hit_count = 0

    # Regular expression patterns to extract % identity and query coverage
    identity_pattern = re.compile(r'Identities = (\d+)/\d+ \((\d+)%\),')
    coverage_pattern = re.compile(r'Gaps = (\d+)/\d+ \((\d+)%\)')

    # Open the BLAST results file for reading
    with open(output_file, "r") as file:
        lines = file.readlines()
        i = 0

        while i < len(lines):
            line = lines[i]
            if line.startswith("Query="):
                current_query = line.split("Query=")[1].strip()
                hit_count = 0
            elif line.startswith(">") and hit_count == 0:
                hit_title = line[1:].strip()
                results["Query"].append(current_query)
                results["Hit_Title"].append(hit_title)

                # Search for % identity and query coverage in the subsequent lines
import argparse
import re
import pandas as pd
from Bio.Blast import NCBIWWW
from Bio import Entrez

# Function to retrieve taxonomy information using Entrez
def get_taxonomy(hit_id):
    try:
        handle = Entrez.efetch(db="nucleotide", id=hit_id, retmode="xml")
        record = Entrez.read(handle)
        taxonomy = record[0]["GBSeq_taxonomy"]
        return taxonomy
    except Exception as e:
        print(f"Error retrieving taxonomy for {hit_id}: {e}")
        return None

# Function to perform BLAST search and parse results
def perform_blast(fasta_file, output_file, output_file2, email):
    Entrez.email = email

    # Perform a BLAST search against NCBI nt database 
    result_handle = NCBIWWW.qblast("blastn", "nr", open(fasta_file).read(), format_type="Text", megablast=True)

    # Save the BLAST results to the output file
    with open(output_file, "w") as output:
        output.write(result_handle.read())

    print(f"Results saved to {output_file}")

    # Parse BLAST results
    results = {"Query": [], "Hit_Title": [], "Taxonomy": [], "Identity": [], "Gaps": []}
    current_query = ""
    hit_count = 0

    # Regular expression patterns to extract % identity and query coverage
    identity_pattern = re.compile(r'Identities = (\d+)/\d+ \((\d+)%\),')
    coverage_pattern = re.compile(r'Gaps = (\d+)/\d+ \((\d+)%\)')

    # Open the BLAST results file for reading
    with open(output_file, "r") as file:
        lines = file.readlines()
        i = 0

        while i < len(lines):
            line = lines[i]
            if line.startswith("Query="):
                current_query = line.split("Query=")[1].strip()
                hit_count = 0
            elif line.startswith(">") and hit_count == 0:
                hit_title = line[1:].strip()
                results["Query"].append(current_query)
                results["Hit_Title"].append(hit_title)

                # Search for % identity and query coverage in the subsequent lines
                j = i + 1
                while j < len(lines):
                    identity_match = identity_pattern.search(lines[j])
                    coverage_match = coverage_pattern.search(lines[j])
                    if identity_match and coverage_match:
                        identity = int(identity_match.group(2))
                        coverage = int(coverage_match.group(2))
                        results["Identity"].append(identity)
                        results["Gaps"].append(coverage)
                        break
                    j += 1

                # Find the lines with taxonomy information (customize this part)
                taxonomy = ""  # You need to extract taxonomy from the file
                results["Taxonomy"].append(taxonomy)

                hit_count += 1

            i += 1

    # Create a DataFrame from the results
    df = pd.DataFrame(results)

    ## Append taxonomy, connecting with the API again
    # Extract Hit IDs from the Hit_Title column and use Entrez to retrieve taxonomy for Hit ID
    df["Hit_ID"] = df["Hit_Title"].str.split(" ").str[0]
    df["Taxonomy"] = df["Hit_ID"].apply(get_taxonomy)

    # Save the DataFrame to a CSV file
    df.to_csv(output_file2, index=False)
    print(f"Results with taxonomy saved to {output_file2}")

def main():
    parser = argparse.ArgumentParser(description="Perform BLAST search and parse results.")
    parser.add_argument("fasta_file", help="Path to the input FASTA file")
    parser.add_argument("output_file", help="Path to save the BLAST results")
    parser.add_argument("output_file2", help="Path to save the parsed BLAST results with taxonomy")
    parser.add_argument("--email", required=True, help="Your email address for NCBI")
    args = parser.parse_args()

    perform_blast(args.fasta_file, args.output_file, args.output_file2, args.email)

if __name__ == "__main__":
    main()
