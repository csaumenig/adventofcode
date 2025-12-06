from __future__ import annotations

YEAR = 2025
DAY = 6

def do_math(i, j, op):
    return op(i, j)

def part1(file_name: str) -> None:
    import re
    import operator
    with open(file_name, 'r') as f:
        operators = []
        lines = []
        for line in f.readlines():
            x = re.split(r"\s+", line.strip())
            if x[0] in ('*', '+'):
                operators = x
            else:
                lines.append(x)
        totals = []
        for l in lines:
            if len(totals) == 0:
                totals = [int(x) for x in l]
            else:
                for i in range(len(operators)):
                    o = operator.mul
                    if operators[i] == '+':
                        o = operator.add
                    totals[i] = do_math(totals[i], int(l[i]), o)
        total = sum(totals)
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {total}')


def part2(file_name: str) -> None:
    import re
    import operator
    with open(file_name, 'r') as f:
        operators = []
        lines = []
        max_len = 0
        for line in f.readlines():
            line = line.replace('\n', '')
            max_len = max(max_len, len(line))
            if re.match(r"[+*]", line):
                operators = re.split(r"\s+", line.strip())
            else:
                lines.append(line)
        lines = [line.rjust(max_len) for line in lines]

    #
    #
    #
    #         x = re.split(r"\s+", line.strip())
    #         if x[0] in ('*', '+'):
    #             operators = x
    #         else:
    #             lines.append(x)
    #     totals = []
    #     for l in lines:
    #         if len(totals) == 0:
    #             totals = [int(x) for x in l]
    #         else:
    #             for i in range(len(operators)):
    #                 o = operator.mul
    #                 if operators[i] == '+':
    #                     o = operator.add
    #                 totals[i] = do_math(totals[i], int(l[i]), o)
    #     total = sum(totals)
    # print(f'AOC {YEAR} Day {DAY} Part 2: Total: {total}')


if __name__ == '__main__':
    # part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    # part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
