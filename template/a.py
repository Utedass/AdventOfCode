import os, argparse

def solve_task(lines):
    for line in lines:
        pass

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