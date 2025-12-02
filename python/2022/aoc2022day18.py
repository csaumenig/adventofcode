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

    def corners(self):
        return self._corners

    def faces_visible(self):
        return self._faces_visible

    def face_invisible(self,
                       face: str):
        self._faces_visible.remove(face)

    def faces(self):
        face_dict: dict[str, list[tuple[int,int,int]]] = {}
        for face_label in self.faces_visible():
            corner_list = []
            for point in FACE_DEFINITIONS.get(face_label):
                corner_list.append(self._corners.get(point))
            face_dict.update({face_label: corner_list})
        return face_dict

    def count_faces(self):
        return len(self._faces_visible)

    def find_face_type(self, corner_set: set[tuple[int, int, int]]) -> str:
        list_corner_types: list[str] = []
        for corner in corner_set:
            for k, v in self._corners.items():
                if v[0] == corner[0] and v[1] == corner[1] and v[2] == corner[2]:
                    list_corner_types.append(k)
        for k, v in FACE_DEFINITIONS.items():
            if set(list_corner_types) == set(v):
                return k
        raise ValueError

    def shares_face(self,
                    other: Cube):
        my_corner_set = set(self._corners.values())
        other_corner_set = set(other.corners().values())

        common_corners = my_corner_set.intersection(other_corner_set)

        if len(common_corners) == 4:
            my_face_type = self.find_face_type(common_corners)
            self.face_invisible(my_face_type)
            other_face_type = other.find_face_type(common_corners)
            other.face_invisible(other_face_type)

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
    import itertools
    grid: list[Cube] = []
    with open(file_name, 'r') as f:
        data = f.read()
        for line in data.split('\n'):
            coords = line.split(',')
            grid.append(Cube((int(coords[0]), int(coords[1]), int(coords[2]))))
    for comb in itertools.combinations(grid, 2):
        comb[0].shares_face(comb[1])
    total_faces = sum(len(c.faces_visible()) for c in grid)
    print(f'AOC {YEAR} Day {DAY} Part 1: Total Faces: {total_faces}')
    return grid


def part2(grid: list[Cube]):
    print(f'AOC {YEAR} Day {DAY} Part 2: ')
    for c in grid:
        for k, v in c.faces().items():
            print(f'{k}: {v}')
    import numpy as np
    from mpl_toolkits.mplot3d import Axes3D
    from mpl_toolkits.mplot3d.art3d import Poly3DCollection
    import matplotlib.pyplot as plt

    vertices = np.zeros([3, 8], dtype=int)
    vertices[0, :] = [1, 7, 5, 8, 2, 4, 6, 3]
    vertices[1, :] = [1, 7, 4, 6, 8, 2, 5, 3]
    vertices[2, :] = [6, 1, 5, 2, 8, 3, 7, 4]
    vertices = vertices - 1  # (adjust the indices by one since python starts with zero indexing)

    # Define an array with dimensions 8 by 3
    # 8 for each vertex
    # -> indices will be vertex1=0, v2=1, v3=2 ...
    # 3 for each coordinate
    # -> indices will be x=0,y=1,z=1
    cube = np.zeros([8, 3])

    # Define x values
    cube[:, 0] = [0, 0, 0, 0, 1, 1, 1, 1]
    # Define y values
    cube[:, 1] = [0, 1, 0, 1, 0, 1, 0, 1]
    # Define z values
    cube[:, 2] = [0, 0, 1, 1, 0, 0, 1, 1]

    # First initialize the fig variable to a figure
    fig = plt.figure()

    axes = Axes3D(fig)
    axes.set_xlim(0,10)
    axes.set_ylim(0, 10)
    axes.set_zlim(0, 10)

    # Add a 3d axis to the figure
    ax = fig.add_subplot(111, projection='3d')
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    plt.yticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    # plotting cube
    # Initialize a list of vertex coordinates for each face
    # faces = [np.zeros([5,3])]*3
    faces = []
    faces.append(np.zeros([5, 3]))
    faces.append(np.zeros([5, 3]))
    faces.append(np.zeros([5, 3]))
    faces.append(np.zeros([5, 3]))
    faces.append(np.zeros([5, 3]))
    faces.append(np.zeros([5, 3]))
    # Bottom face
    faces[0][:, 0] = [4, 4, 4, 4, 0]
    faces[0][:, 1] = [0, 4, 4, 0, 0]
    faces[0][:, 2] = [0, 0, 0, 0, 0]
    # Top face
    faces[1][:, 0] = [0, 0, 4, 4, 0]
    faces[1][:, 1] = [0, 4, 4, 0, 0]
    faces[1][:, 2] = [4, 4, 4, 4, 4]
    # Left Face
    faces[2][:, 0] = [0, 0, 0, 0, 0]
    faces[2][:, 1] = [0, 4, 4, 0, 0]
    faces[2][:, 2] = [0, 0, 4, 4, 0]
    # Left Face
    faces[3][:, 0] = [4, 4, 4, 4, 4]
    faces[3][:, 1] = [0, 4, 4, 0, 0]
    faces[3][:, 2] = [0, 0, 4, 4, 0]
    # front face
    faces[4][:, 0] = [0, 4, 4, 0, 0]
    faces[4][:, 1] = [0, 0, 0, 0, 0]
    faces[4][:, 2] = [0, 0, 4, 4, 0]
    # front face
    faces[5][:, 0] = [0, 4, 4, 0, 0]
    faces[5][:, 1] = [4, 4, 4, 4, 4]
    faces[5][:, 2] = [0, 0, 4, 4, 0]
    ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='k', alpha=.25))

    # plotting lines
    # ax.plot(cube[vertices[0, :], 0], cube[vertices[0, :], 1], cube[vertices[0, :], 2], color='r')
    # ax.plot(cube[vertices[1, :], 0], cube[vertices[1, :], 1], cube[vertices[1, :], 2], color='r')
    # ax.plot(cube[vertices[2, :], 0], cube[vertices[2, :], 1], cube[vertices[2, :], 2], color='r')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()


if __name__ == '__main__':
    grid_a = part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # grid = part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    part2(grid_a)
    # part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
