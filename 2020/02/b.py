import os, argparse, re

def validate_line(first_index, second_index, letter, password):
    first = password[first_index-1]
    second = password[second_index-1]
    if (first == letter and second != letter) or (first != letter and second == letter):
        return 1
    else:
        print(f"Password: {password}, First_index: {first_index}, Second_index: {second_index}, Letter: {letter}, First: {first}, Second: {second}")
        return 0

def check_line(str):
    m = re.search('([0-9]*)-([0-9]*) (.): (.*)', str)
    return validate_line(int(m.group(1)), int(m.group(2)), m.group(3), m.group(4))

def solve_task(filename):
    valid_passwords = 0

    with open(filename) as infile:
        for raw_line in infile:
            line = raw_line.rstrip()
            valid_passwords += check_line(line)
            
    print(f"Valid passwords: {valid_passwords}")
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