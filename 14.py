import enum
import math
import re
import sys
from collections import defaultdict

location = {}
velocity = {}

for particle, line in enumerate(sys.stdin.read().splitlines()):
    x, y, vx, vy = map(int, re.findall(r"-?\d+", line))
    location[particle] = x + y * 1j
    velocity[particle] = vx + vy * 1j


def move(t, width, height):
    ret = {}

    for particle, loc in location.items():
        new_loc = loc + t * velocity[particle]

        x = int(new_loc.real) % width
        y = int(new_loc.imag) % height

        ret[particle] = x + y * 1j

    return ret


class Quadrant(enum.Enum):
    UPPER_LEFT = enum.auto()
    UPPER_RIGHT = enum.auto()
    LOWER_LEFT = enum.auto()
    LOWER_RIGHT = enum.auto()
    MIDDLE = enum.auto()


def determine_quadrant(loc, width, height):
    upper = loc.imag < height // 2
    lower = loc.imag > height // 2
    left = loc.real < width // 2
    right = loc.real > width // 2

    if upper and left:
        return Quadrant.UPPER_LEFT

    if upper and right:
        return Quadrant.UPPER_RIGHT

    if lower and left:
        return Quadrant.LOWER_LEFT

    if lower and right:
        return Quadrant.LOWER_RIGHT

    return Quadrant.MIDDLE


def compute_quadrants(location, width, height):
    ret = defaultdict(int)

    for loc in location.values():
        ret[determine_quadrant(loc, width, height)] += 1

    return (v for k, v in ret.items() if k != Quadrant.MIDDLE)


width = 101
height = 103

print(math.prod(compute_quadrants(move(100, width, height), width, height)))


def compute_distance_sum(location):
    center = width // 2 + height // 2 * 1j
    return int(sum(abs(loc - center) for loc in location.values()))


def get_suspicious_arrangement():
    # If there is regular pattern, the sum of distances should be unsually low
    yield from (
        i for i in range(100000) if compute_distance_sum(move(i, width, height)) < 16000
    )


print(eastern_egg_time := next(get_suspicious_arrangement()))


def print_grid(location, width, height):
    for y in range(height):
        for x in range(width):
            if x + y * 1j in location.values():
                print("#", end="")
            else:
                print(".", end="")
        print()


print_grid(move(eastern_egg_time, width, height), width, height)
