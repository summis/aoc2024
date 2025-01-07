import sys
from collections import defaultdict

data = [x.split() for x in sys.stdin.read().splitlines()]
left = [int(x[0]) for x in data]
right = [int(x[1]) for x in data]


def p1():
    return sum(abs(x - y) for x, y in zip(sorted(left), sorted(right)))


def p2():
    frequency = defaultdict(int)

    for r in right:
        frequency[r] += 1

    return sum(l * frequency[l] for l in left)


print(p1(), p2())
