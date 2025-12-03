from __future__ import annotations
from models.grid import Grid

YEAR = 2015
DAY = 18

def step(grid: Grid) -> Grid:
    new_grid = Grid(grid.rows, grid.cols)
    for r in range(grid.rows):
        for c in range(grid.cols):
            p = (r, c)
            v = grid.value(p)
            nv = '.'
            ln = [x for x in grid.neighbors(p) if grid.value(x) == '#']

            if v == '#':
                if len(ln) in (2,3):
                    nv = '#'
            else:
                if len(ln) == 3:
                    nv = '#'
            new_grid.set_value(p, nv)
    return new_grid


def corners(grid: Grid) -> Grid:
    grid.set_value((0, 0), '#')
    grid.set_value((0, grid.cols - 1), '#')
    grid.set_value((grid.rows - 1, 0), '#')
    grid.set_value((grid.rows - 1, grid.cols - 1), '#')
    return grid

def step2(grid: Grid) -> Grid:
    return corners(step(grid))


def part1(grid: Grid,
          steps: int):
    for _ in range(steps):
        grid = step(grid)
    total = len(grid.cells_by_value('#'))
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {total}')


def part2(grid: Grid,
          steps: int):
    for _ in range(steps):
        grid = step2(grid)
    total = len(grid.cells_by_value('#'))
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {total}')


if __name__ == '__main__':
    g = Grid.new_from_file(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    g1 = Grid.new_from_file(f'../../resources/{YEAR}/inputd{DAY}.txt')

    s = 4
    s1 = 100
    # part1(g, s)
    # part1(g1, s1)

    g2 = corners(Grid.new_from_file(f'../../resources/{YEAR}/inputd{DAY}-a.txt'))
    s2 = 5
    # part2(g2, s2)

    g3 = corners(Grid.new_from_file(f'../../resources/{YEAR}/inputd{DAY}.txt'))
    s3 = 100
    part2(g3, s3)
