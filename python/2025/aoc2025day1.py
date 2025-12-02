from __future__ import annotations

YEAR = 2025
DAY = 1


def part1(file_name: str):
    total = 0
    pointer = 50
    with open(file_name, 'r') as f:
        for line in f.readlines():
            # L = -
            # R = +
            amount = int(line.strip()[1:])
            if line[0:1] == 'L':
                amount *= -1
            pointer += amount
            pointer = pointer % 100
            if pointer == 0:
                total += 1
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {total}')


def part2(file_name: str):
    from math import floor
    total = 0
    pointer = 50
    with open(file_name, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            amount = int(line[1:])
            direction = line[0:1]
            start = pointer
            zeros = 0
            if direction == 'L':
                amount *= -1
            pointer += amount
            if start > 0 >= pointer:
                zeros += 1
            elif start < 0 <= pointer:
                zeros += 1

            abs_val = abs(pointer)
            zeros += floor(abs_val/100)
            pointer_mod = pointer % 100
            total += zeros
            # print(f'Pointer: {pointer}, Pointer Mod: {pointer_mod}, Zeroes: {zeroes}, Total: {total}\n\n')
            pointer = pointer_mod
            print(f'Start: {start} [{line}] {pointer} -> Total: {total}')

    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {total}')


def part2a(file_name: str):
    total = 0
    pointer = 50
    with open(file_name, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            amount = int(line[1:])
            direction = line[0:1]
            for x in range(amount):
                if direction == 'L':
                    pointer -= 1
                    if pointer == 0:
                        pointer = 100
                        total += 1
                else:
                    pointer += 1
                    if pointer == 100:
                        pointer = 0
                        total += 1
            print(f'{line} -> Total: {total}')
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {total}')


if __name__ == '__main__':
    # part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
