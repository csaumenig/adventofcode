from __future__ import annotations
from collections import namedtuple
from operator import itemgetter

from models.grid import Grid

YEAR = 2024
DAY = 4


def read_file(file_name_str: str) -> Grid:
    with open(file_name_str, 'r') as f:
        lines = f.readlines()
        my_grid = Grid(len(lines), len(lines[0].strip()))
        my_grid.read_file(lines)

        # print(my_grid)
        return my_grid


def part1(file_name: str):
    grid: Grid = read_file(file_name)
    total = 0
    start_coords = grid.starters('X')
    while len(start_coords) > 0:
        coords = start_coords.pop(0)
        total += grid.num_words(coords, 'XMAS')
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {total}')


def part2(file_name: str):
    grid: Grid = read_file(file_name)
    total = 0
    start_coords = grid.starters('M')
    num_words_by_slant: dict[str, int] = {}
    while len(start_coords) > 0:
        coords = start_coords.pop(0)
        total += grid.num_words(coords, 'MAS')
        ns = grid.num_words_by_slant(coords, 'MAS')
        for k, v in ns.items():
            num_words_by_slant.update({k: num_words_by_slant.get(k, 0) + v})
    print(num_words_by_slant)
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {total}')


if __name__ == '__main__':
    part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
