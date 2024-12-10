class Grid:
    def __init__(self,
                 rows: int,
                 cols: int) -> None:
        self._rows = rows
        self._cols = cols
        self._dict: dict[tuple[int, int], str] = {}

    def read_file(self,
                  file_lines: list[str]) -> None:
        row: int = 0
        for line in file_lines:
            col = 0
            while col < len(line.strip()):
                self._dict.update({(row, col): line[col]})
                col += 1
            row += 1

    @property
    def cols(self) -> int:
        return self._cols

    @property
    def rows(self) -> int:
        return self._rows

    def __repr__(self) -> str:
        s = ''
        if self._dict and len(self._dict) > 0:
            for k, v in self._dict.items():
                s += f'{k}: {v}\n'
        return s

    def __str__(self) -> str:
        return self.__repr__()
