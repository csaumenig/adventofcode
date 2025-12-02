from __future__ import annotations

from models.grid import Grid

YEAR = 2024
DAY = 4


class WordSearchGrid(Grid):
    def __init__(self,
                 rows: int,
                 cols: int) -> None:
        super().__init__(rows=rows, cols=cols)
        self._slant_midpoints: dict[tuple[int, int], int] = {}

    @property
    def midpoints(self) -> dict[tuple[int, int], int]:
        return self._slant_midpoints

    def starters(self,
                 start_letter: str) -> list[tuple[int, int]]:
        starters: list[tuple[int, int]] = []
        for k, v in self._dict.items():
            if v == start_letter:
                starters.append(k)
        return starters

    def num_words(self,
                  start: tuple[int, int],
                  match: str) -> int:
        total = 0
        row = start[0]
        col = start[1]
        word_length = len(match)
        valid = ['NW', 'N', 'NE', 'E', 'SE', 'S', 'SW', 'W']
        valid = [x for x in valid if self.validate(row, col, x, word_length)]
        if len(valid) > 0:
            for v in valid:
                word = ''
                if v == 'NW':
                    for z in range(word_length):
                        word += self._dict[(row - z, col - z)]
                elif v == 'N':
                    for z in range(word_length):
                        word += self._dict[(row - z, col)]
                elif v == 'NE':
                    for z in range(word_length):
                        word += self._dict[(row - z, col + z)]
                elif v == 'E':
                    for z in range(word_length):
                        word += self._dict[(row, col + z)]
                elif v == 'SE':
                    for z in range(word_length):
                        word += self._dict[(row + z, col + z)]
                elif v == 'S':
                    for z in range(word_length):
                        word += self._dict[(row + z, col)]
                elif v == 'SW':
                    for z in range(word_length):
                        word += self._dict[(row + z, col - z)]
                elif v == 'W':
                    for z in range(word_length):
                        word += self._dict[(row, col - z)]

                if word == match:
                    total += 1
        return total

    def num_words_by_slant(self,
                           start: tuple[int, int],
                           match: str) -> dict[str: int]:
        rd: dict[str: int] = {}
        row = start[0]
        col = start[1]
        word_length = len(match)
        valid = ['NW', 'NE', 'SE', 'SW',]
        valid = [x for x in valid if self.validate(row, col, x, word_length)]
        if len(valid) > 0:
            for v in valid:
                direction = 'P'
                midpoint: tuple[int, int] | None = None
                word = ''
                if v == 'NW':
                    for z in range(word_length):
                        word += self._dict[(row - z, col - z)]
                    direction = 'N'
                    midpoint = row - 1, col - 1
                elif v == 'NE':
                    for z in range(word_length):
                        word += self._dict[(row - z, col + z)]
                    direction = 'P'
                    midpoint = row - 1, col + 1
                elif v == 'SE':
                    for z in range(word_length):
                        word += self._dict[(row + z, col + z)]
                    direction = 'N'
                    midpoint = row + 1, col + 1
                elif v == 'SW':
                    for z in range(word_length):
                        word += self._dict[(row + z, col - z)]
                    direction = 'P'
                    midpoint = row + 1, col - 1
                if word == match:
                    self._slant_midpoints.update({midpoint: self._slant_midpoints.get(midpoint, 0) + 1})
                    rd.update({direction: rd.get(direction, 0) + 1})
        return rd

    def validate(self,
                 row: int,
                 col: int,
                 value: str,
                 word_length: int) -> bool:
        valid_col = True
        if col < word_length - 1 and 'W' in value:
            valid_col = False
        elif col > self.cols - word_length and 'E' in value:
            valid_col = False

        valid_row = True
        if row < word_length - 1 and 'N' in value:
            valid_row = False
        elif row > self.rows - word_length and 'S' in value:
            valid_row = False
        return valid_row and valid_col

    def __repr__(self) -> str:
        s = super().__repr__()
        if self._dict and len(self._dict) > 0:
            for k, v in self._slant_midpoints:
                s += f'{k}: {v}\n'
        return s

    def __str__(self) -> str:
        return self.__repr__()


def read_file(file_name_str: str) -> WordSearchGrid:
    with open(file_name_str, 'r') as f:
        lines = f.readlines()
        my_grid = WordSearchGrid(len(lines), len(lines[0].strip()))
        my_grid.read_file(lines)

        # print(my_grid)
        return my_grid


def part1(file_name: str):
    grid: WordSearchGrid = read_file(file_name)
    total = 0
    start_coords = grid.starters('X')
    while len(start_coords) > 0:
        coords = start_coords.pop(0)
        total += grid.num_words(coords, 'XMAS')
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {total}')


def part2(file_name: str):
    grid: WordSearchGrid = read_file(file_name)
    total = 0
    start_coords = grid.starters('M')
    while len(start_coords) > 0:
        coords = start_coords.pop(0)
        num_words_by_slant = grid.num_words_by_slant(coords, 'MAS')

    midpoints = grid.midpoints
    for k, v in midpoints.items():
        if v > 1:
            total += 1
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {total}')


if __name__ == '__main__':
    part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
