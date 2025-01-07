import sys
from itertools import combinations

data = [[int(x) for x in y.split()] for y in sys.stdin.read().splitlines()]


def calculate_diffs(x):
    return [x - y for x, y in zip(x[1:], x)]


def is_safe(x):
    diffs = calculate_diffs(x)
    return all(d in [1, 2, 3] for d in diffs) or all(-d in [1, 2, 3] for d in diffs)


def p1():
    return len([row for row in data if is_safe(row)])


def is_safe_with_tolerance(x):
    return any(is_safe(list(combo)) for combo in combinations(x, len(x) - 1))


def p2():
    return len([row for row in data if is_safe_with_tolerance(row)])


print(p1(), p2())
