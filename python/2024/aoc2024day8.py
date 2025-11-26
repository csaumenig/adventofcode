from __future__ import annotations
from models.grid import GridXY, Point

YEAR = 2024
DAY = 8

anti_node_labels: dict[str, str] = {
    '`': '~',
    '1': '!',
    '2': '@',
    '3': '#',
    '4': '$',
    '5': '%',
    '6': '^',
    '7': '&',
    '8': '*',
    '9': '(',
    '0': ')',
    '-': '_',
    '=': '+',
    '[': '{',
    ']': '}',
    '\\': '|',
    ';': ':',
    '\'': '"',
    ',': '<',
    '.': '>',
    '/': '?'
}

class AntennaGrid(GridXY):
    def __init__(self,
                 rows: int,
                 cols: int) -> None:
        super().__init__(rows=rows, cols=cols)
        self._antenna_array: dict[str, list[Point]] = {}
        self._anti_node_array: dict[str, list[Point]] = {}
        self._line_node_array: dict[str, list[Point]] = {}
        self._antinodes: list[Point] = []
        self._line_nodes: list[Point] = []

    def __repr__(self) -> str:
        space = ' '
        grid_text = ''
        for y in range(self._rows):
            line = ''
            for x in range(self._cols):
                line += self.get_value(Point(x, y), True)
            if grid_text.strip() != '':
                grid_text += '\n'
            grid_text += line
        grid_text += '\n\n'
        grid_text += '   '
        for x in range(self._cols):
            grid_text += f"{str(x):{space}>3}"
        for y in range(self._rows):
            line = f"{str(y):{space}>2} "
            for x in range(self._cols):
                line += f"{self.get_value(Point(x,y)):{space}>3}"
            if grid_text.strip() != '':
                grid_text += '\n'
            grid_text += line
        return grid_text

    def __str__(self) -> str:
        return self.__repr__()

    @property
    def antinodes(self) -> list[Point]:
        return self._antinodes

    @property
    def line_nodes(self) -> list[Point]:
        return self._line_nodes

    def read_file(self,
                  file_lines: list[str]) -> None:
        super().read_file(file_lines)
        for k, v in self._dict.items():
            if v != '.':
                antenna_loc: list[Point] = self._antenna_array.get(v, [])
                antenna_loc.append(k)
                self._antenna_array.update({v: antenna_loc})

    def find_antinodes(self):
        from itertools import combinations
        for label, antennae in self._antenna_array.items():
            print(label)
            print('======')
            anti_label = get_anti_label(label)
            combos = combinations(antennae, 2)
            anti_nodes = self._anti_node_array.get(anti_label, [])
            for subset in combos:
                p1 = subset[0]
                p2 = subset[1]

                run = p1.x - p2.x
                rise = p1.y - p2.y

                max_x = max(p1.x, p2.x) + abs(run)
                min_x = min(p1.x, p2.x) - abs(run)
                max_y = max(p1.y, p2.y) + abs(rise)
                min_y = min(p1.y, p2.y) - abs(rise)

                """
                Four different line scenarios:
                
                Positive slope => y = mx + b
                Negative slope => y = -mx + b
                Zero slope => y = b
                Undefined slope => x = b
                """
                an1 = None
                an2 = None

                if run == 0:
                    an1 = Point(p1.x, max_y)
                    an2 = Point(p1.x, min_y)
                elif rise == 0:
                    an1 = Point(p1.x, max_y)
                    an2 = Point(p1.x, min_y)
                elif (run > 0 and rise > 0) or (run < 0 and rise < 0):
                    an1 = Point(max_x, max_y)
                    an2 = Point(min_x, min_y)
                else:
                    an1 = Point(max_x, min_y)
                    an2 = Point(min_x, max_y)

                if Point.valid(an1, (0, self._rows), (0, self._cols)):
                    anti_nodes.append(an1)
                    if an1 not in self._antinodes:
                        self._antinodes.append(an1)
                else:
                    an1 = None

                if Point.valid(an2, (0, self._rows), (0, self._cols)):
                    anti_nodes.append(an2)
                    if an2 not in self._antinodes:
                        self._antinodes.append(an2)
                else:
                    an2 = None

                print(f'Points {p1},{p2} have antinodes: {an1}, {an2}')

                self._anti_node_array.update({anti_label: anti_nodes})

    def find_line_nodes(self):
        from itertools import combinations
        for label, antennae in self._antenna_array.items():
            print(label)
            print('======')
            anti_label = get_anti_label(label)
            combos = combinations(antennae, 2)
            anti_nodes = self._anti_node_array.get(anti_label, [])
            line_nodes = self._line_node_array.get(anti_label, [])
            for subset in combos:
                p1 = subset[0]
                p2 = subset[1]

                subset_nodes = []
                line_eq = find_equation(p1, p2)
                print(f'Points {p1},{p2} have line eq: {line_eq}')
                for x1 in range(0, self.cols):
                    my_eq = line_eq.format(x1)
                    y1 = eval(my_eq)
                    if y1 == int(y1):
                        an1 = Point(x1, int(y1))
                        if Point.valid(an1, (0, self._rows), (0, self._cols)):
                            subset_nodes.append(an1)
                            if an1 not in self._line_nodes:
                                self._line_nodes.append(an1)
                ln_string = f'Points {p1},{p2} have {len(subset_nodes)} line_nodes'
                if len(subset_nodes) > 0:
                    ln_string += ': [' + ', '.join([str(x) for x in subset_nodes]) + ']'
                print(ln_string)
                for n in subset_nodes:
                    if n not in line_nodes:
                        line_nodes.append(n)
            self._line_node_array.update({anti_label: line_nodes})


    def get_value(self,
                  p: Point,
                  default: bool = False) -> str:
        base_value = self._dict.get(p, '.')
        antenna_value = None
        anti_node_value = None
        line_node_value = None

        for ant_label, ant_list in self._antenna_array.items():
            if p in ant_list:
                antenna_value = ant_label
                break

        for anti_node_label, anti_node_list in self._anti_node_array.items():
            if p in anti_node_list:
                anti_node_value = anti_node_label
                break

        for line_node_label, line_node_list in self._line_node_array.items():
            if p in line_node_list:
                line_node_value = line_node_label
                break


        if antenna_value is not None:
            return antenna_value
        if anti_node_value is not None:
            if default:
                return '#'
            return anti_node_value
        if line_node_value is not None:
            if default:
                return '#'
            return line_node_value
        return base_value


