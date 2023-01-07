def firstTile(s):
    for i in range(len(s)):
        if s[i] != ' ':
            return i


def lastTile(s):
    for i in range(len(s)-1, -1, -1):
        if s[i] != ' ':
            return i


dirMap = {
    (0, 1): '>',
    (0, -1): '<',
    (1, 0): 'v',
    (-1, 0): '^'
}

faceMap = {
    (0, 1): 0,
    (0, -1): 2,
    (1, 0): 1,
    (-1, 0): 3
}

rMap = {
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
    (-1, 0): (0, 1)
}

lMap = {
    (0, 1): (-1, 0),
    (-1, 0): (0, -1),
    (0, -1): (1, 0),
    (1, 0): (0, 1),
}

iMap = {
    'L': lMap,
    'R': rMap
}


class MonkeyMap:
    def __init__(self) -> None:
        # ranges are inclusive
        self.rowRange = []
        self.colRange = []
        # parse board
        self.parseBoard()

        # parse instruction
        self.instructions = []
        self.parsePaths()

        # execute instruction
        self.executeInstructions()

        # print board
        # for row in self.board:
        #     print(''.join(row))

    def executeInstructions(self):
        currDir = (0, 1)
        currPos = (0, self.rowRange[0][0])
        # mark initial pos
        self.board[currPos[0]][currPos[1]] = dirMap[currDir]

        for instr in self.instructions:
            if isinstance(instr, int):
                for _ in range(instr):
                    nextPos = self.calcNextPos(currPos, currDir)
                    if self.steppable(nextPos[0], nextPos[1]):
                        self.board[nextPos[0]][nextPos[1]] = dirMap[currDir]
                        currPos = nextPos
                    else:
                        break
            else:
                currDir = iMap[instr][currDir]
                self.board[currPos[0]][currPos[1]] = dirMap[currDir]
        print(1000*(currPos[0]+1) + 4*(currPos[1] + 1) + faceMap[currDir])

    def calcNextPos(self, pos, dir):
        i = pos[0] + dir[0]
        j = pos[1] + dir[1]

        if dir == (0, 1):
            if j > self.rowRange[i][1]:
                return (i, self.rowRange[i][0])

        if dir == (0, -1):
            if j < self.rowRange[i][0]:
                return (i, self.rowRange[i][1])

        if dir == (1, 0):
            if i > self.colRange[j][1]:
                return (self.colRange[j][0], j)

        if dir == (-1, 0):
            if i < self.colRange[j][0]:
                return (self.colRange[j][1], j)
        return (i, j)

    def steppable(self, i, j):
        tile = self.board[i][j]
        return tile != ' ' and tile != '#'

    def parsePaths(self) -> None:
        path = open('paths.txt', 'r').read()
        step = ''
        for c in path:
            if c.isdigit():
                step += c
            else:
                self.instructions.append(int(step))
                self.instructions.append(c)
                step = ''
        self.instructions.append(int(step))

    def parseBoard(self) -> None:
        lines = open('board.txt', 'r').read().split('\n')

        self.colCount = max(map(len, lines))
        self.rowCount = len(lines)
        self.board = [[' ' for _ in range(self.colCount)]
                      for _ in range(self.rowCount)]

        rowIter = 0
        for l in lines:
            first, last = firstTile(l), lastTile(l)
            self.rowRange.append((first, last))
            for i in range(first, last + 1):
                self.board[rowIter][i] = l[i]
            rowIter += 1

        for colIter in range(self.colCount):
            l = [row[colIter] for row in self.board]
            first, last = firstTile(l), lastTile(l)
            self.colRange.append((first, last))
            colIter += 1


MonkeyMap()
