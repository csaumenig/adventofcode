from __future__ import annotations
import re
from utils.util import reduce_ranges

YEAR = 2025
DAY = 5
RANGE_REG_EX = r"(\d+)\-(\d+)"

def load(file_name: str) -> tuple[list[tuple[int, int]], list[int]]:
    ranges: list[tuple[int, int]] = []
    items: list[int] = []
    with open(file_name, 'r') as f:
        for l in f.readlines():
            line = l.strip()
            m = re.match(RANGE_REG_EX, line)
            if m:
                ranges.append((int(m.group(1)), int(m.group(2))))
            else:
                m1 = re.match(r"(\d+)", line)
                if m1:
                    items.append(int(m1.group(1)))
    return ranges, items


def part1(ranges: list[tuple[int, int]],
          items: list[int]) -> None:
    ranges = reduce_ranges(ranges)
    v = []
    for item in sorted(items):
        for ra in ranges:
            if ra[0] <= item <= ra[1]:
                v.append(item)
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {len(set(v))}')


def part2(ranges: list[tuple[int, int]]):
    reduced_ranges = reduce_ranges(ranges)
    print(f'AOC {YEAR} Day {DAY} Part 2: Number of Fresh IDs: {sum([(x[1]+1)-x[0] for x in reduced_ranges])}')


if __name__ == '__main__':
    r, i = load(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    r1, i1 = load(f'../../resources/{YEAR}/inputd{DAY}.txt')
    part1(r, i)
    part1(r1, i1)
    part2(r)
    part2(r1)