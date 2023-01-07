def parse_input(s):
    dir, step = s.split()
    step = int(step)
    return [dir, step]


head_pos = (0, 0)
tail_pos = (0, 0)
visited = set([tail_pos])


def simulate_u(step):
    global head_pos, tail_pos
    for _ in range(step[1]):
        head_pos = (head_pos[0], head_pos[1] + 1)
        if head_pos[1]-tail_pos[1] == 2:
            tail_pos = (head_pos[0], head_pos[1]-1)
            visited.add(tail_pos)


def simulate_d(step):
    global head_pos, tail_pos
    for _ in range(step[1]):
        head_pos = (head_pos[0], head_pos[1] - 1)
        if head_pos[1]-tail_pos[1] == -2:
            tail_pos = (head_pos[0], head_pos[1]+1)
            visited.add(tail_pos)


def simulate_l(step):
    global head_pos, tail_pos
    for _ in range(step[1]):
        head_pos = (head_pos[0]-1, head_pos[1])
        if head_pos[0]-tail_pos[0] == -2:
            tail_pos = (head_pos[0]+1, head_pos[1])
            visited.add(tail_pos)


def simulate_r(step):
    global head_pos, tail_pos
    for _ in range(step[1]):
        head_pos = (head_pos[0]+1, head_pos[1])
        if head_pos[0]-tail_pos[0] == 2:
            tail_pos = (head_pos[0]-1, head_pos[1])
            visited.add(tail_pos)


def simulate(steps):
    for step in steps:
        if step[0] == 'D':
            simulate_d(step)
        elif step[0] == 'U':
            simulate_u(step)
        elif step[0] == 'R':
            simulate_r(step)
        elif step[0] == 'L':
            simulate_l(step)


def main():
    simulate(map(parse_input, open('test_in.txt', 'r').read().split('\n')))
    print(visited)


main()
