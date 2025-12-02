
def part1(input_str: str) -> None:
    line_segs: list[list[tuple[int, int]]] = []

    for line in input_str.split('\n'):
        points = line.split(' -> ')
        point1 = eval(points[0])
        point2 = eval(points[1])

        horiz, start, end, y_value = horizontal(point1, point2)
        if horiz:
            segment: list[tuple[int, int]] = []
            for i in range(start, end + 1):
                segment.append((i, y_value))
            line_segs.append(segment)
            continue

        vert, start, end, x_value = vertical(point1, point2)
        if vert:
            segment: list[tuple[int, int]] = []
            for i in range(start, end + 1):
                segment.append((x_value, i))
            line_segs.append(segment)
            continue
    result = find_intersections(line_segs)
    print(f'Day 5 Part 1: Intersections: {len(result)}')


def part2(input_str: str) -> None:
    line_segs: list[list[tuple[int, int]]] = []

    for line in input_str.split('\n'):
        points = line.split(' -> ')
        point1 = eval(points[0])
        point2 = eval(points[1])

        point1, point2 = rearrange_points(point1, point2)


        horiz, start, end, y_value = horizontal(point1, point2)
        if horiz:
            segment: list[tuple[int, int]] = []
            for i in range(start, end + 1):
                segment.append((i, y_value))
            line_segs.append(segment)
            continue

        vert, start, end, x_value = vertical(point1, point2)
        if vert:
            segment: list[tuple[int, int]] = []
            for i in range(start, end + 1):
                segment.append((x_value, i))
            line_segs.append(segment)
            continue

        diag, slope, intercept = diagonal45(point1, point2)
        if diag:
            x = point1[0]
            y = point1[1]
            segment: list[tuple[int, int]] = [(x,y)]
            stop = False
            while stop is False:
                x += 1
                y += slope
                segment.append((x, y))
                if x == point2[0] and y == point2[1]:
                    stop = True
            line_segs.append(segment)
            continue
    result = find_intersections(line_segs)
    print(f'Day 5 Part 2: Intersections: {len(result)}')


def rearrange_points(point1: tuple[int, int],
                     point2: tuple[int, int]) -> tuple[tuple[int, int], tuple[int, int]]:
    if point1[0] > point2[0]:
        return (point2[0], point2[1]), (point1[0], point1[1])
    elif point1[0] == point2[0]:
        if point1[1] > point2[1]:
            return (point2[0], point2[1]), (point1[0], point1[1])
    return point1, point2


def horizontal(point1: tuple[int, int],
               point2: tuple[int, int]) -> tuple[bool, int, int, int]:
    if point1[1] == point2[1]:
        start = min(point1[0], point2[0])
        end = max(point1[0], point2[0])
        return True, start, end, point1[1]
    return False, 0, 0, 0


def vertical(point1: tuple[int, int],
             point2: tuple[int, int]) -> tuple[bool, int, int, int]:
    if point1[0] == point2[0]:
        start = min(point1[1], point2[1])
        end = max(point1[1], point2[1])
        return True, start, end, point1[0]
    return False, 0, 0, 0


def diagonal45(point1: tuple[int, int],
               point2: tuple[int, int]) -> tuple[bool, int, int]:
    # y = mx + b
    slope = int((point2[1] - point1[1])/(point2[0] - point1[0]))
    intercept = point1[1] - (slope * point1[0])
    return True, slope, intercept


def find_intersections(line_segments: list[list[tuple[int, int]]]) -> set[tuple[int, int]]:
    result = []
    for idx1 in range(0, len(line_segments)):
        s1 = set(line_segments[idx1])
        for idx2 in range(0, len(line_segments)):
            if idx2 == idx1:
                continue
            else:
                s2 = set(line_segments[idx2])
                s3 = s1.intersection(s2)
                result.extend(s3)
    return set(result)

if __name__ == '__main__':
    # with open('../../resources/2021/inputd5a.txt', 'r') as f:
    #     test_string = f.read()
    #     part1(test_string)
    #     part2(test_string)

    with open('../../resources/2021/inputd5.txt', 'r') as f:
        test_input = f.read()
        part1(test_input)
        part2(test_input)

