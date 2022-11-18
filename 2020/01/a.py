import os, argparse


def solve_task(filename):
    numbers = [] 
    with open(filename) as infile:
        for raw_line in infile:
            line = raw_line.rstrip()
            numbers.append(int(line))
    
    numbers.sort()

    target = 2020
    
    for a in range(len(numbers)):
        for b in range(a+1, len(numbers)):
            x = numbers[a]
            y = numbers[b]

            if(x+y == target):
                print(f"X: {x}, Y: {y}")
                print(f"Answer: {x*y}")

    #os.system("pause")

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