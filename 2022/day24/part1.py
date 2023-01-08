import sys
sys.setrecursionlimit(1024)


dir2Vec = {
    '.': (0, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1),
    '^': (-1, 0),
}


class Blizzard:
    def __init__(self, pos, sym):
        self.pos = pos
        self.dir = dir2Vec[sym]


def parse_input():
    # return blizzard position and board size
    lines = open('input/in2.txt', 'r').read().split('\n')
    blizs = []
    i = 0
    for l in lines:
        j = 0
        for c in l:
            if c != '.':
                blizs.append(Blizzard((i, j), c))
            j += 1
        i += 1
    boardSize = len(lines), len(lines[0])
    return blizs, boardSize


def printBoard(board):
    for row in board:
        print(''.join(row))


class ValleySim:
    def __init__(self, blizs, boardSize):
        self.blizards = blizs
        self.rowCount = boardSize[0]
        self.colCount = boardSize[1]

        # max time for which simulator runs
        self.LIMIT = 1000
        self.preComputeBoard()

        # set src and destination
        self.src = (-1, 0)
        self.dst = (self.rowCount-1, self.colCount-1)

        self.memo = {}

        # calculate ans
        self.simulate()

    def validMoves(self, pos, board):
        # returns valid moves for board at t+1
        moves = []
        for dir in dir2Vec.values():
            posX = pos[0] + dir[0]
            posY = pos[1] + dir[1]
            if posX >= 0 and posX < self.rowCount:
                if posY >= 0 and posY < self.colCount:
                    if board[posX][posY] == '.':
                        moves.append((posX, posY))

            if (posX, posY) == (-1, 0):
                # handle the starting case
                moves.append((posX, posY))

        return moves

    def calcMinTime(self, src, t):
        if src == self.dst:
            return t

        if t == self.LIMIT - 1:
            # no solution, return max
            return self.LIMIT

        memoKey = (src, t)
        if memoKey in self.memo:
            return self.memo[memoKey]

        nextBoard = self.boardAtTime[t+1]
        nextMoves = self.validMoves(src, nextBoard)

        if len(nextMoves) == 0:
            # no valid moves
            return self.LIMIT

        neighbours = []
        for move in nextMoves:
            neighbours.append(self.calcMinTime(move, t+1))

        self.memo[memoKey] = min(neighbours)
        return self.memo[memoKey]

    def simulate(self):
        print(self.calcMinTime(self.src, -1) + 1)

    def createEmptyBoard(self):
        return [['.' for _ in range(self.colCount)] for _ in range(self.rowCount)]

    def preComputeBoard(self):
        self.boardAtTime = []
        for t in range(self.LIMIT):
            boardT = self.createEmptyBoard()
            for bliz in self.blizards:
                blizX = (bliz.pos[0] + bliz.dir[0]*t) % self.rowCount
                blizY = (bliz.pos[1] + bliz.dir[1]*t) % self.colCount
                boardT[blizX][blizY] = '#'
            self.boardAtTime.append(boardT)


ValleySim(*parse_input())
