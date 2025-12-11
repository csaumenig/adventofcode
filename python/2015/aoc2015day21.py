from __future__ import annotations
from collections import namedtuple
import re

YEAR = 2015
DAY = 21

item_pattern = r"^([A-Za-z]+(\s\+[1-3])?)\s+(\d+)\s+(\d+)\s+(\d+)$"
type_pattern = r"^([A-Za-z]+)\:.*$"

item_limits_by_type = {
    'r': (0, 2),
    's': (0, 1),
    'w': (1, 1)
}

item_types = [('r', 'Ring'), ('s', 'Armor'), ('w', 'Weapon')]

PlayerStats = namedtuple('PlayerStats', ['h', 'd', 'a'])
Item = namedtuple('Item', ['n', 't', 'c', 'd', 'a'])


def item_type_by_code(code: str) -> str:
    for i_t in item_types:
        if i_t[0] == code:
            return i_t[1]
    raise ValueError(f'Unknown item code: {code}')


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
        self._items: list[Item] = []
        self._spent: int = 0
        self.reset()

    @property
    def armor(self) -> int:
        return self._armor
    @property
    def damage(self) -> int:
        return self._damage
    @property
    def hit_points(self) -> int:
        return self._hit_points
    @property
    def items(self) -> str:
        return ', '.join([f'<{it.n} ({item_type_by_code(it.t)})> [a: {it.a}, d: {it.d}]' for it in self._items])
    @property
    def name(self) -> str:
        return self._name
    @property
    def spent(self) -> int:
        return self._armor

    def reset(self) -> None:
        self._hit_points, self._damage, self._armor = self._base_stats

    def hit(self,
            turn: int,
            other_player: Player) -> None:
        hit_cost = max((self._damage - other_player.armor), 1)
        other_player._hit_points -= hit_cost
        print(f'Turn {turn}: {self.name} deals {self.damage}-{other_player.armor} = {hit_cost} damage; '
              f'{other_player.name} goes down to {other_player.hit_points} hit points.')

    def buy_item(self,
                 possible_item: Item) -> None:
        type_count = self.validate_buy(possible_item)
        if type_count == 0:
            self._items.append(possible_item)
            self._spent += possible_item.c
            self._armor += possible_item.a
            self._damage += possible_item.d
        else:
            print(f'Unable to buy item: {possible_item.n}, you already own '
                  f'{type_count} {item_type_by_code(possible_item.t)}(s).')

    def item_type_count(self) -> dict:
        from collections import Counter
        type_list = [i.t for i in self._items]
        type_counts = Counter(type_list)
        return dict(type_counts.items())


    def validate_buy(self,
                     possible_item: Item) -> int:
        # Rules: 1 Weapon, 0-1 Armor, 0-2 Rings
        item_type_counts = self.item_type_count()
        # print(item_type_counts)
        count = item_type_counts.get(possible_item.t, 0)
        limit = item_limits_by_type.get(possible_item.t)
        if limit[0] <= count + 1 <= limit[1]:
            return 0
        return count


shop_items: list[Item] = []
ex_file = f'../../resources/{YEAR}/inputd{DAY}-shop.txt'
with open(ex_file) as f:
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
from operator import itemgetter
shop_items.sort(key = itemgetter(1, 2, 0))
from pprint import pprint
pprint(shop_items)

p1 = Player('Mario', 8, 5, 5)
boss = Player('Bowser', 12, 7, 2)


for item in shop_items:
    p1.buy_item(item)

t = 0
print(f'\n{p1.name}[hp: {p1.hit_points}, d: {p1.damage}, a: {p1.armor}, i: {p1.items}] vs.\n\t'
      f'{boss.name}[hp: {boss.hit_points}, d: {boss.damage}, a: {boss.armor}]\n\nFIGHT!\n')
while p1.hit_points > 0 and boss.hit_points > 0:
    t += 1
    if t % 2 == 1:
        p1.hit(t, boss)
    else:
        boss.hit(t, p1)

if p1.hit_points < 0:
    print(f'\n{boss.name} wins in {t} turns!!!!!')
else:
    print(f'{p1.name} spent {p1.spent} gold to win in {t} turn(s)!!!!!')
