class Node:
    def __init__(self, name, flow, neighbours):
        self.flow = flow
        self.neighbours = neighbours
        self.name = name


def parse_input():
    inputLines = map(str.split, open('input/in1.txt', 'r').read().split('\n'))
    graph = {}
    for line in inputLines:
        graph[line[0]] = Node(line[0], int(line[1]), line[2:])
    return graph


class ValveSystem:
    def __init__(self):
        self.graph = parse_input()
        self.TIME_LIMIT = 30
        self.memo = {}

    def solve(self):
        return self.releasePressure('AA', 0, set())

    def flowOpenedValves(self, openedValves):
        # return pressure release by all opened valves in 1 second
        return sum([self.graph[nodeName].flow for nodeName in openedValves])

    # returns total pressure released from timeLeft to TIME_LIMIT
    def releasePressure(self, src, t, openedValves):
        memoKey = (src, t, tuple(sorted(openedValves)))
        if memoKey in self.memo:
            return self.memo[memoKey]

        if t == self.TIME_LIMIT:
            return 0

        if t == self.TIME_LIMIT - 1:
            # dont open any valve just release pressure
            return self.flowOpenedValves(openedValves)

        currNode = self.graph[src]
        maxReward = 0

        for neighbour in currNode.neighbours:
            currReward = self.releasePressure(neighbour, t + 1, openedValves)
            maxReward = max(maxReward, currReward)
        maxReward = self.flowOpenedValves(openedValves) + maxReward

        if not (currNode.flow == 0 or src in openedValves):
            constReward = 2*self.flowOpenedValves(openedValves) + currNode.flow

            currReward = 0
            openedValves.add(src)
            for neighbour in currNode.neighbours:
                currReward = max(
                    self.releasePressure(neighbour, t + 2, openedValves), currReward)
            openedValves.remove(src)

            currReward += constReward
            maxReward = max(maxReward, currReward)

        self.memo[memoKey] = maxReward
        return maxReward


print(ValveSystem().solve())
