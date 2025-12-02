YEAR = 2015
DAY = 13
reg_ex_pattern = r"^([a-zA-z]*)\swould\s(gain|lose)\s(\d+)\shappiness\sunits\sby\ssitting\snext\sto\s([a-zA-z]*)\.$"


class SeatedGuest:
    def __init__(self,
                 guest: str,
                 left: str,
                 right: str,
                 left_amt: int,
                 right_amt: int):
        self._guest = guest
        self._left = left
        self._left_amt = left_amt
        self._right = right
        self._right_amt = right_amt

    def guest(self):
        return self._guest

    def left(self):
        return self.left

    def left_amt(self):
        return self._left_amt

    def right(self):
        return self._right

    def right_amt(self):
        return self._right_amt


def calc_happiness(seated_arrangement: list[SeatedGuest]) -> int:
    total = 0
    for guest in seated_arrangement:
        total += guest.left_amt() + guest.right_amt()
    return total


def parse_file(file_name: str,
               include_me: bool = False) -> dict[str: dict[str: int]]:
    import re
    happiness: dict[str: dict[str: int]] = {}
    with open(file_name, 'r') as f:
        lines = f.read()
        for line in lines.split('\n'):
            matches = re.findall(reg_ex_pattern, line)
            for match in matches:
                adjustment = 1
                if match[1] == 'lose':
                    adjustment = -1
                targets = happiness.get(match[0], {})
                targets.update({match[3]: int(match[2]) * adjustment})
                if include_me:
                    targets.update({'Me': 0})
                happiness.update({match[0]: targets})
    if include_me:
        targets = {}
        for guest in happiness.keys():
            targets.update({guest: 0})
        happiness.update({'Me': targets})
    return happiness


def determine_optimal_arrangement(happiness: dict[str: dict[str: int]]) -> tuple[list[SeatedGuest], int]:
    from itertools import permutations
    guests = happiness.keys()
    seating_arrangements: list[str] = list(permutations(guests))

    best_arrangement = None
    best_happiness = None
    for arrangement in seating_arrangements:
        seated_arrangement: list[SeatedGuest] = []
        for i in range(len(arrangement)):
            if i == 0:
                left_idx = len(arrangement) - 1
                right_idx = 1
            elif i == len(arrangement) - 1:
                left_idx = len(arrangement) - 2
                right_idx = 0
            else:
                left_idx = i - 1
                right_idx = i + 1
            guest = arrangement[i]
            left_guest = arrangement[left_idx]
            right_guest = arrangement[right_idx]
            left_amt = happiness.get(guest).get(left_guest)
            right_amt = happiness.get(guest).get(right_guest)
            seated_arrangement.append(SeatedGuest(guest, left_guest, right_guest, left_amt, right_amt))
        total_happiness = calc_happiness(seated_arrangement)
        if best_happiness is None or total_happiness > best_happiness:
            best_happiness = total_happiness
            best_arrangement = seated_arrangement
    return best_arrangement, best_happiness


def part1(file_name: str):
    happiness = parse_file(file_name)
    optimal_arrangement, optimal_happiness = determine_optimal_arrangement(happiness)
    output_str = ' -> '.join([f'({a.left_amt()}){a.guest()}({a.right_amt()})' for a in optimal_arrangement])
    print(f'AOC {YEAR} Day {DAY} Part 1: {output_str} => {optimal_happiness}')


def part2(file_name: str):
    happiness = parse_file(file_name, True)
    optimal_arrangement, optimal_happiness = determine_optimal_arrangement(happiness)
    output_str = ' -> '.join([f'({a.left_amt()}){a.guest()}({a.right_amt()})' for a in optimal_arrangement])
    print(f'AOC {YEAR} Day {DAY} Part 2: {output_str} => {optimal_happiness}')


if __name__ == '__main__':
    part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
