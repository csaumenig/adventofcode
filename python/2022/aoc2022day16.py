from __future__ import annotations
from dataclasses import dataclass
from functools import total_ordering
import re

YEAR = 2022
DAY = 16

verbose: bool
grid: dict


@dataclass
class Node:
    name: str
    valve_rate: int
    connects_to: list[str]


def part1(file_name: str,
          minutes: int):
    global verbose
    verbose = False
    with open(file_name, 'r') as f:
        data = f.read()
        # Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
        parts = re.findall(r'Valve ([A-Z]{2}) has flow rate=(\d+); tunnel[s]* lead[s]* to valve[s]*\s(.*)', data)
        nodes: list[Node] = []
        for part in parts:
            name = part[0]
            rate = part[1]
            leads_to: list[str] = [x.strip() for x in part[2].split(",")]
            nodes.append(Node(name=name, valve_rate=int(rate), connects_to=leads_to))
        node_dict = dict(zip([n.name for n in nodes], nodes))
        start = 'AA'
        current_node = node_dict.get(start)
        open_valves: list[Node] = []
        total_pressure = 0
        moved = False
        for i in range(1, minutes + 1):
            print(f'=== Minute {i} ===')
            if len(open_valves) > 0:
                this_pressure = 0
                for valve in open_valves:
                    print(f'Valve {valve.name} open, releasing {valve.valve_rate} pressure.')
                    this_pressure += valve.valve_rate
                print(f'Total pressure this time: {this_pressure}')
                total_pressure += this_pressure
            else:
                print('No valves open')

            if moved:
                if current_node.valve_rate > 0:
                    open_valves.append(current_node)
                    moved = False
            else:
                next_node = None
                highest = None
                for c in current_node.connects_to:
                    neighbor = node_dict.get(c)
                    if neighbor in open_valves:
                        continue

                    if highest is None or neighbor.valve_rate > highest:
                        next_node = neighbor
                        highest = neighbor.valve_rate
                        moved = True
                current_node = next_node
            print(f'')

def part2(file_name: str):
        print(f'AOC {YEAR} Day {DAY} Part 2')


if __name__ == '__main__':
    part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt', 30)
    # part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
