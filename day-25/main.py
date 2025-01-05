from typing import List


def part_1(data: str) -> int:
    data = data.split("\n\n")
    h = 5
    locks = [to_heights(d) for d in data if d.split()[0] == "#####"]
    keys = [to_heights(d) for d in data if d.split()[0] == "....."]
    total = 0
    for l in locks:
        for k in keys:
            if not any(l[i] + k[i] > h for i in range(len(l))):
                total += 1
    return total


def to_heights(input: str) -> List[int]:
    rows = input.split("\n")
    heights = [-1] * len(rows[0])
    for r in rows:
        for i, c in enumerate(r):
            heights[i] += 1 if c == "#" else 0
    return heights


if __name__ == "__main__":
    input_file = "./input.txt"
    with open(input_file) as f:
        data = f.read()

    print(part_1(data))
