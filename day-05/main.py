from collections import defaultdict
from typing import Dict, List


def part_1(input: str) -> int:
    total = 0
    order, updates = input.split("\n\n")
    order_dict = defaultdict(list)
    for o in order.split("\n"):
        fst, lst = o.split("|")
        order_dict[int(lst)].append(int(fst))
    for u in updates.split("\n"):
        out_of_order = False
        for i, page in enumerate(u.split(",")):
            foll = map(int, u.split(",")[i + 1 :])
            must_prec = order_dict[int(page)]
            if any(i in must_prec for i in foll):
                out_of_order = True
                break
        if out_of_order:
            continue
        total += int(u.split(",")[len(u.split(",")) // 2])
    return total


def part_2(input: str) -> int:
    total = 0
    order, updates = input.split("\n\n")
    order_dict = defaultdict(list)
    for o in order.split("\n"):
        fst, lst = o.split("|")
        order_dict[int(lst)].append(int(fst))
    for u in updates.split("\n"):
        out_of_order = False
        for i, page in enumerate(u.split(",")):
            foll = map(int, u.split(",")[i + 1 :])
            must_prec = order_dict[int(page)]
            if any(i in must_prec for i in foll):
                out_of_order = True
                break
        if not out_of_order:
            continue
        fixed_order = fix_order([*map(int, u.split(","))], order_dict)
        total += fixed_order[len(fixed_order) // 2]
    return total


def fix_order(update: List[int], order_dict: Dict[int, List[int]]) -> List[int]:
    out_of_order = True
    while out_of_order:
        for i, page in enumerate(update):
            intersection = set(order_dict[page]) & set(update[i + 1 :])
            if intersection:
                update = (
                    update[:i]
                    + list(intersection)
                    + [page]
                    + [x for x in update[i + 1 :] if x not in intersection]
                )
                update = fix_order(update, order_dict)
                break
        out_of_order = False
    return update


if __name__ == "__main__":
    input_file = "./input.txt"
    with open(input_file) as f:
        input = f.read()

    print(part_1(input))
    print(part_2(input))
