def is_small_case(i):
    return ord('z') >= ord(i) >= ord('a')


def item_to_priority(i):
    if (is_small_case(i)):
        return ord(i) - ord('a') + 1
    else:
        return ord(i) - ord('A') + 27


def priortiy_sum(r):
    n = len(r)
    comp1 = set(r[:n//2])
    comp2 = set(r[n//2:])
    return sum(map(item_to_priority, comp1.intersection(comp2)))


def main():
    print(sum(map(priortiy_sum, open('in.txt', 'r').read().split('\n'))))

main()
