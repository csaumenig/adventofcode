YEAR = 2021
DAY = 17


def part1(file_name_str: str) -> None:
    target_area = read_file(file_name_str)
    print(f'Day {DAY} Part 1: ANSWER')


def part2(file_name_str: str) -> None:
    grid = read_file(file_name_str)
    print(f'Day {DAY} Part 1: ANSWER')


def read_file(file_name_str: str) -> dict[str, tuple[int, int]]:
    target_area: dict[str, tuple[int, int]] = {}
    lines = [line.strip() for line in open(file_name_str, 'r').readlines()]

    return grid


if __name__ == '__main__':
    file_name = f'../../resources/{YEAR}/inputd{DAY}a.txt'
    part1(file_name)
    part2(file_name)

    file_name = f'../../resources/{YEAR}/inputd{DAY}.txt'
    part1(file_name)
    part2(file_name)
