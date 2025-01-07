import sys

data = {
    col + row * 1j: c
    for row, s in enumerate(sys.stdin.read().splitlines())
    for col, c in enumerate(s)
}


def partition():
    all_squares = set(data.keys())
    areas = []

    while all_squares:
        todo = {all_squares.pop()}
        current_area = set()

        while todo:
            pos = todo.pop()
            current_area.add(pos)

            for delta in [1, -1, 1j, -1j]:
                new_pos = pos + delta

                if new_pos in all_squares and data[new_pos] == data[pos]:
                    todo.add(new_pos)
                    all_squares.remove(new_pos)

        areas.append(current_area)

    return areas


def calculate_perimeter(squares):
    return sum(
        pos + delta not in squares for pos in squares for delta in [1, -1, 1j, -1j]
    )


def calculate_area(squares):
    return len(squares)


print(sum(calculate_area(x) * calculate_perimeter(x) for x in partition()))
