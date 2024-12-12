from collections import defaultdict
from typing import Dict, List


def part_1(input: str) -> int:
    h, w = len(input.split("\n")), len(input.split("\n")[0])
    input = "".join(input.split("\n"))
    map = {i // w + (i % w) * 1j: {"v": input[i]} for i in range(len(input))}
    clusters = defaultdict(lambda: {"plots": [], "area": 0, "perimeter": 0})
    cluster_number = 1
    for i in range(h):
        for j in range(w):
            pos = i + j * 1j
            adj_clusters = adjacent_clusters(map, pos)
            if len(set(adj_clusters)) == 0:
                map[pos]["c"] = cluster_number
                clusters[cluster_number]["plots"].append(pos)
                clusters[cluster_number]["area"] += 1
                clusters[cluster_number]["perimeter"] += perimeter(map, pos)
                cluster_number += 1
            elif len(set(adj_clusters)) == 1:
                map[pos]["c"] = adj_clusters[0]
                clusters[adj_clusters[0]]["plots"].append(pos)
                clusters[adj_clusters[0]]["area"] += 1
                clusters[adj_clusters[0]]["perimeter"] += perimeter(map, pos)
            else:
                map[pos]["c"] = max(adj_clusters)
                clusters[max(adj_clusters)]["plots"].append(pos)
                clusters[max(adj_clusters)]["area"] += 1
                clusters[max(adj_clusters)]["perimeter"] += perimeter(map, pos)
                for field in ["plots", "area", "perimeter"]:
                    clusters[max(adj_clusters)][field] += clusters[min(adj_clusters)][
                        field
                    ]
                for p in clusters[min(adj_clusters)]["plots"]:
                    map[p]["c"] = max(adj_clusters)
                del clusters[min(adj_clusters)]
    return sum(c["area"] * c["perimeter"] for c in clusters.values())


def part_2(input: str) -> int:
    h, w = len(input.split("\n")), len(input.split("\n")[0])
    input = "".join(input.split("\n"))
    map = {i // w + (i % w) * 1j: {"v": input[i]} for i in range(len(input))}
    clusters = defaultdict(lambda: {"plots": [], "area": 0, "corners": 0})
    cluster_number = 1
    for i in range(h):
        for j in range(w):
            pos = i + j * 1j
            adj_clusters = adjacent_clusters(map, pos)
            if len(set(adj_clusters)) == 0:
                map[pos]["c"] = cluster_number
                clusters[cluster_number]["plots"].append(pos)
                clusters[cluster_number]["area"] += 1
                cluster_number += 1
            elif len(set(adj_clusters)) == 1:
                map[pos]["c"] = adj_clusters[0]
                clusters[adj_clusters[0]]["plots"].append(pos)
                clusters[adj_clusters[0]]["area"] += 1
            else:
                map[pos]["c"] = max(adj_clusters)
                clusters[max(adj_clusters)]["plots"].append(pos)
                clusters[max(adj_clusters)]["area"] += 1
                for field in ["plots", "area"]:
                    clusters[max(adj_clusters)][field] += clusters[min(adj_clusters)][
                        field
                    ]
                for p in clusters[min(adj_clusters)]["plots"]:
                    map[p]["c"] = max(adj_clusters)
                del clusters[min(adj_clusters)]
    for c in clusters:
        for p in clusters[c]["plots"]:
            for d in [-1j, 1, 1j, -1]:
                if map.get(p + d, {}).get("v") == map[p]["v"]:
                    if map.get(p + d * 1j, {}).get("v") == map[p]["v"]:
                        if map.get(p + d + d * 1j, {}).get("v") != map[p]["v"]:
                            clusters[c]["corners"] += 1
                else:
                    if map.get(p + d * 1j, {}).get("v") != map[p]["v"]:
                        clusters[c]["corners"] += 1
    return sum(c["area"] * c["corners"] for c in clusters.values())


def adjacent_clusters(map: Dict[complex, Dict[str, int]], pos: complex) -> List[int]:
    return [
        map.get(pos + d, {}).get("c")
        for d in [-1j, -1]
        if map.get(pos + d, {}).get("v") == map[pos]["v"]
    ]


def perimeter(map: Dict[complex, Dict[str, int]], pos: complex) -> int:
    return sum(
        [
            True
            for d in [-1j, -1, 1, 1j]
            if map.get(pos + d, {}).get("v") != map[pos]["v"]
        ]
    )


if __name__ == "__main__":
    input_file = "./input.txt"
    with open(input_file) as f:
        input = f.read()

    print(part_1(input))
    print(part_2(input))
