from __future__ import annotations

from models.direction import Direction, turn
from models.grid import Grid

YEAR = 2024
DAY = 6


class LabMap(Grid):
    def __init__(self,
                 rows: int,
                 cols: int) -> None:
        super().__init__(rows=rows, cols=cols)
        self._obstacles: list[tuple[int, int]] = []
        self._guard_pos: tuple[int, int] | None = None
        self._guard_direction: Direction = Direction.NORTH
        self._guard_spots: list[tuple[int, int]] = []

    @property
    def obstacles(self) -> list[tuple[int, int]]:
        return self._obstacles

    @property
    def guard_pos(self) -> tuple[int, int]:
        return self._guard_pos

    @property
    def guard_direction(self) -> Direction:
        return self._guard_direction

    @property
    def guard_spots(self) -> list[tuple[int, int]]:
        return self._guard_spots

    def read_file(self,
                  file_lines: list[str]) -> None:
        super().read_file(file_lines)
        self._init()

    def _init(self) -> None:
        for k, v in self._dict.items():
            if v == '#':
                self._obstacles.append(k)
            elif v == '^':
                self._guard_pos = k
                self._guard_spots.append(k)

    def patrol(self) -> None:
        in_map: bool = True

        while in_map:
            in_map = self.move()

    def move(self) -> bool:
        next_spot = None
        if self._guard_direction == Direction.NORTH:
            next_spot = (self._guard_pos[0] - 1, self._guard_pos[1])
        elif self._guard_direction == Direction.EAST:
            next_spot = (self._guard_pos[0], self._guard_pos[1] + 1)
        elif self._guard_direction == Direction.SOUTH:
            next_spot = (self._guard_pos[0] + 1, self._guard_pos[1])
        elif self._guard_direction == Direction.WEST:
            next_spot = (self._guard_pos[0], self._guard_pos[1] - 1)

        if next_spot[0] < 0 or next_spot[0] == self._rows or next_spot[1] < 0 or next_spot[1] == self._cols:
            return False
        elif next_spot in self._obstacles:
            self._guard_direction = turn(self._guard_direction, -90)
        else:
            self._guard_pos = next_spot
            if next_spot not in self._guard_spots:
                self._guard_spots.append(next_spot)
        return True


def read_file(file_name_str: str) -> LabMap:
    with open(file_name_str, 'r') as f:
        lines = f.readlines()
        my_grid = LabMap(len(lines), len(lines[0].strip()))
        my_grid.read_file(lines)

        # print(my_grid)
        return my_grid


def part1(file_name: str):
    lab_map: LabMap = read_file(file_name)
    lab_map.patrol()
    total = len(lab_map.guard_spots)
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {total}')


def part2(file_name: str):
    total = 0
    with open(file_name, 'r') as f:
        for line in f.readlines():
            print(line)
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {total}')


if __name__ == '__main__':
    part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
