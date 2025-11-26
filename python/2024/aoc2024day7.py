from __future__ import annotations

YEAR = 2024
DAY = 7


def read_line(line: str) -> tuple[int, list[int]]:
    split_line = line.strip().split(':')
    end_value = int(split_line[0])
    operands = [int(x) for x in split_line[1].strip().split(' ')]
    return end_value, operands


def operate(start: int,
            rest: list[int],
            concatenate: bool) -> list[int]:
    plus = start + rest[0]
    concat = None
    if concatenate:
        concat = eval(f'{start}{rest[0]}')
    mult = start * rest[0]

    if len(rest) == 1:
        if concatenate:
            return [plus, concat, mult]

        return [plus, mult]

    if concatenate:
        return operate(plus, rest[1:], concatenate) + operate(concat, rest[1:], concatenate) + operate(mult, rest[1:], concatenate)

    return operate(plus, rest[1:], concatenate) + operate(mult, rest[1:], concatenate)


def conc(x: int,
         y: int) -> int:
    return eval(f'{x}{y}')


def evaluate_line(line: str,
                  concatenate: bool) ->  tuple[bool, int]:
    end_value, operands = read_line(line)
    from functools import reduce
    from operator import add, mul

    if end_value == reduce(add, operands) or end_value == reduce(mul, operands):
        return True, end_value

    elif concatenate and end_value == reduce(conc, operands):
        return True, end_value

    else:
        results =  operate(operands[0], operands[1:], concatenate)
        if end_value in results:
            return True, end_value

    return False, end_value


def part1(file_name: str):
    total = 0
    with open(file_name, 'r') as f:
        for line in [x.strip() for x in f.readlines()]:
            r, t = evaluate_line(line, False)
            if r is True:
                total += t
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {total}')


def part2(file_name: str):
    total = 0
    with open(file_name, 'r') as f:
        for line in [x.strip() for x in f.readlines()]:
            r, t = evaluate_line(line, True)
            if r is True:
                total += t
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {total}')


if __name__ == '__main__':
    part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
