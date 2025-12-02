from __future__ import annotations
import re

YEAR = 2015
DAY = 14


class Reindeer:
    REINDEER_REGEX = (r'^(?P<name>[A-Z][a-z]+)\scan\sfly\s(?P<speed>\d+)\skm/s\sfor\s(?P<interval>\d+)\sseconds,'
                      r'\sbut\sthen\smust\srest\sfor\s(?P<rest>\d+)\sseconds\.$')

    def __init__(self,
                 file_line: str) -> None:
        self._cycles_flown = None
        self._distance_flown = None
        self._name = None
        self._speed = None
        self._interval = None
        self._rest = None
        self._cycle = None
        self._cycle_distance = None

        match = re.search(Reindeer.REINDEER_REGEX, file_line)
        self._initialize(match.group('name'),
                         int(match.group('speed')),
                         int(match.group('interval')),
                         int(match.group('rest')))

    def _initialize(self,
                    name: str,
                    speed: int,
                    interval: int,
                    rest: int) -> None:
        self._name = name
        self._speed = speed
        self._interval = interval
        self._rest = rest
        self._cycle = interval + rest
        self._cycle_distance = speed * interval
        self._cycles_flown = 0
        self._distance_flown = 0

    @property
    def name(self) -> str:
        return self._name

    @property
    def speed(self) -> int:
        return self._speed

    @property
    def interval(self) -> int:
        return self._interval

    @property
    def rest(self) -> int:
        return self._rest

    @property
    def cycle(self) -> int:
        return self._cycle

    @property
    def cycle_distance(self) -> int:
        return self._cycle_distance

    @property
    def cycles_flown(self) -> int:
        return self._cycles_flown

    @property
    def distance_flown(self) -> int:
        return self._distance_flown

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return (f'{self._name}:\n  Speed: {self._speed}km/s\n  Interval: {self._interval}s\n  Rest: {self._rest}s\n  '
                f'Cycle: {self._cycle}s\n  Cycle Distance: {self._cycle_distance}km\n  '
                f'Cycles Flown: {self._cycles_flown}\n  Distance Flown: {self.distance_flown}')

    def fly(self, time: int) -> int:
        self._cycles_flown = time // self._cycle
        leftover = time % self._cycle
        leftover_distance = 0
        if leftover // self._interval >= 1:
            self._cycles_flown += 1
        else:
            leftover_distance = leftover * self.speed
        self._distance_flown = (self.cycles_flown * self.cycle_distance) + leftover_distance
        return self.distance_flown

    @staticmethod
    def load_reindeer(file_name: str) -> list[Reindeer]:
        reindeer: list[Reindeer] = []
        with open(file_name, 'r') as f:
            for line in f.readlines():
                reindeer.append(Reindeer(line.strip()))
        return reindeer


def part1(reindeer_list: list[Reindeer],
          time: int) -> None:
    reindeer: dict[Reindeer, int] = {}
    for r in reindeer_list:
        reindeer.update({r: r.fly(time)})
    import pprint
    pprint.pprint(reindeer)
    deer = max(reindeer, key=reindeer.get)
    distance = reindeer.get(deer, 0)
    print(f'AOC {YEAR} Day {DAY} Part 1: Winning Deer: {deer.name} Distance: {distance}')


def part2(reindeer_list: list[Reindeer],
          time: int):
    reindeer: dict[Reindeer, int] = {}

    for t in range(1, time + 1):
        for r in reindeer_list:
            r.fly(t)
        max_distance = max(reindeer_list, key=lambda d: d.distance_flown).distance_flown
        max_deer = [x for x in reindeer_list if x.distance_flown == max_distance]
        for md in max_deer:
            reindeer.update({md: (reindeer.get(md, 0) + 1)})
    # import pprint
    # pprint.pprint(reindeer)
    deer = max(reindeer, key=reindeer.get)
    points = reindeer.get(deer, 0)
    print(f'AOC {YEAR} Day {DAY} Part 2: Winning Deer: {deer.name} Points: {points}')


if __name__ == '__main__':
    roster_ex = Reindeer.load_reindeer(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    roster = Reindeer.load_reindeer(f'../../resources/{YEAR}/inputd{DAY}.txt')
    race_time_ex = 1000
    race_time = 2503

    part1(roster_ex, race_time_ex)
    part1(roster, race_time)

    part2(roster_ex, race_time_ex)
    part2(roster, race_time)
