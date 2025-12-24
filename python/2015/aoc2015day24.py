from __future__ import annotations
from math import prod

YEAR = 2015
DAY = 24

def find_shortest_subsets_with_combinations(arr: list[int],
                                            target: int) -> list[list[int]]:
    from itertools import combinations
    """
    Finds all subsets of a list that sum to a target number using itertools.
    """
    result = []
    found = False
    # Iterate through all possible subset lengths from 1 to the length of the list
    for i in range(1, len(arr) + 1):
        for subset in combinations(arr, i):
            if sum(subset) == target:
                found = True
                result.append(list(subset))
        if found:
            break
    return result

src_file = f'../../resources/{YEAR}/inputd{DAY}.txt'
with open(src_file, 'r') as f:
    packages = [int(l.strip()) for l in f.readlines()]

subs_3 = find_shortest_subsets_with_combinations(packages, sum(packages)//3)
smallest_qe_3 = min([prod(s) for s in subs_3])
print(f'Part One: {smallest_qe_3}')

subs_4 = find_shortest_subsets_with_combinations(packages, sum(packages)//4)
smallest_qe_4 = min([prod(s) for s in subs_4])
print(f'Part Two: {smallest_qe_4}')