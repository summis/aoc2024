import sys

data = {
    col + row * 1j: int(c)
    for row, s in enumerate(sys.stdin.read().splitlines())
    for col, c in enumerate(s)
}
trailheads = {k for k, v in data.items() if v == 0}


def find_neighbors(pos):
    return [
        pos + delta
        for delta in [1, -1, 1j, -1j]
        if pos + delta in data and data[pos + delta] == data[pos] + 1
    ]


def calculate_reachable(start):
    todo = [start]
    visited = set()

    while todo:
        pos = todo.pop()
        visited.add(pos)
        for n in find_neighbors(pos):
            if n not in visited:
                todo.append(n)

    return visited


def calculate_trail_ends(current):
    yield current
    yield from (
        end for pos in find_neighbors(current) for end in calculate_trail_ends(pos)
    )


for scoring in (calculate_reachable, calculate_trail_ends):
    print(sum(sum(data[end] == 9 for end in scoring(start)) for start in trailheads))
