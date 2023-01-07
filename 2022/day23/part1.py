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
    def __init__(self, rounds=10) -> None:
        # number of rounds to simulate
        self.ROUNDS_COUNT = rounds

        # store elves position
        self.elvesPos = []

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

        self.smallestRectangle()
        # for row in self.board:
        #     print(''.join(row))

    def smallestRectangle(self):
        minX, maxX = 100, 0
        minY, maxY = 100, 0

        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == '#':
                    minX = min(i, minX)
                    minY = min(j, minY)
                    maxX = max(i, maxX)
                    maxY = max(j, maxY)

        emptyTiles = 0
        for i in range(minX, maxX+1):
            for j in range(minY, maxY+1):
                if self.board[i][j] == '.':
                    emptyTiles += 1
        print(emptyTiles)

    def elfPresent(self, elfPos, dirTuple):
        # return true if dirTuple is already occupied
        for dir in dirTuple:
            vecX, vecY = dir2Vec[dir]
            newX, newY = elfPos[0] + vecX, elfPos[1] + vecY
            if self.board[newX][newY] == '#':
                return True
        return False

    def stableElf(self, elfPos):
        for dir in dir2Vec.values():
            adjX, adjY = elfPos[0] + dir[0], elfPos[1] + dir[1]
            if self.board[adjX][adjY] == '#':
                return False
        return True

    def getPreferedPoint(self, elfPos):
        if not self.stableElf(elfPos):
            for dirTuple in self.directions:
                if not self.elfPresent(elfPos, dirTuple):
                    dirX = dir2Vec[dirTuple[0]][0]
                    dirY = dir2Vec[dirTuple[0]][1]
                    return (elfPos[0] + dirX, elfPos[1] + dirY)

    def simulate(self):
        for _ in range(self.ROUNDS_COUNT):
            # find preference of each elf
            elfPreference = {}
            # store count of each prefered point
            preferedPoints = {}

            for elfPos in self.elvesPos:
                point = self.getPreferedPoint(elfPos)
                if point is not None:
                    elfPreference[elfPos] = point
                    if point in preferedPoints:
                        preferedPoints[point] += 1
                    else:
                        preferedPoints[point] = 1

            # second half of round
            for elfPos, i in zip(self.elvesPos, range(len(self.elvesPos))):
                if elfPos in elfPreference:
                    point = elfPreference[elfPos]
                    if preferedPoints[point] == 1:
                        self.updateBoard(elfPos, point)
                        self.elvesPos[i] = point

            self.rotateDirections()

    def updateBoard(self, oldPos, newPos):
        self.board[oldPos[0]][oldPos[1]] = '.'
        self.board[newPos[0]][newPos[1]] = '#'

    def rotateDirections(self):
        self.directions.append(self.directions.pop(0))

    def parse_input(self):
        lines = open('input/in1.txt', 'r').read().split('\n')
        self.rowCount = len(lines) + 2*self.ROUNDS_COUNT
        self.colCount = len(lines[0]) + 2*self.ROUNDS_COUNT

        # create a buffer of ROUNDS_COUNT size on each side
        self.board = [['.' for _ in range(self.colCount)]
                      for _ in range(self.rowCount)]
        rowIter = self.ROUNDS_COUNT
        for line in lines:
            colIter = self.ROUNDS_COUNT
            for c in line:
                self.board[rowIter][colIter] = c
                if c == '#':
                    self.elvesPos.append((rowIter, colIter))
                colIter += 1
            rowIter += 1


DiffusionSimulator()
