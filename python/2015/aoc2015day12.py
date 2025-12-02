YEAR = 2015
DAY = 12


def sum_digits(start_string: str,
               my_string: str) -> int:
    import re
    total = 0
    numbers = re.findall(r'(-*\d+)', my_string)
    for number in numbers:
        total += int(number)
    print(f'{start_string} -> {my_string} -> {numbers} = {total}')
    return total


def ignore_red(json_obj):
    if 'red' in json_obj.values():
        return ''
    return json_obj


def part1(file_name: str):
    with open(file_name, 'r') as f:
        lines = f.read()
        for line in lines.split('\n'):
            total = sum_digits(line, line)
            print(f'AOC {YEAR} Day {DAY} Part 1: {total}')


def part2(file_name: str):
    import json
    with open(file_name, 'r') as f:
        lines = f.read()
        for line in lines.split('\n'):
            json_obj = json.loads(line, object_hook=ignore_red)
            json_string = json.dumps(json_obj)
            total = sum_digits(line, json_string)
            print(f'AOC {YEAR} Day {DAY} Part 2: {total}')


if __name__ == '__main__':
    # part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
