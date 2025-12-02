def get_sets(line: str) -> tuple[set[int], set[int]]:
    elves = line.split(",")
    elf1 = elves[0]
    elf2 = elves[1]
    elf1_endpoints = elf1.split('-')
    elf1_start = int(elf1_endpoints[0])
    elf1_end = int(elf1_endpoints[1])
    elf1_set = set([x for x in range(elf1_start, elf1_end + 1)])
    elf2_endpoints = elf2.split('-')
    elf2_start = int(elf2_endpoints[0])
    elf2_end = int(elf2_endpoints[1])
    elf2_set = set([x for x in range(elf2_start, elf2_end + 1)])
    return elf1_set, elf2_set


def part1(file_name: str):
    overlaps = 0
    with open(file_name, 'r') as f:
        lines = f.read()
        for line in lines.split('\n'):
            elves = get_sets(line)
            if elves[0].issubset(elves[1]) or elves[1].issubset(elves[0]):
                # print(line)
                overlaps += 1
    print(f'AOC 2022 Day 4 Part 1: {overlaps}')


def part2(file_name: str):
    overlaps = 0
    with open(file_name, 'r') as f:
        lines = f.read()
        for line in lines.split('\n'):
            elves = get_sets(line)
            if len(elves[0].intersection(elves[1])) > 0 or len(elves[1].intersection(elves[0])) > 0:
                overlaps += 1
    print(f'AOC 2022 Day 4 Part 2: {overlaps}')


if __name__ == '__main__':
    part1('../../resources/2022/inputd4-a.txt')
    part1('../../resources/2022/inputd4.txt')
    part2('../../resources/2022/inputd4-a.txt')
    part2('../../resources/2022/inputd4.txt')