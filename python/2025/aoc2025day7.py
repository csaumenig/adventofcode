from __future__ import annotations
from models.grid import Grid

YEAR = 2025
DAY = 7

BEAM = '|'
EMPTY = '.'
SPLITTER = '^'
START = 'S'
VISITED_SPLITTER = '*'

VALID = (BEAM, EMPTY)

class Manifold(Grid):
    def __init__(self,
                 grid: Grid) -> None:
        super().__init__(grid.rows, grid.cols)
        self._visited: dict[tuple[int, int], int] = {}
        for c in grid.cells():
            self.set_value(c[0], c[1])
            self._visited[c[0]] = 0
        self._start = None
        self._splitters = []
        self._beams = []

    @property
    def beams(self) -> list[tuple[int, int]]:
        return self.cells_by_value(BEAM)

    @property
    def endpoints(self) -> list[tuple[int, int]]:
        return self.cells_by_value_and_row(BEAM, self.rows-1)

    @property
    def splitters(self) -> list[tuple[int, int]]:
        return self._splitters

    @property
    def start(self) -> tuple[int, int]:
        return self._start

    @property
    def visited(self) -> dict[tuple[int, int], int]:
        return self._visited

    def cell_visits(self,
                    p: tuple[int, int]) -> int:
        return self._visited[p]

    def beams_by_row(self,
                     row: int) -> list[tuple[int, int]]:
        return [b for b in self.beams if b[0] == row]

    def flow(self) -> None:
        current_row = 0
        while current_row < self.rows:
            if current_row == 0:
                starters = [self.start]
                self._visited[self.start] = 1
            else:
                starters = self.beams_by_row(current_row)

            for starter in starters:
                below = (starter[0] + 1, starter[1])
                if self.value(below) == SPLITTER:
                    l_cell_col = below[1] - 1
                    r_cell_col = below[1] + 1

                    if l_cell_col >= 0:
                        below_left = (below[0], l_cell_col)
                        if self.value(below_left) in VALID:
                            self.set_value(below_left, BEAM)
                            self._visited[below_left] += self._visited[starter]
                    if r_cell_col < self.cols:
                        below_right = (below[0], r_cell_col)
                        if self.value(below_right) in VALID:
                            self.set_value(below_right, BEAM)
                            self._visited[below_right] += self._visited[starter]
                    self.set_value(below, VISITED_SPLITTER)
                elif self.value(below) in VALID:
                    self.set_value(below, BEAM)
                    self._visited[below] += self._visited[starter]
            current_row += 1

    def init_manifold(self) -> None:
        self._start = self.cell_by_value(START)
        self._splitters = self.cells_by_value(SPLITTER)

    @staticmethod
    def new_manifold_from_file(file_name: str) -> Manifold:
        nm = Manifold(Grid.new_from_file(file_name))
        nm.init_manifold()
        return nm


def part1(manifold: Manifold) -> None:
    manifold.flow()
    total = len(manifold.cells_by_value('*'))
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {total}')


def part2(manifold: Manifold) -> None:
    total = 0
    endpoints = manifold.endpoints
    for endpoint in endpoints:
        total += manifold.cell_visits(endpoint)
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {total}')


if __name__ == '__main__':
    m = Manifold.new_manifold_from_file(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    m1 = Manifold.new_manifold_from_file(f'../../resources/{YEAR}/inputd{DAY}.txt')
    part1(m)
    part1(m1)
    part2(m)
    part2(m1)
