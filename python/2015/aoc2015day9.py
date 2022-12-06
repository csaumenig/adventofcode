YEAR = 2015
DAY = 9


def load_distances(file_name: str,
                   stops: set[str]) -> tuple[dict[str, dict[str: int]], list[str], list[str]]:
    from itertools import permutations
    import re
    distances = {}
    with open(file_name, 'r', encoding='utf-8') as text_file:
        lines = text_file.read()
        pattern = r'([a-zA-Z]{1,})\sto\s([a-zA-Z]{1,})\s=\s([0-9]{1,})(\n|$)'
        matches = re.findall(pattern, lines)
        for match in matches:
            stops.add(match[0])
            stops.add(match[1])
            update_distances(distances, match[0], match[1], int(match[2]))

    nodes: list[str] = sorted(stops)
    paths: list[str] = list(permutations(nodes))
    return distances, nodes, paths


def update_distances(distances: dict[str, dict[str: int]],
                     node_1: str,
                     node_2: str,
                     distance: int) -> None:
    target = distances.get(node_1, {})
    target.update({node_2: distance})
    distances.update({node_1: target})
    target = distances.get(node_2, {})
    target.update({node_1: distance})
    distances.update({node_2: target})


def print_distances(distances: dict[str, dict[str: int]]) -> None:
    for start in [x for x in sorted(distances.keys())]:
        for end in [x for x in sorted(distances.get(start).keys())]:
            distance = distances.get(start).get(end)
            print(f'{start} -> {end} = {distance}')


def calc_distance(path: list[str],
                  distances: dict[str, dict[str: int]]) -> int:
    total = 0
    last = None
    for x in path:
        if last is not None:
            targets: dict[str: int] = distances.get(last)
            total += targets.get(x)
        last = x
    return total


def part1(file_name: str):
    nodes: list[str]
    stops: set[str] = set()
    distances, nodes, paths = load_distances(file_name, stops)

    short_path = None
    short_dist = None
    for path in paths:
        distance = calc_distance(list(path), distances)
        if short_dist is None or distance < short_dist:
            short_dist = distance
            short_path = path
    print(f'AOC {YEAR} Day {DAY} Part 1: {short_path} - {short_dist}')


def part2(file_name: str):
    nodes: list[str]
    stops: set[str] = set()
    distances, nodes, paths = load_distances(file_name, stops)

    long_path = None
    long_dist = None
    for path in paths:
        distance = calc_distance(list(path), distances)
        if long_dist is None or distance > long_dist:
            long_dist = distance
            long_path = path
    print(f'AOC {YEAR} Day {DAY} Part 2: {long_path} - {long_dist}')


if __name__ == '__main__':
    part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
