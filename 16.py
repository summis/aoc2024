import math
import sys
from collections import namedtuple

grid = {
    col + row * 1j: c
    for row, line in enumerate(sys.stdin.read().splitlines())
    for col, c in enumerate(line)
    if c != "#"
}

Node = namedtuple("Node", ["pos", "dir"])

graph = {}
start = Node(next(p for p in grid if grid[p] == "S"), 1)
todo = [start]

while todo:
    curr, *todo = todo
    if curr in graph:
        continue

    moves = []

    straight = Node(curr.pos + curr.dir, curr.dir)
    if straight.pos in grid:
        moves.append(straight)

    # Graph size optimization: turns are only interesting if
    # 1. The straight move is blocked
    # 2. The square after turn is not blocked
    right = Node(curr.pos, curr.dir * 1j)
    if right.pos + right.dir in grid or straight.pos not in grid:
        moves.append(right)

    left = Node(curr.pos, curr.dir * -1j)
    if left.pos + left.dir in grid or straight.pos not in grid:
        moves.append(left)

    graph[curr] = moves
    todo.extend(moves)


def find_paths():
    """
    Bellman-Ford variant that finds all shortest paths
    """
    distance = {x: math.inf if x != start else 0 for x in graph}
    previous = {
        x: set() for x in graph
    }  # Use set in case multiple paths have the same distance

    while True:
        connection_updated = False
        distance_updated = False

        for curr in graph:
            for new in graph[curr]:
                delta = 1 if new.dir == curr.dir else 1000

                if distance[curr] + delta == distance[new]:
                    distance[new] = distance[curr] + delta

                    if curr not in previous[new]:
                        previous[new].add(curr)
                        connection_updated = True

                elif distance[curr] + delta < distance[new]:
                    distance[new] = distance[curr] + delta
                    previous[new] = set([curr])
                    distance_updated = True

        if not connection_updated and not distance_updated:
            break

    return distance, previous


distance, previous = find_paths()
finish_nodes = [n for n in graph if grid[n.pos] == "E"]
best = min(map(distance.get, finish_nodes))

visited = set()

for finish in finish_nodes:
    if distance[finish] > best:
        continue

    todo = set([finish])
    while todo:
        node = todo.pop()
        visited.add(node.pos)

        for p in previous[node]:
            todo.add(p)

print(best, len(visited))
