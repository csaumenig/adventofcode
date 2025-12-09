from __future__ import annotations
from models.grid import Point3D

YEAR = 2025
DAY = 8

def load_file(file_name: str) -> list[Point3D]:
    return_list: list[Point3D] = []
    with open(file_name, 'r') as f:
        for line in f.readlines():
            if line.strip() != '':
                l = [int(x) for x in line.split(',')]
                return_list.append(Point3D(l[0], l[1], l[2]))
    return return_list


def compute_distances(points: list[Point3D]) -> dict[tuple[Point3D, Point3D], float]:
    distances: dict[tuple[Point3D, Point3D], float] = {}
    for x in range(len(points)):
        p1 = points[x]
        for y in range(x + 1, len(points)):
            p2 = points[y]
            distances[(p1, p2)] = Point3D.straight_line_distance(p1, p2)
    return distances


def compute_circuits(distances: dict[tuple[Point3D, Point3D], float],
                     connect_total: int):
    circuits: list[set[Point3D]] = []
    connections = 0
    for k, v in sorted(distances.items(), key=lambda item: item[1]):
        connections += 1
        circuits = add_to_circuits(k, circuits)
        if connections == connect_total:
            break
    return circuits


def add_to_circuits(points: tuple[Point3D, Point3D],
                    circuits: list[set[Point3D]]) -> list[set[Point3D]]:
    added = False
    for c in circuits:
        if points[0] in c and points[1] in c:
            return circuits
        elif points[0] in c:
            c.add(points[1])
            added = True
        elif points[1] in c:
            c.add(points[0])
            added = True

    if not added:
        circuits.append({points[0], points[1]})

    #  Check to see if there are any intersections in our circuits list, if so, combine them
    cir_include = {}
    for x in range(len(circuits)):
        cir_include[x] = True
        found = False
        for y in range(len(circuits)):
            if x != y:
                if circuits[x].intersection(circuits[y]):
                    found = True
                    if circuits[x].issubset(circuits[y]):
                        cir_include[x] = False
                    else:
                        circuits[x] = circuits[x].union(circuits[y])
                        cir_include[x] = True
                        cir_include[y] = False
        if not found:
            cir_include[x] = True
    t = []
    for x in [k for k, v in cir_include.items() if v]:
        t.append(circuits[x])
    return t


def part1(distances: dict[tuple[Point3D, Point3D], float],
          connect_total: int,
          circuit_total: int) -> None:
    circuits: list[set[Point3D]] = compute_circuits(distances, connect_total)
    total = 0
    num = 0
    for circuit in sorted(circuits, key=lambda c: len(c), reverse=True):
        if num < circuit_total:
            if total == 0:
                total = len(circuit)
            else:
                total = total * len(circuit)
            num += 1
        else:
            break
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {total}')


def part2(distances: dict[tuple[Point3D, Point3D], float],
          num_points: int) -> None:
    circuits: list[set[Point3D]] = []
    total = 0
    connections = 0
    for k, v in sorted(distances.items(), key=lambda item: item[1]):
        connections += 1
        circuits = add_to_circuits(k, circuits)
        if len(circuits) == 1 and len(circuits[0]) == num_points:
            total += k[0].x * k[1].x
            break
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {total}')


if __name__ == '__main__':
    circuits_to_use = 3
    max_connections_1 = 10
    points_1 = load_file(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    distances_1 = compute_distances(points_1)
    max_connections_2 = 1000
    points_2 = load_file(f'../../resources/{YEAR}/inputd{DAY}.txt')
    distances_2 = compute_distances(points_2)

    part1(distances_1, max_connections_1, circuits_to_use)
    part1(distances_2, max_connections_2, circuits_to_use)
    part2(distances_1, len(points_1))
    part2(distances_2, len(points_2))
    # part2(points_2)