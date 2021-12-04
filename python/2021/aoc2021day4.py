from __future__ import annotations


class Square:
    def __init__(self,
                 value: int):
        self._value: int = value
        self._selected: bool = False

    def select(self):
        self._selected = True

    @property
    def value(self) -> int:
        return self._value

    @property
    def selected(self) -> bool:
        return self._selected


class Board:
    def __init__(self):
        self._grid: [tuple[int, int], Square] = {}
        self._bingo = False

    def add_square(self,
                   row: int,
                   col: int,
                   square: Square):
        self._grid.update({(row, col): square})

    def check(self, called: int) -> bool:
        coords_found = ()
        for coords, square in self._grid.items():
            if square.value == called:
                square.select()
                self._grid.update({coords: square})
                coords_found = coords
        if len(coords_found) != 2:
            return False

        row = self.get_row(coords_found[0])
        self._bingo = True
        for s in row:
            if s.selected is False:
                self._bingo = False

        if self._bingo is False:
            col = self.get_col(coords_found[1])
            self._bingo = True
            for s in col:
                if s.selected is False:
                    self._bingo = False
        return self._bingo

    def bingo(self) -> bool:
        return self._bingo

    def get_row(self,
                row: int) -> list[Square]:
        this_row: list[Square] = []
        for k, v in self._grid.items():
            if k[0] == row:
                this_row.append(v)
        return this_row

    def get_col(self,
                col: int) -> list[Square]:
        this_col: list[Square] = []
        for k, v in self._grid.items():
            if k[1] == col:
                this_col.append(v)
        return this_col

    def bingo_sum(self):
        bingo_total = 0
        for k, v in self._grid.items():
            k: tuple[int, int]
            v: Square
            if v.selected is False:
                bingo_total += v.value
        return bingo_total

    @staticmethod
    def new_board(lines: list[str]) -> Board:
        board = Board()
        row = 1
        for line in lines:
            col = 1
            for value in line.split(' '):
                if value.strip() != '':
                    board.add_square(row, col, Square(int(value)))
                    col += 1
            row += 1
        return board


def part1(input_str: str) -> None:
    call_list = get_call_list(input_str)
    boards = get_boards(input_str)
    score = first_bingo(call_list, boards)
    print(f'Day 4 Part 1: First Winning Score = {score}')
    score = last_bingo(call_list, boards)
    print(f'Day 4 Part 2: Last Winning Score = {score}')


def get_call_list(input_str: str) -> list[int]:
    call_list: list[int] = []
    lines = input_str.split('\n')
    for x in lines[0].split(','):
        call_list.append(int(x))
    return call_list


def get_boards(input_str: str) -> list[Board]:
    boards: list[Board] = []
    lines = input_str.split('\n')

    board_list = []
    for i in range(1, len(lines)):
        if lines[i].strip() == '':
            if len(board_list) == 5:
                boards.append(Board.new_board(board_list))
            board_list = []
        else:
            board_list.append(lines[i])
    if len(board_list) == 5:
        boards.append(Board.new_board(board_list))
    return boards


def first_bingo(call_list: list[int],
                boards: list[Board]) -> int:
    bingo = False
    last_num = 0
    bingo_board = None
    for called in call_list:
        for board in boards:
            bingo = board.check(called)
            if bingo:
                bingo_board = board
                break
        if bingo:
            last_num = called
            break
    score = 0
    if bingo_board is not None and last_num > 0:
        bingo_total = bingo_board.bingo_sum()
        score = bingo_total * last_num
    return score


def last_bingo(call_list: list[int],
               boards: list[Board]) -> int:
    last_num = 0
    bingo_board = None

    no_bingo: list[Board] = [b for b in boards]
    for called in call_list:
        num_boards = len(no_bingo)
        if num_boards > 1:
            pop_list: list[int] = []
            for b_idx in range(0, num_boards):
                board = no_bingo[b_idx]
                bingo = board.check(called)
                if bingo:
                    pop_list.append(b_idx)
            for i in sorted(pop_list, reverse=True):
                no_bingo.pop(i)
        else:
            board = no_bingo[0]
            bingo = board.check(called)
            if bingo:
                bingo_board = board
                last_num = called
                break
    score = 0
    if bingo_board is not None and last_num > 0:
        bingo_total = bingo_board.bingo_sum()
        score = bingo_total * last_num
    return score


if __name__ == '__main__':
    with open('../resources/2021/inputd4a.txt', 'r') as f:
        test_string = f.read()
        part1(test_string)

    with open('../resources/2021/inputd4.txt', 'r') as f:
        test_input = f.read()
        part1(test_input)

