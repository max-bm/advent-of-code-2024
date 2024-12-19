import re
from typing import Tuple


def part_1(data: str) -> int:
    A, B, C, *prog = map(int, re.findall(r"(\d+)", data))
    return run_program(A, B, C, prog)


def part_2(data: str) -> int:
    _, B, C, *prog = map(int, re.findall(r"(\d+)", data))
    search_a(0, B, C, prog, 0)


def search_a(A, B, C, prog, depth):
    if run_program(A, B, C, prog) == ",".join(map(str, prog)):
        print(A)
    if run_program(A, B, C, prog) == ",".join(map(str, prog[-depth:])) or not depth:
        for i in range(8):
            search_a(A * 8 + i, B, C, prog, depth + 1)


def run_program(A, B, C, prog):
    pointer = 0

    def combo(operand: int) -> int:
        match operand:
            case x if 0 <= x <= 3:
                return x
            case 4:
                return A
            case 5:
                return B
            case 6:
                return C

    def instr(opcode: int, operand: int) -> Tuple[int, bool]:
        nonlocal A, B, C, pointer
        match opcode:
            case 0:
                A = int(A / 2 ** combo(operand))
            case 1:
                B = B ^ operand
            case 2:
                B = combo(operand) % 8
            case x if x == 3 and A != 0:
                pointer = operand
                return None, True
            case 4:
                B = B ^ C
            case 5:
                return combo(operand) % 8, False
            case 6:
                B = int(A / 2 ** combo(operand))
            case 7:
                C = int(A / 2 ** combo(operand))
        return None, False

    output = ""
    while pointer < len(prog):
        opcode = prog[pointer]
        operand = prog[pointer + 1]
        out, jumped = instr(opcode, operand)
        output += f"{str(out)}," if out is not None else ""
        pointer += 2 if not jumped else 0
    return output.removesuffix(",")


if __name__ == "__main__":
    input_file = "./input.txt"
    with open(input_file) as f:
        data = f.read()

    print(part_1(data))
    part_2(data)
