from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional
import re

YEAR = 2022
DAY = 7


class DirectoryObject(ABC):
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def print_self(self,
                   level: int = 0) -> None:
        pass

    @abstractmethod
    def __iter__(self):
        pass


class Directory(DirectoryObject):
    def __init__(self,
                 name: str,
                 size: int,
                 parent: Optional[Directory],
                 root: Optional[bool]) -> None:
        self._name = name
        self._size = size
        self._children: list[DirectoryObject] = []
        if root:
            self._root = root
        else:
            self._root = None
        if parent:
            self._parent: Directory = parent
        else:
            self._parent = None

    def name(self) -> str:
        return self._name

    def size(self) -> int:
        if self._size == 0:
            tmp_size = 0
            for dir_object in self._children:
                tmp_size += dir_object.size()
            self._size = tmp_size
        return self._size

    def parent(self) -> Directory:
        return self._parent

    def add_child(self,
                  child: DirectoryObject) -> None:
        self._children.append(child)

    def list(self) -> list[DirectoryObject]:
        return self._children

    def print_self(self,
                   level: int = 0) -> None:
        prefix = '- '
        for i in range(level):
            prefix = '  ' + prefix
        print(f'{prefix}{self._name} (dir, size={self._size})')
        for child in self._children:
            child.print_self(level + 1)

    def __iter__(self):
        yield self
        for child in self._children:
            for node in child:
                yield node

    def __repr__(self):
        return self._name


class File(DirectoryObject):
    def __init__(self,
                 name: str,
                 size: int,
                 parent: Directory) -> None:
        self._name = name
        self._size = size
        self._parent = parent

    def name(self) -> str:
        return self._name

    def size(self) -> int:
        return self._size

    def print_self(self,
                   level: int = 0) -> None:
        prefix = '- '
        for i in range(level):
            prefix = '  ' + prefix
        print(f'{prefix}{self._name} (file, size={self._size})')

    def parent(self) -> Directory:
        return self.parent()

    def __iter__(self):
        yield self

    def __repr__(self):
        return self._name


def create_file_tree(file_name: str) -> Directory:
    root_directory: Directory = None
    current_dir: Directory = None
    with open(file_name, 'r') as f:
        lines = f.read()
        for line in lines.split('\n'):
            if line.startswith('$'):
                r = re.findall(r'^\$\s(ls|cd)\s*(\S+)*$', line)
                line_parts = r[0]
                command = line_parts[0]
                if command == 'cd':
                    directory = line_parts[1]
                    if directory == '/':
                        # Create the root directory if it doesn't exist
                        if root_directory is None:
                            root_directory = Directory('/', 0, parent=None, root=True)
                        current_dir = root_directory
                    elif directory == '..':
                        current_dir = current_dir.parent()
                    else:
                        for dir_obj in current_dir.list():
                            if isinstance(dir_obj, Directory) and dir_obj.name() == directory:
                                current_dir = dir_obj
                                break
            elif line.startswith('dir'):
                r = re.findall(r'^(dir)\s(\S+)$', line)
                line_parts = r[0]
                dir_name = line_parts[1]
                this_directory = Directory(dir_name, 0, parent=current_dir, root=False)
                current_dir.add_child(this_directory)
            else:
                r = re.findall(r'^(\d+)\s(\S+)$', line)
                line_parts = r[0]
                file_size = int(line_parts[0])
                file_name = line_parts[1]
                this_file = File(file_name, file_size, current_dir)
                current_dir.add_child(this_file)
    return root_directory


def part1(file_name: str):
    total = 0
    file_directory = create_file_tree(file_name)
    file_directory.size()
    for d in file_directory:
        if isinstance(d, Directory):
            this_size = d.size()
            if this_size <= 100000:
                total += this_size
    print(f'AOC {YEAR} Day {DAY} Part 1: {total}')


def part2(file_name: str):
    total_disk_space = 70000000
    space_needed = 30000000
    file_directory = create_file_tree(file_name)
    used_space = file_directory.size()

    smallest_dir_to_get_space_name = None
    smallest_dir_to_get_space_size = None
    for d in file_directory:
        if isinstance(d, Directory):
            if (total_disk_space - (used_space - d.size())) >= space_needed:
                if smallest_dir_to_get_space_size is None or d.size() < smallest_dir_to_get_space_size:
                    smallest_dir_to_get_space_name = d.name()
                    smallest_dir_to_get_space_size = d.size()

    print(f'AOC {YEAR} Day {DAY} Part 2: {smallest_dir_to_get_space_name} => {smallest_dir_to_get_space_size}')


if __name__ == '__main__':
    part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt')