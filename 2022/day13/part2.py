from enum import Enum
from functools import cmp_to_key


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
        # right ran out of items
        return Relation.GREATER
    else:
        # left ran out of items
        return Relation.LESSER


def sort_comparator(item1, item2):
    relation = cmp(item1, item2)
    if relation == Relation.LESSER:
        return -1
    elif relation == Relation.EQUAL:
        return 0
    else:
        return 1


dividerPacket1 = [[2]]
dividerPacket2 = [[6]]
indices = []

lines = list(map(eval, open('in.txt', 'r').read().split('\n')))
lines.append(dividerPacket1)
lines.append(dividerPacket2)

sorted_lines = sorted(lines, key=cmp_to_key(sort_comparator))

for item, index in zip(sorted_lines, range(len(sorted_lines))):
    if item == dividerPacket1:
        indices.append(index+1)
    if item == dividerPacket2:
        indices.append(index+1)

print(indices, indices[0]*indices[1])
