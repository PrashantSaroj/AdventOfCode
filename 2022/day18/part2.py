"""
x-range: 0 to 21
y-range: 1 to 21
z-range: 0 to 20
"""


def parse_input():
    f = open('in.txt', 'r')
    lines = f.read().split('\n')
    points = []
    for line in lines:
        line = line.split(',')
        points.append(tuple(map(int, line)))
    return points


def getAdjPoints(point):
    return list([
        (point[0]-1, point[1], point[2]),
        (point[0]+1, point[1], point[2]),
        (point[0], point[1]-1, point[2]),
        (point[0], point[1]+1, point[2]),
        (point[0], point[1], point[2]-1),
        (point[0], point[1], point[2]+1),
    ])


def flood_fill(pointsSet):
    min_d, max_d = -1, 22

    def withinBoundary(point):
        return all([min_d <= coOrd <= max_d for coOrd in point])

    floodSet = set()
    floodStack = [(min_d, min_d, min_d)]
    while len(floodStack) > 0:
        currPoint = floodStack.pop()
        adjPoints = getAdjPoints(currPoint)
        floodSet.add(currPoint)

        for neighbour in adjPoints:
            if neighbour not in pointsSet and neighbour not in floodSet and withinBoundary(neighbour):
                floodStack.append(neighbour)
    return floodSet


def surfaceArea(points):
    totalArea = 0
    pointsSet = set(points)
    floodSet = flood_fill(pointsSet)

    for point in points:
        adjPoints = getAdjPoints(point)
        for neighbour in adjPoints:
            if neighbour not in pointsSet and neighbour in floodSet:
                totalArea += 1
    print(totalArea)


surfaceArea(parse_input())
