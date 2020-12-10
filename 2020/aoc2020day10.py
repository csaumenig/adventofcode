def calc_diffs(file_name: str) -> dict:
    with open(file_name, 'r') as f:
        test_input = f.read()
        num_list = list(map(int, test_input.split("\n")))
        num_list.sort()
        with open(file_name.replace('.txt', '-sorted.txt'), 'w') as w:
            first = True
            for x in num_list:
                w.write(('\n' if first is False else '') + str(x))
                first = False

    diffs = {}
    i = 0
    for j in num_list:
        if (j-i) > 3:
            raise ValueError
        diffs.update({(j-i): 1 if diffs.get(j-i) is None else diffs.get(j-i) + 1})
        i = j
    diffs.update({3: 1 if diffs.get(3) is None else diffs.get(3) + 1})
    return diffs


def part1a():
    file_name = '../resources/2020/inputd10p1a.txt'
    diffs = calc_diffs(file_name)
    print('Part 1a: 1 jolt diffs: {} 2 jolt diffs: {} 3 jolt diffs: {}'.format(
        0 if diffs.get(1) is None else diffs.get(1),
        0 if diffs.get(2) is None else diffs.get(2),
        0 if diffs.get(3) is None else diffs.get(3)))


def part1b():
    file_name = '../resources/2020/inputd10p1b.txt'
    diffs = calc_diffs(file_name)
    print('Part 1b: 1 jolt diffs: {} 2 jolt diffs: {} 3 jolt diffs: {}'.format(
        0 if diffs.get(1) is None else diffs.get(1),
        0 if diffs.get(2) is None else diffs.get(2),
        0 if diffs.get(3) is None else diffs.get(3)))


def part1():
    file_name = '../resources/2020/inputd10.txt'
    diffs = calc_diffs(file_name)
    diff1 = 0 if diffs.get(1) is None else int(diffs.get(1))
    diff2 = 0 if diffs.get(2) is None else int(diffs.get(2))
    diff3 = 0 if diffs.get(3) is None else int(diffs.get(3))
    print('Part 1: 1 jolt diffs: {} 2 jolt diffs: {} 3 jolt diffs: {}'.format(diff1, diff2, diff3))
    print('Solution: {} x {} = {}'.format(diff1, diff3, (diff1*diff3)))


part1a()

part1b()

part1()
