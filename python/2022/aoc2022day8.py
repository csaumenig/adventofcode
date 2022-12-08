from __future__ import annotations
from enum import Enum

YEAR = 2022
DAY = 8


class LineType(Enum):
    ROW = 0
    COLUMN = 1


class Tree:
    def __init__(self,
                 row: int,
                 column: int,
                 height: int):
        self._row = row
        self._column = column
        self._height = height
        self._score = 0

    def row(self) -> int:
        return self._row

    def column(self) -> int:
        return self._column

    def height(self) -> int:
        return self._height

    def score(self) -> int:
        return self._score

    def set_score(self,
                  new_score: int) -> None:
        self._score = new_score

    def __repr__(self):
        return f'({self._row}, {self._column}) = {self._height} [{self._score}]'


def read_grid(file_name: str) -> tuple[list[Tree], int, int]:
    grid: list[Tree] = []
    row = 0
    with open(file_name, 'r') as f:
        lines = f.read()
        for line in lines.split('\n'):
            col = 0
            for value in line:
                grid.append(Tree(row, col, int(value)))
                col += 1
            row += 1
    return grid, row, col


def get_visible(line: list[Tree]) -> list[Tree]:
    visible: list[Tree] = []
    highest = None
    for tree in line:
        if highest is None or tree.height() > highest:
            visible.append(tree)
            highest = tree.height()
    line.reverse()
    highest = None
    for tree in line:
        if highest is None or tree.height() > highest:
            visible.append(tree)
            highest = tree.height()
    return visible


def retrieve_line(grid: list[Tree],
                  line_num: int,
                  line_type: LineType) -> list[Tree]:
    raw: list[Tree] = []
    for tree in grid:
        if line_type == LineType.ROW:
            if tree.row() == line_num:
                raw.append(tree)
        else:
            if tree.column() == line_num:
                raw.append(tree)
    if line_type == LineType.ROW:
        raw.sort(key=lambda a: a.column())
    else:
        raw.sort(key=lambda a: a.row())
    return raw


def calculate_scenic_score(tree: Tree,
                           grid: list[Tree]) -> None:
    if tree.row() == 0 or tree.column() == 0:
        tree.set_score(0)
        return

    row = retrieve_line(grid, tree.row(), LineType.ROW)
    if tree.row() == len(row)-1:
        tree.set_score(0)
        return

    column = retrieve_line(grid, tree.column(), LineType.COLUMN)
    if tree.column() == len(column) -1:
        tree.set_score(0)
        return

    row_score = calculate_score(tree, row)
    if row_score == 0:
        tree.set_score(0)
        return
    column_score = calculate_score(tree, column)
    if column_score == 0:
        tree.set_score(0)
        return
    tree.set_score(row_score * column_score)


def calculate_score(tree: Tree, line: list[Tree]) -> int:
    tree_index = line.index(tree)
    low_index = tree_index
    high_index = tree_index

    low_blocked = False
    high_blocked = False
    low_score = 0
    high_score = 0
    for index in range(1, len(line)-1):
        if low_blocked is False:
            low_index = low_index - 1
            if low_index < 0:
                low_blocked = True
            else:
                low_score += 1
                l_tree = line[low_index]
                if l_tree.height() >= tree.height():
                    low_blocked = True
        if high_blocked is False:
            high_index = high_index + 1
            if high_index >= len(line):
                high_blocked = True
            else:
                high_score += 1
                h_tree = line[high_index]
                if h_tree.height() >= tree.height():
                    high_blocked = True
        if low_blocked and high_blocked:
            break
    return low_score * high_score


def part1(file_name: str):
    grid, rows, cols = read_grid(file_name)
    visible: list[Tree] = []
    for r in range(rows):
        row = retrieve_line(grid, r, LineType.ROW)
        # row_output = '[' + ' '.join([str(x[2]) for x in row]) + ']'
        row.reverse()
        visible_row = get_visible(row)
        visible.extend(visible_row)
        # print(f'{row_output} has {len(visible_row)} visible trees.')
    for c in range(cols):
        column = retrieve_line(grid, c, LineType.COLUMN)
        # column_output = '[' + ' '.join([str(x[2]) for x in column]) + ']'
        column.reverse()
        visible_column = get_visible(column)
        visible.extend(visible_column)
        # print(f'{column_output} has {len(visible_column)} visible trees.')
    unique_visible = set(visible)
    # print(unique_visible)
    print(f'AOC {YEAR} Day {DAY} Part 1: {len(unique_visible)}')


def part2(file_name: str):
    grid, rows, cols = read_grid(file_name)
    scenic_score = None
    target_tree = None
    for tree in grid:
        calculate_scenic_score(tree, grid)
        if scenic_score is None or tree.score() > scenic_score:
            scenic_score = tree.score()
            target_tree = tree
    print_grid(grid, rows, cols)
    print(f'AOC {YEAR} Day {DAY} Part 2: Tree ({target_tree.row()}, {target_tree.column()}) = {scenic_score}')


def print_grid(grid: list[Tree],
               rows: int,
               cols: int) -> None:
    grid_dict = convert_list_to_dict(grid)
    for r in range(0, rows):
        row_line = ''
        for c in range(0, cols):
            my_tree = grid_dict.get((r, c))
            row_line += f'{my_tree.height()} [{my_tree.score()}]\t'
        print(row_line)


def convert_list_to_dict(grid: list[Tree]) -> dict[tuple[int, int], Tree]:
    grid_dict: dict[tuple[int, int], Tree] = {}
    for tree in grid:
        grid_dict.update({(tree.row(), tree.column()): tree})
    return grid_dict

if __name__ == '__main__':
    # part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt')