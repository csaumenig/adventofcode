YEAR = 2021
DAY = 11


def part1(file_name_str: str,
          num_steps: int) -> None:
    grid: dict[tuple[int, int], int] = read_file(file_name_str)
    flashes = 0
    # print('Before any steps:')
    # print_grid(grid)
    # print('')
    for i in range(1, num_steps + 1):
        grid, flashed = step(grid)
        flashes += len(flashed)
        # if i % 10 == 0:
        #     print(f'After Step {i}:')
        #     print_grid(grid)
        #     print('')
    print(f'Day {DAY} Part 1: Flashes: {flashes}')


def part2(file_name_str: str) -> None:
    grid: dict[tuple[int, int], int] = read_file(file_name_str)
    flashed = []
    num_step = 0
    while len(flashed) != len(grid):
        grid, flashed = step(grid)
        num_step += 1
    print(f'Day {DAY} Part 2: Steps: {num_step}')


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


def step(grid: dict[tuple[int, int], int]) -> tuple[dict[tuple[int, int], int], list[tuple[int, int]]]:
    flashed = []
    rows = 0
    cols = 0
    # Add one to every octopus
    for k, v in grid.items():
        grid.update({k: v + 1})
        if k[0] > rows:
            rows = k[0]
        if k[1] > cols:
            cols = k[1]
    rows += 1
    cols += 1

    for r in range(0, rows):
        for c in range(0, cols):
            octopus = (r, c)
            value = grid.get(octopus)
            if value > 9:
                grid, flashed = flash(octopus, grid, flashed)

    for octopus in flashed:
        grid.update({octopus: 0})

    return grid, flashed


def flash(octopus: tuple[int, int],
          grid: dict[tuple[int, int], int],
          flashed: list[tuple[int, int]]) -> tuple[dict[tuple[int, int], int], list[tuple[int, int]]]:
    if octopus not in flashed:
        flashed.append(octopus)
        top_left_octopus: tuple[int, int] = (octopus[0] - 1, octopus[1] - 1)
        top_octopus: tuple[int, int] = (octopus[0] - 1, octopus[1])
        top_right_octopus: tuple[int, int] = (octopus[0] - 1, octopus[1] + 1)
        left_octopus: tuple[int, int] = (octopus[0], octopus[1] - 1)
        right_octopus: tuple[int, int] = (octopus[0], octopus[1] + 1)
        bottom_left_octopus: tuple[int, int] = (octopus[0] + 1, octopus[1] - 1)
        bottom_octopus: tuple[int, int] = (octopus[0] + 1, octopus[1])
        bottom_right_octopus: tuple[int, int] = (octopus[0] + 1, octopus[1] + 1)
        neighbors = [top_left_octopus, top_octopus, top_right_octopus, left_octopus, right_octopus, bottom_left_octopus, bottom_octopus, bottom_right_octopus]
        for neighbor in neighbors:
            neighbor_value = grid.get(neighbor)
            if neighbor_value is not None:
                grid.update({neighbor: neighbor_value + 1})
                if neighbor_value + 1 > 9:
                    grid, flashed = flash(neighbor, grid, flashed)
    return grid, flashed


def print_grid(grid: dict[tuple[int, int], int]) -> None:
    rows = 0
    cols = 0
    # Add one to every octopus
    for k, v in grid.items():
        if k[0] > rows:
            rows = k[0]
        if k[1] > cols:
            cols = k[1]
    for r in range(0, rows + 1):
        line = ''
        for c in range(0, cols + 1):
            line = line + str(grid.get((r, c)))
        print(line)


if __name__ == '__main__':
    # file_name = f'../../resources/{YEAR}/inputd{DAY}b.txt'
    # part1(file_name, 2)
    # part2(test_string)

    # file_name = f'../../resources/{YEAR}/inputd{DAY}a.txt'
    # part1(file_name, 100)
    # part2(file_name)

    file_name = f'../../resources/{YEAR}/inputd{DAY}.txt'
    part1(file_name, 100)
    part2(file_name)

    # with open(f'../../resources/{YEAR}/inputd{DAY}a.txt', 'r') as f:
    #     test_string = f.read()
    #     #part1(test_string)
    #     #part2(test_string)
