import sys

grid = {
    col + row * 1j: c
    for row, line in enumerate(sys.stdin.read().splitlines())
    for col, c in enumerate(line)
}

antennas = {marker for marker in grid.values() if marker != "."}
antenna_positions = {
    antenna: [k for k, v in grid.items() if v == antenna] for antenna in antennas
}

antinodes = set()
for antenna in antennas:
    positions = antenna_positions[antenna]
    for x in positions:
        for y in positions:
            if x != y:
                diff = y - x
                antinodes.add(y + diff)
                antinodes.add(x - diff)

extended_antinodes = set()
for antenna in antennas:
    positions = antenna_positions[antenna]
    for x in positions:
        for y in positions:
            if x != y:
                diff = y - x
                for i in range(-60, 61):
                    extended_antinodes.add(y + diff * i)
                    extended_antinodes.add(x - diff * i)


print(sum(1 for a in antinodes if a in grid))
print(sum(1 for a in extended_antinodes if a in grid))
