import re

YEAR = 2021
DAY = 13
COORDS_REGEX = r"\d{1,},\d{1,}"
FOLD_REGEX = r"fold\salong\s[xy]=\d{1,}"


def part1(input_str: str) -> None:
    coord_map, instructions = read(input_str)
    for instruction in instructions:
        coord_map = fold(coord_map, instruction)
        break # Just one instruction for part 1
    count = 0
    for value in coord_map.values():
        if value:
            count += 1
    print(f'Day {DAY} Part 1: {count}')


def part2(input_str: str) -> None:
    coord_map, instructions = read(input_str)
    for instruction in instructions:
        coord_map = fold(coord_map, instruction)
    max_x = 0
    max_y = 0
    for coord in coord_map.keys():
        if coord[0] > max_x:
            max_x = coord[0]
        if coord[1] > max_y:
            max_y = coord[1]

    for y in range(0, max_y + 1):
        line = ''
        for x in range(0, max_x + 1):
            if coord_map.get((x,y)):
                line += '#'
            else:
                line += '.'
        print(line)
    pass


def read(input_str: str) -> tuple[dict[tuple[int, int], bool], list[tuple[str, int]]]:
    coord_map: dict[tuple[int, int], bool] = {}
    instructions: list[tuple[str, int]] = []
    for line in input_str.split('\n'):
        if re.match(COORDS_REGEX, line) is not None:
            coord_map.update({(int(line.split(',')[0]), int(line.split(',')[1])): True})
        elif re.match(FOLD_REGEX, line) is not None:
            instructions.append((line.split('=')[0][-1], int(line.split('=')[1])))
    return coord_map, instructions


def fold(coord_map: dict[[tuple[int,int], bool]],
         instruction: tuple[str, int]) -> dict[[tuple[int,int], bool]]:
    new_map: dict[[tuple[int,int], bool]] = {}
    axis = instruction[0]
    fold_line = instruction[1]
    for coord, v in coord_map.items():
        coord_x = coord[0]
        coord_y = coord[1]
        if axis == 'x' and coord_x > fold_line:
            coord_x = coord_x - 2 * (coord_x - fold_line)
            new_map.update({(coord_x, coord_y): True})
        elif axis == 'y' and coord_y > fold_line:
            coord_y = coord_y - 2 * (coord_y - fold_line)
            new_map.update({(coord_x, coord_y): True})
        else:
            new_map.update({coord: True})
    return new_map



if __name__ == '__main__':
    with open(f'../../resources/{YEAR}/inputd{DAY}a.txt', 'r') as f:
        test_string = f.read()
        part1(test_string)
        part2(test_string)

    with open(f'../../resources/{YEAR}/inputd{DAY}.txt', 'r') as f:
        test_input = f.read()
        part1(test_input)
        part2(test_input)