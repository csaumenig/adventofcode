N = (0, 1)
NE = (1, 1)
E = (1, 0)
SE = (1, -1)
S = (0, -1)
SW = (-1, -1)
W = (-1, 0)
NW = (-1, 1)


def part1a():
    position = (0, 0)
    direction = E
    commands = []
    with open('../resources/2020/inputd12p1a.txt', 'r') as f:
        test_input = f.read()
        for line in test_input.split("\n"):
            commands.append(line)

    for command in commands:
        position, direction = move(command)


def move(command: str):
    # Action N means to move north by the given value.
    # Action S means to move south by the given value.
    # Action E means to move east by the given value.
    # Action W means to move west by the given value.
    # Action L means to turn left the given number of degrees.
    # Action R means to turn right the given number of degrees.
    # Action F means to move forward by the given value in the direction the ship is currently facing.

    pattern = r"^(N|S|E|W|L|R|F)([\d])$"
    regex = re.compile(pattern)
    matches = regex.match(line)


part1a()

#part1()

part2()
