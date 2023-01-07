KEY = 811589153
MIXING_COUNT = 10

def sign(x):
    if x < 0:
        return -1
    else:
        return 1


def do_mixing(encryptedFile):
    N = len(encryptedFile)
    mixedFile = list(zip(encryptedFile, range(len(encryptedFile))))
    for _ in range(MIXING_COUNT):
        for num, i in zip(encryptedFile, range(len(encryptedFile))):
            item = (num, i)
            oldI = mixedFile.index(item)

            # remove the item
            mixedFile.pop(oldI)

            # calc new index
            oldI = (oldI + num) % (N - 1)

            if oldI == 0 or oldI == N-1:
                oldI = N-1-oldI

            mixedFile = mixedFile[:oldI] + [item] + mixedFile[oldI:]
    return [num for num, _ in mixedFile]


def calc_answer(mixedNums):
    N = len(mixedNums)
    zeroIndex = mixedNums.index(0)
    groveCoordinates = [mixedNums[(zeroIndex + (i+1)*1000) % N]
                        for i in range(3)]
    print(sum(groveCoordinates))


def parse_input():
    return list(map(int, open('in.txt', 'r').read().split('\n')))


encryptedFile = parse_input()
encryptedFile = [num * KEY for num in encryptedFile]
calc_answer(do_mixing(encryptedFile))
