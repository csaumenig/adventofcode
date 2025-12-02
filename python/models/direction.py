from __future__ import annotations
from collections import namedtuple
from enum import unique, Enum

DirectionInfo = namedtuple("DirectionInfo", ["direction", "angle"])


class Direction(Enum):
    EASTSOUTHEAST = DirectionInfo('ESE', 337.5)
    SOUTHEAST = DirectionInfo('SE', 315)
    SOUTHSOUTHEAST = DirectionInfo('SSE', 292.5)
    SOUTH = DirectionInfo('S', 270)
    SOUTHSOUTHWEST = DirectionInfo('SSW', 247.5)
    SOUTHWEST = DirectionInfo('SW', 225)
    WESTSOUTHWEST = DirectionInfo('WSW', 202.5)
    WEST = DirectionInfo('W', 180)
    WESTNORTHWEST = DirectionInfo('WNW', 157.5)
    NORTHWEST = DirectionInfo('NW', 135)
    NORTHNORTHWEST = DirectionInfo('WNW', 112.5)
    NORTH = DirectionInfo('N', 90)
    NORTHNORTHEAST = DirectionInfo('NNE', 67.5)
    NORTHEAST = DirectionInfo('NE', 45)
    EASTNORTHEAST = DirectionInfo('ENE', 22.5)
    EAST = DirectionInfo('E', 0)


def find_by_angle(angle) -> Direction:
    members = Direction.__members__
    for name, member in members.items():
        if member.value.angle == angle:
            return member
    raise ValueError('No direction found')


def turn(start: Direction,
         turn_angle) -> Direction:
    new_angle = (start.value.angle + turn_angle) % 360
    return find_by_angle(new_angle)


if __name__ == '__main__':
    print(turn(Direction.SOUTH, 90))
    print(turn(Direction.EAST, -90))
    print(turn(Direction.NORTHEAST, -90))