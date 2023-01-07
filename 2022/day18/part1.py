def parse_input():
    f = open('in.txt', 'r')
    lines = f.read().split('\n')
    points = []
    for line in lines:
        line = line.split(',')
        points.append(tuple(map(int, line)))
    return points


def surfaceArea(points):
    totalArea = 0
    pointsSet = set(points)
    for point in points:
        currArea = 0
        if (point[0]-1, point[1], point[2]) not in pointsSet:
            currArea += 1
        if (point[0]+1, point[1], point[2]) not in pointsSet:
            currArea += 1
        if (point[0], point[1]-1, point[2]) not in pointsSet:
            currArea += 1
        if (point[0], point[1]+1, point[2]) not in pointsSet:
            currArea += 1
        if (point[0], point[1], point[2]-1) not in pointsSet:
            currArea += 1
        if (point[0], point[1], point[2]+1) not in pointsSet:
            currArea += 1
        totalArea += currArea
    print(totalArea)


surfaceArea(parse_input())