def find_equation(p1: Point,
                  p2: Point) -> str | None:
    if p1.x == p2.x:
        return None

    m = (p2.y - p1.y) / (p2.x - p1.x)
    b = p1.y - (m * p1.x)

    return f'{m:.2f} * {{}} + {b:.2f}'


def get_anti_label(label: str) -> str:
    import re
    p = re.compile(r'[a-zA-Z]')
    if p.fullmatch(label):
        return label.swapcase()
    for k, v in anti_node_labels.items():
        if label == k:
            return v
        elif label == v:
            return k
    return ''


def read_file(file_name_str: str) -> AntennaGrid:
    with open(file_name_str, 'r') as f:
        lines = f.readlines()
        my_grid = AntennaGrid(len(lines), len(lines[0].strip()))
        my_grid.read_file(lines)
        return my_grid


def part1(file_name: str):
    grid = read_file(file_name)
    grid.find_antinodes()
    # print(grid)
    total = len(grid.antinodes)
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {total}')


def part2(file_name: str):
    grid = read_file(file_name)
    grid.find_antinodes()
    grid.find_line_nodes()
    print(grid)
    an = grid.antinodes
    an.extend(grid.line_nodes)
    total = len(set(an))
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {total}')


if __name__ == '__main__':
    # part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
    # compare_points(((0, 13),(1, 35)))
