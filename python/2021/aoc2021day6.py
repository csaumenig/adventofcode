def day6(line: str,
         part: int,
         days: int) -> None:

    fish: dict[int, int] = {}
    for i in range(0, 9):
        fish.update({i: 0})

    for x in line.split(','):
        fish.update({int(x) : fish.get(int(x), 0) + 1})
    for i in range(0, days):
        new_dict = {}
        for j in range(0, 9):
            new_dict.update({j: fish.get(j + 1)})
        new_dict.update({8: fish.get(0)})
        new_dict.update({6: new_dict.get(6,0)+fish.get(0)})

        for k,v in new_dict.items():
            fish.update({k: v})
    print(f'Day 6 Part 1: Number of fish after {days} days = {sum(fish.values())}')


def part2(input_str: str) -> None:
    pass


if __name__ == '__main__':
    with open('../../resources/2021/inputd6a.txt', 'r') as f:
        test_string = f.read()
        day6(test_string, 1, 80)
        day6(test_string, 2, 256)

    with open('../../resources/2021/inputd6.txt', 'r') as f:
       test_input = f.read()
       day6(test_input, 1, 80)
       day6(test_input, 2, 256)
    #    part2(test_input)