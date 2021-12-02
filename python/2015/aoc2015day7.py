import re
import regex


regex_three_vowels = re.compile(r'.{0,}([aeiou].{0,}){3,}', re.IGNORECASE)
regex_double_letters = re.compile(r'(.)\1', re.IGNORECASE)
regex_contains_pairs = re.compile(r'(ab|cd|pq|xy)', re.IGNORECASE)


def part1(input_str: str) -> None:



def part2(input_str: str) -> None:


def binary_count(num_bits: int) -> None:
    limit = pow(2, num_bits)
    for i in range(0, limit):
        print(f'{i} = {convert_to_base(i, 2)}')


def convert_to_base(dec_num: int,
                    base: int) -> str:
    return_value = ''
    if dec_num > 1:
        return_value += convert_to_base(dec_num // base, base)
    return_value += str(dec_num % base)
    return return_value


if __name__ == '__main__':
    test_string_1 = '\n'.join(['123 -> x', '456 -> y', 'x AND y -> d', 'x OR y -> e', 'x LSHIFT 2 -> f', 'y RSHIFT 2 -> g', 'NOT x -> h', 'NOT y -> i'])
    part1(test_string_1)
    # test_string_2 = '\n'.join(['qjhvhtzxzqqjkmpb', 'xxyxx', 'uurcxstgmygtbstg', 'ieodomkazucvgmuy'])
    # part2(test_string_2)

    # with open('../../resources/2015/inputd5.txt', 'r') as f:
    #     test_input = f.read()
    # part1(test_input)
    # part2(test_input)
