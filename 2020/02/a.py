import os, argparse, re

def validate_line(min, max, letter, password):
    count = password.count(letter)
    if count < min or count > max:
        print(f"Min: {min}, Max: {max}, Letter: {letter}, Password: {password}, Counted: {count}")
        return 0
    else:
        return 1

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