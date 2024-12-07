from __future__ import annotations

YEAR = 2024
DAY = 2


def check_report(report: list[int],
                 index: int = -1,
                 line_num: int = 0) -> bool:
    direction = 'eq'
    dup_report = [i for i in report]
    if index >= 0:
        dup_report.pop(index)
    index = 0
    while index < len(report) - 2:
        print(f'Report: {dup_report} Index: {index}')
        if abs(dup_report[index] - dup_report[index + 1]) > 3:
            # print(f'Line[{line_num}]: {report} = False')
            return False

        if index == 0:
            if dup_report[index] < dup_report[index + 1]:
                direction = 'asc'
            elif dup_report[index] > dup_report[index + 1]:
                direction = 'desc'
            else:
                # print(f'Line[{line_num}]: {report} = False')
                return False
        else:
            if dup_report[index] < dup_report[index + 1] and direction == 'desc':
                # print(f'Line[{line_num}]: {report} = False')
                return False
            elif dup_report[index] > dup_report[index + 1] and direction == 'asc':
                # print(f'Line[{line_num}]: {report} = False')
                return False
            elif dup_report[index] == dup_report[index + 1]:
                # print(f'Line[{line_num}]: {report} = False')
                return False
        index += 1
    # print(f'{report} = True')
    return True


def part1(file_name: str):
    total = 0
    line = 1
    with open(file_name, 'r') as f:
        for report in [x.strip().split(" ") for x in f.readlines()]:
            if check_report(report=[int(x) for x in report], index=-1, line_num=line):
                total += 1
            line += 1
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {total}')


def part2(file_name: str):
    total = 0
    line = 1
    with open(file_name, 'r') as f:
        for report in [x.strip().split(" ") for x in f.readlines()]:
            for index in range(-1, len(report) - 1):
                if check_report(report=[int(x) for x in report], index=index, line_num=line):
                    total += 1
                    break
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {total}')


def part2_exam(exam_file_name: str,
               src_file_name: str):
    failed: dict[int, int] = {}
    with open(exam_file_name, 'r') as f:
        for line in f.readlines():
            line_num = int(line[5:line.index(']')])
            failed.update({line_num: failed.get(line_num, 0) + 1})
    failed_lines = [k for k, v in failed.items() if v == 3]

    with open(src_file_name, 'r') as f2:
        line_num = 1
        for line in f2.readlines():
            if line_num in failed_lines:
                print(line.strip())
            line_num += 1
    # print(failed_lines)


if __name__ == '__main__':
    # part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
    # part2_exam(f'../../resources/{YEAR}/inputd{DAY}-b.txt',
    #            f'../../resources/{YEAR}/inputd{DAY}.txt')
