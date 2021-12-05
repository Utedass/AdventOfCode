import os, argparse
import numpy as np

class bingo_brick:
    brick = None
    marks = None

    def __init__(self):
        self.marks = np.ones((5,5))
        self.brick = np.ndarray((0))

    def append_row(self, row):
        if self.brick.size == 0:
            self.brick = np.array(row)
        else:
            self.brick = np.vstack((self.brick, row))
    
    def mark(self, mark):
        #self.marks[ där self.brick == mark ] = 0
        self.marks = np.where(self.brick == mark, 0, self.mark)
        pass
    
    def bingo(self):
        return False

    def __str__(self):
        result = ''
        if self.brick.size > 0:
            result = str(self.brick) + '\n'
            result += str(self.mark)
        else:
            result = "Empty brick"
        return result

def solve_task(filename):
    marks = []
    bingo_bricks = []

    with open(filename) as infile:
        
        # Read first line of mark announcements
        marks_str = infile.readline().rstrip().split(',')
        marks = [int(k) for k in marks_str]
        
        # Read the bingo bricks line by line
        for raw_line in infile:
            line = raw_line.rstrip()
            
            if len(line) == 0: # Empty row separates bingo bricks
                bingo_bricks.append(bingo_brick())
            else:
                bingo_line_str = line.split()
                bingo_line = [int(k) for k in bingo_line_str]
                bingo_bricks[-1].append_row(bingo_line)

    # Time to play some bingo!
    
    # Iterate the mark announcements
    winning_brick = None
    for mark in marks:
        for brick in bingo_bricks:
            brick.mark(mark)
            if brick.bingo():
                break

        if winning_brick:
            break
    
    if winning_brick:
        print(winning_brick)
    
    for brick in bingo_bricks:
        print(brick)
        
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