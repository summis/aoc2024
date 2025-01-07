import re
import sys

data = {
    col + row * 1j: c
    for row, s in enumerate(sys.stdin.read().splitlines())
    for col, c in enumerate(s)
}
rowCount = max(int(c.imag) for c in data) + 1
colCount = max(int(c.real) for c in data) + 1

target = "XMAS"


def create_all_strings():
    strings = []

    # Horizontal
    for row in range(rowCount):
        strings.append("".join(data[col + row * 1j] for col in range(colCount)))

    # Vertical
    for col in range(colCount):
        strings.append("".join(data[col + row * 1j] for row in range(rowCount)))

    # Diagonal, top left to bottom right
    left_to_right_diagonal_start_points = list(range(colCount)) + [
        row * 1j for row in range(1, rowCount)
    ]
    for point in left_to_right_diagonal_start_points:
        string = ""

        while point in data:
            string += data[point]
            point += 1 + 1j

        strings.append(string)

    # Diagonal, top right to bottom left
    right_to_left_diagonal_start_points = list(range(colCount)) + [
        colCount - 1 + row * 1j for row in range(1, rowCount)
    ]
    for point in right_to_left_diagonal_start_points:
        string = ""

        while point in data:
            string += data[point]
            point += -1 + 1j

        strings.append(string)

    return strings + ["".join(reversed(s)) for s in strings]


def p1():
    return sum(len(re.findall(target, s)) for s in create_all_strings())


def is_xmas(p):
    first_leg = "".join(data.get(p + i, "") for i in [-1 + -1j, 0, 1 + 1j])
    second_leg = "".join(data.get(p + i, "") for i in [-1 + 1j, 0, 1 - 1j])
    return (first_leg in ("MAS", "SAM")) and (second_leg in ("MAS", "SAM"))


def p2():
    return sum(is_xmas(p) for p in data)


print(p1(), p2())
