Various python scripts to deal with fasta-files and a like.

* lenfilter_fasta.py : filter a (multi-)fasta file based sequence length. 
* extract_sequences.py: subset a multi-fasta or genbank file given a list of ids.
* subset_notin_list.py: get items from longer list not in specified subset, e.g. use to get ids from unbinnned contigs (not BioPython)
* split_fasta.py: split multi-fasta into smaller number of subset files.
* translateKraken2.py: get full taxonomic lineage for NCBI tax IDs in Kraken2 standard output (need taxonkit.sif; script modified from https://raw.githubusercontent.com/microbialman/MetaSequencing/master/workflow/scripts/translateKraken2.py)