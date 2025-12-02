from __future__ import annotations
from typing import Optional
import functools
import re


YEAR = 2022
DAY = 9


@functools.total_ordering
class Knot:
    def __init__(self,
                 name: str,
                 x: int,
                 y: int,
                 tail: Optional[Knot]) -> None:
        self._name = name
        self._x = x
        self._y = y
        if tail:
            self._tail = tail
        else:
            self._tail = None

    def __repr__(self):
        return f'Name: {self._name} ({self._x}, {self._y})'

    def __eq__(self, other):
        if not Knot.is_valid_operand(other):
            return NotImplemented
        return (self._x, self._y) == (other.x(), other.y())

    def __lt__(self, other):
        if not Knot.is_valid_operand(other):
            return NotImplemented
        if self._y < other.y():
            return True
        if self._y == other.y():
            if self._x < other.x():
                return True
        return False

    def __hash__(self):
        return hash(f'name: {self._name}, x: {self._x}, y: {self._y}')

    def x(self):
        return self._x

    def y(self):
        return self._y

    def tail(self):
        return self._tail

    def has_tail(self) -> bool:
        return self._tail is not None

    def increment_x(self,
                    increment: int):
        self._x += increment

    def increment_y(self,
                    increment: int):
        self._y += increment

    def new_knot(self):
        return Knot(f'{self._name}_copy', self._x, self._y, None)

    def move(self,
             direction: str) -> None:
        if direction == 'R':
            self.increment_x(1)
        elif direction == 'L':
            self.increment_x(-1)
        elif direction == 'U':
            self.increment_y(1)
        elif direction == 'D':
            self.increment_y(-1)

    @staticmethod
    def is_valid_operand(other):
        return hasattr(other, "_x") and hasattr(other, "_y")


def touching(head: Knot,
             tail: Knot) -> bool:
    if (tail.x() - 1) <= head.x() <= (tail.x() + 1) and \
       (tail.y() - 1) <= head.y() <= (tail.y() + 1):
        return True
    return False


def move_tail(head: Knot,
              last_visited: list[Knot]) -> None:
    if head.has_tail():
        tail = head.tail()
        if touching(head, tail) is False:
            if head.x() == tail.x():
                if head.y() > tail.y():
                    tail.increment_y(1)
                else:
                    tail.increment_y(-1)
            elif head.y() == tail.y():
                if head.x() > tail.x():
                    tail.increment_x(1)
                else:
                    tail.increment_x(-1)
            else:
                if head.x() > tail.x():
                    tail.increment_x(1)
                else:
                    tail.increment_x(-1)
                if head.y() > tail.y():
                    tail.increment_y(1)
                else:
                    tail.increment_y(-1)
            move_tail(tail, last_visited)
    else:
        try:
            last_visited.index(head.new_knot())
        except ValueError:
            last_visited.append(head.new_knot())


def part1(file_name: str):
    tail = Knot('T1', 0, 0, None)
    head = Knot('H', 0, 0, tail)
    tail_visited: list[Knot] = [tail.new_knot()]
    with open(file_name, 'r') as f:
        matches = re.findall(r'([a-zA-Z])\s(\d+)', f.read())
        for match in matches:
            direction = match[0]
            amount = int(match[1])
            for i in range(amount):
                head.move(direction)
                move_tail(head, tail_visited)
    tail_visited.sort()
    print(f'AOC {YEAR} Day {DAY} Part 1: The tail visited {len(tail_visited)} spaces.')


def part2(file_name: str):
    head = Knot('H', 0, 0, Knot('T1', 0, 0, Knot('T2', 0, 0, Knot('T3', 0, 0, Knot('T4', 0, 0, Knot('T5', 0, 0, Knot('T6', 0, 0, Knot('T7', 0, 0, Knot('T8', 0, 0, Knot('T9', 0, 0, None))))))))))
    tail_visited: list[Knot] = [Knot('T9', 0, 0, None)]
    with open(file_name, 'r') as f:
        matches = re.findall(r'([a-zA-Z])\s(\d+)', f.read())
        for match in matches:
            direction = match[0]
            amount = int(match[1])
            for i in range(amount):
                head.move(direction)
                move_tail(head, tail_visited)
    tail_visited.sort()
    print(f'AOC {YEAR} Day {DAY} Part 2: The tail visited {len(tail_visited)} spaces.')


if __name__ == '__main__':
    # part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    #part2(f'../../resources/{YEAR}/inputd{DAY}-b.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
