class Crab:
    def __init__(self,
                 value: int):
        self._value = value
    
    @property
    def value(self):
        return self._value

    def fuel(self,
             target: int) -> int:
        if target > self._value:
            return target - self._value
        elif target < self.value:
            return self._value - target
        return 0

    def fuel2(self,
              target: int) -> int:
        steps = 0
        if target == self.value:
            return 0
        elif target > self._value:
            steps = target - self._value
        else:
            steps = self._value - target
        # sum of 1 to N = N(N+1)/2
        return int((steps * (steps + 1))/2)


def part1(input_str: str) -> None:
    crabs, values = load(input_str)
    fuel_consumption: dict[int, list[int]] = {}
    for s in range(min(values), max(values) + 1):
        fuel_values = []
        for crab in crabs:
            fuel_values.append(crab.fuel(s))
        fuel_consumption.update({s: fuel_values})
    for k, v in sorted(fuel_consumption.items(), key=lambda item: sum(item[1])):
        print(f'Day 7 Part 1: Position [{k}]: Uses {sum(v)} fuel')
        break


def part2(input_str:str) -> None:
    crabs, values = load(input_str)
    fuel_consumption: dict[int, list[int]] = {}
    for s in range(min(values), max(values) + 1):
        fuel_values = []
        for crab in crabs:
            fuel_values.append(crab.fuel2(s))
        fuel_consumption.update({s: fuel_values})
    for k, v in sorted(fuel_consumption.items(), key=lambda item: sum(item[1])):
        print(f'Day 7 Part 2: Position [{k}]: Uses {sum(v)} fuel')
        break


def load(input_str: str) -> tuple[list[Crab], set[int]]:
    crab_list: list[Crab] = []
    values = [int(i) for i in input_str.split(',')]
    for value in values:
        crab_list.append(Crab(value))
    return crab_list, set(values)


if __name__ == '__main__':
    with open('../../resources/2021/inputd7a.txt', 'r') as f:
        test_string = f.read()
        part1(test_string)
        part2(test_string)

    with open('../../resources/2021/inputd7.txt', 'r') as f:
        test_input = f.read()
        part1(test_input)
        part2(test_input)
