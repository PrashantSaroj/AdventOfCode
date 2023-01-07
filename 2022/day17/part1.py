class Shape:
    def __init__(self):
        self.points = []
        self.symMap = {
            '>': (0, 1),
            '<': (0, -1),
            'v': (-1, 0),
        }

    def applyTransformation(self, sym):
        transformation = self.symMap[sym]
        transformedPts = []
        for point in self.points:
            transformedPts.append(
                (point[0]+transformation[0], point[1] + transformation[1]))
        return transformedPts

    def getTop(self):
        return max([point[0] for point in self.points]) + 1


class Shape1(Shape):
    def __init__(self, currTop):
        super().__init__()
        for i in range(4):
            self.points.append((currTop+3, 2+i))


class Shape2(Shape):
    def __init__(self, currTop):
        super().__init__()
        for i in range(3):
            self.points.append((currTop+4, 2+i))
        self.points.append((currTop+3, 3))
        self.points.append((currTop+5, 3))


class Shape3(Shape):
    def __init__(self, currTop):
        super().__init__()
        for i in range(3):
            self.points.append((currTop+3, 2+i))
        self.points.append((currTop+4, 4))
        self.points.append((currTop+5, 4))


class Shape4(Shape):
    def __init__(self, currTop):
        super().__init__()
        for i in range(4):
            self.points.append((currTop+3+i, 2))


class Shape5(Shape):
    def __init__(self, currTop):
        super().__init__()
        self.points.append((currTop+3, 2))
        self.points.append((currTop+4, 2))
        self.points.append((currTop+3, 3))
        self.points.append((currTop+4, 3))


class Tetris:
    def __init__(self):
        self.MAT_H = 10000
        self.MAT_W = 7
        self.matrix = [['.' for _ in range(self.MAT_W)]
                       for _ in range(self.MAT_H)]
        self.shapes = [Shape1, Shape2, Shape3, Shape4, Shape5]
        self.jetDir = open('in.txt', 'r').read()

        self.ROCKS_COUNT = 2022
        self.SHAPE_COUNT = 5
        self.WINDS_COUNT = len(self.jetDir)

    def validTransformation(self, points):
        for point in points:
            invalidRow = point[0] < 0 or point[0] >= self.MAT_H
            invalidCol = point[1] < 0 or point[1] >= self.MAT_W
            if invalidCol or invalidRow or self.matrix[point[0]][point[1]] == '#':
                return False
        return True

    def markFilled(self, points):
        for point in points:
            self.matrix[point[0]][point[1]] = '#'

    def simulate(self):
        currTop = 0
        currJet = 0
        for i in range(self.ROCKS_COUNT):
            currRock = self.shapes[i % self.SHAPE_COUNT](currTop)
            while True:
                # apply jet transformation
                jetPoints = currRock.applyTransformation(
                    self.jetDir[currJet % self.WINDS_COUNT])
                currJet += 1
                if self.validTransformation(jetPoints):
                    currRock.points = jetPoints
                # apply down transformation
                downPoints = currRock.applyTransformation('v')
                if self.validTransformation(downPoints):
                    currRock.points = downPoints
                else:
                    break
            self.markFilled(currRock.points)
            currTop = max(currTop, currRock.getTop())

        return currTop


print(Tetris().simulate())
