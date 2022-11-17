import os, argparse


def solve_task(filename):
    with open(filename) as infile:
        for raw_line in infile:
            line = raw_line.rstrip()
            inputs = [int(x) for x in line.split(',')]
            bins = {x:0 for x in range(9)}
            for i in inputs:
                bins[i] += 1
            
            print(bins)
            for day in range(80):
                next_bin = {x:0 for x in range(9)}
                for key,val in bins.items():
                    if key == 0:
                        next_bin[6] += val
                        next_bin[8] = val
                    else:
                        next_bin[key-1] += val
                bins = next_bin
            
            number_of_fish = 0
            for k,fish in bins.items():
                number_of_fish += fish

            print(number_of_fish)
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