from __future__ import annotations

from utils.util import dfs_start_end
YEAR = 2025
DAY = 11

def load_edges(file_name: str) -> dict[str, list[str]]:
    return_value: dict[str, list[str]] = {}
    with open(file_name, 'r') as f:
        for line in [l.strip() for l in f.readlines()]:
            key = line.split(': ')[0].strip()
            values = [v.strip() for v in line.split(': ')[1].strip().split(" ")]
            return_value[key] = values
    return return_value


def part1(edges: dict[str, list[str]]) -> None:
    paths = dfs_start_end(edges, [], [], start='you', end='out')
    from pprint import pprint
    pprint(paths)
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {len(paths)}')


def part2(edges: dict[str, list[str]],
          start: str,
          end: str,
          midpoint1: str,
          midpoint2: str) -> None:
    from utils.util import count_paths
    total = 0
    p1 = count_paths(edges, {}, start, midpoint1)
    p2 = count_paths(edges, {}, midpoint1, midpoint2)
    p3 = count_paths(edges, {}, midpoint2, end)
    total += p1 * p2 * p3
    p4 = count_paths(edges, {}, start, midpoint2)
    p5 = count_paths(edges, {}, midpoint2, midpoint1)
    p6 = count_paths(edges, {}, midpoint1, end)
    total += p4 * p5 * p6
    print(f'{start} => {end} passing through both {midpoint1} and {midpoint2} in {total} ways')

if __name__ == '__main__':
    e = load_edges(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    e1 = load_edges(f'../../resources/{YEAR}/inputd{DAY}.txt')
    e2 = load_edges(f'../../resources/{YEAR}/inputd{DAY}-b.txt')
    s = 'svr'
    t = 'out'
    mid1 = 'fft'
    mid2 = 'dac'
    part2(e2, s, t, mid1, mid2)
    part2(e1, s, t, mid1, mid2)
    # part2(e1)
