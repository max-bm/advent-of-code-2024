import re
from typing import List


def part_1(input: str) -> int:
    rows = input.split("\n")
    cols = ["".join(x) for x in zip(*rows)]
    h, w = len(rows), len(cols)
    bwd_diag = []
    for k in range(-h + 1, w):
        diagonal = []
        for i in range(h):
            j = i + k
            if 0 <= j < w:
                diagonal.append(rows[i][j])
        bwd_diag.append("".join(diagonal))
    fwd_diag = []
    for k in range(-h + 1, w):
        diagonal = []
        for i in range(h):
            j = w - 1 - (i + k)
            if 0 <= j < w:
                diagonal.append(rows[i][j])
        fwd_diag.append("".join(diagonal))

    total = 0
    total += len(re.findall(r"XMAS", ",".join(rows + cols + bwd_diag + fwd_diag)))
    total += len(re.findall(r"SAMX", ",".join(rows + cols + bwd_diag + fwd_diag)))
    return total


def part_2(input: List[str]) -> int:
    total = 0
    for i, row in enumerate(input):
        if i == 0 or i == len(input) - 1:
            continue
        for j, char in enumerate(row):
            if j == 0 or j == len(row) - 1:
                continue
            if char != "A":
                continue
            if f"{input[i-1][j-1]}{char}{input[i+1][j+1]}" not in ["SAM", "MAS"]:
                continue
            if f"{input[i-1][j+1]}{char}{input[i+1][j-1]}" not in ["SAM", "MAS"]:
                continue
            total += 1
    return total


if __name__ == "__main__":
    input_file = "./input.txt"
    with open(input_file) as f:
        input = f.read()

    print(part_1(input))
    print(part_2(input.split("\n")))
