import sys
from functools import cmp_to_key

rules, updates = sys.stdin.read().split("\n\n")
rules = [(int(x), int(y)) for x, y in (rule.split("|") for rule in rules.splitlines())]
updates = [tuple(map(int, p.split(","))) for p in updates.splitlines()]


def is_valid_rule(rule, pages):
    left, right = rule

    if left not in pages:
        return True
    if right not in pages:
        return True

    for p in pages:
        if p == left:
            return True
        if p == right:
            return False

    return True


def is_valid_update(rules, pages):
    return all(is_valid_rule(rule, pages) for rule in rules)


p1 = sum(pages[len(pages) // 2] for pages in updates if is_valid_update(rules, pages))

ordering_lookup = {l: [] for l, _ in rules}
for l, r in rules:
    ordering_lookup[l] = ordering_lookup[l] + [r]


def correction_sort(a, b):
    a_preceeds_b = b in ordering_lookup.get(a, [])
    b_preceeds_a = a in ordering_lookup.get(b, [])

    if a_preceeds_b and b_preceeds_a:
        raise ValueError("Invalid data")

    if a_preceeds_b:
        return -1

    if b_preceeds_a:
        return 1

    return 0


corrected_updates = [
    sorted(pages, key=cmp_to_key(correction_sort))
    for pages in updates
    if not is_valid_update(rules, pages)
]
p2 = sum(pages[len(pages) // 2] for pages in corrected_updates)

print(p1, p2)
