import os, argparse, re

def solve_task(lines):
    overlaps = 0
    for line in lines:
        m = re.match("(\d+)-(\d+),(\d+)-(\d+)", line)
        first = (int(m.group(1)), int(m.group(2)))
        second = (int(m.group(3)), int(m.group(4)))
        if ((first[0] >= second[0] and first[1] <= second[1]) or
        (first[0] <= second[0] and first[1] >= second[1])):
            overlaps += 1
    print(f"Number of overlaps: {overlaps}")

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