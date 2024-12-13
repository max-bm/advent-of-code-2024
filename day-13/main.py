import re


def part_1(input: str) -> int:
    machines = input.split("\n\n")
    cost = 0
    for m in machines:
        ax, ay, bx, by, px, py = map(int, re.findall(r"((?:\+|\-)?\d+)", m))
        na = (bx * py - by * px) / (bx * ay - by * ax)
        nb = (ax * py - ay * px) / (ax * by - ay * bx)
        if not na.is_integer() or not nb.is_integer():
            continue
        cost += 3 * int(na) + int(nb)
    return cost


def part_2(input: str) -> int:
    machines = input.split("\n\n")
    cost = 0
    for m in machines:
        ax, ay, bx, by, px, py = map(int, re.findall(r"((?:\+|\-)?\d+)", m))
        px += 10000000000000
        py += 10000000000000
        na = (bx * py - by * px) / (bx * ay - by * ax)
        nb = (ax * py - ay * px) / (ax * by - ay * bx)
        if not na.is_integer() or not nb.is_integer():
            continue
        cost += 3 * int(na) + int(nb)
    return cost


if __name__ == "__main__":
    input_file = "./input.txt"
    with open(input_file) as f:
        input = f.read()

    print(part_1(input))
    print(part_2(input))
