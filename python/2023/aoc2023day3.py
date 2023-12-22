from __future__ import annotations
from collections import namedtuple

YEAR = 2023
DAY = 3

verbose: bool

GridCell = namedtuple('GridCell', 'row column')
GridNumber = namedtuple('GridNumber', 'cells')


class Grid:
    _grid_cells: dict[int, dict[int, any]] = { }
    _rows: int
    _cols: int
    _numbers: list[GridNumber]
    _sum: int
    _gears_to_check: set[GridCell]
    _gear_sum: int

    def __init__(self,
                 src_file_name: str) -> None:
        import re

        self._grid_cells = {}
        self._rows = 0
        self._cols = 0
        self._numbers = []
        self._sum = 0
        self._gears_to_check = set()
        self._gear_sum = 0

        number_pattern = re.compile(r'[0-9]+')
        gear_pattern = re.compile(r'\*')
        with open(src_file_name, 'r') as f:
            row_number = 0
            for line in f.readlines():
                row_number += 1
                col_number = 0
                this_row_dict: [int, any] = {}
                for character in line.strip():
                    col_number += 1
                    this_row_dict.update({col_number: character})
                self._grid_cells.update({row_number: this_row_dict})
                number_results = number_pattern.search(line)
                while number_results:
                    cells: list[GridCell] = []
                    n: int = number_results.start() + 1
                    while n <= number_results.end():
                        cells.append(GridCell(row_number, n))
                        n += 1
                    self._numbers.append(GridNumber(cells))
                    number_results = number_pattern.search(line, number_results.end() + 1)
                gear_results = gear_pattern.search(line)
                while gear_results:
                    self._gears_to_check.add(GridCell(row_number, gear_results.start() + 1))
                    gear_results = gear_pattern.search(line, gear_results.start() + 1)

        if self._grid_cells and len(self._grid_cells.keys()) > 0:
            self._rows = len(self._grid_cells.keys())
            self._cols = len(self._grid_cells.get(1).keys())

        for grid_number in self._numbers:
            include_in_sum: bool = False
            for cell in grid_number.cells:
                adjacent_cells: set[GridCell] = get_adjacent_cells(self, cell)
                for adj_cell in adjacent_cells:
                    cell_value: str = self.get_cell_value(adj_cell.row, adj_cell.column)
                    if not cell_value.isdigit() and cell_value != '.':
                        include_in_sum = True
                        break
                if include_in_sum:
                    break

            if include_in_sum:
                self._sum += grid_number_to_int(self, grid_number)

        for gear in self._gears_to_check:
            gear: GridCell
            adjacent_grid_numbers: list[GridNumber] = []
            adjacent_cells: set[GridCell] = get_adjacent_cells(self, gear)
            for grid_number in self.numbers:
                grid_number: GridNumber
                if len(adjacent_cells.intersection(grid_number.cells)) > 0:
                    adjacent_grid_numbers.append(grid_number)
            if len(adjacent_grid_numbers) == 2:
                self._gear_sum += grid_number_to_int(self, adjacent_grid_numbers[0]) * \
                                  grid_number_to_int(self, adjacent_grid_numbers[1])

    @property
    def cols(self):
        return self._cols

    @property
    def rows(self):
        return self._rows

    @property
    def numbers(self):
        return self._numbers

    @property
    def sum(self):
        return self._sum

    @property
    def gears_to_check(self):
        return self._gears_to_check

    @property
    def gear_sum(self):
        return self._gear_sum

    def get_row(self,
                r: int) -> dict[int, any]:
        return self._grid_cells.get(r)

    def get_cell_value_by_cell(self,
                               grid_cell: GridCell) -> any:
        return self._grid_cells.get(grid_cell.row).get(grid_cell.column)

    def get_cell_value(self,
                       r: int,
                       c: int) -> any:
        return self._grid_cells.get(r).get(c)

    def __repr__(self):
        return print_grid(self)

    def __str__(self):
        return self.__repr__()


def grid_number_to_int(grid: Grid,
                       grid_number: GridNumber) -> int:
    return int(''.join([grid.get_cell_value_by_cell(f) for f in grid_number.cells]))


def _spaces_needed(number_of_slots: int) -> int:
    start: int = 1
    spaces_needed: int = 0
    while number_of_slots >= start:
        spaces_needed += 1
        start = start * 10
    return spaces_needed


def print_grid(grid: Grid) -> str:
    print_lines = ''.rjust(_spaces_needed(grid.rows) + 3, ' ') + \
                  ''.join([str(x).rjust(_spaces_needed(grid.cols) + 1, ' ')
                           for x in range(1, grid.cols)]) + \
                  '\n'
    for r in range(1, grid.rows + 1):
        this_line_dict = grid.get_row(r)
        print_lines += f'[{str(r).rjust(_spaces_needed(grid.rows))}] ' + \
                       ''.join([str(this_line_dict.get(c)).rjust(_spaces_needed(grid.cols) + 1, ' ')
                                for c in range(1, grid.cols)]) + \
                       '\n'
    print_lines += '\n'
    print_lines += f'Grid Numbers: {[grid_number_to_int(grid, x) for x in grid.numbers]}\n'
    print_lines += f'Grid Gears: {grid.gears_to_check}\n'
    print_lines += f'Gear Ratio: {grid.gear_sum}'
    return print_lines


def get_adjacent_cells(grid: Grid,
                       grid_cell: GridCell) -> set[GridCell]:
    cells = set()
    start_row = grid_cell.row - 1
    if start_row < 1:
        start_row = grid_cell.row
    end_row = grid_cell.row + 1
    if end_row > grid.rows:
        end_row = grid_cell.row
    start_col = grid_cell.column - 1
    if start_col < 1:
        start_col = grid_cell.column
    end_col = grid_cell.column + 1
    if grid_cell.column + 1 > grid.cols:
        end_col = grid_cell.column

    for x in range(start_row, end_row + 1):
        for y in range(start_col, end_col + 1):
            if not (x == grid_cell.row and y == grid_cell.column):
                cells.add(GridCell(x, y))
    return cells


def part1(file_name: str):
    grid = Grid(file_name)
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {grid.sum}')


def part2(file_name: str):
    grid = Grid(file_name)
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {grid.gear_sum}')


if __name__ == '__main__':
    part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
