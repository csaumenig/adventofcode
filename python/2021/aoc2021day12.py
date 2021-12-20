from __future__ import annotations

YEAR = 2021
DAY = 12


class Cave:
    def __init__(self,
                 name: str,
                 big: bool):
        self._name = name
        self._big = big
        self._neighbors = []

    def add_neighbor(self,
                     cave: Cave):
        if cave not in self._neighbors:
            self._neighbors.append(cave)
        if self not in cave.neighbors:
            cave.add_neighbor(self)

    @property
    def name(self) -> str:
        return self._name

    @property
    def big(self) -> bool:
        return self._big

    @property
    def neighbors(self) -> list[Cave]:
        return self._neighbors


def part1(input_str: str) -> None:
    my_caves: dict[str, Cave] = {}
    for line in input_str.split('\n'):
        these_caves = line.split('-')
        cave0 = my_caves.get(these_caves[0], Cave(these_caves[0], these_caves[0].isupper()))
        cave1 = my_caves.get(these_caves[1], Cave(these_caves[1], these_caves[1].isupper()))
        cave0.add_neighbor(cave1)
        my_caves.update({these_caves[0]: cave0})
        my_caves.update({these_caves[1]: cave1})

    print(my_caves)
    paths: list[list[Cave]] = []
    print(f'Day {DAY} Part 1: ANSWER')


def part2(input_str: str) -> None:
    for line in input_str.split('\n'):
        print(line)
    print(f'Day {DAY} Part 2: ANSWER')


if __name__ == '__main__':
    with open(f'../../resources/{YEAR}/inputd{DAY}a.txt', 'r') as f:
        test_string = f.read()
        part1(test_string)
        part2(test_string)

    # with open(f'../../resources/{YEAR}/inputd{DAY}b.txt', 'r') as f:
    #     test_string = f.read()
    #     part1(test_string)
    #     part2(test_string)
    #
    # with open(f'../../resources/{YEAR}/inputd{DAY}c.txt', 'r') as f:
    #     test_string = f.read()
    #     part1(test_string)
    #     part2(test_string)
    #
    # with open(f'../../resources/{YEAR}/inputd{DAY}.txt', 'r') as f:
    #     test_string = f.read()
    #     part1(test_string)
    #     part2(test_string)
