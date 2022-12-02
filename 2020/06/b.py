import os, argparse


def solve_task(filename):
    with open(filename) as infile:
        total = 0
        thisGroup = {}
        groupSize = 0
        for raw_line in infile:
            line = raw_line.rstrip()
            if line == "":
                groupWeight = [x for x in thisGroup.values()].count(groupSize)
                #print(groupWeight)
                total += groupWeight
                thisGroup = {}
                groupSize = 0
                
                continue
            groupSize += 1
            thisGuy = {}
            for c in line:
                if c in thisGroup:
                    thisGroup[c] += 1
                else:
                    thisGroup[c] = 1
        groupWeight = [x for x in thisGroup.values()].count(groupSize)
        #print(groupWeight)
        total += groupWeight
        print(f"Total: {total}")
            
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