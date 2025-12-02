from __future__ import annotations
from pprint import pprint
import re

YEAR = 2015
DAY = 16
SUE_REGEX = r'^Sue\s(\d+).*$'
ATTRS_REGEX = r'([a-z]+)\:\s(\d+)'

def load_filter(file_name: str) -> dict[str, int]:
    filters: dict[str, int] = {}
    with open(file_name, 'r') as f:
        for line in f.readlines():
            k, v = line.strip().split(':')
            filters.update({k: int(v)})
    return filters

def load_sues(file_name: str) -> dict[int, dict[str, int]]:
    sues: dict[int, dict[str, int]] = {}
    with open(file_name, 'r') as f:
        for line in f.readlines():
            p = re.compile(SUE_REGEX)
            for m in p.findall(line.strip()):
                sue_no = int(m)

            attrs:[str, int] = {}
            for m1 in re.finditer(ATTRS_REGEX, line.strip()):
                attrs.update({m1.group(1): int(m1.group(2))})
            sues.update({sue_no: attrs})
    return sues

def part1(file_name: str,
          filters: dict[str, int]) -> None:
    sue = 0
    sues = load_sues(file_name)
    # pprint(sues)
    for k, v in sues.items():
        clean = True
        for attr, value in v.items():
            f_val = filters.get(attr, -1)
            if f_val != -1:
                if f_val != value:
                    clean = False
                    break

        if clean:
            sue = k
            break
    print(f'AOC {YEAR} Day {DAY} Part 1: Aunt Sue No: {sue}')


def part2(file_name: str,
          filters: dict[str, int]):
    sue = 0
    sues = load_sues(file_name)
    for k, v in sues.items():
        clean = True
        for attr, value in v.items():
            f_val = filters.get(attr, -1)
            if f_val != -1:
                if attr in ['cats', 'trees']:
                    if f_val >= value:
                        clean = False
                        break
                elif attr in ['pomeranians', 'goldfish']:
                    if f_val <= value:
                        clean = False
                        break
                else:
                    if f_val != value:
                        clean = False
                        break

        if clean:
            sue = k
            break
    print(f'AOC {YEAR} Day {DAY} Part 2: Aunt Sue No: {sue}')

if __name__ == '__main__':
    known: dict[str, int] = load_filter(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part1(f'../../resources/{YEAR}/inputd{DAY}.txt', known)
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt', known)

