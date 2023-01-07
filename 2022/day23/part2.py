dir2Vec = {
    'N': (-1, 0),
    'S': (1, 0),
    'E': (0, 1),
    'W': (0, -1),
    'NE': (-1, 1),
    'SE': (1, 1),
    'NW': (-1, -1),
    'SW': (1, -1)
}


class DiffusionSimulator:
    def __init__(self) -> None:
        # store elves position
        self.elvesPos = set()

        # parse input and simulate
        self.parse_input()

        # store direction preference
        self.directions = [
            ('N', 'NE', 'NW'),
            ('S', 'SE', 'SW'),
            ('W', 'NW', 'SW'),
            ('E', 'NE', 'SE')
        ]

        # simulate
        self.simulate()

    def elfPresent(self, pos):
        return pos in self.elvesPos

    def canPropose(self, elfPos, dirTuple):
        # return true if dirTuple is already occupied
        for dir in dirTuple:
            vecX, vecY = dir2Vec[dir]
            newX, newY = elfPos[0] + vecX, elfPos[1] + vecY
            if self.elfPresent((newX, newY)):
                return True
        return False

    def stableElf(self, elfPos):
        for dir in dir2Vec.values():
            adjX, adjY = elfPos[0] + dir[0], elfPos[1] + dir[1]
            if self.elfPresent((adjX, adjY)):
                return False
        return True

    def propsePoint(self, elfPos):
        if not self.stableElf(elfPos):
            for dirTuple in self.directions:
                if not self.canPropose(elfPos, dirTuple):
                    dirX = dir2Vec[dirTuple[0]][0]
                    dirY = dir2Vec[dirTuple[0]][1]
                    return (elfPos[0] + dirX, elfPos[1] + dirY)

    def simulate(self):
        currRound = 1
        while True:
            # find preference of each elf
            proposedPoints = {}
            # store count of each prefered point
            propsedPointsCount = {}

            for elfPos in self.elvesPos:
                point = self.propsePoint(elfPos)
                if point is not None:
                    proposedPoints[elfPos] = point
                    if point in propsedPointsCount:
                        propsedPointsCount[point] += 1
                    else:
                        propsedPointsCount[point] = 1

            # second half of round
            someoneMoved = False
            elfPosList = list(self.elvesPos)
            for elfPos in elfPosList:
                if elfPos in proposedPoints:
                    point = proposedPoints[elfPos]
                    if propsedPointsCount[point] == 1:
                        someoneMoved = True
                        self.updateBoard(elfPos, point)

            if not someoneMoved:
                print(currRound)
                break

            currRound += 1
            self.rotateDirections()

    def updateBoard(self, oldPos, newPos):
        self.elvesPos.add(newPos)
        self.elvesPos.remove(oldPos)

    def rotateDirections(self):
        self.directions.append(self.directions.pop(0))

    def parse_input(self):
        lines = open('input/in1.txt', 'r').read().split('\n')
        rowIter = 0
        for line in lines:
            colIter = 0
            for c in line:
                if c == '#':
                    self.elvesPos.add((rowIter, colIter))
                colIter += 1
            rowIter += 1


DiffusionSimulator()
