def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


class SnakeSimulator:
    """
    head: last pos of snake
    tail: first pos of snake
    visited: all visited tail positions
    """

    def __init__(self, snakeLen):
        self.SNAKE_LEN = snakeLen
        self.snake = [(0, 0) for _ in range(snakeLen)]
        self.visited = set([self.snake[0]])
        self.stepTransform = {
            'U': (0, 1),
            'R': (1, 0),
            'D': (0, -1),
            'L': (-1, 0)
        }

    def execOneStep(self, step):
        """
        step is '<dir> <count>'
        """
        dir, count = step.split()
        transformedStep = self.stepTransform[dir]
        for _ in range(int(count)):
            currHead = self.snake[self.SNAKE_LEN-1]
            self.snake[self.SNAKE_LEN-1] = (
                currHead[0]+transformedStep[0],
                currHead[1]+transformedStep[1]
            )

            for i in range(self.SNAKE_LEN-2, -1, -1):
                self.snake[i] = self.calcOneStep(
                    self.snake[i+1], self.snake[i])

            self.visited.add(self.snake[0])

    def calcOneStep(self, head, tail):
        x_diff = head[0] - tail[0]
        y_diff = head[1] - tail[1]
        if abs(x_diff) > 1 or abs(y_diff) > 1:
            return (tail[0] + sign(x_diff), tail[1] + sign(y_diff))
        return tail


def main():
    simulator = SnakeSimulator(10)
    for step in open('in.txt', 'r').read().split('\n'):
        simulator.execOneStep(step)
    print(len(simulator.visited))


main()
