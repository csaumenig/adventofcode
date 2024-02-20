from __future__ import annotations
from collections import Counter

YEAR = 2023
DAY = 9


def read_file(file_name: str) -> list[list[int]]:
    return_list = []
    with open(file_name, 'r') as f:
        for line in f.readlines():
            return_list.append([int(x) for x in line.strip().split(" ")])
    return return_list


def create_diff_seq(start_list: list[int]) -> list[int]:
    return_list: list[int] = []
    i = 0
    while i < len(start_list) - 1:
        return_list.append(start_list[i+1]-start_list[i])
        i += 1
    return return_list


def extrapolate_sequences(start_list: list[list[int]]) -> list[list[list[int]]]:
    from copy import deepcopy
    return_list: list[list[list[int]]] = []
    for seq in start_list:
        this_seq = deepcopy(seq)
        my_sequence_extrapolation: list[list[int]] = []
        done = False
        while not done:
            my_sequence_extrapolation.append(this_seq)
            seq_count = Counter(this_seq)
            if len(seq_count.keys()) == 1 and seq_count.get(0):
                done = True
            else:
                this_seq = create_diff_seq(this_seq)
        return_list.append(my_sequence_extrapolation)
    return return_list


def part1(file_name: str):
    total = 0
    expanded_sequences = extrapolate_sequences(read_file(file_name))
    for seq in expanded_sequences:
        x = len(seq)
        last_item = 0
        while x - 2 >= 0:
            last_item += seq[x-2][-1]
            x -= 1
        total += last_item
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {total}')


def part2(file_name: str):
    total = 0
    expanded_sequences = extrapolate_sequences(read_file(file_name))
    for seq in expanded_sequences:
        x = len(seq) - 1
        last_item = 0
        while x >= 0:
            last_item = seq[x][0]- last_item
            x -= 1
        total += last_item
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {total}')


if __name__ == '__main__':
    # part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
