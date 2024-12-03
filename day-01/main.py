from typing import List, Tuple


def part_1(input: List[int]) -> int:
    left, right = split_lists(input)
    return sum([abs(x - y) for x, y in zip(sorted(left), sorted(right))])


def part_2(input: List[int]) -> int:
    left, right = split_lists(input)
    right_count = {}
    for i in right:
        if not right_count.get(i):
            right_count[i] = 0
        right_count[i] += 1
    return sum([x * right_count.get(x, 0) for x in left])


def split_lists(input: List[int]) -> Tuple[List[int], List[int]]:
    return sorted(input[0::2]), sorted(input[1::2])


if __name__ == "__main__":
    input_file = "./input.txt"
    input = [*map(int, open(input_file).read().split())]

    print(part_1(input))
    print(part_2(input))
