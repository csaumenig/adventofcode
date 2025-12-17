from __future__ import annotations
from collections import namedtuple


Item = namedtuple('Item', ['armor', 'cost', 'damage', 'name', 'type'])
ItemType = namedtuple('ItemType', ['code', 'name'])
PlayerStats = namedtuple('PlayerStats', ['armor', 'damage', 'hit_points', 'mana'])
Spell = namedtuple('Spell', ['armor', 'cost', 'damage', 'effect_length', 'health', 'mana', 'name'])

class Player:
    def __init__(self,
                 name: str,
                 armor: int = 0,
                 damage: int = 0,
                 hit_points: int = 0,
                 mana: int = 0) -> None:
        self._armor = 0
        self._damage = 0
        self._hit_points = 0
        self._mana = 0
        self._name = name
        self._base_stats = PlayerStats(armor=armor,
                                       damage=damage,
                                       hit_points=hit_points,
                                       mana=mana)
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
    def mana(self) -> int:
        return self._mana

    @property
    def name(self) -> str:
        return self._name

    def reset(self) -> None:
        self._armor = self._base_stats.armor
        self._damage = self._base_stats.damage
        self._hit_points = self._base_stats.hit_points
        self._mana = self._base_stats.mana


class Warrior(Player):
    def __init__(self,
                 name: str,
                 armor: int = 0,
                 damage: int = 0,
                 hit_points: int = 0) -> None:
        super().__init__(armor=armor, damage=damage, hit_points=hit_points, name=name)
        self._combo: tuple[str, int, int, int] | None = None
        self._combo_name: str = ''
        self._spent: int = 0
        self.reset()

    @property
    def combo(self):
        return self._combo

    @property
    def spent(self) -> int:
        return self._spent

    def reset(self) -> None:
        super().reset()
        self._combo = None
        self._combo_name = ''
        self._spent = 0

    def hit(self,
            other_player: Player,
            turn: int) -> None:
        hit_cost = max((self._damage - other_player.armor), 1)
        print(f'{self.name} does {hit_cost} damage to {other_player.name}')
        other_player._hit_points -= hit_cost

    def buy_combo(self,
                  cmb: tuple[str, int, int, int]):
        self._combo = cmb
        self._spent += cmb[1]
        self._armor += cmb[2]
        self._damage += cmb[3]


class Wizard(Player):
    def __init__(self,
                 name: str,
                 hit_points: int = 0,
                 mana: int = 0) -> None:
        super().__init__(armor=0, damage=0, hit_points=hit_points, mana=mana, name=name)
        self._active_spell_effects: dict[Spell, int] = {}
        self._mana_spent: int = 0
        self.reset()

    @property
    def active_spell_effects(self) -> dict[Spell, int]:
        return self._active_spell_effects

    @property
    def mana_spent(self) -> int:
        return self._mana_spent

    def reset(self) -> None:
        super().reset()
        self._active_spell_effects: dict[Spell, int] = {}
        self._mana_spent = 0

    def cast(self,
             spell: Spell,
             other_player: Player,
             turn: int) -> None:
        if spell.name in self._active_spell_effects:
            raise ValueError('You cannot cast the an active spell')

        print(f'{self.name} casts {spell.name}')
        if spell.effect_length == 0:
            if spell.damage > 0:
                hit_cost = max((spell.damage - other_player.armor), 1)
                other_player._hit_points -= hit_cost

            if spell.health > 0:
                self._hit_points += spell.health
        else:
            self._active_spell_effects[spell] = spell.effect_length

        self._mana -= spell.cost
        self._mana_spent += spell.cost

    def effect(self,
               other_player: Player,
               turn: int) -> None:
        d = self.active_spell_effects
        for spell, turns in self.active_spell_effects.items():
            if turns > 0:
                output = ''
                if spell.armor > 0:
                    output = f'{spell.name} adds {spell.armor} armor to {self.name}.'
                    self._armor = self._base_stats.armor + spell.armor

                if spell.damage > 0:
                    hit_cost = max((spell.damage - other_player.armor), 1)
                    output = f'{spell.name} does {hit_cost} damage to {other_player.name}.'
                    other_player._hit_points -= hit_cost

                if spell.mana > 0:
                    output = f'{spell.name} adds {spell.mana} mana to {self.name}.'
                    self._mana += spell.mana

                turns -= 1
                output += f' Its timer is now at {turns}'
                print(output)
            else:
                if spell.armor > 0:
                    self._armor = self._base_stats.armor
            d.update({spell: turns})
        self._active_spell_effects.update(d)
