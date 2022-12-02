import os, argparse

handEncoding = {"A": "rock", "B": "paper", "C": "scissors"}
resultEncoding = {"X": "lose", "Y": "draw", "Z": "win"}

scoring = {"rock": 1, "paper": 2, "scissors": 3}

beats = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
loses_to = {l: b for b,l in beats.items()}

def throw_hands(me, them):
    if me == them:
        return 3
    if me == beats[them]:
        return 6
    else:
        return 0

def arranged_match(them, result):
    if result == "win":
        return 6 + scoring[beats[them]]
    elif result == "lose":
        return scoring[loses_to[them]]
    else:
        return 3 + scoring[them]

def solve_task(lines):
    score = 0
    for line in lines:
        them = handEncoding[line[0]]
        result = resultEncoding[line[-1]]
        score += arranged_match(them, result)
    print(f"Score: {score}")

def read_lines(filename):
    lines = []
    with open(filename) as infile:
        for raw_line in infile:
            line = raw_line.rstrip()
            lines.append(line)
    return lines

def parse_arguments():
    parser = argparse.ArgumentParser(description="Script that solves the case",epilog="Have a nice day!")
    parser.add_argument('filename', nargs='?', default="example.txt", help='Input file')
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()
    lines = read_lines(args.filename)
    solve_task(lines)

if __name__ == "__main__":
    main()