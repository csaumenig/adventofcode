from __future__ import annotations
from collections import namedtuple
import re

YEAR = 2015
DAY = 21

armor_pattern = r"Armor\:\s(\d+)"
damage_pattern = r"Damage\:\s(\d+)"
hit_point_pattern = r"Hit\sPoints\:\s(\d+)"
item_pattern = r"^([A-Za-z]+(\s\+[1-3])?)\s+(\d+)\s+(\d+)\s+(\d+)$"
type_pattern = r"^([A-Za-z]+)\:.*$"

boss_file = f'../../resources/{YEAR}/inputd{DAY}-boss.txt'
shop_file = f'../../resources/{YEAR}/inputd{DAY}-shop.txt'

item_limits_by_type = {
    'r': (0, 2),
    's': (0, 1),
    'w': (1, 1)
}

item_types = [('r', 'Ring'), ('s', 'Armor'), ('w', 'Weapon')]

PlayerStats = namedtuple('PlayerStats', ['h', 'd', 'a'])

Item = namedtuple('Item', ['n', 't', 'c', 'd', 'a'])


class Player:
    def __init__(self,
                 name: str,
                 base_hit_points: int,
                 base_damage: int,
                 base_armor: int) -> None:
        self._name = name
        self._hit_points = 0
        self._damage = 0
        self._armor = 0
        self._base_stats = PlayerStats(base_hit_points, base_damage, base_armor)
        self._combo: tuple[str, int, int, int] | None = None
        self._combo_name: str = ''
        self._spent: int = 0
        self.reset()

    @property
    def armor(self) -> int:
        return self._armor

    @property
    def combo(self):
        return self._combo

    @property
    def damage(self) -> int:
        return self._damage

    @property
    def hit_points(self) -> int:
        return self._hit_points

    @property
    def name(self) -> str:
        return self._name

    @property
    def spent(self) -> int:
        return self._spent

    def reset(self) -> None:
        self._hit_points, self._damage, self._armor = self._base_stats
        self._combo = None
        self._combo_name = ''
        self._spent = 0

    def hit(self,
            turn: int,
            other_player: Player) -> None:
        hit_cost = max((self._damage - other_player.armor), 1)
        other_player._hit_points -= hit_cost
        # print(f'Turn {turn}: {self.name} deals {self.damage}-{other_player.armor} = {hit_cost} damage; '
        #       f'{other_player.name} goes down to {other_player.hit_points} hit points.')

    def buy_combo(self,
                  cmb: tuple[str, int, int, int]):
        self._combo = cmb
        self._spent += cmb[1]
        self._armor += cmb[2]
        self._damage += cmb[3]


def item_type_name_by_code(code: str) -> str:
    for i_t in item_types:
        if i_t[0] == code:
            return i_t[1]
    raise ValueError(f'Unknown item code: {code}')


def item_type_code_by_name(name: str) -> str:
    for i_t in item_types:
        if i_t[1] == name:
            return i_t[0]
    raise ValueError(f'Unknown item name: {name}')


def sum_combo(cb: tuple) -> tuple[str, int, int, int]:
    c_name: list[str] = []
    c_cost: int = 0
    c_a: int = 0
    c_d: int = 0

    for c in cb:
        if isinstance(c, Item):
            c_name.append(c.n)
            c_cost += c.c
            c_a += c.a
            c_d += c.d
        else:
            if isinstance(c, tuple):
                for c_1 in c:
                    c_name.append(c_1.n)
                    c_cost += c_1.c
                    c_a += c_1.a
                    c_d += c_1.d
    return '/'.join(c_name), c_cost, c_a, c_d


def play(p, b) -> bool:
    t = 0
    # print(f'\n{p.name}[hp: {p.hit_points}, d: {p.damage}, a: {p.armor}, c: {p.combo}] vs.\n\t'
    #       f'{b.name}[hp: {b.hit_points}, d: {b.damage}, a: {b.armor}]\n\nFIGHT!\n')
    while p.hit_points > 0 and b.hit_points > 0:
        t += 1
        if t % 2 == 1:
            p.hit(t, b)
        else:
            b.hit(t, p)

    if p.hit_points <= 0:
        # print(f'{p.name} spent {p.spent} gold to lose in {t} turn(s)!!!!!')
        return False
    # print(f'{p.name} spent {p.spent} gold to win in {t} turn(s)!!!!!')
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
                    i_name = item_match.group(1)
                    i_cost = int(item_match.group(3))
                    i_damage = int(item_match.group(4))
                    i_armor = int(item_match.group(5))
                    shop_items.append(Item(i_name, i_type, i_cost, i_damage, i_armor))
    return shop_items


def load_boss(boss_name: str) -> Player:
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
    return Player(boss_name, b_h, b_d, b_a)


def load_item_combos(shop_items: list[Item]) -> list[tuple[str, int, int, int]]:
    from itertools import product
    from utils.util import all_comb_to_k
    rings = [s for s in shop_items if s.t == item_type_code_by_name('Ring')]
    armors = [s for s in shop_items if s.t == item_type_code_by_name('Armor')]
    weapons = [s for s in shop_items if s.t == item_type_code_by_name('Weapon')]

    ring_combos = all_comb_to_k(rings, 2)
    armor_combos = all_comb_to_k(armors, 1)
    combo_iterator = product(ring_combos, armor_combos, weapons)
    combo_list = list(combo_iterator)
    return sorted(list(map(sum_combo, combo_list)), key=lambda x: x[1])


def part1(player: Player,
          opponent: Player,
          combo_items: list[tuple[str, int, int, int]]) -> None:
    cost = 0
    if not play(player, opponent):
        for c in combo_items:
            player.reset()
            boss.reset()

            player.buy_combo(c)
            if play(player, opponent):
                cost = player.spent
                break
    print(f'AOC {YEAR} Day {DAY} Part 1: Cost: {cost}')


def part2(player: Player,
          opponent: Player,
          combo_items: list[tuple[str, int, int, int]]) -> None:
    cost = 0
    if play(player, opponent):
        for c in combo_items:
            player.reset()
            opponent.reset()
            cost = 0

            player.buy_combo(c)
            if not play(player, opponent):
                cost += player.spent
                break
    print(f'AOC {YEAR} Day {DAY} Part 2: Cost: {cost}')


if __name__ == '__main__':
    player_hit_points = 100
    p1 = Player('Mario', player_hit_points, 0, 0)
    boss = load_boss('Bowser')
    s_i = load_shop_items()
    i_c = load_item_combos(s_i)
    part1(p1, boss, i_c)

    i_c = sorted(i_c, key=lambda x: x[1], reverse=True)
    part2(p1, boss, i_c)
