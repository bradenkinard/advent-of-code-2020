import argparse
import string


def format_passport(passport_string):
    passport = {}
    for string in passport_string.split():
        field, value = string.split(":")
        passport[field] = value
    return passport


def check_year(year_string, min_year=None, max_year=None):
    checks = []
    checks.append(len(year_string) == 4)
    if min_year is not None:
        checks.append(int(year_string) >= min_year)
    if max_year is not None:
        checks.append(int(year_string) <= max_year)
    return all(checks)


def check_hgt(height_string):
    unit = height_string[-2:]
    height = height_string[:-2]
    try:
        height = int(height)
        if unit == "in" and height >= 59 and height <= 76:
            check = True
        elif unit == "cm" and height >= 150 and height <=193:
            check = True
        else:
            check = False 
    except ValueError:
        check = False
    return check


def check_hcl(hair_string):
    checks = []
    checks.append(hair_string[0]=="#")
    checks.append(len(hair_string)==7)
    valid_chars = string.digits + string.ascii_lowercase[:6]
    checks.append(all([c in valid_chars for c in hair_string[1:]]))
    return all(checks)


def check_ecl(eye_string):
    return eye_string in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def check_pid(pid_string):
    try:
        int(pid_string)
        check = len(pid_string)==9
    except:
        check = False
    return check


def check_passport_fields(passport):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    keys = passport.keys()
    checks = [(field in keys) for field in required_fields]
    return all(checks)


def check_passport_values(passport):
    checks = []
    checks.append(check_year(passport["byr"], 1920, 2002))
    checks.append(check_year(passport["iyr"], 2010, 2020))
    checks.append(check_year(passport["eyr"], 2020, 2030))
    checks.append(check_hgt(passport["hgt"]))
    checks.append(check_ecl(passport["ecl"]))
    checks.append(check_hcl(passport["hcl"]))
    checks.append(check_pid(passport["pid"]))
    return all(checks)


def main(args):
    data = [format_passport(line) for line in open(args.filepath, "r").read().split("\n\n")]
    checks = [check_passport_values(passport) for passport in data if check_passport_fields(passport)]
    print(f"Total passports: {len(data)}")
    print(f"Valid passports (fields): {len(checks)}")
    print(f"Valid passports (values): {sum(checks)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filepath", help="path to file to be processed", required=True)
    args = parser.parse_args()
    main(args)