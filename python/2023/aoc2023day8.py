from __future__ import annotations
from reference import lcm

YEAR = 2023
DAY = 8

def read_file(file_name:str) -> tuple[str, dict[str, tuple[str, str]]]:
    instruction_line = ''
    move_map: dict[str, tuple[str, str]] = {}
    with open(file_name, 'r') as f:
        for line in f.readlines():
            if line.strip() != '':
                if instruction_line == '':
                    instruction_line = line.strip()
                    continue
                l1 = line.split('=')
                node_name = l1[0].strip()
                line_instructions = l1[1].replace('(', '').replace(')', '').split(',')
                node_links = (line_instructions[0].strip(), line_instructions[1].strip())
                move_map.update({node_name: node_links})
    return instruction_line, move_map


def check_for_done(node_list) -> bool:
    for x in node_list:
        if x[-1] != 'Z':
            return False
    return True


def part1(file_name: str):
    total = 0
    instruction, node_map = read_file(file_name)
    current = 'AAA'
    instruction_index = 0
    while current != 'ZZZ':
        if instruction_index == len(instruction):
            instruction_index = 0
        this_instruction = instruction[instruction_index]
        total += 1
        instruction_index += 1
        current_node = node_map.get(current)
        if this_instruction == 'L':
            current = current_node[0]
        else:
            current = current_node[1]
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {total}')


def part2(file_name: str):
    total = 0
    instruction, node_map = read_file(file_name)
    current = [x for x in node_map.keys() if x[-1] == 'A']
    instruction_index = 0
    move_totals = []
    for this_current in current:
        moves = 0
        done = False
        moving_current = this_current
        while not done:
            if instruction_index == len(instruction):
                instruction_index = 0
            this_instruction = instruction[instruction_index]
            moves += 1
            instruction_index += 1
            if this_instruction == 'L':
                move_index = 0
            else:
                move_index = 1
            moving_current = node_map.get(moving_current)[move_index]
            done = moving_current[-1] == 'Z'
        move_totals.append(moves)
    total = lcm.lcm_list(move_totals)
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {total}')


if __name__ == '__main__':
    # part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part1(f'../../resources/{YEAR}/inputd{DAY}-b.txt')
    # part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}-c.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
