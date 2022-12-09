import functools
import re

YEAR = 2022
DAY = 9


@functools.total_ordering
class Point:
    def __init__(self,
                 x: int,
                 y: int):
        self._x = x
        self._y = y

    def x(self):
        return self._x

    def y(self):
        return self._y

    def increment_x(self,
                    increment: int):
        self._x += increment

    def increment_y(self,
                    increment: int):
        self._y += increment

    def __repr__(self):
        return f'({self._x}, {self._y})'

    def new_copy(self):
        return Point(self._x, self._y)

    def _is_valid_operand(self, other):
        return (hasattr(other, "_x") and
                hasattr(other, "_y"))

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return (self._x, self._y) == (other.x(), other.y())

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        if self._y < other.y():
            return True
        if self._y == other.y():
            if self._x < other.x():
                return True
        return False

    def __hash__(self):
        return hash(f'x: {self._x}, y: {self._y}')


def touching(head: Point,
             tail: Point) -> bool:
    if (tail.x() - 1) <= head.x() <= (tail.x() + 1) and \
       (tail.y() - 1) <= head.y() <= (tail.y() + 1):
        return True
    return False


def move_tail(head: Point,
              tail: Point) -> None:
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


def part1(file_name: str):
    head = Point(0, 0)
    tail = Point(0, 0)
    tail_visited: list[Point] = [tail.new_copy()]
    # print(f'Head: {head}\t\tTail: {tail}')
    with open(file_name, 'r') as f:
        matches = re.findall(r'([a-zA-Z])\s(\d+)', f.read())
        for match in matches:
            direction = match[0]
            amount = int(match[1])
            for i in range(amount):
                if direction == 'R':
                    head.increment_x(1)
                elif direction == 'L':
                    head.increment_x(-1)
                elif direction == 'U':
                    head.increment_y(1)
                elif direction == 'D':
                    head.increment_y(-1)
                if touching(head, tail) is False:
                    move_tail(head, tail)
                    try:
                        tail_visited.index(tail)
                    except ValueError:
                        tail_visited.append(tail.new_copy())
                # print(f'Head: {head}\t\tTail: {tail}')
    tail_visited.sort()
    print(f'AOC {YEAR} Day {DAY} Part 1:The tail visited {len(tail_visited)} spaces: ({tail_visited}) ')


def part2(file_name: str):
    head = Point(0, 0)
    tail = Point(0, 0)
    tail_visited: list[Point] = [tail.new_copy()]
    # print(f'Head: {head}\t\tTail: {tail}')
    with open(file_name, 'r') as f:
        matches = re.findall(r'([a-zA-Z])\s(\d+)', f.read())
        for match in matches:
            direction = match[0]
            amount = int(match[1])
            for i in range(amount):
                if direction == 'R':
                    head.increment_x(1)
                elif direction == 'L':
                    head.increment_x(-1)
                elif direction == 'U':
                    head.increment_y(1)
                elif direction == 'D':
                    head.increment_y(-1)
                if touching(head, tail) is False:
                    move_tail(head, tail)
                    try:
                        tail_visited.index(tail)
                    except ValueError:
                        tail_visited.append(tail.new_copy())
                # print(f'Head: {head}\t\tTail: {tail}')
    tail_visited.sort()
    print(f'AOC {YEAR} Day {DAY} Part 1:The tail visited {len(tail_visited)} spaces: ({tail_visited}) ')


if __name__ == '__main__':
    part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}.txt')\
