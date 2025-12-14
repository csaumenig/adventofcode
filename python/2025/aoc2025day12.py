from __future__ import annotations
import re
from collections import namedtuple

YEAR = 2025
DAY = 12

Present = namedtuple('Present', ['i', 'l'])
Tree = namedtuple('Tree', ['r', 'c', 'p'])

presents: list[Present] = []
trees: list[Tree] = []

pres_line_regex = r'^([\.\#]{3})$'
pres_num_regex = r'^(\d+)\:.*$'
tree_regex = r'^(\d+)x(\d+)\:\s(.*)$'

def present_by_id(i: int):
    return [p for p in presents if p.i == i][0]

def present_size(present: Present):
    return sum(sum([item != '.' for item in line]) for line in present.l)

def create_tree(m: re.Match) -> Tree:
    r = int(m.group(1))
    c = int(m.group(2))
    plist = [int(x) for x in str(m.group(3)).split(' ')]
    p: dict[int, int] = dict(enumerate(plist))
    return Tree(r, c, p)

def load_file(file_name: str):
    with open(file_name, "r") as file:
        present = False
        present_num = -1
        presents_done = False
        present_lines: list[list[str]] = []
        for line in [l.strip() for l in file.readlines()]:
            if not presents_done:
                if not present:
                    m = re.match(pres_num_regex, line)
                    if m:
                        present_num = int(m.group(1))
                        present = True

                    m = re.match(tree_regex, line)
                    if m:
                        presents_done = True
                        trees.append(create_tree(m))

                if present:
                    m = re.match(pres_line_regex, line)
                    if m:
                        present_lines.append(list(m.group(1).replace('#', str(present_num))))

                if line == '':
                    present = False
                    presents.append(Present(present_num, present_lines))
                    present_lines = []
            else:
                m = re.match(tree_regex, line)
                if m:
                    presents_done = True
                    trees.append(create_tree(m))


def part1() -> None:
    total = len(trees)
    for tree in trees:
        tree_presents = []
        size_of_presents = 0
        area = tree.r * tree.c
        for p, amt in tree.p.items():
            for _ in range(amt):
                present = present_by_id(p)
                tree_presents.append(present)
                size_of_presents += present_size(present)
        if area < size_of_presents:
            total -= 1
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {total}')


if __name__ == '__main__':
    load_file(f'../../resources/{YEAR}/inputd{DAY}.txt')
    part1()
