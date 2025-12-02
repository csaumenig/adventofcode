def get_letter_value(letter: set[str]) -> int:
    offset = 96
    if len(letter) > 1:
        return -1
    for x in letter:
        if x.isupper():
            offset = 38
        return ord(x) - offset
    return -1


def part1(file_name: str):
    score = 0
    with open(file_name, 'r') as f:
        lines = f.read()
        line_num = 1
        for line in lines.split('\n'):
            midpoint = len(line)/2
            left_side = set()
            right_side = set()
            for i in range(0, len(line)):
                # print(f'Line[{line_num}][{i}]: {line[i]}')
                if i < (len(line)/2):
                    left_side.add(line[i])
                else:
                    right_side.add(line[i])
            line_num += 1
            same = left_side.intersection(right_side)
            priority = get_letter_value(same)
            # print(f'{same}: [{priority}]')
            score += priority
    print(f'AOC 2022 Day 3 Part 1: {score}')


def part2(file_name: str):
    score = 0
    with open(file_name, 'r') as f:
        lines = f.read()
        group = []
        for line in lines.split('\n'):
            line_set = set()
            for i in range(0, len(line)):
                line_set.add(line[i])
            group.append(line_set)
            if len(group) == 3:
                same = group[0].intersection(group[1], group[2])
                priority = get_letter_value(same)
                score += priority
                group = []
    print(f'AOC 2022 Day 3 Part 2: {score}')


if __name__ == '__main__':
    #part1('../../resources/2022/inputd3-a.txt')
    part1('../../resources/2022/inputd3.txt')
    # part2('../../resources/2022/inputd3-a.txt')
    part2('../../resources/2022/inputd3.txt')