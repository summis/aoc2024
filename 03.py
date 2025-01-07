import re
import sys

data = sys.stdin.read()
regex = r"mul\((\d+),(\d+)\)"


def p1():
    return sum(int(x) * int(y) for x, y in re.findall(regex, data))


print(p1())
