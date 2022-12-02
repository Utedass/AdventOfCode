import os, argparse
tree = '#'

def hit_function(map, x, y):
    wrapped_x = x % len(map[0])
    print(wrapped_x)
    return map[y][wrapped_x] == tree

def check_stage(map, n):
    x = 3*(n+1)
    y = n+1
    return hit_function(map, x, y)

def solve_task(filename):
    toboggan_slope = []
    with open(filename) as infile:
        for raw_line in infile:
            line = raw_line.rstrip()
            toboggan_slope.append(line)

    trees_hit = 0
    for n in range(len(toboggan_slope)-1):
        if check_stage(toboggan_slope, n):
            trees_hit += 1
    
    print(f"Totally {trees_hit} trees hit")

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