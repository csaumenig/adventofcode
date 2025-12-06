from __future__ import annotations
import operator
from functools import reduce

YEAR = 2025
DAY = 6

ops = {
    '+': operator.add,
    '*': operator.mul,
}

def do_math(i, j, op):
    return op(i, j)

def calc_nums(l: list[tuple]) -> int:
    op = None
    nums = []
    for line in reversed(l):
        nums.append(int(''.join(line[0:-1]).strip()))
        if not op and ops.get(line[-1]):
            op = ops.get(line[-1])
    return reduce(op, nums)

def part1(file_name: str) -> None:
    import re

    with open(file_name, 'r') as f:
        operators = []
        lines = []
        for line in f.readlines():
            x = re.split(r"\s+", line.strip())
            if x[0] in ops.keys():
                operators = x
            else:
                lines.append(x)
        totals = []
        for l in lines:
            if len(totals) == 0:
                totals = [int(x) for x in l]
            else:
                for i in range(len(operators)):
                    totals[i] = do_math(totals[i], int(l[i]), ops.get(operators[i]))
        total = sum(totals)
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {total}')


def part2(file_name: str) -> None:
    total = 0
    lines = []
    with open(file_name, 'r') as f:
        max_len = 0
        for line in f.readlines():
            line = line.replace('\n', '')
            max_len = max(max_len, len(line))
            lines.append(line)

    lines = [f"{line:<{max_len}}" for line in lines]
    nums = []
    for z in zip(*lines):
        if all(c == ' ' for c in z):
            total += calc_nums(nums)
            nums = []
        else:
            nums.append(z)
    total += calc_nums(nums)
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {total}')


if __name__ == '__main__':
    # part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
