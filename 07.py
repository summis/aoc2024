import sys

data = [x.split(":") for x in sys.stdin.read().splitlines()]
data = [(int(x[0]), list(map(int, x[1].split()))) for x in data]


def calculate_outcomes(nums, p):
    if len(nums) == 1:
        return [nums[0]]

    first, second, *rest = nums

    plus = [first + second] + rest
    mult = [first * second] + rest

    if p == "p1":
        return calculate_outcomes(plus, p) + calculate_outcomes(mult, p)

    if p == "p2":
        concat = [first * (10 ** len(str(second))) + second] + rest
        return (
            calculate_outcomes(plus, p)
            + calculate_outcomes(mult, p)
            + calculate_outcomes(concat, p)
        )

    raise ValueError("Invalid p")


p1 = sum(x for x, y in data if x in calculate_outcomes(y, "p1"))
p2 = sum(x for x, y in data if x in calculate_outcomes(y, "p2"))

print(p1, p2)
