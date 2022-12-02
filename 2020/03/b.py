import os, argparse
tree = '#'

def hit_function(map, x, y):
    wrapped_x = x % len(map[0])

    if (map[y][wrapped_x] == tree):
        return 1
    else:
        return 0

def number_of_hits(map, right, down):
    trees_hit = 0
    stages = len(map)//down
    for n in range(stages):
        trees_hit += hit_function(map, n*right, n*down)
    return trees_hit

def solve_task(filename):
    toboggan_slope = []
    with open(filename) as infile:
        for raw_line in infile:
            line = raw_line.rstrip()
            toboggan_slope.append(line)

    tactics = [(1,1),
    (3,1),
    (5,1),
    (7,1),
    (1,2)]

    score = 1
    for tactic in tactics:
        hits = number_of_hits(toboggan_slope, tactic[0], tactic[1])
        score *= hits
        print(f"Hit {hits} trees")

    print(f"Score: {score}")
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