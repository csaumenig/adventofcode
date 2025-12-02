def part1(file_name_str: str) -> None:
    grid = read_file(file_name_str)
    low_spots = find_low_spots(grid)
    risk = sum([grid.get(x) + 1 for x in low_spots])
    print(f'Day 9 Part 1: Total Risk = {risk}')


def part2(file_name_str: str) -> None:
    grid = read_file(file_name_str)
    low_spots = find_low_spots(grid)
    basins: dict[int, int] = {}
    i = 0
    for spot in low_spots:
        this_basin = get_basin_neighbors(spot, grid, [])
        print(f'Basin {i}: {this_basin}')
        basins.update({i: len(this_basin)})
        i += 1
    i = 0
    target = 1
    for size in sorted(basins.values(), reverse=True):
        if i >= 3:
            break
        target = target * size
        i += 1
    print(f'Day 9 Part 2: Basin Score = {target}')


def read_file(file_name_str: str) -> dict[tuple[int, int], int]:
    grid: dict[tuple[int, int], int] = {}
    r = 0
    lines = [line.strip() for line in open(file_name_str, 'r').readlines()]
    for line in lines:
        c = 0
        for char in line:
            grid.update({(r, c): int(char)})
            c += 1
        r += 1
    return grid


def find_low_spots(grid: dict[tuple[int, int], int]) -> list[tuple[int, int]]:
    rows = max([point[0] for point in grid.keys()])
    cols = max([point[1] for point in grid.keys()])
    low_spots: list[tuple[int, int]] = []
    for row in range(0, rows + 1):
        for col in range(0, cols + 1):
            val = is_low_value(grid, row, col)
            if val > -1:
                low_spots.append((row, col))
    return low_spots


def is_low_value(source: dict[tuple[int, int], int],
                 r: int,
                 c: int) -> int:
    my_value = source.get((r, c))

    left = source.get((r, c-1))
    right = source.get((r, c+1))
    top = source.get((r-1, c))
    bottom = source.get((r+1, c))

    if left is not None and left < my_value:
        return -1
    if right is not None and right < my_value:
        return -1
    if top is not None and top < my_value:
        return -1
    if bottom is not None and bottom < my_value:
        return -1
    return my_value


def get_basin_neighbors(point: tuple[int, int],
                        grid: dict[tuple[int, int], int],
                        basin: list[tuple[int, int]]) -> set[tuple[int, int]]:
    if point not in basin:
        basin.append(point)
        top: tuple[int, int] = (point[0] - 1, point[1])
        if grid.get(top) is not None and grid.get(top) != 9:
            basin.extend(get_basin_neighbors(top, grid, basin))
        bottom: tuple[int, int] = (point[0] + 1, point[1])
        if grid.get(bottom) is not None and grid.get(bottom) != 9:
            basin.extend(get_basin_neighbors(bottom, grid, basin))
        left: tuple[int, int] = (point[0], point[1] - 1)
        if grid.get(left) is not None and grid.get(left) != 9:
            basin.extend(get_basin_neighbors(left, grid, basin))
        right: tuple[int, int] = (point[0], point[1] + 1)
        if grid.get(right) is not None and grid.get(right) != 9:
            basin.extend(get_basin_neighbors(right, grid, basin))
    return set(basin)


if __name__ == '__main__':
    file_name = '../../resources/2021/inputd9a.txt'
    part1(file_name)
    part2(file_name)

    file_name = '../../resources/2021/inputd9.txt'
    part1(file_name)
    part2(file_name)