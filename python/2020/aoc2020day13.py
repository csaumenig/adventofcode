from functools import reduce
from typing import Dict, List, Tuple


def load_file(file_name: str):
    with open(file_name, 'r') as f:
        test_input = f.read()
        lines = test_input.split("\n")
        busses = []
        for bus_number in lines[1].split(","):
            if bus_number != 'x':
                busses.append(int(bus_number))
        busses.sort()
    return int(lines[0].strip()), busses


def load_file2(file_name: str) -> list:
    with open(file_name, 'r') as f:
        test_input = f.read()
        lines = test_input.split("\n")
        return lines[1].strip().split(",")


def part1(file_name: str):
    earliest_time, busses = load_file(file_name)
    wait_times = {}
    for bus in busses:
        bus_time = 0
        while bus_time < earliest_time:
            bus_time += int(bus)
        wait_times.update({bus: (bus_time - earliest_time)})

    sorted_busses = sorted(wait_times, key=wait_times.get)
    print('Earliest Bus Time x Wait: {}'.format(int(sorted_busses[0]) * int(wait_times.get(sorted_busses[0]))))


def part2(file_name: str):
    busses = load_file2(file_name)
    offsets = [int(b) - i for i, b in enumerate(busses) if b != "x"]
    print(f"Part 2: {chinese_remainder(busses, offsets)}")


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x1, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


part1('inputd13.txt')


part2('inputd13.txt')
