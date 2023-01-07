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
        currPos = (0, 50)
        # mark initial pos
        self.board[currPos[0]][currPos[1]] = dirMap[currDir]

        for instr in self.instructions:
            if isinstance(instr, int):
                for _ in range(instr):
                    nextPos, nextDir = self.calcNextPos(currPos, currDir)
                    if self.steppable(nextPos[0], nextPos[1]):
                        self.board[nextPos[0]][nextPos[1]] = dirMap[currDir]
                        currPos = nextPos
                        currDir = nextDir
                    else:
                        break
            else:
                currDir = iMap[instr][currDir]
                self.board[currPos[0]][currPos[1]] = dirMap[currDir]
        print(1000*(currPos[0]+1) + 4*(currPos[1] + 1) + faceMap[currDir])

    def calcNextPos(self, pos, dir):
        """
        return new position and direction
        """
        i, j = pos[0], pos[1]
        newPos, newDir = None, None

        if dir == (0, 1):
            if j == 99 and 50 <= i <= 99:
                newPos = (49, i + 50)
                newDir = (-1, 0)
            if j == 99 and 100 <= i <= 149:
                newPos = (149-i, 149)
                newDir = (0, -1)
            if j == 49 and 150 <= i <= 199:
                newPos = (149, i-100)
                newDir = (-1, 0)
            if j == 149 and 0 <= i <= 49:
                newPos = (149 - i, 99)
                newDir = (0, -1)

        if dir == (0, -1):
            if j == 0 and 100 <= i <= 149:
                newPos = (149-i, 50)
                newDir = (0, 1)
            if j == 0 and 150 <= i <= 199:
                newPos = (0, i - 100)
                newDir = (1, 0)
            if j == 50 and 0 <= i <= 49:
                newPos = (149 - i, 0)
                newDir = (0, 1)
            if j == 50 and 50 <= i <= 99:
                newPos = (100, i - 50)
                newDir = (1, 0)

        if dir == (1, 0):
            if i == 49 and 100 <= j <= 149:
                newPos = (j - 50, 99)
                newDir = (0, -1)
            if i == 149 and 50 <= j <= 99:
                newPos = (j + 100, 49)
                newDir = (0, -1)
            if i == 199 and 0 <= j <= 49:
                newPos = (0, j + 100)
                newDir = (1, 0)

        if dir == (-1, 0):
            if i == 0 and 50 <= j <= 99:
                newPos = (j + 100, 0)
                newDir = (0, 1)
            if i == 0 and 100 <= j <= 149:
                newPos = (199, j - 100)
                newDir = (-1, 0)
            if i == 100 and 0 <= j <= 49:
                newPos = (j + 50, 50)
                newDir = (0, 1)

        if newPos is not None:
            return newPos, newDir

        newPos = (i + dir[0], j + dir[1])
        return newPos, dir

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
            for i in range(first, last + 1):
                self.board[rowIter][i] = l[i]
            rowIter += 1


MonkeyMap()
