import re
import regex


regex_three_vowels = re.compile(r'.{0,}([aeiou].{0,}){3,}', re.IGNORECASE)
regex_double_letters = re.compile(r'(.)\1', re.IGNORECASE)
regex_contains_pairs = re.compile(r'(ab|cd|pq|xy)', re.IGNORECASE)


def part1(input_str: str) -> None:
    count = 0
    for line in input_str.split('\n'):
        if find_matches(regex_three_vowels, line.strip()) is False:
            print(f'{line.strip()} doesn''t have 3 vowels')
            continue

        if find_matches(regex_double_letters, line.strip()) is False:
            print(f'{line.strip()} doesn''t have double letters')
            continue

        if find_matches(regex_contains_pairs, line.strip()) is True:
            print(f'{line.strip()} contains one of ab, cd, pq, or xy')
            continue
        count += 1

    print(f'Day 5 Part 1: Number of nice strings: {count}')


def find_matches(pattern: re.Pattern,
                 input_str: str) -> bool:
    matches = pattern.findall(input_str)
    if len(matches) == 0:
        return False
    return True


def part2(input_str: str) -> None:
    count = 0
    for line in input_str.split('\n'):
        my_dict: dict[str, int] = {}
        for i in range(0, len(line.strip()) + 1):
            my_str = line.strip()[i:i+2]
            if len(my_str) == 2:
                if my_str != line.strip()[i-1:i+1]:
                    my_count = my_dict.get(my_str, 0)
                    my_dict.update({my_str: my_count + 1})

        pairs = list(filter(lambda count: count >= 2, my_dict.values()))
        count_of_pairs = len(pairs)
        if count_of_pairs == 0:
            print(f'{line.strip()} has no pair of letters that appears twice')
            continue

        for j in range(0, len(line.strip()) + 1):
            my_str = line.strip()[j:j + 3]
            if len(my_str) == 3:
                if my_str[0] == my_str[2] and my_str[0] != my_str[1]:
                    count += 1
                    break
    print(f'Day 5 Part 2: Number of nice strings: {count}')


if __name__ == '__main__':
    # test_string_1 = '\n'.join(['ugknbfddgicrmopn', 'aaa', 'jchzalrnumimnmhp', 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb'])
    # part1(test_string_1)
    # test_string_2 = '\n'.join(['qjhvhtzxzqqjkmpb', 'xxyxx', 'uurcxstgmygtbstg', 'ieodomkazucvgmuy'])
    # part2(test_string_2)

    with open('../../resources/2015/inputd5.txt', 'r') as f:
        test_input = f.read()
    part1(test_input)
    part2(test_input)
