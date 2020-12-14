direction_dict = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0)
}

direction_list = ['E', 'N', 'W', 'S']


def load_commands(file_name: str) -> list:
    commands = []
    with open(file_name, 'r') as f:
        test_input = f.read()
        for line in test_input.split("\n"):
            commands.append(line)
    return commands


def part1(file_name: str):
    position = (0, 0)
    direction = 'E'
    commands = load_commands(file_name)
    for command in commands:
        position, direction = execute(command, position, direction)

    print('Final Stop - position {} & direction {}'.format(position, direction))
    print('Manhattan Distance: {}'.format(abs(position[0]) + abs(position[1])))


def part2(file_name: str):
    ship_position = (0, 0)
    waypoint_position = (10, 1)
    commands = load_commands(file_name)
    for command in commands:
        ship_position, waypoint_position = execute2(command, ship_position, waypoint_position)

    print('Final Stop - ship position {} & waypoint position {}'.format(ship_position, waypoint_position))
    print('Manhattan Distance: {}'.format(abs(ship_position[0]) + abs(ship_position[1])))


def execute(command: str, position: tuple, direction: str):
    # Action N means to move north by the given value.
    # Action S means to move south by the given value.
    # Action E means to move east by the given value.
    # Action W means to move west by the given value.
    # Action L means to turn left the given number of degrees.
    # Action R means to turn right the given number of degrees.
    # Action F means to move forward by the given value in the direction the ship is currently facing.
    command_code, amount = decode(command)
    if command_code in ('L', 'R'):
        direction = turn1(command_code, amount, direction)
    elif command_code in ('N', 'S', 'E', 'W', 'F'):
        position = move1(command_code, amount, position, direction)
    return position, direction


def decode(command: str):
    import re
    pattern = r"^(N|S|E|W|L|R|F)([\d]+)$"
    regex = re.compile(pattern)
    matches = regex.match(command)
    command_code = ''
    amount = 0
    if matches:
        g = 0
        for group in matches.groups():
            if g == 0:
                command_code = group.upper()
            elif g == 1:
                amount = int(group)
            else:
                raise ValueError
            g += 1
    return command_code, amount


def turn1(command_code: str, amount: int, direction: str) -> str:
    direction_idx = 0
    for d in range(0, 4):
        if direction_list[d] == direction:
            direction_idx = d
            break
    quarter_turns = (int(amount/90) % 4)

    for d in range(0, quarter_turns):
        if command_code == 'L':
            direction_idx += 1
        elif command_code == 'R':
            direction_idx -= 1
    return direction_list[(direction_idx % 4)]


def move1(command_code: str, amount: int, position: tuple, direction: str) -> tuple:
    if command_code == 'F':
        slope = direction_dict.get(direction)
    else:
        slope = direction_dict.get(command_code)

    for i in range(0, amount):
        position = ((position[0] + slope[0]), (position[1] + slope[1]))
    return position


def execute2(command: str, ship_position: tuple, waypoint_position: tuple):
    # Action N means to move the waypoint north by the given value.
    # Action S means to move the waypoint south by the given value.
    # Action E means to move the waypoint east by the given value.
    # Action W means to move the waypoint west by the given value.
    # Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
    # Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
    # Action F means to move forward to the waypoint a number of times equal to the given value.
    command_code, amount = decode(command)
    if command_code in ('L', 'R'):
        waypoint_position = turn2(command_code, amount, waypoint_position)
    elif command_code in ('N', 'S', 'E', 'W'):
        waypoint_position = move2(command_code, amount, waypoint_position)
    elif command_code == 'F':
        ship_position = waypoint(amount, ship_position, waypoint_position)
    return ship_position, waypoint_position


def turn2(command_code: str, amount: int, waypoint_position: tuple) -> tuple:
    quarter_turns = (int(amount/90) % 4)
    if quarter_turns == 1:
        if command_code == 'L':
            waypoint_position = (-waypoint_position[1], waypoint_position[0])
        else:
            waypoint_position = (waypoint_position[1], -waypoint_position[0])
    elif quarter_turns == 2:
        waypoint_position = (-waypoint_position[0], -waypoint_position[1])
    elif quarter_turns == 3:
        if command_code == 'L':
            waypoint_position = (waypoint_position[1], -waypoint_position[0])
        else:
            waypoint_position = (-waypoint_position[1], waypoint_position[0])
    return waypoint_position


def move2(command_code: str, amount: int, waypoint_position: tuple) -> tuple:
    slope = direction_dict.get(command_code)
    for i in range(0, amount):
        waypoint_position = ((waypoint_position[0] + slope[0]), (waypoint_position[1] + slope[1]))
    return waypoint_position


def waypoint(amount: int, ship_position: tuple, waypoint_position: tuple) -> tuple:
    for i in range(0, amount):
        ship_position = ((ship_position[0] + waypoint_position[0]), (ship_position[1] + waypoint_position[1]))
    return ship_position


# part1('../resources/2020/inputd12p1.txt')


part2('../resources/2020/inputd12.txt')
