possible_rounds = {
    'A X': 4,
    'A Y': 8,
    'A Z': 3,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 7,
    'C Y': 2,
    'C Z': 6,
}


def calc_score(round_input):
    return possible_rounds[round_input]


def main():
    print(sum(map(calc_score,  open('in.txt', 'r').read().split('\n'))))


main()
