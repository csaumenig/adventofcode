from __future__ import annotations
from functools import cmp_to_key
import json

YEAR = 2022
DAY = 13

verbose: bool


def compare_lists(left_list, right_list, index=0) -> int:
    prefix = ''
    if verbose:
        prefix = ''.join(['  ' for i in range(index)]) + '- '
        print(f'{prefix}Compare {left_list} and {right_list}')
    left_iter = iter(left_list)
    right_iter = iter(right_list)
    compare = 0
    keep_checking = True
    while keep_checking:
        try:
            left = next(left_iter)
        except StopIteration:
            left = None
        try:
            right = next(right_iter)
        except StopIteration:
            right = None

        if left is None and right is None:
            compare = 0
            keep_checking = False
        elif left is None and right is not None:
            compare = -1
            keep_checking = False
            if verbose:
                print(f'  {prefix}Left side ran out of items, so inputs are in the right order')
        elif left is not None and right is None:
            compare = 1
            keep_checking = False
            if verbose:
                print(f'  {prefix}Right side ran out of items, so inputs are not in the right order')
        else:
            compare = compare_list_items(left, right, index+1)
            if compare != 0:
                keep_checking = False
    return compare


def compare_list_items(left, right, index) -> int:
    prefix = ''
    if verbose:
        prefix = ''.join(['  ' for i in range(index)]) + '- '
        print(f'{prefix}Compare {left} and {right}')
    if type(left) == type(right):
        if isinstance(left, int):
            prefix = ''.join(['  ' for i in range(index + 1)]) + '- '
            if left < right:
                if verbose:
                    print(f'{prefix}Left side is smaller, so inputs are in the right order')
                return -1
            elif left > right:
                if verbose:
                    print(f'{prefix}Right side is smaller, so inputs are not in the right order')
                return 1
            return 0
        elif isinstance(left, list):
            return compare_lists(left, right, index+1)
        else:
            raise Exception
    else:
        if isinstance(left, int):
            left = [left]
        if isinstance(right, int):
            right = [right]
        return compare_lists(left, right, index+1)


def part1(file_name: str):
    global verbose
    verbose = False
    with open(file_name, 'r') as f:
        data = f.read()
        pairs_data = data.split('\n\n')
        index = 1
        total = 0
        for pair in pairs_data:
            lines = pair.splitlines()
            (left_side, right_side) = lines
            left_list = json.loads(left_side)
            right_list = json.loads(right_side)
            if verbose:
                print(f'== Pair {index} ==')
            if compare_lists(left_list, right_list, 0) < 0:
                total += index
                if verbose:
                    print(f' Running total: {total}')
            index += 1
    print(f'AOC {YEAR} Day {DAY} Part 1: {total}')


def part2(file_name: str):
    global verbose
    verbose = False
    with open(file_name, 'r') as f:
        data = f.read()
        lines = [json.loads(x) for x in data.split('\n') if x.strip() != '']
        lines.append(json.loads('[[2]]'))
        lines.append(json.loads('[[6]]'))
        newlines = sorted(lines, key=cmp_to_key(compare_lists))
        decode_key = (newlines.index(json.loads('[[2]]')) + 1) * (newlines.index(json.loads('[[6]]')) + 1)
    print(f'AOC {YEAR} Day {DAY} Part 2: {decode_key}')


if __name__ == '__main__':
    part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
