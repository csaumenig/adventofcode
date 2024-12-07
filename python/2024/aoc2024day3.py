from __future__ import annotations
import re

YEAR = 2024
DAY = 3

do_string = r"(?:do\(\))"
dont_string = r"(?:don't\(\))"
mul_string = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"
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

    with open(file_name, 'r') as f:
        data = f.read()
        do_matches = do_pattern.finditer(data)
        dont_matches = dont_pattern.finditer(data)
        mul_matches = mul_pattern.finditer(data)

        switch_list: list[tuple[int, int, str]] = [(0, 0, 'y')]
        switch_list.extend([(d.start(), d.end(), 'y') for d in do_matches])
        switch_list.extend([(d.start(), d.end(), 'n') for d in dont_matches])
        boundary_list = sorted(switch_list, key=lambda x: x[0])
        segments: list[tuple[int, int]] = []
        start = -1
        start_found = False
        end = -1
        end_found = False
        for b in boundary_list:
            if b[2] == 'y':
                start = b[1]
                start_found = True
            elif b[2] == 'n' and b[0] >= start and start_found:
                end = b[0]
                end_found = True

            if start_found and end_found:
                segments.append((start, end))
                start = -1
                start_found = False
                end = -1
                end_found = False
        if start_found and not end_found:
            segments.append((start, len(data) - 1))

        # print(f'switch_list: {switch_list}')
        # print(f'boundary_list: {boundary_list}')
        print(f'segments: {segments}')
        for m in mul_matches:
            for s in segments:
                if m.start() >= s[0] and m.end() <= s[1]:
                    total += int(m.groups()[0]) * int(m.groups()[1])
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {total}')


if __name__ == '__main__':
    part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}-b.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
