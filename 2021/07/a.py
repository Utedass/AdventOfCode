import os, argparse, math
import numpy as np


def solve_task(filename):
    data = np.genfromtxt(filename, delimiter=',', dtype='int')

    sorted_data = np.sort(data)
    
    median = None
    if len(sorted_data) % 2:
        median = sorted_data[len(sorted_data)//2]
    else:
        median = (sorted_data[len(sorted_data)//2] + sorted_data[len(sorted_data)//2+1])/2

    median = np.median(data)

    print("The median is: " + str(median))
    
    bins = {}

    for k in sorted_data:
        if k not in bins:
            bins[k] = 1
        else:
            bins[k] += 1

    fuel = 0
    for k, v in bins.items():
        fuel += abs(k-median)*v
        
    print("Fuel: " + str(fuel))

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