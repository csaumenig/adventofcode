from __future__ import annotations


class Grid:
    def __init__(self,
                 rows: int,
                 cols: int) -> None:
        self._rows = rows
        self._cols = cols
        self._dict: dict[tuple[int, int], any] = {}
        self._neighbors: dict[tuple[int, int], list[tuple[int, int]]] = {}
        self.__init_neighbors()

    def __key(self) -> tuple[int, int, str]:
        import json
        return self._rows, self._cols, json.dumps(self._dict, default=str, ensure_ascii=True, separators=(',', ':'))

    def __hash__(self) -> int:
        return hash(self.__key())

    def __eq__(self, other) -> bool:
        if isinstance(other, Grid):
            return self.__key() == other.__key()
        return NotImplemented

    def __repr__(self) -> str:
        s = ''
        if self._dict and len(self._dict) > 0:
            last_row = 0
            for k, v in self._dict.items():
                if k[0] > last_row:
                    s += '\n'
                    last_row = k[0]
                s += self.__simple_print(k)
                # s += self.__grid_print(k)
                # s += self.__neighbor_print(k)
        return s

    def __str__(self) -> str:
        return self.__repr__()

    def __simple_print(self,
                       key: tuple[int, int]) -> str:
        return f'{self._dict[key]}'

    def __neighbor_print(self,
                         key: tuple[int, int]) -> str:
        return f'{key}: {len(self.neighbors(key))}'

    def __grid_print(self,
                     key: tuple[int, int]) -> str:
        return f'{key}: {self._dict[key]}'

    def __init_neighbors(self) -> None:
        for r in range(self._rows):
            for c in range(self._cols):
                p = (r, c)
                l: list[tuple[int, int]] = self.__gen_neighbors(p)
                self._neighbors.update({p: l})

    def __gen_neighbors(self,
                        p: tuple[int, int]) -> list[tuple[int, int]]:
        l: list[tuple[int, int]] = []
        r_s = p[0]
        r_e = p[0]
        c_s = p[1]
        c_e = p[1]
        if p[0] > 0:
            r_s = p[0] - 1
        if p[0] < self.rows - 1:
            r_e = p[0] + 1

        if p[1] > 0:
            c_s = p[1] - 1
        if p[1] < self.cols - 1:
            c_e = p[1] + 1

        for r in range(r_s, r_e + 1):
            for c in range(c_s, c_e + 1):
                if p[0] != r or p[1] != c:
                    l.append((r, c))
        return l

    @property
    def cols(self) -> int:
        return self._cols

    @property
    def rows(self) -> int:
        return self._rows

    def set_value(self,
                  p: tuple[int, int],
                  v: any) -> None:
        self._dict[p] = v

    def value(self,
              p: tuple[int, int]) -> any:
        return self._dict.get(p, '')

    def neighbors(self,
                  p: tuple[int, int]) -> list[tuple[int, int]]:
        return self._neighbors.get(p, [])

    def read_file(self,
                  file_lines: list[str]) -> None:
        row: int = 0
        for line in file_lines:
            col = 0
            while col < len(line.strip()):
                self._dict.update({(row, col): line[col].strip()})
                col += 1
            row += 1

    def cells_by_value(self,
                       value: any) -> list[tuple[int, int]]:
        l: list[tuple[int, int]] = []
        for k, v in self._dict.items():
            if v == value:
                l.append(k)
        return l

    @staticmethod
    def new_from_file(file_name: str) -> Grid:
        cols = 0
        rows = 0
        tmp: list[str] = []
        with open(file_name, 'r') as f:
            for l in f.readlines():
                line = l.strip()
                if line != '':
                    rows += 1
                    tmp.append(line)

                if cols == 0:
                    cols = len(line)
        g = Grid(rows, cols)
        g.read_file(tmp)
        return g


class Point:
    def __init__(self,
                 x: int,
                 y: int) -> None:
        self._x = x
        self._y = y

    def __key(self) -> tuple[int, int]:
        return self._x, self._y

    def __hash__(self) -> int:
        return hash(self.__key())

    def __eq__(self, other) -> bool:
        if isinstance(other, Point):
            return self.__key() == other.__key()
        return NotImplemented

    def __repr__(self) -> str:
        return f'Point(x={self.x}, y={self.y})'

    def __str__(self) -> str:
        return self.__repr__()

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    @staticmethod
    def valid(p: Point,
              x_range: tuple[int, int],
              y_range: tuple[int, int]):
        if p:
            if p.x in range(x_range[0], x_range[1]) and p.y in range(y_range[0], y_range[1]):
                return True
        return False


class GridXY:
    def __init__(self,
                 rows: int,
                 cols: int) -> None:
        self._rows = rows
        self._cols = cols
        self._dict: dict[Point, any] = {}

    def __key(self) -> tuple[int, int, str]:
        import json
        return self._rows, self._cols, json.dumps(self._dict, default=str, ensure_ascii=True, separators=(',', ':'))

    def __hash__(self) -> int:
        return hash(self.__key())

    def __eq__(self, other) -> bool:
        if isinstance(other, GridXY):
            return self.__key() == other.__key()
        return NotImplemented

    def __repr__(self) -> str:
        s = ''
        for y1 in range(0, self.rows):
            line = ''
            for x1 in range(0, self.cols):
                line += self._dict.get(Point(x1, y1))
            s += line + '\n'
        return s

    def __str__(self) -> str:
        return self.__repr__()

    @property
    def cols(self) -> int:
        return self._cols

    @property
    def rows(self) -> int:
        return self._rows

    def read_file(self,
                  file_lines: list[str]) -> None:
        y1: int = 0
        for line in file_lines:
            x1 = 0
            while x1 < len(line.strip()):
                key = Point(x1, y1)
                self._dict[key] = line[x1].strip()
                x1 += 1
            y1 += 1
