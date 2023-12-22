from __future__ import annotations
from typing import Optional

YEAR = 2023
DAY = 1

verbose: bool
grid: dict
NAME_PATTERN = 'one|two|three|four|five|six|seven|eight|nine'
NUMBER_PATTERN = '1|2|3|4|5|6|7|8|9'

DIGIT_MAP: dict[str, int] = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def find_integer(input_line: str,
                 pattern_string: str) -> Optional[int]:
    import re
    pattern = re.compile(pattern_string)
    results = pattern.search(input_line)
    if results:
        first = None
        last = None
        while results:
            if not first:
                first = input_line[results.start(): results.end()]
            else:
                last = input_line[results.start(): results.end()]
            results = pattern.search(input_line, results.start() + 1)

        if not last:
            last = first
        first_value = first
        last_value = last
        if DIGIT_MAP.get(first):
            first_value = DIGIT_MAP.get(first)
        if DIGIT_MAP.get(last):
            last_value = DIGIT_MAP.get(last)
        return int(f'{first_value}{last_value}')
    return None


def part1(file_name: str):
    total = 0
    with open(file_name, 'r') as f:
        data = f.readlines()
        line_no = 1
        for line in data:
            two_digit_number = find_integer(line, f'({NUMBER_PATTERN})')
            if two_digit_number:
                total += two_digit_number
            else:
                print(f'No integer found on line[{line_no}]')
        line_no += 1
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {total}')


def part2(file_name: str):
    total = 0
    with open(file_name, 'r') as f:
        data = f.readlines()
        line_no = 1
        for line in data:
            two_digit_number = find_integer(line, f'({NUMBER_PATTERN}|{NAME_PATTERN})')
            if two_digit_number:
                total += two_digit_number
            else:
                print(f'No integer found on line[{line_no}]')
        line_no += 1
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {total}')


if __name__ == '__main__':
    part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}-b.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
