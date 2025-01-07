import sys

data = {
    col + row * 1j: c
    for row, line in enumerate(sys.stdin.read().splitlines())
    for col, c in enumerate(line)
}

dir = -1j
pos = next(k for k, v in data.items() if v == "^")
visited = set()


while True:
    visited.add(pos)

    next_pos = pos + dir

    if next_pos not in data:
        break
    elif data[next_pos] == "#":
        dir *= 1j
        continue
    else:
        pos = next_pos


p1 = len(visited)


print(p1)
