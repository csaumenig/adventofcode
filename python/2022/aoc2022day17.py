from __future__ import annotations
from dataclasses import dataclass
from functools import total_ordering
import re

YEAR = 2022
DAY = 17

verbose: bool
grid: dict

pattern = ['-', '+', 'L', 'i', 'o']


def move_it(gust_pattern: str,
            goal: int):
    stopped_rocks = 0
    new_rock = True
    pattern_index = 0
    gust_pattern_index = 0
    current_level = 0
    starting_level = 0

    while stopped_rocks < goal:
        if new_rock:










def part1():
    global verbose
    verbose = False
    gusts = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
    move_it(gusts)


def part2(file_name: str):
        print(f'AOC {YEAR} Day {DAY} Part 2')


if __name__ == '__main__':
    part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt', 30)
    # part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
