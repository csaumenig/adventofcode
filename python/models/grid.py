from __future__ import annotations


class Grid:
    def __init__(self,
                 rows: int,
                 cols: int) -> None:
        self._rows = rows
        self._cols = cols
        self._dict: dict[tuple[int, int], any] = {}

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
            for k, v in self._dict.items():
                s += f'{k}: {v}'
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
        row: int = 0
        for line in file_lines:
            col = 0
            while col < len(line.strip()):
                self._dict.update({(row, col): line[col].strip()})
                col += 1
            row += 1


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
        for y1 in range(0, self.rows) :
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

