import re
import sys

data = sys.stdin.read()

MULTIPLICATION_REGEX = r"mul\((\d+),(\d+)\)"


def p1():
    return sum(int(x) * int(y) for x, y in re.findall(MULTIPLICATION_REGEX, data))


CONTROL_REGEX = r"(mul\(\d+,\d+\)|do\(\)|don't\(\))"


def filter_enabled_intructions(s):
    enabled = True
    ret = ""

    for x in re.findall(CONTROL_REGEX, s):
        if x == "do()":
            enabled = True
        elif x == "don't()":
            enabled = False
        else:
            if enabled:
                ret += x

    return ret


def p2():
    return sum(
        int(x) * int(y)
        for x, y in re.findall(MULTIPLICATION_REGEX, filter_enabled_intructions(data))
    )


print(p1(), p2())
