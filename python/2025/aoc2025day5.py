from __future__ import annotations

import sys

YEAR = 2025
DAY = 5

def load(file_name: str):
    fresh = []
    check = []
    top = True
    with open(file_name, 'r') as f:
        for l in f.readlines():
            line = l.strip()
            if line == '':
                top = False
                continue
            elif top:
                ends = line.split('-')
                fresh.append((int(ends[0]), int(ends[1])))
            else:
                check.append(int(line))
    return fresh, check

def part1(fresh: list,
          check: list) -> None:
    v = []
    for c in sorted(check):
        for r in fresh:
            if r[0] <= c <= r[1]:
                v.append(c)
    # print(set(v))
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {len(set(v))}')


def set_me(start, end):
    return set(list(range(start, end + 1)))


def part2(fresh: list) -> None:
    ranges = []
#     +++++++                 [RANGE from ranges list]
#   ====                      [FRESH Overlaps at low end - re write to FR[0] - (RA[0]-1)
#           -----             [FRESH Overlaps at high end - re write to (RA[1] + 1) - FR[1]
#       .....                 [FRESH Overlaps at in the middle - throw out
# ,,               ,,,        [FRESH Doesn't overlap at in the middle - keep
#  ********************       [Fresh Contains Range - throw out range
    total = 0
    for fr in fresh:
        if len(ranges) > 0:
            for ra in ranges:
                if fr[0] < ra[0] and ra[0] < fr[1] < ra[1]:
                    fr[1] = ra[0] - 1
                    ranges.append((fr[0], fr[1]))
                elif fr[0] < ra[1] and ra[0] < fr[1] < ra[1]:
                    fr[0] = ra[1] + 1
                    ranges.append((fr[0], fr[1]))
                elif ra[0] <= fr[0] <= fr[1] <= ra[1]:
                    print('Throw out')
                elif fr[0] <= fr[1] < ra[0] or ra[1] < fr[0] <= fr[1]:
                    ranges.append(fr)
                    print('Keepin it')
                elif fr[0] <= fr[1] <= ra[0] and ra[1] <= fr[0] <= fr[1]:
                    ranges.remove((ra[0], ra[1]))
                    ranges.append(fr)
        else:
            ranges.append(fr)

    for r in ranges:
        total += (r[1] - r[0])
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {total}')


if __name__ == '__main__':
    f, c = load(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part1(f, c)
    part2(f)
    f1, c1 = load(f'../../resources/{YEAR}/inputd{DAY}.txt')
    part1(f1, c1)
    part2(f1)
    # part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
