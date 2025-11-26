from __future__ import annotations

YEAR = 2024
DAY = 9


def translate_disk(raw_disk: str) -> list[str]:
    translated: list[str] = []
    file_id: int = 0
    is_byte: bool = True
    for rd in raw_disk:
        for i in range(0, int(rd)):
            if is_byte:
                translated.append(str(file_id))
            else:
                translated.append('.')
        if is_byte:
            file_id += 1
            is_byte = False
        else:
            is_byte = True
    return translated


def defrag_disk(translated_disk: list[str]) -> list[str]:
    for i in range(0, len(translated_disk)):
        if translated_disk[i] == '.':
            for j in range(1, len(translated_disk)-i):
                if translated_disk[-j] != '.':
                    translated_disk[i] = translated_disk[-j]
                    translated_disk[-j] = '.'
                    break
    return translated_disk


def checksum(defragged_disk: list[str]) -> int:
    checksum_int: int = 0
    for i in range(0, len(defragged_disk)):
        if defragged_disk[i] != '.':
            checksum_int += i * int(defragged_disk[i])
    return checksum_int


def part1(file_name: str):
    total = 0
    with open(file_name, 'r') as f:
        for line in f.readlines():
            translated = translate_disk(line.strip())
            # print(f'{line} => {translated}')
            defragged = defrag_disk(translated)
            # print(f'{translated} => {defragged}')
            total = checksum(defragged)
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {total}')


def part2(file_name: str):
    total = 0
    with open(file_name, 'r') as f:
        for line in f.readlines():
            print(line)
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {total}')


if __name__ == '__main__':
    # part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part1(f'../../resources/{YEAR}/inputd{DAY}-b.txt')
    # part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
    games = [1,2,3,4,5,6,7]
    cols = ['B','C','D','E','F']
    rows = [2,3,4,5,6,7,8,9,10,11,12,13]
    for r in rows:
        row_list = []
        for c in cols:
            g_list = []
            for g in games:
                g_list.append(f"'Game {g}'!{c}{r}")
            row_list.append(f"=SUM({','.join(g_list)})")
        print('\t'.join(row_list))