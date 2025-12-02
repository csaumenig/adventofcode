with open('inputd9.txt', 'r') as f:
    test_input = f.read()
    num_list = list(map(int, test_input.split("\n")))


def find(p: int) -> int:
    from itertools import combinations
    for i in range(p, len(num_list)):
        x = num_list[i]
        pair_list = [pair for pair in combinations(num_list[(i-p): i], 2) if sum(pair) == x]
        if len(pair_list) == 0:
            return x


def sum_it(start, target):
    list_sum = 0
    i = 1
    while list_sum < target:
        i += 1
        list_sum = sum(num_list[start:i])
    if list_sum == target:
        return num_list[start:i]
    return []


def part1a():
    print('Sample: {}'.format(find(5)))


def part1():
    print('Part1: {}'.format(find(25)))


def part2():
    target = find(25)
    list_sum = []
    i = 0
    while len(list_sum) == 0:
        list_sum = sum_it(i, target)
        i += 1

    print('Part1: {}'.format((min(list_sum) + max(list_sum))))


part1()


part2()
