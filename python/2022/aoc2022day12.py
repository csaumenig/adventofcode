from __future__ import annotations
from collections import defaultdict

import heapq as heap


YEAR = 2022
DAY = 12

squares = {}


def get_elevation(my_char):
    if my_char == 'S':
        return ord('a')
    elif my_char == 'E':
        return ord('z')
    return ord(my_char)


def load_squares(file_name: str):
    global squares
    squares = {}
    with open(file_name, 'r') as f:
        lines = f.readlines()
        row = len(lines) - 1
        col = 0
        for line in lines:
            for character in line.strip():
                squares.update({(col, row): character})
                col += 1
            col = 0
            row += -1


def load_grid_part_1():
    grid = {}
    start = None
    finish = None

    for point, elevation in squares.items():
        x_coord, y_coord = point
        if elevation == 'S':
            start = (point[0], point[1])
        elif elevation == 'E':
            finish = (point[0], point[1])
        my_elevation = get_elevation(elevation)

        accessible_neighbors = []
        up = squares.get((x_coord, y_coord + 1), None)
        if up and get_elevation(up) <= my_elevation + 1:
            accessible_neighbors.append((x_coord, y_coord + 1))
        down = squares.get((x_coord, y_coord - 1), None)
        if down and get_elevation(down) <= my_elevation + 1:
            accessible_neighbors.append((x_coord, y_coord - 1))
        right = squares.get((x_coord + 1, y_coord), None)
        if right and get_elevation(right) <= my_elevation + 1:
            accessible_neighbors.append((x_coord + 1, y_coord))
        left = squares.get((x_coord - 1, y_coord), None)
        if left and get_elevation(left) <= my_elevation + 1:
            accessible_neighbors.append((x_coord - 1, y_coord))
        grid.update({point: {accessible_neighbor: 1 for accessible_neighbor in accessible_neighbors}})
    return grid, start, finish


def load_grid_part_2():
    grid = {}
    start = None
    finish = []

    for point, elevation in squares.items():
        x_coord, y_coord = point
        if elevation == 'S' or elevation == 'a':
            finish.append((point[0], point[1]))
        elif elevation == 'E':
            start = (point[0], point[1])
        my_elevation = get_elevation(elevation)

        accessible_neighbors = []

        up = squares.get((x_coord, y_coord + 1), None)
        if up and get_elevation(up) >= my_elevation - 1:
            accessible_neighbors.append((x_coord, y_coord + 1))
        down = squares.get((x_coord, y_coord - 1), None)
        if down and get_elevation(down) >= my_elevation - 1:
            accessible_neighbors.append((x_coord, y_coord - 1))
        right = squares.get((x_coord + 1, y_coord), None)
        if right and get_elevation(right) >= my_elevation - 1:
            accessible_neighbors.append((x_coord + 1, y_coord))
        left = squares.get((x_coord - 1, y_coord), None)
        if left and get_elevation(left) >= my_elevation - 1:
            accessible_neighbors.append((x_coord - 1, y_coord))
        grid.update({point: {accessible_neighbor: 1 for accessible_neighbor in accessible_neighbors}})
    return grid, start, finish


def dijkstra(grid, start):
    visited = set()
    parents_map = {}
    pq = []
    node_costs = defaultdict(lambda: float('inf'))
    node_costs[start] = 0
    heap.heappush(pq, (0, start))
    while pq:
        # go greedily by always extending the shorter cost nodes first
        _, node = heap.heappop(pq)
        visited.add(node)

        for adj_node, weight in grid[node].items():
            if adj_node in visited:
                continue
            new_cost = node_costs[node] + weight
            if node_costs[adj_node] > new_cost:
                parents_map[adj_node] = node
                node_costs[adj_node] = new_cost
                heap.heappush(pq, (new_cost, adj_node))
    return parents_map


# def display_starting_grid():
#     cols = max([item[0] for item in squares.keys()]) + 1
#     rows = max([item[1] for item in squares.keys()])
#     row = rows
#     while row >= 0:
#         line = ''
#         for c in range(cols):
#             line += squares.get((c, row))
#         print(line)
#         row += -1


def generate_path(parents_map, start, finish):
    parent = parents_map.get(finish)
    if parent is None:
        return None
    path = [finish]
    while parent != start:
        path.append(parent)
        parent = parents_map.get(parent)
    path.reverse()
    return path


def part1(file_name: str):
    load_squares(file_name)
    grid, start, finish = load_grid_part_1()
    parents_map = dijkstra(grid, start)
    path = generate_path(parents_map, start, finish)
    print(f'AOC {YEAR} Day {DAY} Part 1: Number of moves = {len(path)}')
    # for c in range(0, 8):
    #     for r in range(4, -1, -1):
    #         neighbors = grid.get((c, r))
    #         res_int = sorted(neighbors.keys(), key=lambda x: x[0], reverse=True)
    #         res = sorted(res_int, key=lambda x: x[0])
    #         # print(f'{c}.{r} = {res}')
    # print('')
    # display_starting_grid()
    # display_path(parents_map)
    # print(parents_map)
     # display_solution(parents_map)


def part2(file_name: str):
    load_squares(file_name)
    grid, start, finish = load_grid_part_2()
    parents_map = dijkstra(grid, start)
    shortest_length = None
    for finish_pt in finish:
        path = generate_path(parents_map, start, finish_pt)
        print(f'Start: {start} Finish: {finish_pt}: {path}')
        if path:
            if shortest_length is None or len(path) < shortest_length:
                shortest_length = len(path)
    print(f'AOC {YEAR} Day {DAY} Part 2: Shortest path: {shortest_length}')


if __name__ == '__main__':
    # part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
