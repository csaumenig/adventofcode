from __future__ import annotations
import re

YEAR = 2024
DAY = 3

do_string = r"(?:do\(\))"
dont_string = r"(?:don't\(\))"
mul_string = r"mul\(([0-9]+),([0-9]+)\)"
do_pattern = re.compile(do_string)
dont_pattern = re.compile(dont_string)
mul_pattern = re.compile(mul_string)


def part1(file_name: str):
    total = 0
    with open(file_name, 'r') as f:
        data = f.read()
        mul_matches = mul_pattern.findall(data)
        total += sum([int(m[0]) * int(m[1]) for m in mul_matches])
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {total}')


def part2(file_name: str):
    total = 0
    enabled = True

    file_info: dict[int, tuple] = {}

    with open(file_name, 'r') as f:
        data = f.read()
        do_matches = do_pattern.finditer(data)
        for match in do_matches:
            file_info[match.start()] = ('O',)

        dont_matches = dont_pattern.finditer(data)
        for match in dont_matches:
            file_info[match.start()] = ('X',)

        mul_matches = mul_pattern.finditer(data)
        for match in mul_matches:
            file_info[match.start()] = ('M', int(match.group(1)), int(match.group(2)))

        ordered_keys = sorted(file_info.keys())

        for key in ordered_keys:
            value: tuple = file_info[key]
            if value[0] == 'X':
                enabled = False
            elif value[0] == 'O':
                enabled = True
            elif value[0] == 'M' and enabled:
                total += (value[1] * value[2])
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {total}')


if __name__ == '__main__':
    part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}-b.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
