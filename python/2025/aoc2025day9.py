from __future__ import annotations
from models.grid import Point

YEAR = 2025
DAY = 9


def load_file(file_name: str) -> list[Point]:
    return_list: list[Point] = []
    with open(file_name, 'r') as f:
        for line in f.readlines():
            if line.strip() != '':
                l = [int(x) for x in line.split(',')]
                return_list.append(Point(l[0], l[1]))
    return return_list

def load_lines(points: list[Point]) -> list[tuple[Point, Point]]:
    return_value: list[tuple[Point, Point]] = []
    tmp = [p for p in points]
    tmp.append(tmp.pop(0))
    for m, n in zip(points, tmp):
        return_value.append((m, n))
    return return_value

def outside(point1: Point,
            point2: Point,
            min_point: Point,
            max_point: Point) -> bool:
    x = False
    y = False
    if (point1.x <= min_point.x and point2.x <= min_point.x) or (point1.x >= max_point.x and point2.x >= max_point.x):
        x = True
    if (point1.y <= min_point.y and point2.y <= min_point.y) or (point1.y >= max_point.y and point2.y >= max_point.y):
        y = True
    return x or y

def part1(points: list[Point]) -> None:
    total = 0
    area: dict[tuple[Point, Point], int] = {}
    for m in range(len(points)):
        for n in range(m + 1, len(points)):
            area[(points[m], points[n])] = (abs(points[m].x - points[n].x) + 1) * (abs(points[m].y - points[n].y) + 1)

    for k, v in sorted(area.items(), key=lambda item: item[1], reverse=True):
        total += v
        break
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {total}')


def part2(points: list[Point]) -> None:
    """
    Was stuck here for a while - looked at reddit and found this, which I ended up basing my answer on:
      https://www.reddit.com/r/adventofcode/comments/1phywvn/comment/nt6f5fa/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
    """
    total = 0
    area: dict[tuple[Point, Point], int] = {}
    lines = load_lines(points)

    for m in range(len(points)):
        for n in range(m + 1, len(points)):
            my_min = Point(min(points[m].x, points[n].x), min(points[m].y, points[n].y))
            my_max = Point(max(points[m].x, points[n].x), max(points[m].y, points[n].y))

            if all(outside(p1, p2, my_min, my_max) for p1, p2 in lines):
                area[(my_min, my_max)] = (abs(my_max.x - my_min.x) + 1) * (abs(my_max.y - my_min.y) + 1)

    for k, v in sorted(area.items(), key=lambda item: item[1], reverse=True):
        total += v
        break
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {total}')


if __name__ == '__main__':
    points1 = load_file(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part1(points1)
    part2(points1)

    points2 = load_file(f'../../resources/{YEAR}/inputd{DAY}.txt')
    part1(points2)
    part2(points2)

