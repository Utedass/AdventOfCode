import os, argparse, re


def solve_task(filename):
    horizontal_position = 0
    depth = 0
    
    match_string = r"(?P<command>[a-z]*) (?P<distance>\d*)"
    matcher = re.compile(match_string)
    
    with open(filename) as infile:
        for raw_line in infile:
            line = raw_line.rstrip()
            m = matcher.match(line)
            command = m.group('command')
            distance = int(m.group('distance'))
            
            match command:
                case 'forward':
                    horizontal_position += distance
                case 'up':
                    depth -= distance
                case 'down':
                    depth += distance
    
    print("Current depth: " + str(depth))
    print("Current horizontal_position: " + str(horizontal_position))
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