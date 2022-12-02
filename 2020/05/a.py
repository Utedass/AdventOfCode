import os, argparse

mapping = {'F': '0', 'B': '1', 'R': '1', 'L': '0'}

def solve_task(filename):
    highest = 0
    occupiedSeats = []
    with open(filename) as infile:
        for raw_line in infile:
            line = raw_line.rstrip()
            rowRaw = line[0:7]
            colRaw = line[7:10]
            row = int(''.join([mapping[x] for x in rowRaw]),2)
            col = int(''.join([mapping[x] for x in colRaw]),2)
            id = row*8+col
            #print(f"Row: {row}, col: {col}, id: {id}")
            highest = max(highest, id)
            occupiedSeats.append(id)
    print(f"Highest: {highest}")
    occupiedSeats.sort()
    #print(occupiedSeats)
    for i in range(len(occupiedSeats)):
        k = occupiedSeats[i+1]
        if occupiedSeats[i]+1 != k:
            print(f"Sit the fuck down!: {occupiedSeats[i]+1}")
            break

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