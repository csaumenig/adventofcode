from __future__ import annotations
from models.list_holder import ListHolder


YEAR = 2025
DAY = 10

ON = '#'
OFF = '.'


class Machine:
    def __init__(self,
                 running_state: str) -> None:
        self._running_state: str = running_state[1:-1]
        self._state: str = "".ljust(len(self._running_state), OFF)

    def __eq__(self, other) -> bool:
        if isinstance(other, Machine):
            return self.__key__() == other.__key__()
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.__key__())

    def __repr__(self) -> str:
        return (f'Machine({self.__hash__()}) [Current State: {self.current_state} Running State: {self._running_state}'
                f' Running: {self.running}]')

    def __str__(self) -> str:
        return self.__repr__()

    def __key__(self) -> tuple[str, str]:
        return self._state, self._running_state

    @property
    def current_state(self) -> str:
        return f'["".join(self._lights]'

    @property
    def running(self) -> bool:
        return self._state == self._running_state


class ButtonSchematic(ListHolder):
    def __init__(self,
                 item_list: str) -> None:
        super().__init__(item_list, int)


class JoltageRequirements(ListHolder):
    def __init__(self,
                 item_list: str) -> None:
        super().__init__(item_list, int)


def part1(file_name: str) -> None:
    total = 0
    with open(file_name, 'r') as f:
        for line in f.readlines():
            print(line)
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {total}')


def part2(file_name: str) -> None:
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
