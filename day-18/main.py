import heapq
from collections import defaultdict
from typing import Dict


def part_1(data: str) -> int:
    w, h = 70, 70
    grid = {i + j * 1j: "." for i in range(w + 1) for j in range(h + 1)}
    start = 0 + 0j
    end = w + h * 1j
    n_bytes = 1024
    for n, byte in enumerate(data.split("\n")):
        if n > n_bytes - 1:
            break
        x, y = byte.split(",")
        grid[int(x) + int(y) * 1j] = "#"
    return a_star_search(grid, start, 1, end)


def part_2(data: str) -> int:
    w, h = 70, 70
    grid = {i + j * 1j: "." for i in range(w + 1) for j in range(h + 1)}
    start = 0 + 0j
    end = w + h * 1j
    n_bytes = 1024
    for n, byte in enumerate(data.split("\n")):
        x, y = byte.split(",")
        grid[int(x) + int(y) * 1j] = "#"
        if n <= n_bytes - 1:
            continue
        b = int(x) + int(y) * 1j
        if a_star_search(grid, start, 1, end):
            continue
        return b


def a_star_search(
    maze: Dict[complex, str], start: complex, d: complex, end: complex
) -> int:
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
            return g
        for r, v in (1, 1), (+1j, 1), (-1j, 1):
            new_g, t, next, new_d = g + v, t + 1, current + d * r, d * r
            if next not in maze or maze[next] == "#":
                continue
            if next not in visited:
                heapq.heappush(open, (new_g, t, next, new_d, path + [next]))
                visited.add(next)
    return None


if __name__ == "__main__":
    input_file = "./input.txt"
    with open(input_file) as f:
        data = f.read()

    print(part_1(data))
    print(part_2(data))
