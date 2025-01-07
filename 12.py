import sys

data = {
    col + row * 1j: c
    for row, s in enumerate(sys.stdin.read().splitlines())
    for col, c in enumerate(s)
}


def partition_squares_by_label(squares):
    while squares:
        todo = {squares.pop()}
        current = set()

        while todo:
            pos = todo.pop()
            current.add(pos)

            for delta in [1, -1, 1j, -1j]:
                new_pos = pos + delta

                if new_pos in squares and data[new_pos] == data[pos]:
                    todo.add(new_pos)
                    squares.remove(new_pos)

        yield current


def perimeter(squares):
    return [
        pos
        for delta in [1, -1, 1j, -1j]
        for pos in squares
        if pos + delta not in squares
    ]


print(
    sum(
        len(p) * len(perimeter(p)) for p in partition_squares_by_label(set(data.keys()))
    )
)


def extract_connected_regions(squares):
    while squares:
        todo = {squares.pop()}
        current = set()

        while todo:
            pos = todo.pop()
            current.add(pos)

            for delta in [1, -1, 1j, -1j]:
                new_pos = pos + delta

                if new_pos in squares:
                    todo.add(new_pos)
                    squares.remove(new_pos)

        yield current


def calculate_sides(squares):
    for x in set(pos.real for pos in squares):
        for direction in [1, -1]:
            yield from extract_connected_regions(
                set(z for z in squares if z.real == x and z + direction not in squares)
            )

    for y in set(pos.imag for pos in squares):
        for direction in [1j, -1j]:
            yield from extract_connected_regions(
                set(z for z in squares if z.imag == y and z + direction not in squares)
            )


print(
    sum(
        len(p) * sum(1 for _ in calculate_sides(p))
        for p in partition_squares_by_label(set(data.keys()))
    )
)
