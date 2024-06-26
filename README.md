Various python scripts to deal with fasta-files and a like.

* lenfilter_fasta.py : filter a (multi-)fasta file based sequence length. 
* extract_sequences.py : subset a multi-fasta or genbank file given a list of ids. Spaces may be present in fasta header, but then the list of ids should match everything before.
* subset_notin_list.py : get items from longer list not in specified subset, e.g. use to get ids from unbinnned contigs (not BioPython)
* split_fasta.py : split multi-fasta into smaller number of subset files.
* translateKraken2.py : get full taxonomic lineage for NCBI tax IDs in Kraken2 standard output (need taxonkit.sif; script modified from https://raw.githubusercontent.com/microbialman/MetaSequencing/master/workflow/scripts/translateKraken2.py)
* merge_multifasta.py : combine several multi-fasta into one file.
* reduce_identical_blast.py : given a blast_result with 100% identity hits kept and self-blasts removed, create a reduced set of unique sequences and map old Ids
* blast_16S_besthit_api.py : blastn and get taxonomy for besthit. uses API to connect to NCBI, works for only handful seqs at a time.
* get_hits_hmmer3.py: given hmmsearch (hmmer3) output, filter Sequence ids for selected e-value threshold
