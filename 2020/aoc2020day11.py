N = (0, 1)
NE = (1, 1)
E = (1, 0)
SE = (1, -1)
S = (0, -1)
SW = (-1, -1)
W = (-1, 0)
NW = (-1, 1)


def grid(file_name: str) -> list:
    seating_grid = []
    with open(file_name, 'r') as f:
        test_input = f.read()
        for line in test_input.split("\n"):
            if line.strip() != '':
                row = []
                for seat in line.strip():
                    row.append(seat)
                seating_grid.append(row)
    return seating_grid


def part1a():
    my_grid = grid('../resources/2020/inputd11p1a.txt')
    changed = True

    while changed is True:
        # print_grid(my_grid)
        changed, my_grid = move(my_grid)

    print('Occupied Seats: {}'.format(count_occupied(my_grid)))


def part1():
    my_grid = grid('../resources/2020/inputd11.txt')
    changed = True

    while changed is True:
        # print_grid(my_grid)
        changed, my_grid = move(my_grid)

    print('Occupied Seats: {}'.format(count_occupied(my_grid)))


def part2():
    my_grid = grid('../resources/2020/inputd11.txt')
    changed = True

    while changed is True:
        # print_grid(my_grid)
        changed, my_grid = move2(my_grid)

    print('Occupied Seats: {}'.format(count_occupied(my_grid)))


def print_grid(my_grid: list) -> None:
    for row in my_grid:
        print('{}'.format(''.join(row)))
    # print('')
    # print('')
    # print('')


def move(seating_grid: list) -> tuple:
    changed = False
    my_copy = copy(seating_grid)
    for r in range(0, len(seating_grid)):
        row = seating_grid[r]
        for c in range(0, len(row)):
            seat = row[c]
            if seat == 'L':
                if count_occupied_adjacent(r, c, seating_grid) == 0:
                    my_copy[r][c] = '#'
                    changed = True
            elif seat == '#':
                if count_occupied_adjacent(r, c, seating_grid) >= 4:
                    my_copy[r][c] = 'L'
                    changed = True
    return changed, my_copy


def count_occupied_adjacent(row_idx: int, col_idx: int, seating_grid: list) -> int:
    r_start = 0
    c_start = 0
    occupied_seats = 0
    for i in range(-1, 1):
        if (row_idx + i) >= 0:
            r_start = (row_idx + i)
            break

    for i in range(-1, 1):
        if (col_idx + i) >= 0:
            c_start = (col_idx + i)
            break

    for r in range(r_start, (row_idx + 2)):
        if r < len(seating_grid):
            row = seating_grid[r]
            for c in range(c_start, (col_idx + 2)):
                if c < len(row):
                    if (r != row_idx) or (c != col_idx):
                        if row[c] == '#':
                            occupied_seats += 1
    return occupied_seats


def move2(seating_grid: list) -> tuple:
    changed = False
    my_copy = copy(seating_grid)
    for r in range(0, len(seating_grid)):
        row = seating_grid[r]
        for c in range(0, len(row)):
            seat = row[c]
            if seat == 'L':
                if count_occupied_visible(r, c, seating_grid) == 0:
                    my_copy[r][c] = '#'
                    changed = True
            elif seat == '#':
                if count_occupied_visible(r, c, seating_grid) >= 5:
                    my_copy[r][c] = 'L'
                    changed = True
    return changed, my_copy


def count_occupied_visible(row_idx: int, col_idx: int, seating_grid: list) -> int:
    occupied_seats = 0
    for direction in (N, NE, E, SE, S, SW, W, NW):
        occupied_seats += find_seat_in_direction(row_idx, col_idx, seating_grid, direction)
    return occupied_seats


def find_seat_in_direction(row_idx: int, col_idx: int, seating_grid: list, direction: tuple) -> int:
    new_col_idx = col_idx + direction[0]
    new_row_idx = row_idx + direction[1]

    if (new_row_idx < 0) or (new_row_idx == len(seating_grid)):
        return 0
    if (new_col_idx < 0) or (new_col_idx == len(seating_grid[0])):
        return 0

    if seating_grid[new_row_idx][new_col_idx] == 'L':
        return 0
    elif seating_grid[new_row_idx][new_col_idx] == '#':
        return 1
    return find_seat_in_direction(new_row_idx, new_col_idx, seating_grid, direction)


def copy(seating_grid: list) -> list:
    grid_copy = []
    for row in seating_grid:
        grid_copy.append(row.copy())
    return grid_copy


def count_occupied(seating_grid: list) -> int:
    occupied_seats = 0
    for row in seating_grid:
        for seat in row:
            if seat == '#':
                occupied_seats += 1
    return occupied_seats


#part1a()

#part1()

part2()
