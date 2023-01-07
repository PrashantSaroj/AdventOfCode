"""
x-range: 489 -> 580
y-range: 13 -> 171
MATRIX(y, x) = co-ordinate system (x, y)
"""

HEGIHT, WIDTH = 200, 200
START = (100, 0)
Y_THRESHOLD = 172


def simulate_tetris(mat):
    ripCount = 0
    eqmReach = False
    while not eqmReach:
        currX, currY = START[0], START[1]
        while True:
            if mat[currY+1][currX] == '.':
                currY = currY+1
            elif mat[currY+1][currX-1] == '.':
                currY = currY+1
                currX = currX-1
            elif mat[currY+1][currX+1] == '.':
                currY = currY+1
                currX = currX+1
            else:
                mat[currY][currX] = 'o'
                ripCount += 1
                break

            if currY > Y_THRESHOLD:
                eqmReach = True
                break
    print(ripCount)


def between_points(p1, p2):
    # return all points between p1 and p2 (including both)
    vec_x = (p1[0]-p2[0]) // max(abs(p1[0]-p2[0]), 1)
    vec_y = (p1[1]-p2[1]) // max(abs(p1[1]-p2[1]), 1)
    points = [p2]
    curren = p2
    while curren != p1:
        curren = [curren[0]+vec_x, curren[1]+vec_y]
        points.append(curren)
    return points


def create_mat(points_list):
    mat = [['.' for _ in range(WIDTH)] for _ in range(HEGIHT)]
    for points in points_list:
        for i in range(len(points)-1):
            # mark rock in points[i] -> points[i+1]
            for rock in between_points(points[i], points[i+1]):
                mat[rock[1]][rock[0]] = '#'
    return mat


def parse_point(point):
    x, y = point.split(',')
    return [int(x)-400, int(y)]


def parse_line(line):
    # input = ['int,int', 'int,int', ....]
    return list(map(parse_point, line))


def parse_lines(lines):
    lines = map(lambda l: l.split(' -> '), lines)
    return list(map(parse_line, lines))


lines = open('in.txt', 'r').read().split('\n')
points = parse_lines(lines)
mat = create_mat(points)
simulate_tetris(mat)
for l in mat:
    print(''.join(l))
