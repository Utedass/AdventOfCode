import os, argparse, math
import numpy as np


def solve_task(filename):
    data = np.genfromtxt(filename, delimiter=',', dtype='int')

    sorted_data = np.sort(data)
    
    rms = np.sqrt(np.mean(data**2))
    mean = np.mean(data)
    
    print("The rms is: " + str(rms))
    print("The mean is: " + str(mean))
    
    bins = {}

    for k in sorted_data:
        if k not in bins:
            bins[k] = 1
        else:
            bins[k] += 1

    #target = np.floor(rms)
    target = np.floor(mean)
    
    print("Target: " + str(target))
    
    fuel = 0
    for k, v in bins.items():
        distance = abs(k-target)
        consumption = ((distance*distance+distance)/2)
        #print("Movement from " + str(k) + " consumes " + str(consumption) + " for a total of " + str(consumption*v))
        fuel += consumption*v
        
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