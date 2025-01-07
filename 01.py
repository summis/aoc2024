import sys

data = [x.split() for x in sys.stdin.read().splitlines()]


def p1():
    left = [int(x[0]) for x in data]
    right = [int(x[1]) for x in data]

    return sum(abs(x - y) for x, y in zip(sorted(left), sorted(right)))


print(p1())
