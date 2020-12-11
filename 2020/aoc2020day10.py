def calc_diffs(file_name: str) -> dict:
    with open(file_name, 'r') as f:
        test_input = f.read()
        num_list = list(map(int, test_input.split("\n")))
        num_list.sort()
        # with open(file_name.replace('.txt', '-sorted.txt'), 'w') as w:
        #     first = True
        #     for x in num_list:
        #         w.write(('\n' if first is False else '') + str(x))
        #         first = False

    diffs = {}
    num_list.insert(0, int(0))
    num_list.append(int(max(num_list)) + int(3))

    i = 0
    for j in num_list:
        if (j-i) > 3:
            raise ValueError
        diffs.update({(j-i): 1 if diffs.get(j-i) is None else diffs.get(j-i) + 1})
        i = j
    return diffs


def part1a():
    file_name = '../resources/2020/inputd10p1a.txt'
    diffs = calc_diffs(file_name)
    print('Part 1a:\n 1 jolt diffs: {}\n 2 jolt diffs: {}\n 3 jolt diffs: {}'.format(
        0 if diffs.get(1) is None else diffs.get(1),
        0 if diffs.get(2) is None else diffs.get(2),
        0 if diffs.get(3) is None else diffs.get(3)))


def part1b():
    file_name = '../resources/2020/inputd10p1b.txt'
    diffs = calc_diffs(file_name)
    print('Part 1b:\n 1 jolt diffs: {}\n 2 jolt diffs: {}\n 3 jolt diffs: {}'.format(
        0 if diffs.get(1) is None else diffs.get(1),
        0 if diffs.get(2) is None else diffs.get(2),
        0 if diffs.get(3) is None else diffs.get(3)))


def part1():
    file_name = '../resources/2020/inputd10.txt'
    diffs = calc_diffs(file_name)
    diff1 = 0 if diffs.get(1) is None else int(diffs.get(1))
    diff2 = 0 if diffs.get(2) is None else int(diffs.get(2))
    diff3 = 0 if diffs.get(3) is None else int(diffs.get(3))
    print('Part 1:\n 1 jolt diffs: {}\n 2 jolt diffs: {}\n 3 jolt diffs: {}'.format(diff1, diff2, diff3))
    print('Solution: {} x {} = {}'.format(diff1, diff3, (diff1*diff3)))

def part2a():
    # (0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
    # (0), 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, (22)
    # (0), 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, (22)
    # (0), 1, 4, 5, 7, 10, 12, 15, 16, 19, (22)
    # (0), 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, (22)
    # (0), 1, 4, 6, 7, 10, 12, 15, 16, 19, (22)
    # (0), 1, 4, 7, 10, 11, 12, 15, 16, 19, (22)
    # (0), 1, 4, 7, 10, 12, 15, 16, 19, (22)
    file_name = '../resources/2020/inputd10p1a.txt'
    num_paths = calc_paths(file_name)
    print('Solution: {}'.format(num_paths))


def calc_paths(file_name: str):
    with open(file_name, 'r') as f:
        test_input = f.read()
        num_list = list(map(int, test_input.split("\n")))
        num_list.sort()
        with open(file_name.replace('.txt', '-sorted.txt'), 'w') as w:
            first = True
            for x in num_list:
                w.write(('\n' if first is False else '') + str(x))
                first = False
        num_list.insert(0,0)
        target = int(max(num_list)) + int(3)
        num_list.append(target)
    paths = []
    for i in range(0, len(num_list)):
        paths = find_next_step(i, num_list, paths)
    count = 0
    for p in paths:
        if p[-1] == target:
            print(p)
            count += 1
    return count


def find_next_step(index, list, path_list):
    new_paths = path_list.copy()
    idx = index
    p_idx = 0
    if len(new_paths) == 0:
        p = []
        p.append([0])
        return p

    for path in path_list:
        end_value = path[-1]
        diff = list[idx] - end_value
        updated = False
        while diff <= 3:
            if diff > 0:
                p = path.copy()
                p.append(list[idx])
                if updated is False:
                    new_paths[p_idx] = p
                    updated = True
                else:
                    new_paths.insert(p_idx, p)
            idx += 1
            if idx < len(list):
                diff = list[idx] - end_value
            else:
                diff = 4
        idx = index
        p_idx += 1
    return new_paths

#part1a()
#
# part1b()
#
# part1()

part2a()
