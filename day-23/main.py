from itertools import combinations


def part_1(data: str) -> int:
    comps, conns = set(), set()
    for conn in data.split("\n"):
        a, b = conn.split("-")
        comps.update([a, b])
        conns.update([(a, b), (b, a)])
    total = 0
    for a, b, c in combinations(comps, 3):
        if {(a, b), (b, c), (c, a)} < conns and any(n[0] == "t" for n in (a, b, c)):
            total += 1
    return total


def part_2(data: str) -> int:
    comps, conns = set(), set()
    for conn in data.split("\n"):
        a, b = conn.split("-")
        comps.update([a, b])
        conns.update([(a, b), (b, a)])
    nets = [{c} for c in comps]
    for net in nets:
        for pc in comps:
            if all((pc, node) in conns for node in net):
                net.add(pc)
    return ",".join(sorted(max(nets, key=len)))


if __name__ == "__main__":
    input_file = "./input.txt"
    with open(input_file) as f:
        data = f.read()

    print(part_1(data))
    print(part_2(data))
