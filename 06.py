import enum
import sys


class Outcome(enum.Enum):
    LOOP = enum.auto()
    OUT = enum.auto()


data = {
    col + row * 1j: c
    for row, line in enumerate(sys.stdin.read().splitlines())
    for col, c in enumerate(line)
}


def run_simulation(graph, pos, dir):
    visited = set()
    visited_turn_points = set()

    while True:
        visited.add(pos)

        next_pos = pos + dir

        if next_pos not in graph:
            return Outcome.OUT, visited
        elif graph[next_pos] == "#":
            if (pos, dir) in visited_turn_points:
                return Outcome.LOOP, visited

            visited_turn_points.add((pos, dir))
            dir *= 1j
            continue
        else:
            pos = next_pos


start_point = next(k for k, v in data.items() if v == "^")
start_dir = -1j

_, visited = run_simulation(data, start_point, start_dir)
p1 = len(visited)


def p2():
    loop_count = 0
    obstacle_positions = visited - {start_point}

    for point in obstacle_positions:
        updated_graph = data | {point: "#"}
        outcome, _ = run_simulation(updated_graph, start_point, start_dir)

        if outcome == Outcome.LOOP:
            loop_count += 1

    return loop_count


print(p1, p2())
