from __future__ import annotations

YEAR = 2022
DAY = 14

verbose: bool
grid: dict


def set_up_grid(file_name: str):
    global grid
    grid = {}
    with open(file_name, 'r') as f:
        data = f.read()
        for line in [x.strip() for x in data.split('\n') if x.strip() != '']:
            points = line.split(' -> ')
            start = None
            end = None
            for x_coord, y_coord in [point.split(',') for point in points]:
                this_point = (int(x_coord), int(y_coord))
                if start is None:
                    start = this_point
                elif end is None:
                    end = this_point
                    add_line_to_grid(start, end)
                    start = this_point
                    end = None
    draw_grid()


def add_line_to_grid(start, end):
    grid.update({start: '#'})
    grid.update({end: '#'})
    if start[0] == end[0]:
        if start[1] > end[1]:
            for i in range(start[1], end[1] - 1, -1):
                grid.update({(start[0], i): '#'})
        else:
            for i in range(start[1], end[1] + 1):
                grid.update({(start[0], i): '#'})
    elif start[1] == end[1]:
        if start[0] > end[0]:
            for i in range(start[0], end[0] - 1, -1):
                grid.update({(i, start[1]): '#'})
        else:
            for i in range(start[0], end[0] + 1):
                grid.update({(i, start[1]): '#'})


def draw_grid():
    min_row = 0
    max_row = max([key[1] for key in grid.keys()])
    min_col = min([key[0] for key in grid.keys()])
    max_col = max([key[0] for key in grid.keys()])

    cols = max_col - min_col
    for r in range(3):
        this_line = '  '
        for m in range(min_col, max_col + 1):
            if m in (min_col, 500, max_col):
                this_line += str(m)[r:r+1]
            else:
                this_line += ' '
        print(this_line)
    for row in range(min_row, max_row + 1):
        this_line = f'{row} '
        for col in range(min_col, max_col + 1):
            this_line += grid.get((col, row), '.')
        print(this_line)


def drop_sand_part_1():
    max_row = max([key[1] for key in grid.keys()])
    sand = [500, 0]
    grains = 0
    while grid.get((sand[0], sand[1]), '.') == '.' and sand[1] <= max_row:
        next_spot = [sand[0], sand[1] + 1]
        if grid.get((next_spot[0], next_spot[1]), '.') == '.':
            sand = [next_spot[0], next_spot[1]]
            continue
        else:
            next_spot = [sand[0] - 1, sand[1] + 1]
            if grid.get((next_spot[0], next_spot[1]), '.') == '.':
                sand = [next_spot[0], next_spot[1]]
                continue
            else:
                next_spot = [sand[0] + 1, sand[1] + 1]
                if grid.get((next_spot[0], next_spot[1]), '.') == '.':
                    sand = [next_spot[0], next_spot[1]]
                    continue
                else:
                    grid.update({(sand[0], sand[1]): 'o'})
                    grains += 1
                    sand = [500, 0]
                    # draw_grid()
    return grains


def drop_sand_part_2():
    max_row = max([key[1] for key in grid.keys()])
    sand = [500, 0]
    grains = 0
    while grid.get((sand[0], sand[1]), '.') == '.':
        if sand[1] + 1 == max_row + 2:
            grid.update({(sand[0] - 1, sand[1] + 1): '#'})
            grid.update({(sand[0], sand[1] + 1): '#'})
            grid.update({(sand[0] + 1, sand[1] + 1): '#'})

        next_spot = [sand[0], sand[1] + 1]
        if grid.get((next_spot[0], next_spot[1]), '.') == '.':
            sand = [next_spot[0], next_spot[1]]
            continue
        else:
            next_spot = [sand[0] - 1, sand[1] + 1]
            if grid.get((next_spot[0], next_spot[1]), '.') == '.':
                sand = [next_spot[0], next_spot[1]]
                continue
            else:
                next_spot = [sand[0] + 1, sand[1] + 1]
                if grid.get((next_spot[0], next_spot[1]), '.') == '.':
                    sand = [next_spot[0], next_spot[1]]
                    continue
                else:
                    grains += 1
                    grid.update({(sand[0], sand[1]): 'o'})
                    if sand[0] == 500 and sand[1] == 0:
                        break
                    sand = [500, 0]
    return grains


def part1(file_name: str):
    global verbose
    verbose = False
    set_up_grid(file_name)
    grains = drop_sand_part_1()
    draw_grid()
    print(f'AOC {YEAR} Day {DAY} Part 1: {grains}')


def part2(file_name: str):
    global verbose
    verbose = False
    set_up_grid(file_name)
    grains = drop_sand_part_2()
    draw_grid()
    print(f'AOC {YEAR} Day {DAY} Part 2: {grains}')


if __name__ == '__main__':
    part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
