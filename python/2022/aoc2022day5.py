YEAR = 2022
DAY = 5


def read_file(file_name: str,
              crates: dict[int: list[str]],
              instructions: list[tuple[int, int, int]]):
    import re
    with open(file_name, 'r') as f:
        lines = f.read()
        crate_lines = []
        instruction_lines = []
        for line in lines.split('\n'):
            if re.match(r'.*\[.*', line) is not None:
                crate_lines.append(line)
            elif re.match(r'move.*', line) is not None:
                instruction_lines.append(line)
        process_crates(crate_lines, crates)
        process_instructions(instruction_lines, instructions)


def process_crates(crate_lines: list[str],
                   crates: dict[int: list[str]]):
    import re
    for line in crate_lines:
        matches = re.findall(r'[A-Z]', line)
        index = 0
        for match in matches:
            index = line.find(match, index + 1)
            crate_number = int(((index - 1) / 4) + 1)
            crate_items = crates.get(crate_number, [])
            crate_items.append(match)
            crates.update({crate_number: crate_items})
    for crate_number, crate_items in crates.items():
        crate_items.reverse()
        crates.update({crate_number: crate_items})

    for key in sorted(crates.keys()):
        print(f'[{key}]: {crates.get(key)}')


def process_instructions(instruction_lines: list[str],
                         instructions: list[tuple[int, int, int]]):
    import re
    for line in instruction_lines:
        matches = re.findall(r'move\s([0-9]+)\sfrom\s([0-9]+)\sto\s([0-9]+)', line)
        for match in matches:
            instructions.append(match)
    print(instructions)


def part1(file_name: str):
    crates: dict[int: list[str]] = {}
    instructions: list[tuple[int, int, int]] = []
    read_file(file_name, crates, instructions)
    for instruction in instructions:
        amount = int(instruction[0])
        source = crates.get(int(instruction[1]))
        destination = crates.get(int(instruction[2]))
        print(instruction)
        for i in range(amount):
            destination.append(source.pop())
    print(crates)
    output = ''
    for index in range(1, len(crates.keys()) + 1):
        output += crates.get(index).pop()
    print(f'AOC {YEAR} Day {DAY} Part 1: {output}')


def part2(file_name: str):
    crates: dict[int: list[str]] = {}
    instructions: list[tuple[int, int, int]] = []
    read_file(file_name, crates, instructions)
    for instruction in instructions:
        amount = int(instruction[0])
        source = crates.get(int(instruction[1]))
        destination = crates.get(int(instruction[2]))
        print(instruction)
        tmp = []
        for i in range(amount):
            tmp.append(source.pop())
        tmp.reverse()
        destination.extend(tmp)
    print(crates)
    output = ''
    for index in range(1, len(crates.keys()) + 1):
        output += crates.get(index).pop()
    print(f'AOC {YEAR} Day {DAY} Part 2: {output}')


if __name__ == '__main__':
    # part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt')