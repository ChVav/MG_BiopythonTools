import argparse

def main():
    parser = argparse.ArgumentParser(description="Find items in a long list that are not in a subset.")
    parser.add_argument("--long-list", nargs="+", type=int, required=True, help="The long list of items.")
    parser.add_argument("--subset", nargs="+", type=int, required=True, help="The subset of items.")

    args = parser.parse_args()
    
    subset_set = set(args.subset)
    not_in_subset = [item for item in args.long_list if item not in subset_set]
    
    print(not_in_subset)

if __name__ == "__main__":
    main()
