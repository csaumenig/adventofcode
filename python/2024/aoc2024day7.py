from __future__ import annotations
from random import randint
import re

from utils.util import dec_to_bin

YEAR = 2024
DAY = 7

OPS = ('+', '*')
eq_string = r"(\d+(\+|\*)\d+)"
eq_pattern = re.compile(eq_string)


def sort_operators(operators: list[str]) -> list[str]:
    if len(operators) < 2:
        return operators

    low, same, high = [], [], []

    pivot = operators[randint(0, len(operators) - 1)]
    number_of_pivot_mult = pivot.count('*')
    for item in operators:
        number_of_item_mult = item.count('*')
        if number_of_item_mult < number_of_pivot_mult:
            low.append(item)
        elif number_of_item_mult == number_of_pivot_mult:
            same.append(item)
        elif number_of_item_mult > number_of_pivot_mult:
            high.append(item)
    return sort_operators(low) + same + sort_operators(high)


def to_operator(bin_string: str) -> str:
    return ''.join([OPS[int(o)] for o in bin_string])


def evaluate_line(line: str) -> bool:
    split_line = line.strip().split(':')
    end_value = int(split_line[0])
    operands = [int(x) for x in split_line[1].strip().split(' ')]
    num_operators = len(operands) - 1
    num_values = 2**num_operators
    print(f'Number of Operators: {num_operators}')
    print(f'Number of Values: {num_values}')
    print(f'Target Value: {end_value}')
    operators = sort_operators([to_operator(dec_to_bin(x, len(operands)-1)) for x in range(num_values)])
    # print(operators)
    equation = '{}'.join([str(x) for x in operands])

    for operator in operators:
        this_equation = equation.format(*operator)
        new_equation = this_equation
        # print(this_equation)
        match = eq_pattern.match(new_equation)
        while match:
            mini = eval(match.string[match.start():match.end()])
            if mini > end_value:
                match = None
                new_equation = None
            else:
                new_equation = str(mini) + new_equation[match.end():]
                # print(this_equation)
                match = eq_pattern.match(new_equation)
        if new_equation is None:
            continue
        # print(f'{this_equation} = {new_equation}')
        if int(new_equation) == end_value:
            print(f'{this_equation} = {new_equation}')
            return True
        # this_value = eval(this_equation)
        # print(f'{this_equation} = {this_value}')

    # # print(equation)
    return False


def part1(file_name: str):
    total = 0
    with open(file_name, 'r') as f:
        for line in f.readlines():
            if evaluate_line(line):
                total += 1
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {total}')


def part2(file_name: str):
    total = 0
    with open(file_name, 'r') as f:
        for line in f.readlines():
            print(line)
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {total}')


if __name__ == '__main__':
    # part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
