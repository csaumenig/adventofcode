def part1(input_str: str) -> None:
    numbers: list[str] = input_str.split('\n')
    place_counts:dict[int, dict[int, int]] = get_place_counts(numbers)
    gamma_rate = ''
    epsilon_rate = ''
    for k, v in place_counts.items():
        if v.get(0, 0) > v.get(1, 0):
            gamma_rate += '0'
            epsilon_rate += '1'
        else:
            gamma_rate += '1'
            epsilon_rate += '0'
    gamma = int(gamma_rate, 2)
    epsilon = int(epsilon_rate, 2)
    print(f'Gamma: {gamma} [{gamma_rate}] Epsilon: {epsilon} [{epsilon_rate}]')
    power_consumption = gamma * epsilon
    print(f'Power Consumption: {power_consumption}')


def part2(input_str: str) -> None:
    numbers: list[str] = input_str.split('\n')
    prefix = ''
    place = 0
    while len(numbers) != 1:
        place_counts: dict[int, dict[int, int]] = get_place_counts(numbers)
        counts = place_counts.get(place)
        if counts.get(0, 0) > counts.get(1, 0):
            prefix += '0'
        elif counts.get(0, 0) < counts.get(1, 0):
            prefix += '1'
        else:
            prefix += '1'
        numbers = [x for x in numbers if x.startswith(prefix)]
        place += 1
    oxygen_generator_rating = numbers[0]

    numbers: list[str] = input_str.split('\n')
    prefix = ''
    place = 0
    while len(numbers) != 1:
        place_counts: dict[int, dict[int, int]] = get_place_counts(numbers)
        counts = place_counts.get(place)
        if counts.get(0, 0) < counts.get(1, 0):
            prefix += '0'
        elif counts.get(0, 0) > counts.get(1, 0):
            prefix += '1'
        else:
            prefix += '0'
        numbers = [x for x in numbers if x.startswith(prefix)]
        place += 1
    co2_scrubber_rating = numbers[0]
    o2_rating = int(oxygen_generator_rating, 2)
    co2_rating = int(co2_scrubber_rating, 2)
    print(f'O2 Rating: {o2_rating} [{oxygen_generator_rating}] CO2 Rating {co2_rating} [{co2_scrubber_rating}]')
    life_support_rating =  o2_rating * co2_rating
    print(f'Power Consumption: {life_support_rating}')


def get_place_counts(lines: list[str]) -> dict[int, dict[int, int]]:
    place_counts: dict[int, dict[int, int]] = {}
    for line in lines:
        bin_str = line.strip()
        place = 0
        for b in bin_str:
            count: dict[int, int] = place_counts.get(place)
            if count is None:
                count = {}
            if b == '0':
                count.update({0: count.get(0, 0) + 1})
            elif b == '1':
                count.update({1: count.get(1, 0) + 1})
            place_counts.update({place: count})
            place += 1

    return place_counts

if __name__ == '__main__':
    # test_string = ('\n').join(['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010'])
    # part1(test_string)
    # part2(test_string)
    with open('../resources/2021/inputd3.txt', 'r') as f:
        test_input = f.read()
        part1(test_input)
        part2(test_input)
