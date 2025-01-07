import sys

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


print(sum(pages[len(pages) // 2] for pages in updates if is_valid_update(rules, pages)))
