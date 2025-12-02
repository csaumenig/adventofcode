from itertools import combinations
from numpy import prod
from typing import List


class RectangularPrismDimensions:

    def __init__(self,
                 dimensions: List[int]) -> None:
        self._dimensions = sorted(dimensions)
        self._wrap_size = self._calc_wrap()
        self._ribbon_size = self._calc_ribbon()

    def _calc_wrap(self) -> int:
        side_areas: List[int] = []
        c = combinations(self._dimensions, 2)
        for c1 in c:
            side_areas.append(c1[0] * c1[1])
        wrapping_area = min(side_areas)
        wrapping_area += sum([2 * x for x in side_areas])
        return wrapping_area

    def _calc_ribbon(self) -> int:
        side_perimeters: List[int] = []
        c = combinations(self._dimensions, 2)
        for c1 in c:
            side_perimeters.append(2 * c1[0] + 2 * c1[1])
        ribbon_length = min(side_perimeters)
        ribbon_length += prod(self._dimensions)
        return ribbon_length

    def dim_print(self) -> str:
        return_str = ''
        for d in self._dimensions:
            if return_str.strip() != '':
                return_str += ' x '
            return_str += str(d)
        return return_str

    def ribbon_size(self) -> int:
        return self._ribbon_size

    def wrap_size(self) -> int:
        return self._wrap_size


def compute(input_str: str):
    box_dimensions: List[RectangularPrismDimensions] = []
    for line in input_str.split('\n'):
        if line.strip() != '':
            box_dimensions.append(RectangularPrismDimensions([int(i) for i in line.split('x')]))
    box = 1
    wrap_area = 0
    ribbon_length = 0
    for x in box_dimensions:
        print(f'{box}: {x.dim_print()}: Wrapping Area:[{x.wrap_size()}] RibbonLength:[{x.ribbon_size()}]')
        wrap_area += x.wrap_size()
        ribbon_length += x.ribbon_size()
        box += 1
    print(f'Day 2 Part 1: Wrap Area = {wrap_area}')
    print(f'Day 2 Part 2: Ribbon Length = {ribbon_length}')


if __name__ == '__main__':
    with open('inputd2.txt', 'r') as f:
        test_input = f.read()
        compute(test_input)

