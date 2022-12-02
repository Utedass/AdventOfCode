import os, argparse, re

def parse_line(line):
    pairs = {}
    for m in re.finditer("([^\s:]+):([^\s:]+)", line):
        print(f"Found {m.group(1)}:{m.group(2)}")
        pairs[m.group(1)] = m.group(2)
    return pairs

def validate_number(val, min, max):
    if not re.match("^\d{4}$", val):
        return False
    if int(val) < min or int(val) > max:
        return False
    return True

def validate_height(val):
    m = re.match("^(\d+)(cm|in)$", val)

    if not m:
        return False

    len = int(m.group(1))
    
    if m.group(2) == "cm":
        if len >= 150 and len <= 193:
            return True
    elif m.group(2) == "in":
        if len >= 59 and len <= 76:
            return True
    return False

def validate_hair_color(val):
    m = re.match("^#[\da-f]{6}$", val)
    if not m:
        return False
    return True

def validate_eye_color(val):
    if val not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    return True

def validate_passport_number(val):
    m = re.match("^\d{9}$", val)
    if not m:
        return False
    return True

def validate_field(key, value):
    match key:
        case "byr":
            return validate_number(value, 1920, 2002)
        case "iyr":
            return validate_number(value, 2010, 2020)
        case "eyr":
            return validate_number(value, 2020, 2030)
        case "hgt":
            return validate_height(value)
        case "hcl":
            return validate_hair_color(value)
        case "ecl":
            return validate_eye_color(value)
        case "pid":
            return validate_passport_number(value)
    return False

def validate_passport(passport):
    mandatory_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for k in mandatory_fields:
        if not k in passport:
            print(f"Invalid passport! Missing {k}")
            return False
        if not validate_field(k, passport[k]):
            print(f"Invalid field! {k}:{passport[k]}")
            return False
    print("Passport valid!")
    return True

def solve_task(filename):
    valid_passports = 0
    current_passport = {}
    with open(filename) as infile:
        for raw_line in infile:
            line = raw_line.rstrip()
            if line == "":
                if validate_passport(current_passport):
                    valid_passports += 1
                print("")
                current_passport = {}
                continue
            current_passport.update(parse_line(line))

    if validate_passport(current_passport):
        valid_passports += 1

    print(f"\nTotal number of valid passports: {valid_passports}")
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