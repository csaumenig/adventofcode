YEAR = 2022
DAY = 6


def is_unique(my_string: str) -> bool:
    for this_char in my_string:
        if my_string.count(this_char) > 1:
            return False
    return True


def find_index(file_name: str,
               unique_chars: int) -> int:
    with open(file_name, 'r') as f:
        lines = f.read()
        for line in lines.split('\n'):
            for index in range(unique_chars, len(line) + 1):
                if is_unique(line[index-unique_chars: index]):
                    return index


def part1(file_name: str):
    print(f'AOC {YEAR} Day {DAY} Part 1: {find_index(file_name, 4)}')


def part2(file_name: str):
    print(f'AOC {YEAR} Day {DAY} Part 2: {find_index(file_name, 14)}')


if __name__ == '__main__':
    part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt')