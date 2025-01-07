import sys

data = {
    col + row * 1j: int(c)
    for row, s in enumerate(sys.stdin.read().splitlines())
    for col, c in enumerate(s)
}

trailheads = {k for k, v in data.items() if v == 0}


def climb(start):
    todo = [start]
    visited = set()

    while todo:
        pos = todo.pop()
        visited.add(pos)

        for delta in [1, -1, 1j, -1j]:
            new_pos = pos + delta
            if (
                new_pos in data
                and new_pos not in visited
                and data[new_pos] == data[pos] + 1
            ):
                todo.append(new_pos)

    return visited


total = 0
for trailhead in trailheads:
    total += sum(1 for pos in climb(trailhead) if data[pos] == 9)

print(total)
