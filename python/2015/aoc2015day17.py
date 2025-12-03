from __future__ import annotations

YEAR = 2015
DAY = 17

def load_containers(file_name: str) -> list[int]:
    containers: list[int] = []
    with open(file_name, 'r') as f:
        for line in f.readlines():
            containers.append(int(line.strip()))
    return containers


def get_containers_by_total(my_list: list[int],
                            target: int) -> list[list[int]]:
    from itertools import combinations
    results: list[list[int]] = []
    for r in range(1, len(my_list) + 1):  # Iterate through combination lengths
        for combo in combinations(my_list, r):
            if sum(combo) == target:
                results.append(list(combo))
    return results


def part1(con_list: list[int],
          t: int) -> None:
    print(f'AOC {YEAR} Day {DAY} Part 1: Number of Combos: {len(get_containers_by_total(con_list, t))}')


def part2(con_list: list[int],
          t: int) -> None:
    c = get_containers_by_total(con_list, t)
    least = min([len(x) for x in c])
    total = len([x for x in c if len(x) == least])
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {total}')


if __name__ == '__main__':
    # c = load_containers(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # t = 25
    # part1(c, t)
    #
    # c = load_containers(f'../../resources/{YEAR}/inputd{DAY}.txt')
    # t = 150
    # part1(c, t)

    # c = load_containers(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # t = 25
    # part2(c, t)

    c = load_containers(f'../../resources/{YEAR}/inputd{DAY}.txt')
    t = 150
    part2(c, t)

