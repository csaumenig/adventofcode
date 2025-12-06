from __future__ import annotations
from pprint import pprint
from wsgiref.validate import PartialIteratorWrapper

from utils.util import nth_string_replace

YEAR = 2015
DAY = 19


def load(file_name: str) -> tuple[list[tuple[str, str]], str]:
    import re
    pattern = r"([A-Za-z]+)\s\=\>\s([A-Za-z]+)|([A-Za-z]+)"
    repl: list[tuple[str, str]] = []
    molecule: str | None = None
    with open(file_name, 'r') as f:
        data = f.read().strip()
        for m in re.finditer(pattern, data):
            if m.group(1) and m.group(2):
                repl.append((m.group(1), m.group(2)))
            elif m.group(3):
                molecule = m.group(3)
    return repl, molecule


def num_atoms(target: str) -> int:
    import re
    my_reg_ex = r"([A-Z][a-z]?)"
    return len(re.findall(my_reg_ex, target))


def step(replacements: list[tuple[str, str]],
         molecule: str) -> list[str]:
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
    return list(set(new_molecules))


def next_step(replacements: list[tuple[str, str]],
              target: str,
              molecule: list[str],
              steps: int = 0) -> int:
    print(steps)

    if steps > num_atoms(target):
        return -1

    if target in molecule:
        return steps
    else:
        steps += 1
        nm = []
        for mol in molecule:
            nm.extend(step(replacements, mol))
    return next_step(replacements, target, list(set(nm)), steps)


def part1(replacements: list[tuple[str, str]],
          molecule: str) -> None:
    nm = step(replacements, molecule)
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {len(nm)}')


def part2a(replacements: list[tuple[str, str]],
           target: str) -> None:
    print(f'Target=> {num_atoms(target)}')
    print(f"AOC {YEAR} Day {DAY} Part 2: Total: {next_step(replacements, target, ['e'])}")

def backtrack(s, rep):
    import random
    count = 0
    old_s = ''
    keys = list(rep.keys())
    random.shuffle(keys)
    while old_s != s:
        old_s = s
        for key in keys:
            while key in s:
                count += s.count(key)
                s = s.replace(key, rep[key])
    return int(s == 'e') * count

def part2(file_name: str) -> None:
    """
    Borrowed from here: https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4jxdr/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
    """
    rep = {}
    inv_rep = {}
    s = ''
    with open(file_name) as f:
        for line in f.readlines():
            if '=>' in line:
                key, val = line.rstrip().split(' => ')
                inv_rep[val] = key
                if key not in rep:
                    rep[key] = []
                rep[key].append(val)
            else:
                s = line.rstrip()

    p2 = 0
    while p2 == 0:
        p2 = backtrack(s, inv_rep)
    print("Problem 2: %d" % p2)


if __name__ == '__main__':
    t, m = load(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    t1, m1 = load(f'../../resources/{YEAR}/inputd{DAY}.txt')
    t2, m2 = load(f'../../resources/{YEAR}/inputd{DAY}-b.txt')
    # part1(t, m)
    # part1(t1, m1)
    # part2(t2, m2)
    # part2(t1, m1)
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
