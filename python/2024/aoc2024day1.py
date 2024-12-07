from __future__ import annotations
from typing import Optional

YEAR = 2024
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
        left_nums = []
        right_nums = []
        for line in data:
            left_nums.append(int(line.split("   ")[0]))
            right_nums.append(int(line.split("   ")[1]))

        left_nums = sorted(left_nums)
        right_nums = sorted(right_nums)

        for pair in zip(left_nums, right_nums):
            total += abs(pair[0] - pair[1])
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {total}')


def part2(file_name: str):
    total = 0
    with open(file_name, 'r') as f:
        data = f.readlines()
        left_nums = []
        right_nums: dict[int, int] = {}
        for line in data:
            ln = int(line.split("   ")[0])
            rn = int(line.split("   ")[1])

            left_nums.append(ln)
            right_num_total = right_nums.get(rn, 0)
            right_nums.update({rn: right_num_total+1})
        for ln in left_nums:
            total += ln * right_nums.get(ln, 0)
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {total}')


if __name__ == '__main__':
    # part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}-b.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
