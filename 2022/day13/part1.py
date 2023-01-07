from enum import Enum


class Relation(Enum):
    LESSER = 1
    EQUAL = 2
    GREATER = 3


def cmp_ints(i1, i2):
    if i1 < i2:
        return Relation.LESSER
    if i1 == i2:
        return Relation.EQUAL
    if i1 > i2:
        return Relation.GREATER


def cmp(item1, item2):
    if isinstance(item1, int) and isinstance(item2, int):
        return cmp_ints(item1, item2)
    if isinstance(item1, int) and not isinstance(item2, int):
        return cmp([item1], item2)
    if not isinstance(item1, int) and isinstance(item2, int):
        return cmp(item1, [item2])

    for i in range(min(len(item1), len(item2))):
        relation = cmp(item1[i], item2[i])
        if relation == Relation.GREATER or relation == Relation.LESSER:
            return relation

    if len(item1) == len(item2):
        return Relation.EQUAL
    elif len(item1) > len(item2):
        return Relation.GREATER
    else:
        # left ran out of items
        return Relation.LESSER


indicesSum = 0
lines = list(map(eval, open('in.txt', 'r').read().split('\n')))
pairs = [(lines[i], lines[i+1]) for i in range(0, len(lines), 2)]


for pair, index in zip(pairs, range(1, len(pairs)+1)):
    if cmp(pair[0], pair[1]) == Relation.LESSER:
        indicesSum += index

print(indicesSum)
