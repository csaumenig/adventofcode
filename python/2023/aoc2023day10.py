from __future__ import annotations
from collections import namedtuple
from typing import Optional

YEAR = 2023
DAY = 10

class Point:
    def __init__(self,
                 row: int,
                 col: int,
                 value: str):
        self._row = row
        self._col = col
        self._value = value

    def __repr__(self):
        return f'({self._row},{self._col}): {self._value}'

    def __str__(self):
        return self.__repr__()

    @property
    def row(self):
        return self._row

    @property
    def col(self):
        return self._col

    @property
    def value(self):
        return self._value

    def move(self,
             row_adj: int,
             col_adj: int,
             grid: list[list[str]]) -> Optional[Point]:
        if self.row + row_adj < 0 or self.row + row_adj >= len(grid):
            return None
        if self.col + col_adj < 0 or self.row + col_adj >= len(grid[0]):
            return None

        return Point(row=(self.row + row_adj),
                     col=(self.col + col_adj),
                     value=grid[(self.row + row_adj)][(self.col + col_adj)])


NORTH = [0, -1]
SOUTH = [0, 1]
EAST = [1, 0]
WEST = [-1, 0]

tiles = {
    '|': [NORTH, SOUTH],
    '-': [EAST, WEST],
    'L': [NORTH, EAST],
    'J': [NORTH, WEST],
    '7': [SOUTH, WEST],
    'F': [SOUTH, EAST],
    '.': [],
    'S': []
}


def read_grid(file_name: str) -> list[list[str]]:
    return_list: list[list[str]] = []
    with open(file_name, 'r') as f:
        for line in f.readlines():
            if line.strip() != '':
                return_list.append([*line.strip()])
    return return_list


def get_connected_tiles(point: Point,
                        grid: list[list[str]],
                        loop: dict[Point, int]):
    return_values: list[Point] = []
    new_point = move_point(point, NORTH, SOUTH, grid)
    if new_point and loop.get(new_point, -1) == -1:
        return_values.append(new_point)
    new_point = move_point(point, SOUTH, NORTH, grid)
    if new_point and loop.get(new_point, -1) == -1:
        return_values.append(new_point)
    new_point = move_point(point, EAST, WEST, grid)
    if new_point and loop.get(new_point, -1) == -1:
        return_values.append(new_point)
    new_point = move_point(point, WEST, EAST, grid)
    if new_point and loop.get(new_point, -1) == -1:
        return_values.append(new_point)
    return return_values


def move_point(point: Point,
               direction_to_move,
               direction_to_check,
               grid: list[list[str]]) -> Optional[Point]:
    new = point.move(direction_to_move[0], direction_to_move[1], grid)
    if new:
        if direction_to_check in tiles.get(new.value):
            return new
    return None


def part1(file_name: str):
    total = 0
    grid = read_grid(file_name)
    start = None
    row_idx = 0
    col_idx = 0
    while not start:
        if grid[row_idx][col_idx] == 'S':
            print(f'Start point is ({row_idx},{col_idx})')
            start = Point(row_idx, col_idx, grid[row_idx][col_idx])
        if col_idx + 1 == len(grid[row_idx]):
            col_idx = 0
            if row_idx + 1 == len(grid):
                print('No start found')
                start = Point(-1, -1, '')
            row_idx += 1
        else:
            col_idx += 1

    if start.value != '':
        moves = 0
        loop = {}
        connecting_tiles = [start]
        while len(set(connecting_tiles).intersection(set(loop.keys()))) == 0:

            loop = {
                start: moves
            }
        connecting_tiles = get_connected_tiles(start, grid, loop)

        while len(set(connecting_tiles).intersection(set(loop.keys()))) == 0:
            moves += 1
            for tile in connecting_tiles:
                loop.update({tile: moves})
        max_point = 0
        point = None
        for k, v in loop.items():
            if v > max_point:
                max_point = v
                point = k
                break
        print(f'{point} is furthest from {start} at {max_point} moves')
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {total}')


def part2(file_name: str):
    total = 0
    with open(file_name, 'r') as f:
        for line in f.readlines():
            print(line)
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {total}')


if __name__ == '__main__':
    part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
