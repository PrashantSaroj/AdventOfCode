from collections import deque

crates = {
    1: deque(['T', 'Q', 'V', 'C', 'D', 'S', 'N']),
    2: deque(['V', 'F', 'M']),
    3: deque(['M', 'H', 'N', 'P', 'D', 'W', 'Q', 'F']),
    4: deque(['F', 'T', 'R', 'Q', 'D']),
    5: deque(['B', 'V', 'H', 'Q', 'N', 'M', 'F', 'R']),
    6: deque(['Q', 'W', 'P', 'N', 'G', 'F', 'C']),
    7: deque(['T', 'C', 'L', 'R', 'F', 'W']),
    8: deque(['S', 'N', 'Z', 'T']),
    9: deque(['N', 'H', 'Q', 'R', 'J', 'D', 'S', 'M']),
}


def apply_instruction(instruction):
    """
    instruction = [x, y, z] move x from y to z
    """
    for _ in range(instruction[0]):
        crates[instruction[2]].appendleft(crates[instruction[1]].popleft())


def main():
    list(map(apply_instruction, map(lambda l: list(map(int, l.split())),open('in.txt', 'r').read().split('\n'))))
    print(''.join([crate.popleft() for crate in crates.values()]))

main()
