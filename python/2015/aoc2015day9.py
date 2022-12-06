YEAR = 2015
DAY = 9


def load_distances(file_name: str,
                   stops: set[str]) -> dict[str, dict[str: int]]:
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
    return distances


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


def part1(file_name: str):
    import json
    nodes: list[str]
    stops: set[str] = set()
    distances = load_distances(file_name, stops)
    nodes = sorted(stops)
    print(nodes)
    # print_distances(distances)
    # print_combination(nodes, 2)
    print_paths(nodes)


def part2(file_name: str):
    raw_len = 0
    enc_len = 0
    with open(file_name, 'r', encoding='utf-8') as text_file:
        lines = text_file.read()
        for line in lines.split('\n'):
            raw_len += len(line)
            enc_line = '"' + line.replace('\\', '\\\\').replace('"', '\\"') + '"'
            enc_len += len(enc_line)
            # print(f'Raw: {line}\tEncoded: {enc_line}')
    print(f'Raw Length: {raw_len}')
    print(f'Encoded Length: {enc_len}')
    print(f'AOC {YEAR} Day {DAY} Part 2: {enc_len - raw_len}')


def print_paths(nodes: list[str]):





    path = []
    for node in nodes:
        if node in path:
            continue
        else:
            path.append(node)
            for node1 in nodes:
                if node1 in path:
                    continue
                else:
                    path.append(node1)
                    for node2 in nodes:
                        if node2 in path:
                            continue
                        else:
                            path.append(node2)
                            for node3 in nodes:
                                if node3 in path:
                                    continue
                                else:
                                    path.append(node3)
                                    for node4 in nodes:
                                        if node4 in path:
                                            continue
                                        else:
                                            path.append(node4)
                                            for node5 in nodes:
                                                if node5 in path:
                                                    continue
                                                else:
                                                    path.append(node5)
                                                    for node6 in nodes:
                                                        if node6 in path:
                                                            continue
                                                        else:
                                                            path.append(node6)
                                                            for node7 in nodes:
                                                                if node7 in path:
                                                                    continue
                                                                else:
                                                                    path.append(node7)
                                                                    print('->'.join(path))


def recur(current: list[str],
          paths: list[list[str]],
          cities: list[str]):
    if len(current) == len(cities):
        paths.append(current)
        return

    for dest in cities:
        if dest in current:
            continue
        else:
            current.append(dest)
            recur(current, paths, cities)


def print_combination(cities: list[str],
                      combination_size: int):
    data = [0] * combination_size
    combination_util(cities, data, 0, len(cities) - 1, 0, combination_size)


def combination_util(cities: list[str],
                     data,
                     start: int,
                     end: int,
                     index: int,
                     combination_size: int):
    if index == combination_size:
        for j in range(combination_size):
            print(data[j], end=" ")
        print()
        return

    i = start
    while i <= end and end - i + 1 >= combination_size - index:
        data[index] = cities[i]
        combination_util(cities,
                         data,
                         i + 1,
                         end,
                         index + 1,
                         combination_size)
        i += 1


if __name__ == '__main__':
    part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
