import os, argparse


def solve_task(filename):
    with open(filename) as infile:
        all_elves = []
        current_elf = 0
        highest = 0
        for raw_line in infile:
            line = raw_line.rstrip()
            if line != "":
                current_elf += int(line)
            else:
                all_elves.append(current_elf)
                highest = max(current_elf, highest)
                current_elf = 0
        
        print(f"Highest ammount {highest}")
            
    os.system("pause")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Script that solves the case",epilog="Have a nice day!")
    parser.add_argument('filename', nargs='?', default="example.txt", help='Input file')
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()
    solve_task(args.filename)

if __name__ == "__main__":
    main()