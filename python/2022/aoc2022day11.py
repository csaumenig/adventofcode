from __future__ import annotations

from dataclasses import dataclass

import functools
import math
import operator
import re

YEAR = 2022
DAY = 11

OPERATOR_MAPPER = {
    '+': operator.add,
    '*': operator.mul
}

lcm = 0


@dataclass
class Monkey:
    items: list[int]
    operation: list[str]
    divisor: int
    true_id: int
    false_id: int
    inspections: int = 0

    @staticmethod
    def parse_number(s: str,
                     n: int) -> int:
        return n if s == 'old' else int(s)

    def apply_operation(self, old: int) -> int:
        n1 = self.parse_number(self.operation[0], old)
        n2 = self.parse_number(self.operation[2], old)
        return OPERATOR_MAPPER[self.operation[1]](n1, n2)


def load_monkeys(file_name: str) -> list[Monkey]:
    monkeys: list[Monkey] = []
    with open(file_name, 'r') as f:
        data = f.read()
        monkeys_data = data.split('\n\n')
        for monkey in monkeys_data:
            lines = monkey.splitlines()
            (_, items_l, operation_l, test_l, true_l, false_l) = lines
            items = [int(x.strip()) for x in re.findall(r'Starting\sitems:\s(.*)', items_l)[0].split(',')]
            operation = re.findall(r'Operation:\s[a-zA-Z]+\s=\s([a-zA-Z]+)\s([\+\*])\s(\d+|[a-zA-Z]+)', operation_l)[0]
            divisor = int(re.findall(r'Test:\s[a-zA-Z]+\sby\s(\d+)', test_l)[0])
            true_match = int(re.findall(r'If true:.*(\d+)', true_l)[0])
            false_match = int(re.findall(r'If false:.*(\d+)', false_l)[0])
            monkeys.append(Monkey(items, operation, divisor, true_match, false_match))
    print(f'Monkeys Post Load: {monkeys}')
    return monkeys


def inspect(monkeys: list[Monkey],
            worry_divisor: int):
    for monkey in monkeys:
        if monkey.items is not None:
            for item in monkey.items:
                monkey.inspections += 1
                inspected_value = math.floor(monkey.apply_operation(item) / worry_divisor)
                inspected_value = inspected_value % lcm
                to_monkey = monkey.true_id if inspected_value % monkey.divisor == 0 else monkey.false_id
                monkeys[to_monkey].items.append(inspected_value)
        monkey.items = []


def play_game(part_number: int,
              file_name: str,
              worry_divisor: int,
              rounds: int):
    monkeys: list[Monkey] = load_monkeys(file_name)
    global lcm
    lcm = functools.reduce(lambda cd, x: cd * x, (m.divisor for m in monkeys))
    for this_rd in range(rounds):
        inspect(monkeys, worry_divisor)
    top = 0
    second = 0
    for monkey in monkeys:
        if monkey.inspections > top:
            second = top
            top = monkey.inspections
            continue
        elif monkey.inspections > second:
            second = monkey.inspections
    answer = top * second
    print(f'AOC {YEAR} Day {DAY} Part {part_number}: {answer}')


def part1(file_name: str):
    play_game(1, file_name, 3, 20)


def part2(file_name: str):
    play_game(2, file_name, 1, 10_000)


if __name__ == '__main__':
    part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
