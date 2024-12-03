import re


def part_1(input: str) -> None:
    return sum([int(x) * int(y) for x, y in re.findall(r"mul\((\d+)\,(\d+)\)", input)])


def part_2(input: str) -> None:
    total = 0
    enabled = True
    for x, y, do, dont in re.findall(
        r"mul\((\d+)\,(\d+)\)|(do\(\))|(don\'t\(\))", input
    ):
        if do or dont:
            enabled = bool(do)
            continue
        total += int(x) * int(y) * enabled
    return total


if __name__ == "__main__":
    input_file = "./input.txt"
    with open(input_file) as f:
        input = f.read()

    print(part_1(input))
    print(part_2(input))
