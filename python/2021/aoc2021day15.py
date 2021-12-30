import copy
import math
import types
from enum import Enum

YEAR = 2021
DAY = 15


class CellMark(Enum):
    No = 0
    Start = 1
    End = 2


class Cell:
    def __init__(self,
                 value: int,
                 pos: tuple[int, int] = None):
        self.count = 0
        self.value = value
        self.mark = CellMark.No
        self.pos = pos
        self.path_from = None


class CellGrid:
    def __init__(self, board):
        self.board = board
        self.rows = 0
        self.cols = 0
        for o in self.board:
            if o.pos[0] > self.cols:
                self.cols = o.pos[0]
            if o.pos[1] > self.rows:
                self.rows = o.pos[1]
        self.rows += 1
        self.cols += 1

    def at(self, pos: tuple[int, int]):
        for o in self.board:
            if o.pos == pos:
                return o

    def clone(self):
        return CellGrid(copy.deepcopy(self.board))

    def clear_count(self, count):
        for o in self.board:
            o.count = count
            o.path_from = None

    def is_valid_point(self,
                       pos: tuple[int, int]):
        return pos[0] in range(0, self.rows) and pos[1] in range(0, self.cols)

    def __repr__(self):
        output = ''
        for r in range(0, self.rows):
            line = ''
            if output.strip() != '':
                output += '\n'
            for c in range(0, self.cols):
                line += str(self.at((c, r)).value)
            output += line
        return output


def create_empty_map(x: int,
                     y: int,
                     start: tuple[int, int],
                     end: tuple[int, int]):
    return types.SimpleNamespace(
        board=CellGrid([[Cell(pos=(ix, iy), value=0) for iy in range(y)] for ix in range(x)]),
        start=start,
        end=end)


def create_map_from_grid(grid: dict[tuple[int, int], int],
                         start: tuple[int, int],
                         end: tuple[int, int]):
    return types.SimpleNamespace(
        board=CellGrid([Cell(pos=(k[1], k[0]), value=v) for k, v in grid.items()]),
        start=start,
        end=end)


def add_point(a: tuple[int, int],
              b: tuple[int, int]) -> tuple[int, int]:
    return a[0] + b[0], a[1] + b[1]


def find_least_risk_path(board: CellGrid,
                         start: tuple[int, int],
                         end: tuple[int, int],
                         max_distance=math.inf):
    nboard = board.clone()
    nboard.clear_count(math.inf)

    # mark the start and end for the UI
    nboard.at(start).mark = CellMark.Start
    nboard.at(end).mark = CellMark.End

    # we start here, thus a distance of 0
    open_list = [start]
    nboard.at(start).count = 0

    # (x,y) offsets from current cell
    neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while open_list:
        cur_pos = open_list.pop(0)
        cur_cell = nboard.at(cur_pos)

        for neighbour in neighbours:
            ncell_pos = add_point(cur_pos, neighbour)
            if not nboard.is_valid_point(ncell_pos):
                continue
            cell = nboard.at(ncell_pos)
            dist = cur_cell.count + 1
            if dist > max_distance:
                continue

            if cell.count > dist:
                cell.count = dist
                cell.path_from = cur_cell
                open_list.append(ncell_pos)
    return nboard


def backtrack_to_start(board: CellGrid,
                       end: tuple[int, int]):
    """
    Returns the path to the end, assuming the board has been filled in via fill_shortest_path
    """
    cell = board.at(end)
    path = []
    while cell is not None:
        path.append(cell)
        cell = cell.path_from
    return path


def part1(file_name_str: str) -> None:
    grid, rows, cols = read_file(file_name_str)
    start = (0, 0)
    end = (cols - 1, rows - 1)
    my_map = create_map_from_grid(grid, start, end)
    filled = find_least_risk_path(my_map.board, start, end)
    print(filled)
    print(f'Day {DAY} Part 1: ANSWER')


def part2(file_name_str: str) -> None:
    grid, rows, cols = read_file(file_name_str)
    print(f'Day {DAY} Part 2: ANSWER')


def read_file(file_name_str: str) -> tuple[dict[tuple[int, int], int], int, int]:
    grid: dict[tuple[int, int], int] = {}
    r = 0
    c = 0
    lines = [line.strip() for line in open(file_name_str, 'r').readlines()]
    for line in lines:
        c = 0
        for char in line:
            grid.update({(r, c): int(char)})
            c += 1
        r += 1
    return grid, r, c


if __name__ == '__main__':
    file_name = f'../../resources/{YEAR}/inputd{DAY}a.txt'
    part1(file_name)
    part2(file_name)

    # file_name = f'../../resources/{YEAR}/inputd{DAY}.txt'
    # part1(file_name)
    # part2(file_name)
