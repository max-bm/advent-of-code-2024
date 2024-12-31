from functools import reduce


def part_1(data: str) -> int:
    iterations = 2000
    return sum(
        reduce(lambda x, _: step(x), range(iterations), int(s))
        for s in map(int, data.split("\n"))
    )


def part_2(data: str) -> int:
    iterations = 2000
    total = {}
    all_changes = []
    for i, s in enumerate(map(int, data.split("\n"))):
        all_changes.append({})
        changes = []
        for j in range(iterations):
            t = step(s)
            changes.append(t % 10 - s % 10)
            s = t
            if len(changes) >= 4 and tuple(changes[-4:]) not in all_changes[i]:
                all_changes[i][tuple(changes[-4:])] = t % 10
    for d in all_changes:
        for k, v in d.items():
            if k in total:
                total[k] += v
            else:
                total[k] = v
    return max(total.values())


def step(n: int) -> int:
    n = prune(mix(n << 6, n))
    n = prune(mix(n >> 5, n))
    n = prune(mix(n << 11, n))
    return n


def mix(val: int, sec: int) -> int:
    return val ^ sec


def prune(sec: int) -> int:
    return sec & 16777215


if __name__ == "__main__":
    input_file = "./input.txt"
    with open(input_file) as f:
        data = f.read()

    print(part_1(data))
    print(part_2(data))
