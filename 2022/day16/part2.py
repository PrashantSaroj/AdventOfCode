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
        self.TIME_LIMIT = 26
        self.memo = {}

    def solve(self):
        return self.releasePressure('AA', 0, set(), True)

    def flowOpenedValves(self, openedValves):
        # return pressure release by all opened valves in 1 second
        return sum([self.graph[nodeName].flow for nodeName in openedValves])

    # returns total pressure released from timeLeft to TIME_LIMIT
    def releasePressure(self, src, t, openedValves, otherPlayers):
        memoKey = (src, t, tuple(sorted(openedValves)), otherPlayers)
        if memoKey in self.memo:
            return self.memo[memoKey]

        if t == self.TIME_LIMIT:
            if otherPlayers:
                return self.releasePressure('AA', 0, openedValves, False)
            else:
                return 0

        currNode = self.graph[src]
        ans = 0

        if not (currNode.flow == 0 or src in openedValves):
            openedValves.add(src)
            ans = max(ans, (self.TIME_LIMIT - t - 1) * currNode.flow +
                      self.releasePressure(src, t + 1, openedValves, otherPlayers))

            openedValves.remove(src)

        for neighbour in currNode.neighbours:
            ans = max(ans, self.releasePressure(
                neighbour, t + 1, openedValves, otherPlayers))

        self.memo[memoKey] = ans
        return ans


print(ValveSystem().solve())
