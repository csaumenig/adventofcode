from collections import Counter
from functools import lru_cache

YEAR = 2021
DAY = 14


def get_differences(part: int,
                    file_name_str: str,
                    num_runs_int: int) -> None:
    template, instructions = read_file(file_name_str)
    this_counter = polymerize(template, instructions, num_runs_int)
    max_element_count = sorted(this_counter.values(), reverse=True)[0]
    min_element_count = sorted(this_counter.values(), reverse=False)[0]
    print(f'Day {DAY} Part {part}: Difference of Max and Min elements = {max_element_count-min_element_count}')


def polymerize(template: str,
               instructions: dict[str, str],
               number_of_runs: int) -> Counter:
    @lru_cache(maxsize=None)
    def count(pair: str, step: int) -> Counter:
        if step == number_of_runs or pair not in instructions:
            return Counter()
        step += 1
        new_element = instructions.get(pair)
        my_counter = Counter(new_element)
        my_counter.update(count(pair[0] + new_element, step))
        my_counter.update(count(new_element + pair[1], step))
        return my_counter

    counter = Counter(template)
    for left, right in zip(template, template[1:]):
        counter.update(count(left + right, 0))
    return counter


def read_file(file_name_str: str) -> tuple[str, dict[str, str]]:
    lines = [line.strip() for line in open(file_name_str, 'r').readlines()]
    template = lines[0]
    instructions = {a: b for a, b in (line.split(' -> ') for line in lines[2:])}
    return template, instructions


if __name__ == '__main__':
    file_name = f'../../resources/{YEAR}/inputd{DAY}a.txt'
    runs = 10
    get_differences(1, file_name, runs)

    file_name = f'../../resources/{YEAR}/inputd{DAY}.txt'
    runs = 10
    get_differences(1, file_name, runs)

    file_name = f'../../resources/{YEAR}/inputd{DAY}a.txt'
    runs = 40
    get_differences(2, file_name, runs)

    file_name = f'../../resources/{YEAR}/inputd{DAY}.txt'
    runs = 40
    get_differences(2, file_name, runs)
