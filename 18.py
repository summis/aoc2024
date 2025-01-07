import math
import sys

bytes = [tuple(map(int, x.split(","))) for x in sys.stdin.read().splitlines()]


def best_time_to_target(target, byte_count):
    max_x, max_y = target

    start = (0, 0)
    todo = {start}

    distances = {(x, y): math.inf for x in range(max_x + 1) for y in range(max_y + 1)}
    distances[start] = 0

    corrupted = bytes[:byte_count]

    while todo:
        pos = min(todo, key=distances.get)
        todo.remove(pos)
        x, y = pos

        for new in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            new_x, new_y = new

            if new_x < 0 or new_x > max_x:
                continue

            if new_y < 0 or new_y > max_y:
                continue

            if new in corrupted:
                continue

            if distances[pos] + 1 < distances[new]:
                distances[new] = distances[pos] + 1
                todo.add(new)

    return distances[target]


print(best_time_to_target((70, 70), 1024))


def calculate_reachable_set(target, corrupted):
    max_x, max_y = target

    start = (0, 0)
    todo = [start]
    visited = set()

    while todo:
        pos = todo.pop()
        visited.add(pos)
        x, y = pos

        for new in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            new_x, new_y = new

            if new_x < 0 or new_x > max_x:
                continue

            if new_y < 0 or new_y > max_y:
                continue

            if new in corrupted:
                continue

            if new in visited:
                continue

            todo.append(new)

    return visited


a = 0
b = len(bytes)

while b - a > 1:
    mid = (a + b) // 2

    if (70, 70) in calculate_reachable_set((70, 70), set(bytes[:mid])):
        a = mid
    else:
        b = mid

print(bytes[a])
