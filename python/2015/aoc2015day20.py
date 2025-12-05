from __future__ import annotations

from utils.util import factors

YEAR = 2015
DAY = 20


def part1(target: int) -> None:
    p = 0
    r = 1
    while p < target:
        p = sum([f * 10 for f in factors(r)])
        r += 1
    print(f'AOC {YEAR} Day {DAY} Part 1: First House: {r}')


def part2(target: int) -> None:
    p = 0
    r = 1
    valid_factors = []
    while p <= target:
        valid_factors = [f for f in factors(r) if r//f <= 50]
        p = sum([v1 * 11 for v1 in valid_factors])
        if r < 50:
            print(f'{r} => {p}')
        r += 1
    print(valid_factors)
    print(f'AOC {YEAR} Day {DAY} Part 1: First House: {r}')


if __name__ == '__main__':
    t = 36000000
    # part1(t)
    part2(t)
