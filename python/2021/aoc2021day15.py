from __future__ import annotations
from queue import PriorityQueue

YEAR = 2021
DAY = 15


class Graph:
    def __init__(self,
                 num_of_rows,
                 num_of_cols):
        self.rows = num_of_rows
        self.cols = num_of_cols
        self.grid = [[-1 for i in range(num_of_rows)] for j in range(num_of_cols)]
        self.visited = []
        self.neighbors: dict[tuple[int, int], list[tuple[int, int]]] = {}

    def add_risk(self, r, c, risk) -> None:
        self.grid[r][c] = risk
        self.add_neighbors(r, c)

    def add_neighbors(self, r, c) -> None:
        my_neighbors: list[tuple[int, int]] = []
        if r > 0:
            my_neighbors.append((r - 1, c))
        if r < self.rows:
            my_neighbors.append((r + 1, c))
        if c > 0:
            my_neighbors.append((r, c - 1))
        if c < self.cols:
            my_neighbors.append((r, c + 1))
        self.neighbors.update({(r, c): my_neighbors})

    def expand(self,
               num_times: int) -> None:
        pass




    @staticmethod
    def from_file(file: str) -> Graph:
        tmp_grid = read_file(file)
        rows = len(tmp_grid)
        columns = len(tmp_grid[0])
        graph = Graph(rows, columns)
        for row in range(rows):
            for column in range(columns):
                graph.add_risk(row, column, tmp_grid[row][column])
        return graph


def part1(f: str) -> None:
    graph = Graph.from_file(f)
    risk_dict = dijkstra(graph, (0, 0))
    print(f'Day {DAY} Part 1: Lowest Total Risk: {risk_dict.get((graph.rows - 1, graph.cols - 1))}')
    # print(risk_dict)


def part2(f: str) -> None:
    graph = Graph.from_file(f)



def dijkstra(graph: Graph,
             start: tuple[int, int]):
    risk_dict = {(row, column): float('inf') for row in range(graph.rows) for column in range(graph.cols)}
    risk_dict[start] = 0

    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        (distance, current_point) = pq.get()
        graph.visited.append(current_point)

        for x in range(graph.rows):
            for y in range(graph.cols):
                if (x, y) in graph.neighbors.get(current_point):
                    if (x, y) not in graph.visited:
                        risk = graph.grid[x][y]
                        old_risk = risk_dict.get((x, y))
                        new_risk = risk_dict.get(current_point) + risk
                        if new_risk < old_risk:
                            pq.put((new_risk, (x, y)))
                            risk_dict.update({(x, y): new_risk})
    return risk_dict


def read_file(file_name_str: str) -> list[list[int]]:
    grid: list[list[int]] = []
    lines = [line.strip() for line in open(file_name_str, 'r').readlines()]
    for line in lines:
        this_line = []
        for risk in line:
            this_line.append(int(risk))
        grid.append(this_line)
    return grid


if __name__ == '__main__':
    file_name = f'../../resources/{YEAR}/inputd{DAY}a.txt'
    part1(file_name)
    # part2(file_name)

    file_name_str = f'../../resources/{YEAR}/inputd{DAY}.txt'
    part1(file_name_str)
    # part2(file_name_str)
