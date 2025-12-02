def step1(input_str: str) -> int:
    return input_str.count('(') - input_str.count(')')


def step2(input_str: str) -> int:
    floor = 0
    index = 1
    for c in input_str:
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
        if floor < 0:
            return index
        index += 1
    return 0


if __name__ == '__main__':
    with open('resources/inputd1.txt', 'r') as f:
         test_input = f.read()

    print('Santa is on floor: {}'.format(step1(test_input)))

    print('Santa goes into the basement in step: {}'.format(step2(test_input)))

