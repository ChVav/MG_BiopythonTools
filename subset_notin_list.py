import argparse

def main():
    parser = argparse.ArgumentParser(description="Find items in a long list that are not in a subset.")
    parser.add_argument("--long-list-file", type=str, required=True, help="Input file containing the long list items, one item per line.")
    parser.add_argument("--subset-file", type=str, required=True, help="Input file containing the subset items, one item per line.")
    parser.add_argument("--output-file", type=str, required=True, help="Output file to store the result.")

    args = parser.parse_args()
    
    with open(args.long_list_file, "r") as long_list_file:
        long_list = [line.strip() for line in long_list_file]

    with open(args.subset_file, "r") as subset_file:
        subset = [line.strip() for line in subset_file]
    
    subset_set = set(subset)
    not_in_subset = [item for item in long_list if item not in subset_set]
    
    with open(args.output_file, "w") as output_file:
        for item in not_in_subset:
            output_file.write(item + "\n")

if __name__ == "__main__":
    main()