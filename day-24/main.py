import heapq
from typing import Dict


def part_1(data: str) -> int:
    initial, conns = data.split("\n\n")
    initial = {k: int(v) for k, v in (l.split(": ") for l in initial.split("\n"))}
    conns = {v: k for k, v in (l.split(" -> ") for l in conns.split("\n"))}
    return calculate(initial, conns)


def part_2(data: str) -> int:
    initial, conns = data.split("\n\n")
    initial = {k: int(v) for k, v in (l.split(": ") for l in initial.split("\n"))}
    conns = {v: k for k, v in (l.split(" -> ") for l in conns.split("\n"))}
    r_conns = {v: k for k, v in conns.items()}
    x = int(
        "".join(
            map(str, (initial[k] for k in sorted(initial, reverse=True) if k[0] == "x"))
        ),
        2,
    )
    y = int(
        "".join(
            map(str, (initial[k] for k in sorted(initial, reverse=True) if k[0] == "y"))
        ),
        2,
    )
    z = x + y
    out = calculate(initial, conns)
    wrong_bits = {
        b: (conns[b], initial[b])
        for b in [f"z{i}" for i, d in enumerate(reversed(bin(z ^ out))) if d == "1"]
    }
    swaps = []
    for b in wrong_bits:
        i = int(b[1:])
        xor = r_conns.get(f"x{i} XOR y{i}") or r_conns.get(f"y{i} XOR x{i}")
        if xor in wrong_bits[b][0] and "XOR" in wrong_bits[b][0]:
            continue
        for r in r_conns:
            j, g, k = wrong_bits[b][0].split(" ")
            if xor in r and "XOR" in r:
                swaps.append((b, r_conns[r]))
                break
            elif g == "XOR":
                t = j if str(i) in conns[j] else k
                swaps.append((xor, t))
                break
    return ",".join(sorted([i for s in swaps for i in s]))


def calculate(initial: Dict[str, int], conns: Dict[str, str]) -> int:
    conns = conns.copy()
    gates = {
        "AND": lambda a, b: a & b,
        "OR": lambda a, b: a | b,
        "XOR": lambda a, b: a ^ b,
    }
    open = [(i, c) for i, c in enumerate(conns)]
    while open:
        p, c = heapq.heappop(open)
        a, g, b = conns[c].split(" ")
        if a not in initial or b not in initial:
            heapq.heappush(open, (p + 1, c))
            continue
        conns[c] = gates[g](initial[a], initial[b])
        initial[c] = conns[c]
    return int(
        "".join(
            map(str, (conns[k] for k in sorted(conns, reverse=True) if k[0] == "z"))
        ),
        2,
    )


if __name__ == "__main__":
    input_file = "./input.txt"
    with open(input_file) as f:
        data = f.read()

    print(part_1(data))
    print(part_2(data))
