def is_small_case(i):
    return ord('z') >= ord(i) >= ord('a')


def item_to_priority(i):
    if (is_small_case(i)):
        return ord(i) - ord('a') + 1
    else:
        return ord(i) - ord('A') + 27


def priortiy_sum(elf_group):
    return sum(map(item_to_priority, set.intersection(*map(set, elf_group))))


GROUP_SZ = 3


def main():
    all_lines = open('in.txt', 'r').read().split('\n')
    print(sum(map(priortiy_sum, [all_lines[i:i+GROUP_SZ] for i in range(0, len(all_lines), GROUP_SZ)])))


main()
