def part1(input_str: str) -> None:
    source: dict[tuple[int,int], int] = {}
    r = 0
    c = 0
    risk = 0
    for line in input_str.split('\n'):
        c = 0
        for char in line:
            source.update({(r, c): int(char)})
            c += 1
        r += 1
    for row in range(0, r):
        for col in range(0, c):
            val = check_value(source, row, col)
            if val > -1:
                risk += val+1
    print(f'Day 9 Part 1: Total Risk = {risk}')


def part2(input_str: str) -> None:
    pass


def check_value(source: dict[tuple[int,int], int],
                r: int,
                c: int) -> int:
    my_value = source.get((r, c))

    left = source.get((r, c-1))
    right = source.get((r, c+1))
    top = source.get((r-1, c))
    bottom = source.get((r+1, c))

    if left is not None and left < my_value:
        return -1
    if right is not None and right < my_value:
        return -1
    if top is not None and top < my_value:
        return -1
    if bottom is not None and bottom < my_value:
        return -1
    return my_value


if __name__ == '__main__':
    with open('../../resources/2021/inputd9a.txt', 'r') as f:
         test_string = f.read()
         part1(test_string)
         part2(test_string)

    with open('../../resources/2021/inputd9.txt', 'r') as f:
         test_input = f.read()
         part1(test_input)
         part2(test_input)