import re
from typing import Tuple


def part_1(input: str) -> int:
    h, w = len(input.split("\n")), len(input.split("\n")[0])
    input = "".join(input.split("\n"))
    p, o = get_current_pos(input)
    while True:
        q = get_next_pos(p, o, w)
        if guard_route_complete(p, q, h, w):
            input = input[:p] + "X" + input[p + 1 :]
            break
        input, p, o = move(input, p, q, o)
    return input.count("X")


def part_2(input: str) -> int:
    h, w = len(input.split("\n")), len(input.split("\n")[0])
    input = "".join(input.split("\n"))
    p, o = get_current_pos(input)
    start = p
    new_obstacles = []
    not_obstacles = []
    while True:
        q = get_next_pos(p, o, w)
        if guard_route_complete(p, q, h, w):
            input = input[:p] + "X" + input[p + 1 :]
            break
        if (
            input[q] != "#"
            and q != start
            and q not in new_obstacles
            and q not in not_obstacles
        ):
            if test_new_obstacle(input, p, q, o, h, w):
                new_obstacles.append(q)
            else:
                not_obstacles.append(q)
        input, p, o = move(input, p, q, o)
    return len(set(new_obstacles))


def get_current_pos(input: str) -> Tuple[int, str]:
    match = re.search(r"(\^|\>|\v|\<)", input)
    return match.start(), match.group()


def get_next_pos(p: int, o: str, w: int) -> Tuple[int, int, str]:
    match o:
        case "^":
            return p - w
        case ">":
            return p + 1
        case "v":
            return p + w
        case "<":
            return p - 1


def get_next_o(o: str) -> str:
    match o:
        case "^":
            return ">"
        case ">":
            return "v"
        case "v":
            return "<"
        case "<":
            return "^"


def move(input: str, p: int, q: int, o: str) -> Tuple[str, int, str]:
    if input[q] == "#":
        o = get_next_o(o)
        input = input[:p] + o + input[p + 1 :]
        return input, p, o
    input = input[:p] + "X" + input[p + 1 :]
    input = input[:q] + o + input[q + 1 :]
    return input, q, o


def guard_route_complete(p: int, q: int, h: int, w: int) -> bool:
    if q < 0 or q >= h * w or (abs(q - p) == 1 and p // w != q // w):
        return True
    return False


def test_new_obstacle(input: str, p: int, q: int, o: str, h: int, w: int) -> int:
    input = input[:q] + "#" + input[q + 1 :]
    test_obstacles = []
    while True:
        q = get_next_pos(p, o, w)
        if guard_route_complete(p, q, h, w):
            return False
        if input[q] == "#":
            if (q, o) in test_obstacles:
                return True
            test_obstacles.append((q, o))
        input, p, o = move(input, p, q, o)


if __name__ == "__main__":
    input_file = "./input.txt"
    with open(input_file) as f:
        input = f.read()

    print(part_1(input))
    print(part_2(input))
