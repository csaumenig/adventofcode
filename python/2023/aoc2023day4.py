from __future__ import annotations

YEAR = 2023
DAY = 4


def part1(file_name: str):
    total = 0
    with open(file_name, 'r') as f:
        card_no = 1
        for line in f.readlines():
            value = 0
            numbers: list[str] = line.strip().split(':')[1].strip().split('|')
            winners: list[int] = sorted([int(x.strip()) for x in numbers[0].strip().split(" ") if x.isnumeric()])
            mine: list[int] = sorted([int(x.strip()) for x in numbers[1].strip().split(" ") if x.isnumeric()])
            number_of_winners = len([x for x in winners if x in mine])
            if number_of_winners >= 1:
                value = 2**(number_of_winners-1)
            card_no += 1
            total += value
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {total}')


def part2(file_name: str):
    cards: dict[int, int] = {}
    with open(file_name, 'r') as f:
        card_no = 1
        for line in f.readlines():
            quant = cards.get(card_no, 0)
            if quant == 0:
                quant = 1
            cards.update({card_no: quant})
            numbers: list[str] = line.strip().split(':')[1].strip().split('|')
            winners: list[int] = sorted([int(x.strip()) for x in numbers[0].strip().split(" ") if x.isnumeric()])
            mine: list[int] = sorted([int(x.strip()) for x in numbers[1].strip().split(" ") if x.isnumeric()])
            number_of_winners = len([x for x in winners if x in mine])
            i = 1
            while i <= number_of_winners:
                card_quant = cards.get(card_no + i, 0)
                if card_quant == 0:
                    card_quant = 1
                cards.update({card_no + i: card_quant + quant})
                i += 1
            card_no += 1
    total = sum(cards.values())
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {total}')


if __name__ == '__main__':
    part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
