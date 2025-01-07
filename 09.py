import sys

data = list(map(int, sys.stdin.read()))

decoded = []
for i, x in enumerate(data):
    for y in range(x):
        if i % 2 == 0:
            decoded.append(i // 2)
        else:
            decoded.append(".")

dots = [i for i, x in enumerate(decoded) if x == "."]
chars = [i for i, x in enumerate(decoded) if x != "."]
swaps = ((from_, to) for from_, to in zip(reversed(chars), dots) if from_ > to)

ordered = [*decoded]
for from_index, to_index in swaps:
    ordered[to_index] = ordered[from_index]
    ordered[from_index] = "."

print(sum(i * int(x) for i, x in enumerate(ordered) if x != "."))


free_space = {}
used_space = {}
files = []

for i, x in enumerate(data):
    _id = i // 2
    if i % 2 == 0:
        files.append(_id)
        used_space[_id] = x
    else:
        free_space[_id] = x


moves = {destination: [] for destination in files}
for source in reversed(files):
    data = used_space[source]
    for destination in files[:source]:
        capacity = free_space[destination]
        if data <= capacity:
            moves[destination].append(source)
            free_space[destination] -= data
            break


def expand():
    moved_files = set(y for x in moves.values() for y in x)

    for file in files:
        yield from ["." if file in moved_files else file] * used_space[file]
        yield from (source for source in moves[file] for _ in range(used_space[source]))
        yield from "." * free_space.get(file, 0)


print(sum(i * x for i, x in enumerate(expand()) if x != "."))
