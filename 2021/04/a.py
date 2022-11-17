import os, argparse
import numpy as np

class bingo_brick:
    brick = None
    marks = None

    def __init__(self):
        self.marks = np.ones((5,5), dtype=bool)
        self.brick = np.ndarray((0))

    def append_row(self, row):
        if self.brick.size == 0:
            self.brick = np.array(row)
        else:
            self.brick = np.vstack((self.brick, row))
    
    def mark(self, mark):
        #self.marks[ där self.brick == mark ] = 0
        self.marks[self.brick == mark] = False
    
    def bingo(self):
        vert = self.marks.sum(axis = 0) == 0
        if vert.any():
            return True
        
        hor = self.marks.sum(axis = 1) == 0
        if hor.any():
            return True
            
        return False

    def score(self):
        remainder = self.brick[self.marks]
        score = remainder.sum()
        return score

    def __str__(self):
        result = ''
        if self.brick.size > 0:
            result = str(self.brick) + '\n'
            result += str(self.marks)
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
    winning_mark = None
    for mark in marks:
        print("Draws number: " + str(mark))
        for brick in bingo_bricks:
            brick.mark(mark)
            if brick.bingo():
                winning_brick = brick
                winning_mark = mark
                break
                

        if winning_brick:
            break

    if winning_brick:
        print(winning_brick)
        
    print("Brick score: " + str(winning_brick.score()) + "\nLast mark: " + str(winning_mark))
    print("Total score: " + str(winning_brick.score() * winning_mark))
        
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