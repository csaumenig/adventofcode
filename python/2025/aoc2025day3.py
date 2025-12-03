from __future__ import annotations

YEAR = 2025
DAY = 3


def part1(file_name: str):
    total = 0
    with open(file_name, 'r') as f:
        for line in f.readlines():
            bank = line.strip()
            first = max([int(x) for x in bank[0:-1]])
            pos = bank.find(str(first), 0)
            second = max([int(x) for x in bank[pos+1:]])
            print(f'{bank}')
            print(f'First: {first}, Pos: {pos}, Second: {second}')
            total += int(str(first) + str(second))
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {total}')


def part2(file_name: str):
    total = 0
    with open(file_name, 'r') as f:
        for line in f.readlines():
            bat = ''
            bank = line.strip()
            pos = 0
            r_pos = -11
            while len(bat) < 12:
                i = max([int(x) for x in bank[pos:r_pos]])
                pos = bank.find(str(i), pos) + 1
                if r_pos < -1:
                    r_pos += 1
                else:
                    r_pos = len(bank)
                bat += str(i)
            print(f'Battery: {bat}')
            total += int(bat)
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {total}')


if __name__ == '__main__':
    # part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
