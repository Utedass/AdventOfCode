import os, argparse

def solve_task(lines):
    duplicate_objects = []
    priority_sum = 0
    for line in lines:
        half_index = len(line)//2
        dupes_in_this_pack = {}
        for i in line[:half_index]:
            if i in line[half_index:] and i not in dupes_in_this_pack:
                print(f"{i} is in {line[half_index:]}, first half {line[:half_index]}")
                priority_sum += get_priority(i)
                dupes_in_this_pack[i] = True
    print(duplicate_objects)
    print(priority_sum)

def get_priority(item):
    item_code = ord(item)
    if item >= 'a' and item <= 'z':
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