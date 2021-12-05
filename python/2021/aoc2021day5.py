def part1(input_str: str) -> None:
    grid: dict[tuple[int, int], int] = {}
    line_segs: list[str] = []
    line_format = '{}: {}'
    for line in input_str.split('\n'):
        points = line.split(' -> ')
        point1 = eval(points[0])
        point2 = eval(points[1])

        horiz, start, end = horizontal(point1, point2)
        if horiz:
            line_segs.append(line_format.format('h', line))
            for i in (start, end + 1):
                count(grid, (point1[0], i))
            continue

        vert, start, end = vertical(point1, point2)
        if vert:
            line_segs.append(line_format.format('v', line))
            for i in (start, end + 1):
                count(grid, (i, point1[0]))
            continue

    totals = 0
    for values in grid.values():
        if values >= 2:
            totals += 1

    print(f'Day 5 Part 1: More than two overlap: {totals}')


def horizontal(point1: tuple[int, int],
                point2: tuple[int, int]) -> tuple[bool, int, int]:
    if point1[1] == point2[1]:
        start = min(point1[0], point2[0])
        end = max(point1[0], point2[0])
        return True, start, end
    return False, 0, 0


def are_points_vertical(point1: tuple[int, int],
                        point2: tuple[int, int]) -> bool:
    if point1[0] == point2[0]:
        return True
    return False


if __name__ == '__main__':
    # with open('../../resources/2021/inputd5a.txt', 'r') as f:
    #     test_string = f.read()
    #     part1(test_string)

    with open('../../resources/2021/inputd5.txt', 'r') as f:
        test_input = f.read()
        part1(test_input)

