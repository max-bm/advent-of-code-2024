import re
from typing import Dict, Tuple


def part_1(data: str) -> int:
    warehouse, instructions = data.split("\n\n")
    inst = "".join(instructions.split("\n"))
    h, w = len(warehouse.split("\n")), len(warehouse.split("\n")[0])
    wh = {i + j * 1j: warehouse.split("\n")[j][i] for i in range(w) for j in range(h)}
    match = re.search(r"@", "".join(warehouse.split("\n")))
    robot = match.start() % w + (match.start() // w) * 1j
    for i in inst:
        wh, robot = move(wh, robot, i)
    total = 0
    for i in range(w):
        for j in range(h):
            if wh[i + j * 1j] == "O":
                total += i + 100 * j
    return total


def part_2(data: str) -> int:
    warehouse, instructions = data.split("\n\n")
    inst = "".join(instructions.split("\n"))
    warehouse = (
        warehouse.replace("#", "##")
        .replace("O", "[]")
        .replace(".", "..")
        .replace("@", "@.")
    )
    h, w = len(warehouse.split("\n")), len(warehouse.split("\n")[0])
    wh = {i + j * 1j: warehouse.split("\n")[j][i] for i in range(w) for j in range(h)}
    match = re.search(r"@", "".join(warehouse.split("\n")))
    robot = match.start() % w + (match.start() // w) * 1j
    for i in inst:
        wh, robot = move(wh, robot, i, part=2)
    total = 0
    for i in range(w):
        for j in range(h):
            if wh[i + j * 1j] == "[":
                total += i + 100 * j
    return total


def move(
    wh: Dict[complex, str], robot: complex, i: str, part: int = 1
) -> Tuple[Dict[complex, str], complex]:
    dirs = {"^": -1j, ">": 1, "v": 1j, "<": -1}
    moving = []
    update = {robot: ".", robot + dirs[i]: "@"}
    next = {robot}
    while True:
        next = {j + dirs[i] for j in next}
        if any(wh[j] == "#" for j in next):
            return wh, robot
        if all(wh[j] == "." for j in next):
            for j in next:
                update[j] = wh[j - dirs[i]]
            break
        if part == 2 and i in ["^", "v"]:
            rb = "]" if i == "^" else "["
            lb = "[" if i == "^" else "]"
            left = -1 if i == "^" else 1
            lookahead = set()
            for j in next:
                if wh[j] == rb:
                    moving.append(j)
                    lookahead.update([j + left, j])
                elif wh[j] == lb:
                    moving.append(j)
                    lookahead.update([j, j - left])
            next = lookahead
        for j in next:
            update[j] = "." if j not in update else update[j]
            update[j + dirs[i]] = wh[j]
    for j in update:
        wh[j] = update[j]
    return wh, robot + dirs[i]


if __name__ == "__main__":
    input_file = "./input.txt"
    with open(input_file) as f:
        data = f.read()

    print(part_1(data))
    print(part_2(data))
