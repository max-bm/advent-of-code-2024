import re
from collections import defaultdict
from statistics import mean, variance
from typing import Tuple

W, H = 101, 103


def part_1(input: str) -> int:
    robots = []
    for robot in input.split("\n"):
        px, py, vx, vy = map(int, re.findall(r"((?:\+|\-)?\d+)", robot))
        robots.append((px + py * 1j, vx + vy * 1j))
    for _ in range(100):
        robots = map(update_pos, robots)
    tiles = defaultdict(int)
    for robot in robots:
        tiles[robot[0]] += 1
    q1, q2, q3, q4 = 0, 0, 0, 0
    for t in tiles:
        if t.real < W // 2:
            if t.imag < H // 2:
                q1 += tiles[t]
            elif t.imag > H // 2:
                q3 += tiles[t]
        elif t.real > W // 2:
            if t.imag < H // 2:
                q2 += tiles[t]
            elif t.imag > H // 2:
                q4 += tiles[t]
    return q1 * q2 * q3 * q4


def part_2(input: str) -> int:
    robots = []
    for robot in input.split("\n"):
        px, py, vx, vy = map(int, re.findall(r"((?:\+|\-)?\d+)", robot))
        robots.append((px + py * 1j, vx + vy * 1j))
    t = 0
    x_vars, y_vars = [variance([robot[0].real for robot in robots])], [
        variance([robot[0].imag for robot in robots])
    ]
    while True:
        t += 1
        robots = [*map(update_pos, robots)]
        x_var = variance([robot[0].real for robot in robots])
        y_var = variance([robot[0].imag for robot in robots])
        if x_var < mean(x_vars) / 2 and y_var < mean(y_vars) / 2:
            break
        x_vars.append(x_var)
        y_vars.append(y_var)
    return t


def update_pos(robot: Tuple[complex]) -> Tuple[complex]:
    new_pos = robot[0] + robot[1]
    return (new_pos.real % W + (new_pos.imag % H) * 1j, robot[1])


if __name__ == "__main__":
    input_file = "./input.txt"
    with open(input_file) as f:
        input = f.read()

    print(part_1(input))
    print(part_2(input))
