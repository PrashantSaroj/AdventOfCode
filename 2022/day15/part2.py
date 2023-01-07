def parse_input():
    raw_input = open('in.txt', 'r').read().split('\n')
    sensors, beacons = [], []
    for line in raw_input:
        s_x, s_y, b_x, b_y = list(map(int, line.split(',')))
        sensors.append((s_x, s_y))
        beacons.append((b_x, b_y))
    return sensors, beacons


MIN_LIMIT = 0
MAX_LIMIT = 4000000


def clip(n):
    if n < MIN_LIMIT:
        return MIN_LIMIT
    if n > MAX_LIMIT:
        return MAX_LIMIT
    return n


def impossible_beacon_range(sensor, beacon, baseLineY):
    # return [x1, x2] where beacon cannot be present
    # return None if baseline doesn't intersect with Manhattan block
    manhattanDist = abs(sensor[0]-beacon[0]) + abs(beacon[1]-sensor[1])
    botY = sensor[1] + manhattanDist
    topY = sensor[1] - manhattanDist
    if topY <= baseLineY <= sensor[1]:
        distX = baseLineY-topY
        return list(map(clip, [sensor[0]-distX, sensor[0]+distX]))
    elif sensor[1] <= baseLineY <= botY:
        distX = botY - baseLineY
        return list(map(clip, [sensor[0]-distX, sensor[0]+distX]))
    else:
        return None


def coalesce(ranges):
    sortedRanges = sorted(ranges, key=lambda x: x[0])
    coalescedRanges = []
    curr = sortedRanges[0]
    for i in range(1, len(sortedRanges)):
        if curr[0] <= sortedRanges[i][0] <= curr[1]:
            curr[1] = max(sortedRanges[i][1], curr[1])
        else:
            coalescedRanges.append(curr)
            curr = sortedRanges[i]
    coalescedRanges.append(curr)
    return coalescedRanges


def main():
    sensors, beacons = parse_input()
    beacons_set = set(beacons)

    for baselineY in range(MAX_LIMIT + 1):
        allImpossibleRanges = []
        for sensor, beacon in zip(sensors, beacons):
            impossibleRange = impossible_beacon_range(
                sensor, beacon, baselineY)
            if impossibleRange is not None:
                allImpossibleRanges.append(impossibleRange)
        coalasced = coalesce(allImpossibleRanges)
        if len(coalasced) != 1:
            print(coalasced, baselineY)


main()
