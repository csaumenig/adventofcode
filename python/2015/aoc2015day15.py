from __future__ import annotations
import re

YEAR = 2015
DAY = 15


class Ingredient:
    INGREDIENT_REGEX = (r'^(?P<name>[A-Za-z]+)\:\scapacity\s(?P<capacity>\-?\d+)\,\sdurability\s'
                        r'(?P<durability>\-?\d+)\,\sflavor\s(?P<flavor>\-?\d+)\,\stexture\s(?P<texture>\-?\d+)\,'
                        r'\scalories\s(?P<calories>\-?\d+).*$')

    def __init__(self,
                 file_line: str) -> None:
        self._calories = None
        self._capacity = None
        self._durability = None
        self._flavor = None
        self._name = None
        self._texture = None

        match = re.search(Ingredient.INGREDIENT_REGEX, file_line)
        self._initial_specs = (int(match.group('calories')),
                               int(match.group('capacity')),
                               int(match.group('durability')),
                               int(match.group('flavor')),
                               int(match.group('texture')))

        self._initialize(match.group('name'),
                         int(match.group('calories')),
                         int(match.group('capacity')),
                         int(match.group('durability')),
                         int(match.group('flavor')),
                         int(match.group('texture')))

    def _initialize(self,
                    name: str,
                    calories: int,
                    capacity: int,
                    durability: int,
                    flavor: int,
                    texture: int) -> None:
        self._name = name
        self._calories = calories
        self._capacity = capacity
        self._durability = durability
        self._flavor = flavor
        self._texture = texture

    @property
    def name(self) -> str:
        return self._name

    @property
    def calories(self) -> int:
        return self._calories

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def durability(self) -> int:
        return self._durability

    @property
    def flavor(self) -> str:
        return self._flavor

    @property
    def texture(self) -> int:
        return self._texture

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return (f'{self._name}:\n  Capacity: {self.capacity}\n  Durability: {self.durability}\n  '
                f'Flavor: {self.flavor}\n  Texture: {self.texture}\n  Calories: {self.calories}\n')

    def scale(self,
              amount: int) -> None:
        self._calories = amount * self.calories
        self._capacity = amount * self.capacity
        self._durability = amount * self.durability
        self._flavor = amount * self.flavor
        self._texture = amount * self.texture

    def re_initialize(self) -> None:
        self._initialize(self.name,
                         self._initial_specs[0],
                         self._initial_specs[1],
                         self._initial_specs[2],
                         self._initial_specs[3],
                         self._initial_specs[4])

    @staticmethod
    def load_ingredients(file_name: str) -> list[Ingredient]:
        ingredients: list[Ingredient] = []
        with open(file_name, 'r') as f:
            for line in f.readlines():
                ingredients.append(Ingredient(line.strip()))
        return ingredients


def score(ingredients: list[Ingredient]) -> int:
    from math import prod
    attrs = (sum(i.capacity for i in ingredients),
             sum(i.durability for i in ingredients),
             sum(i.flavor for i in ingredients),
             sum(i.texture for i in ingredients))

    if all(x > 0 for x in attrs):
        return prod(attrs)
    else:
        return 0


def part1(ingredient_list: list[Ingredient]) -> None:
    from pprint import pprint
    from utils.util import find_sum

    winning_ingredients: dict[str, int] = {}
    max_score = 0
    for seq in find_sum(len(ingredient_list), 100):
        z = zip(ingredient_list, seq)
        recipe: dict[Ingredient, int] = dict(z)
        for k, v in recipe.items():
            k.scale(v)

        cur_score = score(ingredient_list)
        if cur_score > max_score:
            max_score = cur_score
            for k, v in recipe.items():
                winning_ingredients.update({k.name: v})

        for i in ingredient_list:
            i.re_initialize()

    pprint(winning_ingredients)
    print(f'AOC {YEAR} Day {DAY} Part 1: {max_score}')


def part2(ingredient_list: list[Ingredient],
          calorie_amount: int) -> None:
    from pprint import pprint
    from utils.util import find_sum

    winning_ingredients: dict[str, int] = {}
    max_score = 0
    for seq in find_sum(len(ingredient_list), 100):
        z = zip(ingredient_list, seq)
        recipe: dict[Ingredient, int] = dict(z)
        for k, v in recipe.items():
            k.scale(v)

        if sum(i.calories for i in ingredient_list) == calorie_amount:
            cur_score = score(ingredient_list)
            if cur_score > max_score:
                max_score = cur_score
                for k, v in recipe.items():
                    winning_ingredients.update({k.name: v})

        for i in ingredient_list:
            i.re_initialize()

    pprint(winning_ingredients)
    print(f'AOC {YEAR} Day {DAY} Part 1: {max_score}')

if __name__ == '__main__':
    roster_ex = Ingredient.load_ingredients(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    roster = Ingredient.load_ingredients(f'../../resources/{YEAR}/inputd{DAY}.txt')

    # part1(roster_ex)
    # part1(roster)

    part2(roster_ex, 500)
    part2(roster, 500)
