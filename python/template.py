YEAR = 2021
DAY = <<DAY>>


def part1(file_name_str: str) -> None:
    grid = read_file(file_name_str)
    print(f'Day {DAY} Part 1: ANSWER')


def part2(file_name_str: str) -> None:
    grid = read_file(file_name_str)
    print(f'Day {DAY} Part 1: ANSWER')


def read_file(file_name_str: str) -> dict[tuple[int, int], int]:
    grid: dict[tuple[int, int], int] = {}
    r = 0
    lines = [line.strip() for line in open(file_name_str, 'r').readlines()]
    for line in lines:
        c = 0
        for char in line:
            grid.update({(r, c): int(char)})
            c += 1
        r += 1
    return grid


if __name__ == '__main__':
    file_name = f'../../resources/{YEAR}/inputd{DAY}a.txt'
    part1(file_name)
    part2(file_name)

    file_name = f'../../resources/{YEAR}/inputd{DAY}.txt'
    part1(file_name)
    part2(file_name)