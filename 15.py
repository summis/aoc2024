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


print(calculate_score(run_simulation(grid)))
