from functools import cache
from typing import Tuple


def part_1(data: str) -> int:
    return sum(
        int(code.removesuffix("A")) * get_length(code.removesuffix("A"), 2)
        for code in data.split("\n")
    )


def part_2(data: str) -> int:
    return sum(
        int(code.removesuffix("A")) * get_length(code.removesuffix("A"), 25)
        for code in data.split("\n")
    )


def get_instructions(keys: Tuple[str, str]) -> str:
    (y, x), (Y, X) = [divmod("789456123_0A<v>".find(k), 3) for k in keys]
    instructions = ">" * (X - x) + "v" * (Y - y) + "0" * (y - Y) + "<" * (x - X)
    return instructions if (3, 0) in [(y, X), (Y, x)] else instructions[::-1]


@cache
def get_length(instructions: str, n_robots: int) -> int:
    if n_robots < 0:
        return len(instructions) + 1
    return sum(
        get_length(get_instructions(i), n_robots - 1)
        for i in zip("A" + instructions, instructions + "A")
    )


if __name__ == "__main__":
    input_file = "./input.txt"
    with open(input_file) as f:
        data = f.read()

    print(part_1(data))
    print(part_2(data))
