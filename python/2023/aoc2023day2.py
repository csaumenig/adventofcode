from __future__ import annotations
from collections import namedtuple

YEAR = 2023
DAY = 2

verbose: bool
grid: dict


GameTry = namedtuple("GameTry", "b g r")


class Game:
    _number: int
    _tries: list[GameTry]

    def __init__(self,
                 number: int,
                 tries: list[GameTry]) -> None:
        self._number = number
        self._tries = tries

    @property
    def number(self):
        return self._number

    @property
    def tries(self):
        return self._tries

    def is_possible(self,
                    compare_game_try: GameTry) -> bool:
        for this_try in self._tries:
            if this_try.b > compare_game_try.b or this_try.g > compare_game_try.g or this_try.r > compare_game_try.r:
                return False
        return True

    def power(self) -> int:
        f = self.fewest()
        return f.b * f.g * f.r

    def fewest(self) -> GameTry:
        max_b = 0
        max_g = 0
        max_r = 0
        for this_try in self._tries:
            if this_try.b > max_b:
                max_b = this_try.b
            if this_try.g > max_g:
                max_g = this_try.g
            if this_try.r > max_r:
                max_r = this_try.r
        return GameTry(max_b, max_g, max_r)

    def __repr__(self):
        tries = ','.join([t.__repr__() for t in self._tries])
        return f'Game[{self._number}] Tries[{tries}]'

    def __str__(self):
        return self.__repr__()


def convert_line_to_game(input_line: str) -> Game:
    s = input_line.split(':')
    game_number = int(s[0][5:])

    try_list = s[1].split(';')
    game_tries: list[GameTry] = []
    for game_try in try_list:
        blue = 0
        green = 0
        red = 0
        for x in game_try.split(','):
            a_t = x.strip().split(' ')
            if a_t[1].lower() == 'blue':
                blue = int(a_t[0])
            elif a_t[1].lower() == 'green':
                green = int(a_t[0])
            elif a_t[1].lower() == 'red':
                red = int(a_t[0])
        game_tries.append(GameTry(blue, green, red))
    return Game(game_number, game_tries)


def part1(file_name: str):
    total = 0
    compare_try = GameTry(14, 13, 12)
    with open(file_name, 'r') as f:
        data = f.readlines()
        line_no = 1
        for line in data:
            this_game = convert_line_to_game(line)
            if not this_game:
                print(f'Unable to convert line [{line_no}]')
            else:
                if this_game.is_possible(compare_try):
                    total += this_game.number
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {total}')


def part2(file_name: str):
    total = 0
    with open(file_name, 'r') as f:
        data = f.readlines()
        line_no = 1
        for line in data:
            this_game = convert_line_to_game(line)
            if not this_game:
                print(f'Unable to convert line [{line_no}]')
            else:
                total += this_game.power()
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {total}')


if __name__ == '__main__':
    part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
