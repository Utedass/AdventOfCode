import os, argparse

def get_marker_index(line, window_length):
    marker_window = []
    for i in range(len(line)):
        c = line[i]
        marker_window.append(c)
        if len(marker_window)>=window_length:
            if only_uniques(marker_window):
                return i+1
            del marker_window[0]

def only_uniques(list):
    return len(list) == len(set(list))

def solve_task(lines):
    for line in lines:
        print(f"First task: {get_marker_index(line, 4)}")
        print(f"Second task: {get_marker_index(line, 14)}")

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