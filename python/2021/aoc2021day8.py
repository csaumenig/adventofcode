display = {
    0: 'ABCEFG',
    1: 'CF',
    2: 'ACDEG',
    3: 'ACDFG',
    4: 'BCDF',
    5: 'ABDFG',
    6: 'ABDEFG',
    7: 'ACF',
    8: 'ABCDEFG',
    9: 'ABCDFG'
}

solve_it = {
    'a': 'C',
    'b': 'F',
    'c': 'G',
    'd': 'A',
    'e': 'B',
    'f': 'D',
    'g': 'E'
}


def part1(input_str: str) -> None:
    count = 0
    for line in input_str.split('\n'):
        for output_num in line.split('|')[1].strip().split(' '):
            if len(output_num) in (2, 3, 4, 7):
                count += 1
    print(f'Day 8 Part 1: Count: {count}')


def part2(input_str: str) -> None:
    total = 0
    line_num = 1
    for line in input_str.split('\n'):
        io_parts = line.split('|')
        input_list = io_parts[0].strip().split(' ')
        output_list = io_parts[1].strip().split(' ')

        key_dict = decode_input(input_list)
        output_num = decode_output(output_list, key_dict)
        total += output_num
        print(f'Line {line_num}: {output_num}')
        line_num += 1
    print(f'Day 8 Part 2: Total = {total}')


def decode_input(input_list: list[str]) -> dict[str, str]:
    # display = {
    #     1: 'CF',
    #     7: 'ACF',
    #     4: 'BCDF',

    #     5: 'ABDFG', => ADG(BF)
    #     2: 'ACDEG', => ADG(CE)
    #     3: 'ACDFG', => ADG(CF)

    #     9: 'ABCDFG'
    #     0: 'ABCEFG',
    #     6: 'ABDEFG',

    #     8: 'ABCDEFG',
    # }
    # 'ab', 'abd', 'abef', 'bcdef', 'acdfg', 'abcdf', 'abcdef', 'bcdefg', 'abcdeg', 'abcdefg'
    # 1.
    # ab -> CF => (ab ~ CF)
    # abd -> ACF => d = 'A'

    # 2.
    # abef -> BCDF => (ef ~ BD)
    # cdf -> ADG => (cf ~ DG)
    # f = 'D', e = 'B', c = 'G'

    # 3.
    # bcdef -> (ABDG)b => b = 'F', a = 'C'
    # acdfg -> (ADG)ag => g = 'E'

    sorted_list = [''.join(sorted(list_num)) for list_num in sorted(input_list, key=len)]
    tmp_dict = {}
    solved_dict = {}
    for x in sorted_list:
        if len(x) in (2, 3, 4, 7):
            tmp_dict.update({len(x): x})
        elif len(x) == 5:
            my_list = tmp_dict.get(5, [])
            my_list.append(x)
            tmp_dict.update({5: sorted(my_list)})

    # 1.
    my_a = ''.join(set(tmp_dict.get(3))-set(tmp_dict.get(2)))
    solved_dict.update({'A': my_a})

    # 2.
    four_and_two = set(tmp_dict.get(4)) - set(tmp_dict.get(2))
    five_and_three = set.intersection(set(tmp_dict.get(5)[0]), set(tmp_dict.get(5)[1]), set(tmp_dict.get(5)[2]))
    five_and_two = copy_set(five_and_three)
    five_and_two.discard(solved_dict.get('A'))
    tmp_d = four_and_two.intersection(five_and_two)
    my_d = ''.join(tmp_d)

    tmp_b = copy_set(four_and_two)
    tmp_b.discard(my_d)
    my_b = ''.join(tmp_b)

    tmp_g = copy_set(five_and_two)
    tmp_g.discard(my_d)
    my_g = ''.join(tmp_g)

    solved_dict.update({'D': my_d})
    solved_dict.update({'B': my_b})
    solved_dict.update({'G': my_g})

    # 3.
    for tmp_5 in tmp_dict.get(5):
        tmp_5_set = set(tmp_5)
        for v in solved_dict.values():
            tmp_5_set.discard(v)
        if len(tmp_5_set) == 1:
            my_f = ''.join(tmp_5_set)
            solved_dict.update({'F': my_f})
            tmp_2 = set(tmp_dict.get(2))
            tmp_2.discard(my_f)
            my_c = ''.join(tmp_2)
            solved_dict.update({'C': my_c})
            break

    # 4.
    tmp_7_set = set(tmp_dict.get(7))
    for v in solved_dict.values():
        tmp_7_set.discard(v)
    my_e = ''.join(tmp_7_set)
    solved_dict.update({'E': my_e})
    print(sorted_list)
    print(solved_dict)
    return solved_dict


def copy_set(my_set: set) -> set:
    return set([x for x in my_set])


def find_intersections(master_list: list[list[str]]) -> set[str]:
    result = []
    for idx1 in range(0, len(master_list)):
        s1 = set(master_list[idx1])
        for idx2 in range(0, len(master_list)):
            if idx2 == idx1:
                continue
            else:
                s2 = set(master_list[idx2])
                s3 = s1.intersection(s2)
                result.extend(s3)
    return set(result)


def decode_output(output_list: list[str],
                  key_dict: dict[str, str]) -> int:
    my_key_dict = dict((v, k) for k, v in key_dict.items())
    str_value = ''
    for output_num in output_list:
        decode = ''
        for char in sorted(output_num):
            decode += my_key_dict.get(char).upper()
        decode = ''.join(sorted(decode))
        for k, v in display.items():
            if v == decode:
                str_value += str(k)
                break
    return int(str_value)


if __name__ == '__main__':
    with open('../../resources/2021/inputd8a.txt', 'r') as f:
        test_string = f.read()
        part1(test_string)
        part2(test_string)

    with open('../../resources/2021/inputd8.txt', 'r') as f:
        test_input = f.read()
        part1(test_input)
        part2(test_input)
