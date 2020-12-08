def find_answer_part1(input_str: str):
    input_list = input_str.split()
    input_list2 = input_list.copy()
    for first in input_list:
        for second in input_list2:
            if int(first) + int(second) == 2020:
                return first, second, (int(first) * int(second))


def find_answer_part2(input_str: str):
    input_list = input_str.split()
    input_list2 = input_list.copy()
    input_list3 = input_list.copy()
    for first in input_list:
        for second in input_list2:
            for third in input_list3:
                if int(first) + int(second) + int(third) == 2020:
                    return first, second, third, (int(first) * int(second) * int(third))


if __name__ == '__main__':
    with open('resources/inputd1.txt', 'r') as f:
        test_input = f.read()

    x1, x2, product1 = find_answer_part1(test_input)
    print('First: {}, Second: {}, Product: {} '.format(x1, x2, product1))

    y1, y2, y3, product2 = find_answer_part2(test_input)
    print('First: {}, Second: {}, Third: {}, Product: {} '.format(y1, y2, y3, product2))
