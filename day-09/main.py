from collections import defaultdict


def part_1(input: str) -> int:
    file_id = 0
    blocks = []
    for i in range(0, len(input), 2):
        blocks += [str(file_id)] * int(input[i])
        if i < len(input) - 1:
            blocks += ["."] * int(input[i + 1])
        file_id += 1
    for i in range(len(blocks)):
        if i >= len(blocks):
            break
        if blocks[i] != ".":
            continue
        while (last := blocks.pop(-1)) == "." and i < len(blocks):
            ...
        if i >= len(blocks):
            break
        blocks[i] = last
    return sum([i * int(b) for i, b in enumerate(blocks)])


def part_2(input: str) -> int:
    file_id = 0
    blocks = []
    files = defaultdict(tuple)
    free_blocks = []
    for i in range(0, len(input), 2):
        blocks += [str(file_id)] * int(input[i])
        files[file_id] = (int(input[i]), len(blocks) - int(input[i]))
        if i < len(input) - 1:
            blocks += ["."] * int(input[i + 1])
            free_blocks.append((int(input[i + 1]), len(blocks) - int(input[i + 1])))
        file_id += 1
    for i in range(file_id - 1, -1, -1):
        required_size = files[i][0]
        for j in range(len(free_blocks)):
            if free_blocks[j][1] > files[i][1]:
                break
            if free_blocks[j][0] >= required_size:
                blocks[free_blocks[j][1] : free_blocks[j][1] + required_size] = [
                    str(i)
                ] * required_size
                free_blocks[j] = (
                    free_blocks[j][0] - required_size,
                    free_blocks[j][1] + required_size,
                )
                blocks = [
                    "." if b == str(i) and k >= free_blocks[j][1] else b
                    for k, b in enumerate(blocks)
                ]
                break
    return sum([i * int(b) for i, b in enumerate(blocks) if b != "."])


if __name__ == "__main__":
    input_file = "./input.txt"
    with open(input_file) as f:
        input = f.read()

    print(part_1(input))
    print(part_2(input))
