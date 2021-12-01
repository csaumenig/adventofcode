import itertools


def part1(input_str: str):
    count = 0
    depths = input_str.split('\n')
    for (d1, d2) in zip(depths, depths[1:]):
        if int(d2) > int(d1):
            count += 1
    print(f'Day 1 Part 1: Number of depth increases: {count}')


def part2(input_str: str):
    count = 0
    depths = input_str.split('\n')
    sums = []
    for (d1, d2, d3) in zip(depths, depths[1:], depths[2:]):
        sums.append(int(d1) + int(d2) + int(d3))
    for (s1, s2) in zip(sums, sums[1:]):
        if int(s2) > int(s1):
            count += 1
    print(f'Day 1 Part 2: Number of depth increases (sum of 3 consecutive): {count}')


if __name__ == '__main__':
    with open('inputd1.txt', 'r') as f:
        test_input = f.read()
        part1(test_input)
        part2(test_input)
