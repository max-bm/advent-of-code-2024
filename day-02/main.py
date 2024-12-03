from typing import List


def part_1(input: List[List[int]]) -> int:
    total = 0
    for row in input:
        if is_safe(row):
            total += 1
    return total


def part_2(input: List[List[int]]) -> int:
    total = 0
    for row in input:
        if is_safe(row):
            total += 1
            continue
        for i in range(len(row)):
            if is_safe(row[:i] + row[i + 1 :]):
                total += 1
                break
    return total


def is_safe(levels: List[int]) -> bool:
    diffs = [y - x for x, y in zip(levels[:-1], levels[1:])]
    return set(diffs) <= {1, 2, 3} or set(diffs) <= {-1, -2, -3}


if __name__ == "__main__":
    input_file = "./input.txt"
    input = [[*map(int, l.split())] for l in open(input_file)]

    print(part_1(input))
    print(part_2(input))
