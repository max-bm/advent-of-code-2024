import re


def part_1(input: str) -> int:
    h, w = len(input.split("\n")), len(input.split("\n")[0])
    antennae = [
        (match.group(0), (match.start() // w) + (match.start() % w) * 1j)
        for match in re.finditer(r"([^\.])", "".join(input.split("\n")))
    ]
    antinodes = []
    for a in range(len(antennae)):
        for b in range(a + 1, len(antennae)):
            if antennae[a][0] == antennae[b][0]:
                grad = antennae[b][1] - antennae[a][1]
                an = [antennae[b][1] + n * grad for n in [-2, 1]]
                antinodes += [n for n in an if 0 <= n.real < h and 0 <= n.imag < w]
    return len(set(antinodes))


def part_2(input: str) -> int:
    h, w = len(input.split("\n")), len(input.split("\n")[0])
    antennae = [
        (match.group(0), (match.start() // w) + (match.start() % w) * 1j)
        for match in re.finditer(r"([^\.])", "".join(input.split("\n")))
    ]
    antinodes = []
    for a in range(len(antennae)):
        for b in range(a + 1, len(antennae)):
            if antennae[a][0] == antennae[b][0]:
                grad = antennae[b][1] - antennae[a][1]
                an = [antennae[b][1] + n * grad for n in range(-h * w - 1, h * w)]
                antinodes += [n for n in an if 0 <= n.real < h and 0 <= n.imag < w]
    return len(set(antinodes))


if __name__ == "__main__":
    input_file = "./input.txt"
    with open(input_file) as f:
        input = f.read()

    print(part_1(input))
    print(part_2(input))
