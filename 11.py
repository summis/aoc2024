import sys

data = list(map(int, sys.stdin.read().split()))


def apply_rule(num):
    if num == 0:
        return [1]

    num_string = str(num)

    if len(num_string) % 2 == 0:
        return [
            int(num_string[: len(num_string) // 2]),
            int(num_string[len(num_string) // 2 :]),
        ]

    return [2024 * num]


def construct_closed_set(num):
    lookup = {num: apply_rule(num)}

    while todo := [v for values in lookup.values() for v in values if v not in lookup]:
        for v in todo:
            lookup[v] = apply_rule(v)

    return lookup


def run(repeats):
    total = 0

    for num in data:
        lookup = construct_closed_set(num)
        scores = {num: 1 for num in lookup}

        for _ in range(repeats):
            scores = {k: sum(scores[v] for v in values) for k, values in lookup.items()}

        total += scores[num]

    return total


print(run(25), run(75))
