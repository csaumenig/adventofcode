from __future__ import annotations
from models.list_holder import ListHolder


YEAR = 2025
DAY = 10

ON = '#'
OFF = '.'

class Machine:
    def __init__(self,
                 running_state: str,
                 running_joltage: list[int]) -> None:
        self._running_state: str = running_state
        self._running_joltage: list[int] = running_joltage
        self._state: str = ''
        self._joltage: list[int] = []
        self.reset()

    def __eq__(self, other) -> bool:
        if isinstance(other, Machine):
            return self.__key__() == other.__key__()
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.__key__())

    def __repr__(self) -> str:
        return (f'Machine({self.__hash__()}) [State: [{self.current_state}], Running State: [{self._running_state}],'
                f" Running: {self.running}, Joltage: [{','.join(map(str, self._joltage))}],"
                f" Running Joltage: [{','.join(map(str, self._running_joltage))}]]")

    def __str__(self) -> str:
        return self.__repr__()

    def __key__(self) -> tuple:
        return self._state, self._running_state, tuple(self._running_joltage), tuple(self._joltage)

    @property
    def current_state(self) -> str:
        return self._state

    @property
    def running_joltage(self) -> int:
        num = 0
        power = 0
        for joltage in reversed(self._running_joltage):
            num += pow(10, power) * joltage
            power += 1
        return num

    @property
    def running_joltages(self) -> list[int]:
        return self._running_joltage

    @property
    def running(self) -> bool:
        return self._state == self._running_state

    def reset(self) -> None:
        self._state = "".ljust(len(self._running_state), OFF)
        self._joltage = [0 for _ in range(len(self._running_joltage))]

    def apply_schematic_to_state(self,
                                 button_schematic: ButtonSchematic) -> Machine:
        for i in button_schematic.items:
            self._state = self._state[0:i] + Machine.toggle(self._state[i]) + self._state[i+1:]
        return self

    def apply_schematic_to_joltage(self,
                                   button_schematic: ButtonSchematic) -> Machine:
        for i in button_schematic.items:
            self._joltage[i] = self._joltage[i] + 1
        return self

    @staticmethod
    def toggle(spot: str) -> str:
        if spot == ON:
            return OFF
        return ON

class ButtonSchematic(ListHolder):
    def __init__(self,
                 item_list: str) -> None:
        super().__init__(item_list, int)

    def __repr__(self) -> str:
        return f"<{','.join(map(str, self._items))}>"

class JoltageSchematic(ListHolder):
    def __init__(self,
                 button: ButtonSchematic,
                 dials: int) -> None:
        super().__init__(','.join(map(str, button.items)), int)
        self._dials = dials

    def convert_to_dec(self):
        start = ''.ljust(self._dials, '0')
        for i in self.items:
            start = start[0:i] + '1' + start[i+1:]
        return int(start)

    def __repr__(self) -> str:
        return f"<{','.join(map(str, self._items))}>"

def least_amount(num_list: list[int],
                 total: int) -> int:
    from itertools import combinations_with_replacement, permutations
    for i in range(1, total + 1):
        for tup in combinations_with_replacement(num_list, i):
            if sum(tup) == total:
                print(f'{num_list}, {total} => {tup}')
                return len(tup)
    return 0

def solve_min_presses(buttons, targets):
    """
    Again - stuck, so called on Reddit:
    https://www.reddit.com/r/adventofcode/comments/1pity70/comment/ntdfny4/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
    """

    import pulp
    m = len(targets)
    k = len(buttons)
    prob = pulp.LpProblem("MinPresses", pulp.LpMinimize)
    x = [pulp.LpVariable(f"x{j}", lowBound=0, cat='Integer') for j in range(k)]
    prob += pulp.lpSum(x)
    for p in range(m):
        prob += pulp.lpSum(x[j] for j in range(k) if p in buttons[j]) == targets[p]
    status = prob.solve(pulp.PULP_CBC_CMD(msg=False))
    if status != 1:
        print("unsolvable, something went wrong")
        assert False
    return int(pulp.value(prob.objective))


def load(file_name: str) -> list[tuple[Machine, list[ButtonSchematic]]]:
    return_value = []
    import re
    line_regex = r"\[(?P<target>[.#]+)\]\s(?P<buttons>[\(\)\d\,\s]+)\s\{(?P<joltage>[\d\,]+)\}"
    with open(file_name, 'r') as f:
        for line in f.readlines():
            matches = re.findall(line_regex, line)
            for match in matches:
                machine = Machine(str(match[0]), [int(x) for x in str(match[2]).split(',')])
                buttons: list[ButtonSchematic] = []
                for b in str(match[1]).split(' '):
                    buttons.append(ButtonSchematic(b.replace('(', '').replace(')','')))
                return_value.append((machine, buttons))
    return return_value

def part1(working_list: list[tuple[Machine, list[ButtonSchematic]]]) -> None:
    total = 0
    from utils.util import get_all_combinations
    for machine, buttons in working_list:
        button_combinations = get_all_combinations(buttons)
        local_total = 0
        for combo in button_combinations:
            for b in combo:
                machine = machine.apply_schematic_to_state(b)
            if machine.running:
                if local_total == 0 or len(combo) < local_total:
                    local_total = len(combo)
            machine.reset()
        total += local_total
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {total}')

def part2(working_list: list[tuple[Machine, list[ButtonSchematic]]]) -> None:
    total = 0
    for machine, buttons in working_list:
        # values = [JoltageSchematic(y, len(machine.current_state)).convert_to_dec() for y in buttons]
        total += solve_min_presses([b.items for b in buttons], machine.running_joltages)
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {total}')


if __name__ == '__main__':
    wl = load(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    wl1 = load(f'../../resources/{YEAR}/inputd{DAY}.txt')
    # part1(wl)
    # part1(wl1)
    part2(wl)
    part2(wl1)
    # part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
