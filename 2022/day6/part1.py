MARKER_SZ = 14


def main():
    signal = open('in.txt', 'r').read()
    for i in range(len(signal)-MARKER_SZ):
        if len(set(signal[i:i+MARKER_SZ])) == MARKER_SZ:
            print(i+MARKER_SZ)
            break


main()
