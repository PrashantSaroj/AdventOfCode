def parse_input():
    raw_input = open('in.txt', 'r').read().split('\n')
    sensors, beacons = [], []
    for line in raw_input:
        s_x, s_y, b_x, b_y = list(map(int, line.split(',')))
        sensors.append((s_x, s_y))
        beacons.append((b_x, b_y))
    return sensors, beacons


BASELINE_Y = 2000000


def impossible_beacon_range(sensor, beacon, baseLineY=BASELINE_Y):
    # return [x1, x2] where beacon cannot be present
    # return None if baseline doesn't intersect with Manhattan block
    manhattanDist = abs(sensor[0]-beacon[0]) + abs(beacon[1]-sensor[1])
    botY = sensor[1] + manhattanDist
    topY = sensor[1] - manhattanDist
    if topY <= baseLineY <= sensor[1]:
        distX = baseLineY-topY
        return [sensor[0]-distX, sensor[0]+distX]
    elif sensor[1] <= baseLineY <= botY:
        distX = botY - baseLineY
        return [sensor[0]-distX, sensor[0]+distX]
    else:
        return None


def main():
    sensors, beacons = parse_input()
    beacons_set = set(beacons)
    impossibleBeaconPoints = set()
    for sensor, beacon in zip(sensors, beacons):
        impossibleBeaconRange = impossible_beacon_range(sensor, beacon)
        if impossibleBeaconRange is not None:
            x1, x2 = impossibleBeaconRange
            for x in range(x1, x2+1):
                if (x, BASELINE_Y) not in beacons_set:
                    impossibleBeaconPoints.add((x, BASELINE_Y))

    print(len(impossibleBeaconPoints))


main()
