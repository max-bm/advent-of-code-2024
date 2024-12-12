import re
from functools import cache


def part_1(input: str) -> int:
    stones = re.findall(r"\d+", input)
    return sum([blink(stone, 25) for stone in stones])


def part_2(input: str) -> int:
    stones = re.findall(r"\d+", input)
    return sum([blink(stone, 75) for stone in stones])


@cache
def blink(stone: str, blinks: int) -> int:
    if blinks == 0:
        return 1
    if stone == "0":
        return blink("1", blinks - 1)
    if len(stone) % 2 == 0:
        return blink(stone[: len(stone) // 2], blinks - 1) + blink(
            str(int(stone[len(stone) // 2 :])), blinks - 1
        )
    return blink(str(int(stone) * 2024), blinks - 1)


if __name__ == "__main__":
    input_file = "./input.txt"
    with open(input_file) as f:
        input = f.read()

    print(part_1(input))
    print(part_2(input))
