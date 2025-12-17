from __future__ import annotations
import operator

YEAR = 2015
DAY = 23

instruction_regex = r"^(?P<command>[a-z]{3})\s(?:(?P<register>[ab]),?)?(?:\s?(?P<operator>[-+])(?P<increment>[\d]*))?.*$"
ops = {
    '+': operator.add,
    '-': operator.sub,
}

def read_file(file_name: str) -> list[str]:
    rv = []
    with open(file_name, 'r') as f:
        for line in [l.strip() for l in f.readlines()]:
            rv.append(line)
    return rv


def execute(instructions: list[str],
            registers: dict[str, int]):
    import re
    finished = False
    index = 0
    max_index = len(instructions)

    while not finished:
        match = re.search(instruction_regex, instructions[index])
        if match:
            all_groups = match.groupdict()
            command = all_groups['command']
            register = all_groups['register']
            operator_symbol = all_groups['operator']
            if not operator_symbol:
                operator_symbol = '+'
            inc = all_groups['increment']
            if not inc:
                increment = 1
            else:
                increment = int(inc)

            print(f'command: {command}, register: {register}, operator_symbol: {operator_symbol}, increment: {increment}')

            if command == 'hlf':
                registers[register] //= 2
            elif command == 'tpl':
                registers[register] *= 3
            elif command == 'inc':
                registers[register] += 1
            elif command == 'jie':
                if registers[register] % 2 == 1:
                    operator_symbol = '+'
                    increment = 1
            elif command == 'jio':
                if registers[register] != 1:
                    operator_symbol = '+'
                    increment = 1

            index = ops[operator_symbol](index, increment)

            if index >= max_index or index < 0:
                finished = True

    from pprint import pprint
    pprint(registers)


example_file = f'../../resources/{YEAR}/inputd{DAY}-a.txt'
example_registers = {
    'a': 0,
    'b': 0,
}
example_inst = read_file(example_file)
execute(example_inst, example_registers)

real_file = f'../../resources/{YEAR}/inputd{DAY}.txt'
real_registers = {
    'a': 1,
    'b': 0,
}
real_inst = read_file(real_file)
execute(real_inst, real_registers)


