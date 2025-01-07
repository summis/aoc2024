import re
import sys

pattern = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"
matches = re.findall(pattern, sys.stdin.read())
scores = []

for match in matches:
    xa, ya, xb, yb, X, Y = map(int, match)

    # System of equations:
    # na * xa + nb * xb = X
    # na * ya + nb * yb = Y
    #
    # Solve for na and nb
    # na = (Y * xb - X * yb) / (ya * xb - xa * yb)
    # nb = (X - na * xa) / xb
    na = (Y * xb - X * yb) / (ya * xb - xa * yb)
    nb = (X - na * xa) / xb

    if na.is_integer() and nb.is_integer() and na <= 100 and nb <= 100:
        scores.append(3 * na + nb)

print(sum(scores))

scores = []

for match in matches:
    xa, ya, xb, yb, X, Y = map(int, match)
    X += 10000000000000
    Y += 10000000000000

    na = (Y * xb - X * yb) / (ya * xb - xa * yb)
    nb = (X - na * xa) / xb

    if na.is_integer() and nb.is_integer():
        scores.append(3 * na + nb)

print(int(sum(scores)))
