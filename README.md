Various python scripts to deal with fasta-files and a like.

Sure! Here are the Python scripts listed in alphabetical order:

- **blast_16S_besthit_api.py**: blastn and get taxonomy for besthit. uses API to connect to NCBI, works for only handful seqs at a time.
- **calc_seq_lengthy.py**: given a multi-fasta file (.fna or .fasta), calculate sequence length for each DNA molecule.
- **extract_sequences.py**: subset a multi-fasta or genbank file given a list of ids. Spaces may be present in fasta header, but then the list of ids should match everything before.
- **get_hits_hmmer3.py**: given hmmsearch (hmmer3) output, filter Sequence ids for selected e-value threshold.
- **lenfilter_fasta.py**: filter a (multi-)fasta file based on sequence length.
- **merge_multifasta.py**: combine several multi-fasta into one file.
- **parse_gbk_cds2fna.py**: given a gbk file, extract the nucleotide sequences for all CDS into a fasta file using /locus_tag as headers.
- **parse_gbk_df.py**: given a folder with .gbk files, create a tidy df (.csv) with sequences and annotated features.
- **reduce_identical_blast.py**: given a blast_result with 100% identity hits kept and self-blasts removed, create a reduced set of unique sequences and map old Ids.
- **replace_fasta_headers.py**: given a multi-fasta file and a map of old and new ids, rename the fasta headers.
- **split_fasta.py**: split multi-fasta into smaller number of subset files.
- **subset_notin_list.py**: get items from longer list not in specified subset, e.g., use to get ids from unbinned contigs (not BioPython).
- **translateKraken2.py**: get full taxonomic lineage for NCBI tax IDs in Kraken2 standard output (need taxonkit.sif; script modified from https://raw.githubusercontent.com/microbialman/MetaSequencing/master/workflow/scripts/translateKraken2.py).