from __future__ import annotations
from dataclasses import dataclass
from functools import total_ordering
import re

YEAR = 2022
DAY = 15

verbose: bool
grid: dict


def find_side_with_bounds(start: Point,
                          end: Point,
                          min_range: int,
                          max_range: int) -> set[Point]:
    slope = int((end.y - start.y)/(end.x - start.x))
    b = end.y - (slope * end.x)
    points = set()
    step = 1
    e_x = end.x + 1
    if start.x > end.x:
        step = -1
        e_x = end.x - 1

    for x in range(start.x, e_x, step):
        y = slope * x + b
        if (min_range <= x <= max_range) and (min_range <= y <= max_range):
            points.add(Point(x, y))
    return points


def find_side(start: Point,
              end: Point) -> set[Point]:
    slope = int((end.y - start.y)/(end.x - start.x))
    # y = mx + b -> b = y - mx
    b = end.y - (slope * end.x)
    line = set()
    step = 1
    s_x = start.x
    e_x = end.x + 1
    if start.x > end.x:
        e_x = end.x - 1
        step = -1

    for x in range(s_x, e_x, step):
        y = slope * x + b
        line.add(Point(x, y))
    return line

@dataclass
class Sensor:
    point: Point
    range: int

    def __init__(self,
                 point: Point,
                 beacon: Point,
                 min_range: int,
                 max_range: int):
        self.point = point
        self.range = Point.manhattan(self.point, beacon)
        self.points = self.points_to_check(min_range, max_range)

    def is_point_in_range(self,
                          point: Point):
        if Point.manhattan(self.point, point) <= self.range:
            return True
        return False

    def sides(self) -> list[set[Point]]:
        sides: list[set[Point]] = []
        corners = [Point(self.point.x, self.point.y + self.range),
                   Point(self.point.x + self.range, self.point.y),
                   Point(self.point.x, self.point.y - self.range),
                   Point(self.point.x - self.range, self.point.y)]
        sides.append(find_side(corners[0], corners[1]))
        sides.append(find_side(corners[1], corners[2]))
        sides.append(find_side(corners[2], corners[3]))
        sides.append(find_side(corners[3], corners[0]))
        return sides

    def points_to_check(self,
                        min_range: int,
                        max_range: int) -> set[Point]:
        points: set[Point] = set()
        corners = [Point(self.point.x, self.point.y + self.range + 1),
                   Point(self.point.x + self.range + 1, self.point.y),
                   Point(self.point.x, self.point.y - self.range - 1),
                   Point(self.point.x - self.range - 1, self.point.y)]
        points.update(find_side_with_bounds(corners[0], corners[1], min_range, max_range))
        points.update(find_side_with_bounds(corners[1], corners[2], min_range, max_range))
        points.update(find_side_with_bounds(corners[2], corners[3], min_range, max_range))
        points.update(find_side_with_bounds(corners[3], corners[0], min_range, max_range))
        return points


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

    def non_beacon_points(self, beacon: Point, row_number):
        points = []
        distance = Point.manhattan(self, beacon)
        if self.y - distance <= row_number <= self.y + distance + 1:
            for x_coord in range(self.x - distance, (self.x + distance + 1)):
                new_point = Point(x=x_coord, y=row_number)
                if new_point.__eq__(beacon) is False and Point.manhattan(self, new_point) <= distance:
                    points.append(new_point)
        return points

    def non_beacon_points_in_range(self, beacon: Point, min_range: int, max_range: int):
        points = set()
        distance = Point.manhattan(self, beacon)

        for y_coord in range(max(min_range, self.y - distance), min(max_range, self.y + distance) + 1):
            for x_coord in range(max(min_range, self.x - distance), min(max_range, self.x + distance) + 1):
                new_point = Point(x=x_coord, y=y_coord)
                if new_point.__eq__(beacon) is False and Point.manhattan(self, new_point) <= distance:
                    points.add(new_point)
        return points

    def all_manhattan_points(self, beacon: Point):
        points = set()
        distance = Point.manhattan(self, beacon)

        for y_coord in range(self.y - distance, self.y + distance + 1):
            for x_coord in range(self.x - distance, self.x + distance + 1):
                new_point = Point(x=x_coord, y=y_coord)
                if new_point.__eq__(beacon) is False and Point.manhattan(self, new_point) <= distance:
                    points.add(new_point)
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


def is_in_ranges(sensors: set,
                 point: Point):
    for sensor in sensors:
        if Point.manhattan(sensor, point) <= sensor.range:
            return True
    return False


def find_point(sensors, min_range, max_range):
    for x_coord in range(min_range, max_range + 1):
        for y_coord in range(min_range, max_range + 1):
            if is_in_ranges(sensors, Point(x_coord, y_coord)) is False:
                return Point(x_coord, y_coord)


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
            # sensors.append(sensor)
            # beacons.append(beacons)
            affected_points.extend([point for point in sensor.non_beacon_points(beacon, row_number)])
        non_beacons = set(affected_points)
        # for point in affected_points:
        #     if point in beacons or point in sensors:
        #         print('No good')
        #     else:
        #         non_beacons.add(point)
    print(f'AOC {YEAR} Day {DAY} Part 1: Number of non beacon points in row {row_number} = {len(non_beacons)}')


def part2(file_name: str, min_range: int, max_range: int):
    with open(file_name, 'r') as f:
        data = f.read()
        parts = re.findall(r'Sensor at x=(-*\d+), y=(-*\d+): closest beacon is at x=(-*\d+), y=(-*\d+)', data)
        sensors: list[Sensor] = []
        checkpoints: set[Point] = set()
        for pair in parts:
            sensor = Sensor(Point(x=int(pair[0]), y=int(pair[1])), Point(x=int(pair[2]), y=int(pair[3])), min_range, max_range)
            checkpoints.update(sensor.points)
            sensors.append(sensor)
        unvisited = checkpoints.copy()
        for point in checkpoints:
            for sensor in sensors:
                if sensor.is_point_in_range(point):
                    try:
                        unvisited.remove(point)
                    except KeyError:
                        # Nothing should happen here
                        false_flag = True

        if len(unvisited) == 1:
            point = unvisited.pop()
            total = (point.x * 4_000_000) + point.y
            print(f'AOC {YEAR} Day {DAY} Part 2: Point = {total}')


if __name__ == '__main__':
    # part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt', 10)
    # part1(f'../../resources/{YEAR}/inputd{DAY}.txt', 2_000_000)
    #part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt', 0, 20)
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt', 0, 4_000_000)
    # point = {}
    # part2a(Point(2889465, 3040754))
