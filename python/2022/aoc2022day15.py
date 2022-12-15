from __future__ import annotations
from dataclasses import dataclass
from functools import total_ordering

import re
YEAR = 2022
DAY = 15

verbose: bool
grid: dict


@dataclass
@total_ordering
class Point:
    x: int
    y: int

    def manhattan_range(self, other: Point):
        points = []
        distance = Point.manhattan(self, other)
        for x_coord in range(self.x - distance, (self.x + distance + 1)):
            for y_coord in range(self.y - distance, (self.y + distance + 1)):
                new_point = Point(x=x_coord, y=y_coord)
                if Point.manhattan(self, new_point) <= distance:
                    points.append(new_point)
        return points

    def move_x(self, increment: int):
        self.x += increment

    def move_y(self, increment: int):
        self.y += increment

    def new_copy(self):
        return Point(x=self.x, y=self.y)

    @staticmethod
    def manhattan(start: Point,
                  finish: Point):
        return abs(finish.x - start.x) + abs(finish.y - start.y)

    @staticmethod
    def is_valid_operand(other):
        return hasattr(other, "x") and hasattr(other, "y")

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        if not Point.is_valid_operand(other):
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)

    def __lt__(self, other):
        if not Point.is_valid_operand(other):
            return NotImplemented
        if self.y < other.y:
            return True
        if self.y == other.y:
            if self.x < other.x:
                return True
        return False

    def __hash__(self):
        return hash(f'x: {self.x}, y: {self.y}')


def part1(file_name: str, row_number: int):
    global verbose
    verbose = False
    with open(file_name, 'r') as f:
        data = f.read()
        parts = re.findall(r'Sensor at x=(-*\d+), y=(-*\d+): closest beacon is at x=(-*\d+), y=(-*\d+)', data)
        sensors = []
        beacons = []
        affected_points = []
        for pair in parts:
            sensor = Point(x=int(pair[0]), y=int(pair[1]))
            beacon = Point(x=int(pair[2]), y=int(pair[3]))
            sensors.append(sensor)
            beacons.append(beacons)
            manhattan_points = sensor.manhattan_range(beacon)
            affected_points.extend([point for point in manhattan_points if point.y == row_number])
        non_beacons = set()
        for point in affected_points:
            if point in beacons or point in sensors:
                print('No good')
            else:
                non_beacons.add(point)
    print(f'AOC {YEAR} Day {DAY} Part 1: Number of non beacon points in row {row_number} = {len(non_beacons)}')


def part2(file_name: str):
    print(f'AOC {YEAR} Day {DAY} Part 2:')


if __name__ == '__main__':
    part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt', 10)
    # part1(f'../../resources/{YEAR}/inputd{DAY}.txt', 20_000)
    # part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
