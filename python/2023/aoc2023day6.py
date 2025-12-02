from __future__ import annotations
from collections import namedtuple

YEAR = 2023
DAY = 6

time_pattern_string = 'Time:'
distance_pattern_string = 'Distance:'

Race = namedtuple("Race", "time distance")


def part1(file_name: str):
    total = 0
    races: list[Race] = []
    with open(file_name, 'r') as f:
        race_times: list[int] = []
        race_distances: list[int] = []
        for line in f.readlines():
            if line.strip().startswith(time_pattern_string):
                race_times = [int(x.strip()) for x in line.strip().split(':')[1].strip().split(' ') if x.isnumeric()]
            elif line.strip().startswith(distance_pattern_string):
                race_distances = [int(x.strip()) for x in line.strip().split(':')[1].strip().split(' ') if x.isnumeric()]
        races = [Race(x[0], x[1]) for x in zip(race_times, race_distances)]
    for race in races:
        i = 0
        total_distance = 0
        number_of_winners = 0
        while i <= race.time:
            total_distance = i * (race.time - i)
            if total_distance > race.distance:
                number_of_winners += 1
            i += 1
        if total == 0:
            total = number_of_winners
        else:
            total = total * number_of_winners
        print(f'{race}: number_of_winners: {number_of_winners}')
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {total}')


def part2(file_name: str):
    total = 0
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {total}')


if __name__ == '__main__':
    part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
