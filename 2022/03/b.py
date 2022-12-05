import os, argparse

def solve_task(backpacks):
    group_size = 3
    sum_of_priorities = 0

    # Run once per group
    for group_number in range(len(backpacks)//group_size):
        group_backpacks = backpacks[group_number * group_size : (group_number + 1)*group_size]
        # Special treatment for the first backpack
        items_sieve = get_unique_items(group_backpacks[0])

        # For the remaining packs..
        for backpack in group_backpacks[1:]:
            for item in list(items_sieve.keys()):
                if item not in backpack:
                    items_sieve.pop(item)
        
        # Simple error check
        if len(items_sieve) != 1:
            print("This is so wrong!")
            quit()
        
        # Add the sole remaining item to the results
        sum_of_priorities += get_priority(next(iter(items_sieve)))

    print(sum_of_priorities)

def get_unique_items(line):
    uniques = {}
    for c in line:
        uniques[c] = 1
    #return [k for k in uniques.keys()]
    return uniques

def get_priority(item):
    item_code = ord(item)
    if item >= 'a':
        return item_code - ord('a') + 1
    else:
        return item_code - ord('A') + 27

def read_lines(filename):
    lines = []
    with open(filename) as infile:
        for raw_line in infile:
            line = raw_line.rstrip()
            lines.append(line)
    return lines

def parse_arguments():
    parser = argparse.ArgumentParser(description="Script that solves the case",epilog="Have a nice day!")
    parser.add_argument('filename', nargs='?', default="example.txt", help='Input file')
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()
    lines = read_lines(args.filename)
    solve_task(lines)

if __name__ == "__main__":
    main()