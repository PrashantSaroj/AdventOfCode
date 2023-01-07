class Node:
    def __init__(self, name, flow, neighbours):
        self.flow = flow
        self.neighbours = neighbours
        self.name = name


def parse_input():
    inputLines = map(str.split, open('test_in.txt', 'r').read().split('\n'))
    graph = {}
    for line in inputLines:
        graph[line[0]] = Node(line[0], int(line[1]), line[2:])
    return graph


class ValveSystem:
    def __init__(self):
        self.graph = parse_input()

    def solve(self):
        return self.releasePressure(self.graph['AA'], 5)

    def releasePressure(self, currNode, timeLeft):
        if timeLeft <= 1:
            return 0

        # two possibilites - open this valve or not
        currReward = 0
        for neighbour in currNode.neighbours:
            currReward = max(currReward, self.releasePressure(
                self.graph[neighbour], timeLeft-1))

        if currNode.flow != 0:
            tempFlow = currNode.flow
            self.graph[currNode.name].flow = 0
            for neighbour in currNode.neighbours:
                currReward = max(currReward, self.releasePressure(
                    self.graph[neighbour], timeLeft-2))
            self.graph[currNode.name].flow = tempFlow
            currReward += (timeLeft - 1)*tempFlow
        return currReward


print(ValveSystem().solve())
