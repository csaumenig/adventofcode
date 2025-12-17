from __future__ import annotations
from models.rpg import Spell, Warrior, Wizard, Player

YEAR = 2015
DAY = 22

spell_book = {
    # Spell('armor', 'cost', 'damage', 'effect_length', 'health', 'mana', 'name'
    Spell(armor=0, cost=53, damage=4, effect_length=0, health=0, mana=0, name='Magic Missile'),
    Spell(armor=0, cost=73, damage=2, effect_length=0, health=2, mana=0, name='Drain'),
    Spell(armor=7, cost=113, damage=0, effect_length=6, health=0, mana=0, name='Shield'),
    Spell(armor=0, cost=173, damage=3, effect_length=6, health=0, mana=0, name='Poison'),
    Spell(armor=0, cost=229, damage=0, effect_length=5, health=0, mana=101, name='Recharge')
}


def get_spell_by_name(name: str) -> Spell:
    for spell in spell_book:
        if spell.name == name:
            return spell
    raise ValueError(f'Spell with name {name} not found')

def report(player_1: Player,
           player_2: Player):
    for p in (player_1, player_2):
        print(f'{p.name} has {p.hit_points} hit points, {p.armor} armor, {p.mana} mana.')

def choose_spell(player1: Player) -> Spell:

    return get_spell_by_name('Magic Missile')


def play(player_1: Wizard,
         boss: Warrior,
         script: list) -> bool:
    t = 0
    print('')
    print(f'---------------------------------------')
    print(f'--- {player_1.name} vs. {boss.name} ---')
    print(f'---------------------------------------')
    print('')
    while player_1.hit_points > 0 and boss.hit_points > 0:
        t += 1
        if t % 2 == 1:
            print(f'--- {player_1.name} Turn: ---')
            report(player_1, boss)
            player_1.effect(boss, t)
            if player_1.hit_points > 0 and boss.hit_points > 0:
                player_1.cast(get_spell_by_name(script.pop(0)), boss, t)
        else:
            print(f'--- {boss.name} Turn: ---')
            report(player_1, boss)
            player_1.effect(boss, t)
            if player_1.hit_points > 0 and boss.hit_points > 0:
                boss.hit(player_1, t)
        print('')
        if player_1.hit_points <= 0:
            return False
    return True


def play_noscript(player_1: Wizard,
                  boss: Warrior) -> bool:
    t = 0
    print('')
    print(f'---------------------------------------')
    print(f'--- {player_1.name} vs. {boss.name} ---')
    print(f'---------------------------------------')
    print('')
    while player_1.hit_points > 0 and boss.hit_points > 0:
        t += 1
        if t % 2 == 1:
            print(f'--- {player_1.name} Turn: ---')
            report(player_1, boss)
            player_1.effect(boss, t)
            if player_1.hit_points > 0 and boss.hit_points > 0:
                player_1.cast(choose_spell(player_1), boss, t)
        else:
            print(f'--- {boss.name} Turn: ---')
            report(player_1, boss)
            player_1.effect(boss, t)
            if player_1.hit_points > 0 and boss.hit_points > 0:
                boss.hit(player_1, t)
        print('')
        if player_1.hit_points <= 0:
            return False
    return True


def example1():
    boss_hit_points=13
    boss_damage=8
    player_hit_points=10
    player_mana=250

    first_script = ['Poison', 'Magic Missile']

    player_1 = Wizard(name='Mario', hit_points=player_hit_points, mana=player_mana)
    boss = Warrior(name='Bowser', hit_points=boss_hit_points, damage=boss_damage)

    if play(player_1, boss, first_script):
        print(f'{player_1.name} spent {player_1.mana_spent} mana to defeat {boss.name}.')
    else:
        print(f'{boss.name} defeats {player_1.name}.')


def example2():
    boss_hit_points=14
    boss_damage=8
    player_hit_points=10
    player_mana=250

    second_script = ['Recharge', 'Shield', 'Drain', 'Poison', 'Magic Missile']

    player_1 = Wizard(name='Mario', hit_points=player_hit_points, mana=player_mana)
    boss = Warrior(name='Bowser', hit_points=boss_hit_points, damage=boss_damage)

    if play(player_1, boss, second_script):
        print(f'{player_1.name} spent {player_1.mana_spent} mana to defeat {boss.name}.')
    else:
        print(f'{boss.name} defeats {player_1.name}.')


def part1():
    boss_hit_points=55
    boss_damage=8
    player_hit_points=50
    player_mana=500

    player_1 = Wizard(name='Mario', hit_points=player_hit_points, mana=player_mana)
    boss = Warrior(name='Bowser', hit_points=boss_hit_points, damage=boss_damage)

    if play_noscript(player_1, boss):
        print(f'{player_1.name} spent {player_1.mana_spent} mana to defeat {boss.name}.')
    else:
        print(f'{boss.name} defeats {player_1.name}.')


if __name__ == '__main__':
    # example1()
    example2()
    # part1()