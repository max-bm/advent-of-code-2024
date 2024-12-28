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
    _, base_path = a_star_search(maze, start, 1 + 0j, end)
    score_diff = 100
    total = 0
    for shortcut_start in base_path:
        for r in (1, 1j, -1, -1j):
            shortcut_end = shortcut_start + 2 * r
            if maze[shortcut_start + r] != "#" or shortcut_end not in base_path:
                continue
            saved = base_path.index(shortcut_end) - base_path.index(shortcut_start) - 2
            if saved >= score_diff:
                total += 1
    return total


def part_2(data: str) -> int:
    h, w = len(data.split("\n")), len(data.split("\n")[0])
    maze = {i + j * 1j: data.split("\n")[j][i] for i in range(w) for j in range(h)}
    start_match = re.search(r"S", "".join(data.split("\n")))
    start = start_match.start() % w + (start_match.start() // w) * 1j
    end_match = re.search(r"E", "".join(data.split("\n")))
    end = end_match.start() % w + (end_match.start() // w) * 1j
    _, base_path = a_star_search(maze, start, 1 + 0j, end)
    score_diff = 100
    shortcut_length_limit = 20
    good_cheats = set()
    for i, shortcut_start in enumerate(base_path):
        for j, shortcut_end in enumerate(base_path):
            if j < score_diff:
                continue
            dist = abs((shortcut_end - shortcut_start).real) + abs(
                (shortcut_end - shortcut_start).imag
            )
            if dist <= shortcut_length_limit and j - i - dist >= score_diff:
                good_cheats.add((shortcut_start, shortcut_end))
    return len(good_cheats)


def a_star_search(
    maze: Dict[complex, str], start: complex, d: complex, end: complex, part: int = 1
) -> Tuple[List[complex], int]:
    dist = defaultdict(lambda: float("inf"))
    visited = {start}
    open = [(0, t := 0, start, d, [start])]

    while open:
        g, _, current, d, path = heapq.heappop(open)
        if g > dist[current, d]:
            continue
        else:
            dist[current, d] = g
        if current == end:
            return g, path
        for r, v in (1, 1), (+1j, 1), (-1j, 1), (-1, 1):
            new_g, t, next, new_d = g + v, t + 1, current + d * r, d * r
            if next not in maze or maze[next] == "#":
                continue
            if next not in visited:
                heapq.heappush(open, (new_g, t, next, new_d, path + [next]))
                visited.add(next)
    return None, None


if __name__ == "__main__":
    input_file = "./input.txt"
    with open(input_file) as f:
        data = f.read()

    print(part_1(data))
    print(part_2(data))
