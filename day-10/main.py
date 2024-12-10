import re
from typing import Dict, List


def part_1(input: str) -> int:
    w = len(input.split("\n")[0])
    input = "".join(input.split("\n"))
    map = {i // w + (i % w) * 1j: int(input[i]) for i in range(len(input))}
    match = re.finditer(r"0", input)
    trailheads = {m.start() // w + (m.start() % w) * 1j: [] for m in match}
    for t in trailheads:
        trailheads[t] += get_trail_end(t, map)
    scores = {k: len(set(v)) for k, v in trailheads.items()}
    return sum(scores.values())


def part_2(input: str) -> int:
    w = len(input.split("\n")[0])
    input = "".join(input.split("\n"))
    map = {i // w + (i % w) * 1j: int(input[i]) for i in range(len(input))}
    match = re.finditer(r"0", input)
    trailheads = {m.start() // w + (m.start() % w) * 1j: [] for m in match}
    for t in trailheads:
        trailheads[t] += get_trail_end(t, map)
    ratings = {k: len(v) for k, v in trailheads.items()}
    return sum(ratings.values())


def get_trail_end(trailhead: complex, map: Dict[complex, int]) -> List[complex]:
    height = map[trailhead]
    if height == 9:
        return [trailhead]
    steps = []
    for d in [trailhead + 1j, trailhead - 1j, trailhead + 1, trailhead - 1]:
        if d in map and map[d] == height + 1:
            steps += get_trail_end(d, map)
    return steps


if __name__ == "__main__":
    input_file = "./input.txt"
    with open(input_file) as f:
        input = f.read()

    print(part_1(input))
    print(part_2(input))
