from enum import Enum, unique
from math import floor
from typing import Optional
import json


CHUNK_CHARS: dict[str, tuple[str, int, int]] = {
    '(': (')', 3, 1),
    '[': (']', 57, 2),
    '{': ('}', 1197, 3),
    '<': ('>', 25137, 4)
}

@unique
class LineType(Enum):
    INCOMPLETE = 1
    CORRUPTED = 2


def part1(input_str: str) -> None:
    score = 0
    line_num = 1
    for line in input_str.split('\n'):
        line_type, expected, found = process_line_part1(line)
        if line_type == LineType.CORRUPTED:
            print(f'Line {line_num}: Expected: {expected}, but found: {found}')
            score += get_score_part1(found)
        line_num += 1
    print(f'Day 10 Part 1: Total Syntax Error Score = {score}')


def part2(input_str: str) -> None:
    scores: list[int] = []
    line_num = 1
    for line in input_str.split('\n'):
        try:
            expected = process_line_part2(line)
            scores.append(get_score_part2(expected))
        except ValueError:
            line_num += 1
            continue
        line_num += 1
    # print(scores)
    scores = sorted(scores)
    # print(scores)
    middle = floor(len(scores)/2)
    middle_score = scores[middle]
    print(f'Day 10 Part 2: Middle Completion Score = {middle_score}')


def process_line_part1(line: str) -> tuple[LineType, str, str]:
    expected: list[str] = []
    for character in line:
        if character in CHUNK_CHARS.keys():
            expected.append(CHUNK_CHARS.get(character)[0])
        else:
            if character != expected[-1]:
                return LineType.CORRUPTED, expected[-1], character
            expected.pop()
    return LineType.INCOMPLETE, '', ''


def process_line_part2(line: str) -> list[str]:
    expected: list[str] = []
    for character in line:
        if character in CHUNK_CHARS.keys():
            expected.append(CHUNK_CHARS.get(character)[0])
        else:
            if character != expected[-1]:
                raise ValueError('Corrupted')
            expected.pop()
    expected.reverse()
    return expected


def get_score_part1(found: str) -> int:
    for v in CHUNK_CHARS.values():
        if v[0] == found:
            return v[1]
    return 0


def get_score_part2(expected: list[str]) -> int:
    score = 0
    for character in expected:
        for v in CHUNK_CHARS.values():
            if v[0] == character:
                score = (score * 5) + v[2]
                break
    return score


if __name__ == "__main__":
    with open('../../resources/2021/inputd10a.txt') as f:
        input_str = f.read()
        part1(input_str)
        part2(input_str)

    with open('../../resources/2021/inputd10.txt') as f:
        input_str = f.read()
        part1(input_str)
        part2(input_str)
