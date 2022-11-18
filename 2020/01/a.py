import os, argparse


def solve_task(filename):
    numbers = [] 
    with open(filename) as infile:
        for raw_line in infile:
            line = raw_line.rstrip()
            numbers.append(int(line))
    
    numbers.sort()

    target = 2020
    biggerIndex = len(numbers)-1
    smallerIndex = 0
    solved = False
    
    while not solved:
        smaller = numbers[smallerIndex]
        bigger = numbers[biggerIndex]
        #print("Smaller: " + str(smaller) + ", Bigger: " + str(bigger))
        if((smaller+bigger) == target):
            soved = True
            print("Answer: " + str(smaller*bigger))
            break
        if(bigger < target/2):
            print("No solusion found")
            break

        if(bigger + numbers[smallerIndex+1] > target):
            #print("Decreasing bigger")
            biggerIndex -= 1
            #smallerIndex = 0
            if(biggerIndex < 0):
                print("No solusion found")
                break
        else:
            #print("Increasing smaller")
            smallerIndex += 1
            if (smallerIndex >= len(numbers)):
                print("No solusion found")
                break

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