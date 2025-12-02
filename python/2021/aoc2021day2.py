from typing import Tuple


def get_position_part1(current_position: Tuple[int, int],
                   command: str) -> Tuple[int, int]:
    position = None
    direction: str = command.split(' ')[0]
    amount: int = int(command.split(' ')[1])
    if direction.lower() == 'forward':
        position = (current_position[0] + amount, current_position[1])
    elif direction.lower() == 'up':
        position = (current_position[0], current_position[1] - amount)
    elif direction.lower() == 'down':
        position = (current_position[0], current_position[1] + amount)
    return position


def get_position_part2(current_position: Tuple[int, int, int],
                       command: str) -> Tuple[int, int, int]:
    position = None
    direction: str = command.split(' ')[0]
    amount: int = int(command.split(' ')[1])
    if direction.lower() == 'forward':
        position = (current_position[0] + amount, current_position[1] + (current_position[2] * amount), current_position[2])
    elif direction.lower() == 'up':
        position = (current_position[0], current_position[1], current_position[2] - amount)
    elif direction.lower() == 'down':
        position = (current_position[0], current_position[1], current_position[2] + amount)
    return position


def part1(input_str: str):
    position: Tuple[int, int] = (0, 0)
    commands = input_str.split('\n')
    for command in commands:
        position = get_position_part1(position, command)
    print(f'Day 2 Part 1: Final position = {position}, product = {position[0] * position[1]}')


def part2(input_str: str):
    position: Tuple[int, int, int] = (0, 0, 0)
    commands = input_str.split('\n')
    for command in commands:
        position = get_position_part2(position, command)
    print(f'Day 2 Part 2: Final position = {position}, product = {position[0] * position[1]}')


if __name__ == '__main__':
    with open('../../resources/2021/inputd2.txt', 'r') as f:
        test_input = f.read()
        part1(test_input)
        part2(test_input)
