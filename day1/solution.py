import argparse
from itertools import combinations
from math import prod

def main(args):
    data = [int(line) for line in open(args.filepath, "r").read().split("\n")[0:-1]]
    tuples = combinations(data, args.r)
    answer = f"There are no {args.r} values that sum to 2020."
    for tup in tuples:
        if sum(tup) == 2020:
            product = 1
            answer = prod(tup)
            break
    print(answer)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filepath", help="path to file to be processed", required=True)
    parser.add_argument(
        "-r", type=int, help="the number of values to be selected for each combination", required=True
    )
    args = parser.parse_args()
    main(args)
