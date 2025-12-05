from __future__ import annotations
from models.grid import Grid

YEAR = 2025
DAY = 4


def step(grid: Grid) -> tuple[int, Grid]:
    new_grid = Grid.new_from_grid(grid)
    change: list[tuple[int, int]] = []
    for c in grid.cells_by_value('@'):
        rolls = len([x for x in grid.neighbors(c) if grid.value(x) == '@'])
        if rolls < 4:
            change.append(c)
    for c in change:
        new_grid.set_value(c, 'x')
    return len(change), new_grid

def part1(grid: Grid) -> None:
    total = 0
    for c in grid.cells_by_value('@'):
        rolls = len([x for x in grid.neighbors(c) if grid.value(x) == '@'])
        if rolls < 4:
            total += 1
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {total}')


def part2(grid: Grid) -> None:
    total = 0
    num, grid = step(grid)
    while num > 0:
        total += num
        num, grid = step(grid)
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {total}')


if __name__ == '__main__':
    g = Grid.new_from_file(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    g1 = Grid.new_from_file(f'../../resources/{YEAR}/inputd{DAY}.txt')
    # part1(g)
    # part1(g1)
    # part2(g)
    part2(g1)
