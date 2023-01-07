def overlap(r1, r2):
    return r2[0] <= r1[0] <= r2[1] or r1[0] <= r2[0] <= r1[1]


def desired_assignment(assignment):
    """
    assignment is one line of input
    """
    r1, r2 = map(lambda x: list(map(int, x.split('-'))), assignment.split(','))
    return overlap(r1, r2)


def main():
    print(sum(map(desired_assignment, open('in.txt', 'r').read().split('\n'))))


main()
