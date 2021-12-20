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

    def __repr__(self):
        return f'{self._name}'

    def __str__(self):
        return 'Cave [{}, {}]: {}'.format(self._name, 'Big' if self._big else 'Small', self._neighbors)

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
    my_caves: dict[str, Cave] = load_caves(input_str)
    paths = get_paths_1(caves=my_caves, start='start', end='end', path=None)
    print(f'Day {DAY} Part 1: Number of Paths {len(paths)}')


def part2(input_str: str) -> None:
    my_caves: dict[str, Cave] = load_caves(input_str)
    paths = get_paths_2(caves=my_caves, start='start', end='end', path=None)
    print(f'Day {DAY} Part 2: Number of Paths {len(paths)}')


def load_caves(input_str: str) -> dict[str, Cave]:
    caves: dict[str, Cave] = {}
    for line in input_str.split('\n'):
        these_caves = line.split('-')
        cave0 = caves.get(these_caves[0], Cave(these_caves[0], these_caves[0].isupper()))
        cave1 = caves.get(these_caves[1], Cave(these_caves[1], these_caves[1].isupper()))
        cave0.add_neighbor(cave1)
        caves.update({these_caves[0]: cave0})
        caves.update({these_caves[1]: cave1})
    return caves


def get_paths_1(caves: dict[str, Cave],
                start: str,
                end: str,
                path: list[Cave] = None) -> list[list[Cave]]:
    start_cave: Cave = caves.get(start)
    if path is None:
        path = []
    this_path = path + [start_cave]
    if start == end:
        return [this_path]
    paths: list[list[Cave]] = []
    for node in start_cave.neighbors:
        node: Cave
        if node not in this_path or node.big:
            new_paths = get_paths_1(caves, node.name, end, this_path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths


def get_paths_2(caves: dict[str, Cave],
                start: str,
                end: str,
                path: list[Cave] = None) -> list[list[Cave]]:
    start_cave: Cave = caves.get(start)
    if path is None:
        path = []
    this_path = path + [start_cave]
    if start == end:
        return [this_path]
    paths: list[list[Cave]] = []
    for node in start_cave.neighbors:
        node: Cave
        if node.name in ('start'):
            continue
        if node not in this_path:
            new_paths = get_paths_2(caves, node.name, end, this_path)
            if new_paths is not None:
                for new_path in new_paths:
                    paths.append(new_path)
        else:
            if node.big:
                new_paths = get_paths_2(caves, node.name, end, this_path)
                if new_paths is not None:
                    for new_path in new_paths:
                        paths.append(new_path)
            else:
                if can_visit(node=node.name, path=this_path):
                    new_paths = get_paths_2(caves, node.name, end, this_path)
                    if new_paths is not None:
                        for new_path in new_paths:
                            paths.append(new_path)
    return paths


def can_visit(node: str,
              path: list[Cave]) -> bool:
    if len(path) > 0:
        my_count: dict[str, int] = {}
        for node in filter(lambda x: x.big is False, path):
            my_count.update({node.name: my_count.get(node.name, 0) + 1})
        if my_count.get(node.name, 0) == 0:
            return True
        else:
            if max(my_count.values()) == 2:
                return False
    return True


if __name__ == '__main__':
    with open(f'../../resources/{YEAR}/inputd{DAY}a.txt', 'r') as f:
        test_string = f.read()
        part1(test_string)
        part2(test_string)

    with open(f'../../resources/{YEAR}/inputd{DAY}b.txt', 'r') as f:
        test_string = f.read()
        part1(test_string)
        part2(test_string)

    with open(f'../../resources/{YEAR}/inputd{DAY}c.txt', 'r') as f:
        test_string = f.read()
        part1(test_string)
        part2(test_string)

    with open(f'../../resources/{YEAR}/inputd{DAY}.txt', 'r') as f:
        test_string = f.read()
        part1(test_string)
        part2(test_string)
