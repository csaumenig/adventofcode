from __future__ import annotations
from dataclasses import dataclass
from functools import total_ordering
import re

YEAR = 2022
DAY = 20


def part1(file_name: str):
    verbose = False
    stuff = []
    with open(file_name, 'r') as f:
        lines = f.read()
        for line in lines.split('\n'):
            stuff.append([int(line.strip()), False])
        if verbose:
            print(f'Initial arrangement:\n{[x[0] for x in stuff]}\n')
        num_items = len(stuff)
        items_to_move = True
        while items_to_move is True:
            moved = False
            for i in range(0, num_items):
                item = stuff[i]
                value = item[0]
                item_moved = item[1]
                if item_moved is False:
                    item = stuff.pop(i)
                    spot = i + value
                    if spot < 0:
                        spot = (num_items - 1) + spot
                    elif spot == 0:
                        spot = num_items - 1
                    elif spot > num_items:
                        spot = spot + 1
                    new_index = spot % num_items
                    item[1] = True
                    stuff.insert(new_index, item)

                    if value == 0:
                        if verbose:
                            print('0 does not move:')
                    else:
                        if verbose:
                            print(f'{value} moves between {stuff[(new_index - 1) % num_items][0] } and {stuff[(new_index + 1) % num_items][0]}')
                    if verbose:
                        print(f'{[x[0] for x in stuff]}')
                    moved = True
                    break
            if moved is False:
                items_to_move = False
            else:
                if verbose:
                    print('')
        start = 0
        for i in range(0, num_items):
            if stuff[i][0] == 0:
                 start = i
                 break
        one_thousandth = stuff[(start + 1000) % num_items][0]
        two_thousandth = stuff[(start + 2000) % num_items][0]
        three_thousandth = stuff[(start + 3000) % num_items][0]
        code = one_thousandth + two_thousandth + three_thousandth
        print(f'AOC {YEAR} Day {DAY} Part 1: Code = {code}')


def part2(file_name: str):
        print(f'AOC {YEAR} Day {DAY} Part 2')


if __name__ == '__main__':
    part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
