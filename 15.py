import sys

grid, moves = sys.stdin.read().split("\n\n")
grid = {
    i + j * 1j: c
    for j, line in enumerate(grid.splitlines())
    for i, c in enumerate(line)
}
moves = [
    {
        "<": -1,
        ">": 1,
        "^": -1j,
        "v": 1j,
    }[c]
    for c in moves.strip("\n")
    if c in "<>^v"
]


def apply_move(pos, move, grid):
    new_pos = pos + move

    # Next position is a wall
    if grid.get(new_pos) == "#":
        return pos

    # Next position is open
    if grid.get(new_pos) == ".":
        grid[pos] = "."
        grid[new_pos] = "@"
        return new_pos

    # Next position is a box
    if grid.get(new_pos) == "O":
        # Get all the boxes in direction
        boxes = []
        step = 1
        while grid.get(pos + move * step) == "O":
            boxes.append(new_pos + move * step)
            step += 1

        # Check if the boxes can move
        if grid.get(pos + move * step) == "#":
            return pos

        # Move the boxes
        grid[pos] = "."
        grid[new_pos] = "@"
        grid[pos + move * step] = "O"
        return new_pos


def run_simulation(grid):
    grid_copy = grid.copy()
    pos = next(k for k, v in grid_copy.items() if v == "@")

    for move in moves:
        pos = apply_move(pos, move, grid_copy)

    return grid_copy


def calculate_score(grid):
    return int(sum(100 * z.imag + z.real for z, c in grid.items() if c == "O"))


def expand_grid(grid):
    items = set(k for k, v in grid.items() if v == "O")
    items = set((x + x.real, x + x.real + 1) for x in items)

    walls = set(k for k, v in grid.items() if v == "#")
    walls = set(x + x.real for x in walls) | set(x + x.real + 1 for x in walls)

    print(walls)

    start = next(k + k.real for k, v in grid.items() if v == "@")

    return items, walls, start


def run_simulation_2(items, walls, start, moves):
    pos = start
    for move in moves:
        pos, items = apply_move_2(pos, move, walls, items)

    return pos, items


def apply_move_2(pos, move, walls, items):
    new_pos = pos + move

    if new_pos in walls:
        return pos, items

    if any(new_pos in x for x in items):
        boxes = set()
        todo = [next(x for x in items if new_pos in x)]
        while todo:
            item = todo.pop()

            if any(x + move in walls for x in item):
                return pos, items

            for y in items:
                if y == item:
                    continue

                if any(x + move in y for x in item):
                    todo.append(y)

            boxes.add(item)

        new_items = items - boxes
        new_items = new_items | set(tuple(x + move for x in box) for box in boxes)

        return new_pos, new_items

    return new_pos, items


print(calculate_score(run_simulation(grid)))


def p2():
    items, walls, start = expand_grid(grid)
    print(start)

    pos, items = run_simulation_2(items, walls, start, moves)

    zs = [item[0] for item in items]
    return int(sum(100 * z.imag + z.real for z in zs))


print(p2())
