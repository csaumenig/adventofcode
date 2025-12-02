YEAR = 2021
DAY = 18


def part1(file_name_str: str) -> None:
    grid = read_file(file_name_str)
    print(f'Day {DAY} Part 1: ANSWER')


def part2(file_name_str: str) -> None:
    grid = read_file(file_name_str)
    print(f'Day {DAY} Part 1: ANSWER')


def part_a(input_str: str) -> None:
    added = ('[' + input_str.replace(' + ', ', ').replace(' ', '') + ']').replace('[', '(').replace(']', ')')
    added_tuple = eval(added)
    print(f'Added Tuple: {added_tuple}')
    pair_count = 0
    left_side = True
    for c in added:
        if c == '(':
            pair_count += 1
            left_side = True
        elif c == ')':
            pair_count -= 1
        elif c == ',':
            left_side = False
        print(f'Pair Count ({pair_count}): {c}')


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


if __name__ == '__main__':
    # file_name = f'../../resources/{YEAR}/inputd{DAY}a.txt'
    # part1(file_name)
    # part2(file_name)
    #
    # file_name = f'../../resources/{YEAR}/inputd{DAY}.txt'
    # part1(file_name)
    # part2(file_name)
    add_str = '[[[[4, 3], 4], 4], [7, [[8, 4], 9]]] + [1, 1]'
    part_a(add_str)
