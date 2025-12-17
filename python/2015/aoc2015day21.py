from __future__ import annotations
import re

from models.rpg import Item, ItemType, Warrior

YEAR = 2015
DAY = 21

armor_pattern = r"Armor\:\s(\d+)"
damage_pattern = r"Damage\:\s(\d+)"
hit_point_pattern = r"Hit\sPoints\:\s(\d+)"
item_pattern = r"^([A-Za-z]+(\s\+[1-3])?)\s+(\d+)\s+(\d+)\s+(\d+)$"
type_pattern = r"^([A-Za-z]+)\:.*$"

boss_file = f'../../resources/{YEAR}/inputd{DAY}-boss.txt'
shop_file = f'../../resources/{YEAR}/inputd{DAY}-shop.txt'

armor = ItemType(name='Armor', code='s')
ring = ItemType(name='Ring', code='r')
weapon = ItemType(name='Weapon', code='w')

item_types = [ armor, ring, weapon ]

item_limits_by_type = {
    armor: (0, 1),
    ring: (0, 2),
    weapon: (1, 1)
}

def item_type_name_by_code(code: str) -> str:
    for i_t in item_types:
        if i_t.code == code:
            return i_t.name
    raise ValueError(f'Unknown item code: {code}')


def item_type_code_by_name(name: str) -> str:
    for i_t in item_types:
        if i_t.name == name:
            return i_t.code
    raise ValueError(f'Unknown item name: {name}')


def sum_combo(cb: tuple) -> tuple[str, int, int, int]:
    c_name: list[str] = []
    c_cost: int = 0
    c_a: int = 0
    c_d: int = 0

    for c in cb:
        if isinstance(c, Item):
            c_name.append(c.name)
            c_cost += c.cost
            c_a += c.armor
            c_d += c.damage
        else:
            if isinstance(c, tuple):
                for c_1 in c:
                    c_name.append(c_1.name)
                    c_cost += c_1.cost
                    c_a += c_1.armor
                    c_d += c_1.damage
    return '/'.join(c_name), c_cost, c_a, c_d


def play(p, b) -> bool:
    t = 0
    while p.hit_points > 0 and b.hit_points > 0:
        t += 1
        if t % 2 == 1:
            p.hit(b, t)
        else:
            b.hit(p, t)

    if p.hit_points <= 0:
        return False
    return True


def load_shop_items() -> list[Item]:
    shop_items: list[Item] = []
    with open(shop_file) as f:
        i_type = ''
        for line in [l.strip() for l in f.readlines()]:
            type_match = re.match(type_pattern, line)
            if type_match:
                i_type = str(type_match.group(1))[0].lower().replace('a', 's')
            else:
                item_match = re.match(item_pattern, line)
                if item_match:
                    shop_items.append(Item(name=item_match.group(1),
                                           type=i_type,
                                           cost=int(item_match.group(3)),
                                           damage=int(item_match.group(4)),
                                           armor=int(item_match.group(5))))
    return shop_items


def load_boss(boss_name: str) -> Warrior:
    b_a, b_d, b_h = 0, 0, 0
    with open(boss_file) as f:
        for line in [l.strip() for l in f.readlines()]:
            armor_match = re.match(armor_pattern, line)
            if armor_match:
                b_a = int(armor_match.group(1))
            else:
                damage_match = re.match(damage_pattern, line)
                if damage_match:
                    b_d = int(damage_match.group(1))
                else:
                    hit_point_match = re.match(hit_point_pattern, line)
                    if hit_point_match:
                        b_h = int(hit_point_match.group(1))
    return Warrior(name=boss_name, armor=b_a, damage=b_d, hit_points=b_h)


def load_item_combos(shop_items: list[Item]) -> list[tuple[str, int, int, int]]:
    from itertools import product
    from utils.util import all_comb_to_k
    rings = [s for s in shop_items if s.type == item_type_code_by_name('Ring')]
    armors = [s for s in shop_items if s.type == item_type_code_by_name('Armor')]
    weapons = [s for s in shop_items if s.type == item_type_code_by_name('Weapon')]

    ring_combos = all_comb_to_k(rings, 2)
    armor_combos = all_comb_to_k(armors, 1)
    combo_iterator = product(ring_combos, armor_combos, weapons)
    combo_list = list(combo_iterator)
    return sorted(list(map(sum_combo, combo_list)), key=lambda x: x[1])


def part1(player_1: Warrior,
          opponent: Warrior,
          combo_items: list[tuple[str, int, int, int]]) -> None:
    cost = 0
    if not play(player_1, opponent):
        for c in combo_items:
            player_1.reset()
            boss.reset()

            player_1.buy_combo(c)
            if play(player_1, opponent):
                cost = player_1.spent
                break
    print(f'AOC {YEAR} Day {DAY} Part 1: Cost: {cost}')


def part2(player_1: Warrior,
          opponent: Warrior,
          combo_items: list[tuple[str, int, int, int]]) -> None:
    cost = 0
    if play(player_1, opponent):
        for c in combo_items:
            player_1.reset()
            opponent.reset()
            cost = 0
            player_1.buy_combo(c)
            if not play(player_1, opponent):
                cost += player_1.spent
                break
    print(f'AOC {YEAR} Day {DAY} Part 2: Cost: {cost}')


if __name__ == '__main__':
    player_hit_points = 100
    p1 = Warrior(name='Mario', hit_points=player_hit_points, armor=0, damage=0)
    boss = load_boss('Bowser')
    s_i = load_shop_items()
    i_c = load_item_combos(s_i)
    part1(p1, boss, i_c)

    i_c = sorted(i_c, key=lambda x: x[1], reverse=True)
    part2(p1, boss, i_c)
