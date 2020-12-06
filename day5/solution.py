import argparse
import math


def identify_seat(seat_string):
    row = partition_binary_space(seat_string[:7], max_val=127, upper_char="B", lower_char="F")
    column = partition_binary_space(seat_string[7:], max_val=7, upper_char="R", lower_char="L")
    return get_seat_id(row, column)


def partition_binary_space(seat_string, max_val, upper_char, lower_char, min_val=0):
    for c in seat_string:
        if c == lower_char:
            max_val = min_val +  math.floor((max_val - min_val) / 2)
        elif c == upper_char:
            min_val = min_val + math.ceil((max_val - min_val) / 2)
    return min_val

def get_seat_id(row, column):
    return row * 8 + column


def main(args):
    data = [line for line in open(args.filepath, "r").read().split("\n")]
    possible_ids = list(range(1024))
    ids = set([identify_seat(seat_string) for seat_string in data])
    prev_missing = 0
    for i in possible_ids:
        if i not in ids:
            diff = i - prev_missing
            if diff > 1:
                seat = i
                break
            else:
                prev_missing = i

    print(f"(Part 1) Max seat ID: {max(ids)}")
    print(f"(Part 2) My seat ID: {seat}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filepath", help="path to file to be processed", required=True)
    args = parser.parse_args()
    main(args)