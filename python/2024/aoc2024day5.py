from __future__ import annotations
from random import randint

YEAR = 2024
DAY = 5


def read_file(file_name: str) -> tuple[dict[int, list[int]], list[str]]:
    page_orders: dict[int, list[int]] = {}
    updates: list[str] = []
    with open(file_name, 'r') as f:
        for line in [x.strip() for x in f.readlines()]:
            line: str
            if '|' in line:
                l = line.split('|')
                sub_pages = page_orders.get(int(l[0]), [])
                sub_pages.append(int(l[1]))
                page_orders[int(l[0])] = sub_pages
            elif ',' in line:
                updates.append(line)
    return page_orders, updates

'''
Sort using quicksort
'''
def sort_pages(pages: list[int],
               page_orders: dict[int, list[int]]) -> list[int]:
    if len(pages) < 2:
        return pages

    low, high = [], []

    # Select your `pivot` element randomly
    pivot = pages[randint(0, len(pages) - 1)]
    after = page_orders.get(pivot, [])
    for item in pages:
        if item in after:
            high.append(item)
        else:
            low.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return sort_pages(low, page_orders) + sort_pages(high, page_orders)


def part1(file_name: str):
    total = 0
    page_orders, updates = read_file(file_name)
    for u in updates:
        valid = True
        pages = u.split(',')
        num_pages = len(pages)
        for i in range(len(pages)):
            if i > 0:
                if int(pages[i]) not in page_orders.get(int(pages[i-1]), []):
                    valid = False
                    break
        if valid:
            midpoint = num_pages // 2
            # print(pages)
            # print(f'midpoint = {int(pages[midpoint])}')
            total += int(pages[midpoint])
    print(f'AOC {YEAR} Day {DAY} Part 1: Total: {total}')


def part2(file_name: str):
    total = 0
    page_orders, updates = read_file(file_name)
    for u in updates:
        valid = True
        pages: list[int] = [int(z) for z in u.split(',')]
        num_pages = len(pages)
        for i in range(num_pages):
            if i > 0:
                if pages[i] not in page_orders.get(pages[i - 1], []):
                    valid = False
                    break
        if not valid:
            ordered_pages = sort_pages(pages=pages, page_orders=page_orders)
            midpoint = num_pages // 2
            # print(ordered_pages)
            # print(f'midpoint = {int(ordered_pages[midpoint])}')
            total += int(ordered_pages[midpoint])
    print(f'AOC {YEAR} Day {DAY} Part 2: Total: {total}')


if __name__ == '__main__':
    part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    part2(f'../../resources/{YEAR}/inputd{DAY}.txt')
