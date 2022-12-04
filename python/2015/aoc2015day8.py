import re

from typing import Dict, List, Optional


def part1(file_name: str):
    import codecs

    raw_len = 0
    txt_len = 0
    line_num = 1
    with open(file_name, 'r', encoding='utf-8') as text_file:
        lines = text_file.read()
        for line in lines.split('\n'):
            new_text = line[1:-1]
            new_text = bytes(new_text, 'utf-8').decode('unicode_escape')
            raw_len += len(line)
            txt_len += len(new_text)
            print(f'Line[{line_num}]: {line}[{len(line)}] -> {new_text}[{len(new_text)}]')
            line_num += 1
    print(f'Raw Length: {raw_len}')
    print(f'Text Length: {txt_len}')
    print(f'AOC 2022 Day 8 Part 1: {raw_len - txt_len}')


def part2(file_name: str):
    elf_cals = {}
    cals = 0
    elf_num = 1
    with open(file_name, 'r') as f:
        lines = f.read()
        for line in lines.split('\n'):
            if line.strip() == '':
                elf_cals.update({elf_num: cals})
                elf_num += 1
                cals = 0
            else:
                cals += int(line)
    sorted_elf_cals = {k: v for k, v in sorted(elf_cals.items(), key=lambda item: item[1], reverse=True)}

    count = 1
    total = 0
    for k, v in sorted_elf_cals.items():
        if count > 3:
            break
        total += v
        count += 1
    print(f'AOC 2022 Day 1 Part 2: {total}')


if __name__ == '__main__':
    part1('../../resources/2015/inputd8-1.txt')
    part1('../../resources/2015/inputd8.txt')
    # part2('../../resources/2015/inputd8.txt')
