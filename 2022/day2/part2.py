possible_rounds = {
    'A X': 3,
    'A Y': 4,
    'A Z': 8,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 2,
    'C Y': 6,
    'C Z': 7,
}


def calc_score(round_input):
    return possible_rounds[round_input]


def main():
    print(sum(map(calc_score,  open('in.txt', 'r').read().split('\n'))))


main()
