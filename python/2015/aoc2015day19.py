from __future__ import annotations
from pprint import pprint

from utils.util import nth_string_replace

YEAR = 2015
DAY = 19


def load(file_name: str) -> tuple[list[tuple[str,str]], str]:
    import re
    pattern = r"([A-Za-z]+)\s\=\>\s([A-Za-z]+)|([A-Za-z]+)"
    repl: list[tuple[str,str]] = []
    molecule: str | None = None
    with open(file_name, 'r') as f:
        data = f.read().strip()
        for m in re.finditer(pattern, data):
            if m.group(1) and m.group(2):
                repl.append((m.group(1), m.group(2)))
            elif m.group(3):
                molecule = m.group(3)
    return repl, molecule


def step(replacements: list[tuple[str, str]],
         target: str,
         molecule: str) -> int:
     # Todo: Recursion


    new_molecule = molecule
    while new_molecule != target:
        for r in replacements:
            old, new = r
            start_index = 0
            n = 1

            while True:
                index = molecule.find(old, start_index)
                if index == -1:  # Substring not found
                    break
                new_molecule = nth_string_replace(molecule, old, new, steps)
                n += 1





    steps += 1
    for r in replacements:
        old, new = r
        start_index = 0
        n = 1

        while True:
            index = molecule.find(old, start_index)
            if index == -1:  # Substring not found
                break
            new_molecule = nth_string_replace(molecule, old, new, steps)
            n += 1
            if new_molecule == target:

            elif len(new_molecule) == len(target):
                return num_steps
            else:
                return step(replacements, target, new_molecule, steps)
            start_index = index + 1


    return steps



def part1(replacements: list[tuple[str,str]],
          molecule: str) -> None:
    new_molecules: list[str] = []
    for r in replacements:
        old, new = r
        start_index = 0
        n = 1
        while True:
            index = molecule.find(old, start_index)
            if index == -1:  # Substring not found
                break
            new_molecules.append(nth_string_replace(molecule, old, new, n))
            n += 1
            start_index = index + 1
    # pprint(new_molecules)
    nm_set = set(new_molecules)
    # pprint(nm_set)
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {len(nm_set)}')


def part2(replacements: list[tuple[str, str]],
          target: str) -> None:
    num_ways = step(replacements, target,'e')
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {min(num_ways)}')


if __name__ == '__main__':
    # t, m = load(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # t1, m1 = load(f'../../resources/{YEAR}/inputd{DAY}.txt')
    # pprint(t)
    # print(m)
    # part1(t, m)
    # part1(t1, m1)

    t2, m2 = load(f'../../resources/{YEAR}/inputd{DAY}-b.txt')
    part2(t2, m2)
    # part1(table1, molecule1)
