from __future__ import annotations
import re

YEAR = 2025
DAY = 2
RANGE_REGEX = r'(\d+)-(\d+)'
REPEAT_REGEX_TMPL_TWICE = r'(.{length})\1'
REPEAT_REGEX_TMPL_AT_LEAST_TWICE = r'(.{length})\1+'


def part1(file_name: str):
    total = 0
    with open(file_name, 'r') as f:
        for line in f.readlines():
            p = re.compile(RANGE_REGEX)
            matches = p.findall(line)
            for match in matches:
                half_length = 0
                p1 = None
                for i in range(int(match[0]), int(match[1]) + 1):
                    candidate = str(i)
                    if len(candidate) % 2 == 0:
                        candidate_half_length = len(candidate)//2
                        if candidate_half_length != half_length:
                            half_length = candidate_half_length
                            my_pattern = REPEAT_REGEX_TMPL_TWICE.replace('length', str(half_length))
                            p1 = re.compile(my_pattern)

                        if p1:
                            if p1.fullmatch(candidate):
                                print(candidate)
                                total += i

    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {total}')


def part2(file_name: str):
    from math import floor
    total = 0
    with open(file_name, 'r') as f:
        for line in f.readlines():
            p = re.compile(RANGE_REGEX)
            matches = p.findall(line)
            for match in matches:
                for i in range(int(match[0]), int(match[1]) + 1):
                    candidate = str(i)
                    candidate_half_length = floor(len(candidate)/2)
                    found = False
                    for j in range(1, candidate_half_length + 1):
                        if not found:
                            my_pattern = REPEAT_REGEX_TMPL_AT_LEAST_TWICE.replace('length', str(j))
                            p1 = re.compile(my_pattern)
                            if p1.fullmatch(candidate):
                                print(candidate)
                                total += i
                                found = True
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {total}')


if __name__ == '__main__':
    # part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
