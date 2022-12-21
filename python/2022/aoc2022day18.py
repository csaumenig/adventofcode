from __future__ import annotations
from dataclasses import dataclass
from functools import total_ordering
import re

YEAR = 2022
DAY = 18

FACE_DEFINITIONS = {
    'front':  ['fld', 'frd', 'flt', 'frt'],
    'top':    ['flt', 'frt', 'blt', 'brt'],
    'right':  ['frt', 'frd', 'brt', 'brd'],
    'bottom': ['fld', 'frd', 'bld', 'brd'],
    'left':   ['flt', 'fld', 'blt', 'bld'],
    'back':   ['bld', 'brd', 'blt', 'brt']
}


class Cube:
    def __init__(self,
                 corner: tuple[int, int, int]):
        self._corners: dict[str, tuple[int, int, int]] = Cube.unit_cube_corners(corner)
        self._faces_visible: list[str] = ['top', 'right', 'left', 'bottom', 'front', 'back']

    def has_face(self,
                 face: list[tuple[int, int, int]]):
        pass

    def face_invisible(self,
                       face: str):
        self._faces_visible.remove(face)

    def count_faces(self):
        return len(self._faces_visible)

    def find_face_type(self, corner_list: list[tuple[int, int, int]]) -> str:
        list_corner_types: list[str] = []
        for corner in corner_list:
            for k, v in self._corners:
                if v[0] == corner[0] and v[1] == corner[1] and v[2] == corner[2]:
                    list_corner_types.append(k)
        for k, v in FACE_DEFINITIONS:
            if set(list_corner_types) == set(v):
                return k
        raise ValueError

    def __repr__(self):
        message: str = 'Cube ['
        if self._corners:
            message += ' corners = {'
            for k, v in self._corners.items():
                message += f'{k}: {v} '
            message += '}'
        if self._faces_visible:
            message += ' faces_visible = ['
            message += ','.join(self._faces_visible)
            message += ']'
        message += ']'
        return message

    @staticmethod
    def unit_cube_corners(corner: tuple[int, int, int]) -> dict[str, tuple[int, int, int]]:
        return {
            'fld': (corner[0], corner[1], corner[2]),
            'frd': (corner[0] + 1, corner[1], corner[2]),
            'flt': (corner[0], corner[1] + 1, corner[2]),
            'frt': (corner[0] + 1, corner[1] + 1, corner[2]),
            'bld': (corner[0], corner[1], corner[2] + 1),
            'brd': (corner[0] + 1, corner[1], corner[2] + 1),
            'blt': (corner[0], corner[1] + 1, corner[2] + 1),
            'brt': (corner[0] + 1, corner[1] + 1, corner[2] + 1)
        }


def part1(file_name: str):
    grid: list[Cube] = []
    with open(file_name, 'r') as f:
        data = f.read()
        for line in data.split('\n'):
            coords = line.split(',')
            grid.append(Cube((int(coords[0]), int(coords[1]), int(coords[2]))))

    print(grid)


def part2(file_name: str):
        print(f'AOC {YEAR} Day {DAY} Part 2')


if __name__ == '__main__':
    part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
