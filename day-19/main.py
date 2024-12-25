from functools import cache
from typing import List


def part_1(data: str) -> int:
    available, display = data.split("\n\n")
    available = available.split(", ")
    return sum(is_possible(d, available) for d in display.split("\n"))


def part_2(data: str) -> int:
    available, display = data.split("\n\n")
    available = available.split(", ")

    @cache
    def arrangements(target: str) -> int:
        if len(target) == 0:
            return 1
        total = 0
        for a in available:
            if target.startswith(a):
                total += arrangements(target[len(a) :])
        return total

    return sum(arrangements(d) for d in display.split("\n"))


def is_possible(target: str, available: List[str]) -> bool:
    if len(target) == 0:
        return True
    for a in available:
        if target.startswith(a):
            if is_possible(target[len(a) :], available):
                return True
    return False


if __name__ == "__main__":
    input_file = "./input.txt"
    with open(input_file) as f:
        data = f.read()

    print(part_1(data))
    print(part_2(data))
