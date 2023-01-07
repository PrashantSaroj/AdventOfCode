def first_range_contains_second(r1, r2):
    return r1[0] <= r2[0] and r1[1] >= r2[1]

def desired_assignment(assignment):
    """
    assignment is one line of input
    """
    r1, r2 = map(lambda x: list(map(int, x.split('-'))) ,assignment.split(','))
    return first_range_contains_second(r1, r2) or first_range_contains_second(r2, r1)



def main():
    print(sum(map(desired_assignment, open('in.txt', 'r').read().split('\n'))))


main()