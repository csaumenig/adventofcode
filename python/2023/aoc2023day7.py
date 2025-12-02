from __future__ import annotations
from collections import Counter
from enum import Enum, unique

YEAR = 2023
DAY = 7

card_value = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2
}


card_value_jokers = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'J': 1
}


class HandRank(Enum):
    FIVE_OF_A_KIND = 100
    FOUR_OF_A_KIND = 90
    FULL_HOUSE = 80
    THREE_OF_A_KIND = 70
    TWO_PAIR = 60
    ONE_PAIR = 50
    HIGH_CARD = 1
    NONE = 0
    UNRANKED = -1


class Hand:
    def __init__(self,
                 cards: str,
                 bid: int):
        self._cards = cards
        self._bid = bid
        self._rank = HandRank.NONE

    def __repr__(self):
        return f'cards: {self._cards}, bid: {self._bid}, rank:{self._rank}'

    def __str__(self):
        return self.__repr__()

    @property
    def cards(self):
        return self._cards

    @property
    def rank(self):
        return self._rank

    @property
    def bid(self):
        return self._bid

    def set_rank(self,
                 rank: HandRank) -> None:
        self._rank = rank

    def set_cards(self,
                  cards: str) -> None:
        self._cards = cards

    def copy(self):
        return Hand(self._cards,
                    self._bid)


def read_hands(file_name:str) -> list[Hand]:
    hands: list[Hand] = []
    with open(file_name, 'r') as f:
        for line in f.readlines():
            line_parts = line.split(' ')
            hands.append(Hand(line_parts[0],  int(line_parts[1])))
    return hands


def rank_hand(hand: Hand) -> None:
    hand_counter = Counter(hand.cards)
    if len(hand_counter) == 5:
        hand.set_rank(HandRank.HIGH_CARD)
    elif len(hand_counter) == 1:
        hand.set_rank(HandRank.FIVE_OF_A_KIND)
    elif len(hand_counter) == 2:
        if max(hand_counter.values()) == 4:
            hand.set_rank(HandRank.FOUR_OF_A_KIND)
        else:
            hand.set_rank(HandRank.FULL_HOUSE)
    elif len(hand_counter) == 3:
        if max(hand_counter.values()) == 3:
            hand.set_rank(HandRank.THREE_OF_A_KIND)
        else:
            hand.set_rank(HandRank.TWO_PAIR)
    else:
        hand.set_rank(HandRank.ONE_PAIR)


def rank_hand_joker(hand: Hand) -> None:
    if hand.cards.__contains__('J') is False:
        return rank_hand(hand)
    sorting_hand = hand.copy()

    hand_counter = Counter(sorting_hand.cards)
    cards_in_descending_order = sorted(hand_counter.keys(),
                                       key=lambda x: (hand_counter.get(x),
                                                      card_value_jokers.get(x)),
                                       reverse=True)
    replace_card = cards_in_descending_order[0]
    if replace_card == 'J':
        if hand_counter.get('J') == 5:
            replace_card = 'A'
        else:
            replace_card = cards_in_descending_order[1]
    sorting_hand.set_cards(sorting_hand.cards.replace('J', replace_card))
    rank_hand(sorting_hand)
    hand.set_rank(sorting_hand.rank)


def sort_my_hands(hands: list[Hand],
                  sorting_dict: dict[str, int]) -> list[Hand]:
    return sorted(hands,
                  key=lambda x: (x.rank.value,
                                 sorting_dict.get(x.cards[0]),
                                 sorting_dict.get(x.cards[1]),
                                 sorting_dict.get(x.cards[2]),
                                 sorting_dict.get(x.cards[3]),
                                 sorting_dict.get(x.cards[4])),
                  reverse=True)


def part1(file_name: str):
    total = 0
    hands = read_hands(file_name)
    for hand in hands:
        rank_hand(hand)
    sorted_hands = sort_my_hands(hands, card_value)

    i = 1
    for hand in sorted_hands[::-1]:
        total += i * hand.bid
        i += 1
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {total}')


def part2(file_name: str):
    total = 0
    hands = read_hands(file_name)
    for hand in hands:
        rank_hand_joker(hand)
    sorted_hands = sort_my_hands(hands, card_value_jokers)
    i = 1
    for hand in sorted_hands[::-1]:
        total += i * hand.bid
        i += 1
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {total}')


if __name__ == '__main__':
    # part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
