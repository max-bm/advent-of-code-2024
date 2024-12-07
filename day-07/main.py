import re
from functools import reduce
from itertools import product
from operator import mul
from typing import List


def part_1(input: List[str]) -> int:
    total = 0
    for row in input:
        value, *numbers = map(int, re.findall(r"\d+", row))
        total += value * test_numbers(value, numbers)
    return total


def part_2(input: List[str]) -> int:
    total = 0
    operators = {
        "*": lambda x, y: x * y,
        "+": lambda x, y: x + y,
        "||": lambda x, y: int(str(x) + str(y)),
    }
    for row in input:
        value, *numbers = map(int, re.findall(r"\d+", row))
        n_operators = len(numbers) - 1
        operator_perms = list(product(operators.keys(), repeat=n_operators))
        for p in operator_perms:
            expr = [x for pair in zip(numbers[:-1], p) for x in pair] + [numbers[-1]]
            expr_total = expr.pop(0)
            while expr:
                expr_total = operators[expr.pop(0)](expr_total, expr.pop(0))
            if expr_total == value:
                total += expr_total
                break
    return total


def test_numbers(target: int, numbers: List[int]) -> bool:
    prod_total, sum_total = reduce(mul, numbers), sum(numbers)
    if target in [prod_total, sum_total]:
        return True
    if len(numbers) == 1:
        return False
    last = numbers[-1]
    if target % last == 0 and test_numbers(int(target / last), numbers[:-1]):
        return True
    if target - last > 0 and test_numbers(target - last, numbers[:-1]):
        return True
    return False


if __name__ == "__main__":
    input_file = "./input.txt"
    with open(input_file) as f:
        input = f.read()

    print(part_1(input.split("\n")))
    print(part_2(input.split("\n")))
