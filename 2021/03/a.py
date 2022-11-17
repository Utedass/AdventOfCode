import os, argparse


def solve_task(filename):
    binary_extraction_array = []
    
    with open(filename) as infile:
        for raw_line in infile:
            line = raw_line.rstrip()
            if len(binary_extraction_array) != len(line):
                #prepare binary_extraction_array
                for i in range(len(line)):
                    binary_extraction_array.append({'0':0, '1':0})
            
            for i in range(len(binary_extraction_array)):
                if line[i] == '0':
                    binary_extraction_array[i]['0'] += 1
                else:
                    binary_extraction_array[i]['1'] += 1

    gamma_rate_array = []
    epsilon_rate_array = []
    
    for g in binary_extraction_array:
        if g['0'] > g['1']:
            gamma_rate_array.append('1')
            epsilon_rate_array.append('0')
        else:
            gamma_rate_array.append('0')
            epsilon_rate_array.append('1')
            
            
    gamma_rate_str = ''.join(gamma_rate_array)
    epsilon_rate_str = ''.join(epsilon_rate_array)
    
    gamma_rate = int(gamma_rate_str, 2)
    epsilon_rate = int(epsilon_rate_str, 2)
    
    print("Gamma: " + str(gamma_rate))
    print("Epsilon: " + str(epsilon_rate))
    print("Power consumption: " + str(gamma_rate*epsilon_rate))
    
    os.system("pause")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Script that solves the case",epilog="Have a nice day!")
    parser.add_argument('filename', nargs='?', default="infile.txt", help='Input file')
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()
    solve_task(args.filename)

if __name__ == "__main__":
    main()