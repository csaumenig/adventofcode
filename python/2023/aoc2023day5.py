from __future__ import annotations
import re

YEAR = 2023
DAY = 5

seed_list_pattern_string = r'^seeds: ([0-9]+ ?)+$'
seed_list_pattern = re.compile(seed_list_pattern_string)
map_header_pattern_string = r'^([a-z]+)-to-([a-z]+) map:$'
map_header_pattern = re.compile(map_header_pattern_string)
map_line_pattern_string = r'^([0-9]+ ?){3}$'
map_line_pattern = re.compile(map_line_pattern_string)


def get_destination_id(source_id: int,
                       map_list: list[tuple[int, int, int]]) -> int:
    for range_def in map_list:
        range_def: tuple[int, int, int]
        if range_def[0] <= source_id <= range_def[0] + range_def[2]:
            return range_def[1] + (source_id - range_def[0])
    return source_id


def part1(file_name: str):
    closest_location = 0
    seed_list: list[int] = []
    maps: dict[tuple[str, str]: list[tuple[int, int, int]]] = {}
    with open(file_name, 'r') as f:
        map_id = ('', '')
        map_list: list[tuple[int, int, int]] = []
        for line in f.readlines():
            results = seed_list_pattern.search(line)
            if results:
                seed_list = [int(x.strip()) for x in line.split(':')[1].strip().split(' ') if x.isnumeric()]
            results = map_header_pattern.search(line)
            if results:
                line.strip().split(' ')[0].strip().split('-to-')[0].strip()
                map_id: tuple[str, str] = (line.strip().split(' ')[0].strip().split('-to-')[0].strip(),
                                           line.strip().split(' ')[0].strip().split('-to-')[1].strip())
                map_list = []
            results = map_line_pattern.search(line)
            if results:
                numbers = line.split(' ')
                dest_range_start: int = int(numbers[0].strip())
                source_range_start: int = int(numbers[1].strip())
                range_length: int = int(numbers[2].strip())
                map_list.append((source_range_start, dest_range_start, range_length))

            if line.strip() == '':
                if map_id and map_list:
                    maps.update({map_id: map_list})
        if map_id and map_list:
            maps.update({map_id: map_list})

    for seed in seed_list:
        soil = get_destination_id(seed, maps.get(('seed', 'soil')))
        fertilizer = get_destination_id(soil, maps.get(('soil', 'fertilizer')))
        water = get_destination_id(fertilizer, maps.get(('fertilizer', 'water')))
        light = get_destination_id(water, maps.get(('water', 'light')))
        temperature = get_destination_id(light, maps.get(('light', 'temperature')))
        humidity = get_destination_id(temperature, maps.get(('temperature', 'humidity')))
        location = get_destination_id(humidity, maps.get(('humidity', 'location')))
        # print(f'Seed {seed}, Soil {soil}, Fertilizer {fertilizer}, Water {water}, Light {light}, Temperature {temperature}, Humidity {humidity}, Location {location}')
        if closest_location == 0 or location < closest_location:
            closest_location = location
    # print(seed_list)
    # print(maps)
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {closest_location}')


def part2(file_name: str):
    closest_location = 0
    seed_list: list[tuple[int, int]] = []
    maps: dict[tuple[str, str]: list[tuple[int, int, int]]] = {}
    with open(file_name, 'r') as f:
        map_id = ('', '')
        map_list: list[tuple[int, int, int]] = []
        for line in f.readlines():
            results = seed_list_pattern.search(line)
            if results:
                start = -1
                range = -1
                for x in line.split(':')[1].strip().split(' '):
                    if x.isnumeric():
                        if start == -1:
                            start = int(x)
                        elif range == -1:
                            range = int(x)
                            seed_list.append((start, range))
                            start = -1
                            range = -1
            results = map_header_pattern.search(line)
            if results:
                line.strip().split(' ')[0].strip().split('-to-')[0].strip()
                map_id: tuple[str, str] = (line.strip().split(' ')[0].strip().split('-to-')[0].strip(),
                                           line.strip().split(' ')[0].strip().split('-to-')[1].strip())
                map_list = []
            results = map_line_pattern.search(line)
            if results:
                numbers = line.split(' ')
                dest_range_start: int = int(numbers[0].strip())
                source_range_start: int = int(numbers[1].strip())
                range_length: int = int(numbers[2].strip())
                map_list.append((source_range_start, dest_range_start, range_length))

            if line.strip() == '':
                if map_id and map_list:
                    maps.update({map_id: map_list})
        if map_id and map_list:
            maps.update({map_id: map_list})

    seeds: list[int] = []
    for seed in seed_list:
        s = seed[0]
        while s < seed[0] + seed[1]:
            seeds.append(s)
            s += 1
    # print(f"Number of seeds: {len(seeds)}")
    for seed in seeds:
        soil = get_destination_id(seed, maps.get(('seed', 'soil')))
        fertilizer = get_destination_id(soil, maps.get(('soil', 'fertilizer')))
        water = get_destination_id(fertilizer, maps.get(('fertilizer', 'water')))
        light = get_destination_id(water, maps.get(('water', 'light')))
        temperature = get_destination_id(light, maps.get(('light', 'temperature')))
        humidity = get_destination_id(temperature, maps.get(('temperature', 'humidity')))
        location = get_destination_id(humidity, maps.get(('humidity', 'location')))
        # print(f'Seed {seed}, Soil {soil}, Fertilizer {fertilizer}, Water {water}, Light {light}, Temperature {temperature}, Humidity {humidity}, Location {location}')
        if closest_location == 0 or location < closest_location:
            closest_location = location
    # # print(seed_list)
    # # print(maps)
    print(f'AOC {YEAR} Day {DAY} Part 2: Closest Location: {closest_location}')


if __name__ == '__main__':
    # part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
