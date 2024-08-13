import os
import pandas as pd
from Bio import SeqIO

# Directory containing .gbk files
gbk_dir = "test_contigs_gbk"

# Initialize an empty list to collect data for the DataFrame
data = []

# Iterate over all .gbk files in the directory
for gbk_file in os.listdir(gbk_dir):
    if gbk_file.endswith(".gbk"):
        file_path = os.path.join(gbk_dir, gbk_file)

        # Extract the contig name from the filename (without extension)
        contig_name = os.path.splitext(gbk_file)[0]

        # Parse the .gbk file
        for record in SeqIO.parse(file_path, "genbank"):
            for feature in record.features:
                if feature.type == "CDS":
                    # Extract locus_tag, type, start, end, and annotation (product)
                    locus_tag = feature.qualifiers.get("locus_tag", [""])[0]
                    feature_type = feature.type
                    start = int(feature.location.start)
                    end = int(feature.location.end)
                    if feature.location.strand == -1:
                        start, end = end, start
                    annot = feature.qualifiers.get("product", [""])[0]

                    # Append the extracted data to the list
                    data.append([contig_name, locus_tag, feature_type, start, end, annot])

# Create a DataFrame from the collected data
df = pd.DataFrame(data, columns=["seq_id", "feat_id", "type", "start", "end", "annot"])

# Save the DataFrame as a CSV file
df.to_csv("parsed_gbk_data.csv", index=False)

print("Data parsing complete and saved as 'parsed_gbk_data.csv'.")
