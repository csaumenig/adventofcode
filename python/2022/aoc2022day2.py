from __future__ import annotations

rps_moves = {
    'A': 1,
    'X': 1,
    'B': 2,
    'Y': 2,
    'C': 3,
    'Z': 3
}

results_2 = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

results = {
    ('A', 'X'): 3,
    ('A', 'Y'): 6,
    ('A', 'Z'): 0,
    ('B', 'X'): 0,
    ('B', 'Y'): 3,
    ('B', 'Z'): 6,
    ('C', 'X'): 6,
    ('C', 'Y'): 0,
    ('C', 'Z'): 3
}


def get_move(result: int,
             opp: str) -> str:
    for x in ('X','Y','Z'):
        if results.get((opp, x)) == result:
            return x
    return ''


def part1(file_name: str):
    score = 0
    with open(file_name, 'r') as f:
        lines = f.read()
        for line in lines.split('\n'):
            moves = line.split(' ')
            opp = moves[0]
            me = moves[1]
            me_value = rps_moves.get(me)
            result = results.get((opp, me))
            score += (me_value + result)
            #print(f'{opp} : {me}[{me_value}] -> result: {result}')
    print(f'AOC 2022 Day 2 Part 1: {score}')


def part2(file_name: str):
    # X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
    score = 0
    with open(file_name, 'r') as f:
        lines = f.read()
        for line in lines.split('\n'):
            moves = line.split(' ')
            opp = moves[0]
            result = results_2.get(moves[1])
            me = get_move(result, opp)
            me_value = rps_moves.get(me)
            score += (me_value + result)
            # print(f'opp: [{opp}]\t me: [{me}({me_value})]\t result: [{result}]\tscore: [{me_value + result}]')
    print(f'AOC 2022 Day 2 Part 2: {score}')


if __name__ == '__main__':
    # part1('../../resources/2022/inputd2-a.txt')
    part1('../../resources/2022/inputd2.txt')
    # part2('../../resources/2022/inputd2-a.txt')
    part2('../../resources/2022/inputd2.txt')