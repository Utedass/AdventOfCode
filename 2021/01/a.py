import os, argparse


def solve_task(filename):
    with open(filename) as infile:
        last_depth = None
        decrements = 0
        for line in infile:
            depth = int(line)
            if last_depth:
                if depth > last_depth:
                    decrements += 1
            last_depth = depth
                
        print(decrements)
    os.system("pause")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Script that toggles output of a Tenma PSU",epilog="Have a nice day!")
    parser.add_argument('filename', nargs='?', default="infile.txt", help='Input file')
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()
    solve_task(args.filename)

if __name__ == "__main__":
    main()