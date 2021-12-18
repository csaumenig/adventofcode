YEAR = 2021
DAY = 13


def part1(input_str: str) -> None:
    for line in input_str.split('\n'):
        print(line)
    print(f'Day {DAY} Part 1: ANSWER')


def part2(input_str: str) -> None:
    for line in input_str.split('\n'):
        print(line)
    print(f'Day {DAY} Part 2: ANSWER')


if __name__ == '__main__':
    with open(f'../../resources/{YEAR}/inputd{DAY}a.txt', 'r') as f:
         test_string = f.read()
         part1(test_string)
         part2(test_string)

    with open(f'../../resources/{YEAR}/inputd{DAY}a.txt', 'r') as f:
         test_input = f.read()
         part1(test_input)
         part2(test_input)