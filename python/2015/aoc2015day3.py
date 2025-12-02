from typing import Dict, Tuple

house_dict: Dict[Tuple[int, int], int] = {}


def reset(step: int) -> None:
    house_dict.clear()
    house_dict.update({(0, 0): step})


def get_position(current_position: Tuple[int, int], direction: str) -> Tuple[int, int]:
    position = None
    if direction == 'v':
        position = (current_position[0], current_position[1] + 1)
    elif direction == '>':
        position = (current_position[0] + 1, current_position[1])
    elif direction == '<':
        position = (current_position[0] - 1, current_position[1])
    elif direction == '^':
        position = (current_position[0], current_position[1] - 1)
    return position


def increment(position: Tuple[int, int]) -> None:
    house_count = house_dict.get(position, 0)
    house_dict.update({position: (house_count + 1)})


def part1(directions: str) -> None:
    reset(1)
    position: tuple = (0, 0)
    for x in directions:
        position = get_position(position, x)
        increment(position)
    print(f'Day 3 Part 1: Number of houses with 1 present: {len(list(filter(lambda count: count > 0, house_dict.values())))}')


def part2(directions: str) -> None:
    reset(2)
    santa_position: tuple = (0, 0)
    robosanta_position: tuple = (0, 0)
    santa = True
    for x in directions:
        if santa:
            santa_position = get_position(santa_position, x)
            increment(santa_position)
            santa = False
        else:
            robosanta_position = get_position(robosanta_position, x)
            increment(robosanta_position)
            santa = True
    total_houses = len(list(filter(lambda count: count > 0, house_dict.values())))
    print(f'Day 3 Part 2: Number of houses with at least 1 present: {total_houses}')


if __name__ == '__main__':
    with open('inputd3.txt', 'r') as f:
        test_input = f.read()
        part1(test_input)
        part2(test_input)
