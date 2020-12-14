with open('../resources/2020/inputd10p1a.txt', 'r') as f:
    test_input = f.read()
    num_list = list(map(int, test_input.split("\n")))
    num_list.sort()

    diffs = {}
    num_list.insert(0, int(0))
    num_list.append(int(max(num_list)) + int(3))

    i = 0
    for j in num_list:
        if (j-i) > 3:
            raise ValueError
        diffs.update({(j-i): 1 if diffs.get(j-i) is None else diffs.get(j-i) + 1})
        i = j

    print('Part 1a:\n 1 jolt diffs: {}\n 2 jolt diffs: {}\n 3 jolt diffs: {}'.format(
        0 if diffs.get(1) is None else diffs.get(1),
        0 if diffs.get(2) is None else diffs.get(2),
        0 if diffs.get(3) is None else diffs.get(3)))

    # (0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
    # (0), 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, (22)
    # (0), 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, (22)
    # (0), 1, 4, 5, 7, 10, 12, 15, 16, 19, (22)
    # (0), 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, (22)
    # (0), 1, 4, 6, 7, 10, 12, 15, 16, 19, (22)
    # (0), 1, 4, 7, 10, 11, 12, 15, 16, 19, (22)
    # (0), 1, 4, 7, 10, 12, 15, 16, 19, (22)


with open('../resources/2020/inputd10p1b.txt', 'r') as f:
    test_input = f.read()
    num_list = list(map(int, test_input.split("\n")))
    num_list.sort()

    diffs = {}
    num_list.insert(0, int(0))
    num_list.append(int(max(num_list)) + int(3))

    i = 0
    for j in num_list:
        if (j - i) > 3:
            raise ValueError
        diffs.update({(j - i): 1 if diffs.get(j - i) is None else diffs.get(j - i) + 1})
        i = j

    print('Part 1b:\n 1 jolt diffs: {}\n 2 jolt diffs: {}\n 3 jolt diffs: {}'.format(
        0 if diffs.get(1) is None else diffs.get(1),
        0 if diffs.get(2) is None else diffs.get(2),
        0 if diffs.get(3) is None else diffs.get(3)))

with open('../resources/2020/inputd10.txt', 'r') as f:
    test_input = f.read()
    num_list = list(map(int, test_input.split("\n")))
    num_list.sort()

    diffs = {}
    num_list.insert(0, int(0))
    num_list.append(int(max(num_list)) + int(3))

    i = 0
    for j in num_list:
        if (j - i) > 3:
            raise ValueError
        diffs.update({(j - i): 1 if diffs.get(j - i) is None else diffs.get(j - i) + 1})
        i = j

    diff1 = 0 if diffs.get(1) is None else int(diffs.get(1))
    diff2 = 0 if diffs.get(2) is None else int(diffs.get(2))
    diff3 = 0 if diffs.get(3) is None else int(diffs.get(3))
    print('Part 1:\n 1 jolt diffs: {}\n 2 jolt diffs: {}\n 3 jolt diffs: {}'.format(diff1, diff2, diff3))
    print('Solution: {} x {} = {}'.format(diff1, diff3, (diff1 * diff3)))


    num_list.pop(0)
    num_list.pop()

    



part2a()
