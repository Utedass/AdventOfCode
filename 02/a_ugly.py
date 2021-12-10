import os, argparse, re


def solve_task(filename):
    horizontal_position = 0
    depth = 0
        
    with open(filename) as infile:
        for line in infile:
            distance = int(re.search(r"(?P<command>[a-z]*) (?P<distance>\d*)", line).group('distance'))
            horizontal_position += distance if 'forward' in line else 0
            depth += distance if 'down' in line else -distance if 'up' in line else 0
    
    print("Product: " + str(depth * horizontal_position))
    os.system("pause")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Solves a part of advent of code.",epilog="Have a nice day!")
    parser.add_argument('filename', nargs='?', default="infile.txt", help='Input file')
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()
    solve_task(args.filename)

if __name__ == "__main__":
    main()