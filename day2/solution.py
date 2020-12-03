import argparse


def parse_line(line):
    policy_range, policy_letter, password = line.split()
    policy_min, policy_max = [int(n) for n in policy_range.split("-")]
    policy_letter = policy_letter[0]
    return (policy_min, policy_max), policy_letter, password

def check_password_part1(policy_range, policy_letter, password):
    letter_count = password.count(policy_letter)
    if letter_count >= policy_range[0] and letter_count <= policy_range[1]:
        passed = True
    else:
        passed = False
    return passed

def check_password_part2(policy_indices, policy_letter, password):
    char_checks = [password[i - 1]==policy_letter for i in policy_indices]
    if sum(char_checks) == 1:
        passed = True
    else:
        passed = False
    return passed

def main(args):
    data = [line for line in open(args.filepath, "r").read().split("\n")][0:-1]
    checks_part1 = []
    checks_part2 = []
    for line in data:
        parsed = parse_line(line)
        checks_part1.append(check_password_part1(*parsed))
        checks_part2.append(check_password_part2(*parsed))
    print(f"Part 1: {sum(checks_part1)}")
    print(f"Part 2: {sum(checks_part2)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filepath", help="path to file to be processed", required=True)
    args = parser.parse_args()
    main(args)
