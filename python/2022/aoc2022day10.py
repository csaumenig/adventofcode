from __future__ import annotations
import re

YEAR = 2022
DAY = 10


def part1(file_name: str):
    register: dict[int, tuple[str, int]] = {}
    cycle = 1
    x = 1
    total = 0
    indices = [20, 60, 100, 140, 180, 220]
    with open(file_name, 'r') as f:
        matches = re.findall(r'(noop|addx)(\s*-*\d+)*', f.read())
        for match in matches:
            command = match[0].strip()
            amount = None
            if len(match) == 2 and match[1].strip() != '':
                amount = int(match[1].strip())
            if command == 'noop':
                register.update({cycle: (command, x)})
            else:
                register.update({cycle: (f'addx({amount})', x)})
                cycle += 1
                x += amount
                register.update({cycle: (f'addx({amount})', x)})
            cycle += 1
    # print('{')
    # for key, value in register.items():
    #     print(f'  Cycle: {key:<4}Command: {value[0]:<10}Value: {value[1]}')
    # print('}')
    for index in indices:
        value = register.get(index - 1, None)
        if value:
            adjusted_value = value[1] * index
            print(f'The value at index [{index}] = {value} ({adjusted_value} adj.)')
            total += adjusted_value
    print(f'AOC {YEAR} Day {DAY} Part 1: {total}')


def part2(file_name: str):
    register: dict[int, tuple[str, int]] = {}
    cycle = 1
    x = 1
    sprite = (0, 1, 2)
    crt: list[str] = []
    with open(file_name, 'r') as f:
        matches = re.findall(r'(noop|addx)(\s*-*\d+)*', f.read())
        for match in matches:
            command = match[0].strip()
            amount = None
            if len(match) == 2 and match[1].strip() != '':
                amount = int(match[1].strip())
            if command == 'noop':
                if (cycle % 40) - 1 in sprite:
                    crt.append('#')
                else:
                    crt.append('.')
            else:
                if (cycle % 40) - 1 in sprite:
                    crt.append('#')
                else:
                    crt.append('.')
                cycle += 1
                if (cycle % 40) - 1 in sprite:
                    crt.append('#')
                else:
                    crt.append('.')
                x += amount
                sprite = (x - 1, x, x + 1)
            cycle += 1
    print(f'AOC {YEAR} Day {DAY} Part 2: CRT:')
    print(''.join(crt[0:39]))
    print(''.join(crt[40:79]))
    print(''.join(crt[80:119]))
    print(''.join(crt[120:159]))
    print(''.join(crt[160:199]))
    print(''.join(crt[200:239]))


if __name__ == '__main__':
    # part1(f'../../resources/{YEAR}/inputd{DAY}-b.txt')
    # part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}-b.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
