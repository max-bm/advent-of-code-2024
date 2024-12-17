import heapq
import re
from collections import defaultdict
from typing import Dict, List, Tuple


def part_1(data: str) -> int:
    h, w = len(data.split("\n")), len(data.split("\n")[0])
    maze = {i + j * 1j: data.split("\n")[j][i] for i in range(w) for j in range(h)}
    start_match = re.search(r"S", "".join(data.split("\n")))
    start = start_match.start() % w + (start_match.start() // w) * 1j
    end_match = re.search(r"E", "".join(data.split("\n")))
    end = end_match.start() % w + (end_match.start() // w) * 1j
    score, _ = a_star_search(maze, start, 1 + 0j, end)
    return score


def part_2(data: str) -> int:
    h, w = len(data.split("\n")), len(data.split("\n")[0])
    maze = {i + j * 1j: data.split("\n")[j][i] for i in range(w) for j in range(h)}
    start_match = re.search(r"S", "".join(data.split("\n")))
    start = start_match.start() % w + (start_match.start() // w) * 1j
    end_match = re.search(r"E", "".join(data.split("\n")))
    end = end_match.start() % w + (end_match.start() // w) * 1j
    _, unique = a_star_search(maze, start, 1 + 0j, end, part=2)
    return unique


def a_star_search(
    maze: Dict[complex, str], start: complex, d: complex, end: complex, part: int = 1
) -> Tuple[List[complex], int]:
    visited = []
    best_score = float("inf")
    dist = defaultdict(lambda: float("inf"))
    open = [(0, t := 0, start, d, [start])]

    while open:
        g, _, current, d, path = heapq.heappop(open)
        if g > dist[current, d]:
            continue
        else:
            dist[current, d] = g
        if current == end and g <= best_score:
            visited += path
            best_score = g
        for r, v in (1, 1), (+1j, 1001), (-1j, 1001):
            new_g, t, next, new_d = g + v, t + 1, current + d * r, d * r
            if current not in maze or maze[current] == "#":
                continue
            heapq.heappush(open, (new_g, t, next, new_d, path + [next]))
    return best_score, len(set(visited))


if __name__ == "__main__":
    input_file = "./input.txt"
    with open(input_file) as f:
        data = f.read()

    print(part_1(data))
    print(part_2(data))
