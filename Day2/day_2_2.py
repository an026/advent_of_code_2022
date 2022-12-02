filename = 'input_day2.txt'

# part 1
def rps_strategy_revealed(filename : str) -> int:
    # A = Rock, B = Paper, C = Scissors
    # X = Rock, Y = Paper, Z = Scissors
    strategy_win = {
        "A": "Y",
        "B": "Z",
        "C": "X"
    }

    strategy_lose = {
        "A": "Z",
        "B": "X",
        "C": "Y"
    }

    convert = {
        "A": "X",
        "B": "Y",
        "C": "Z"
    }

    score = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    # X = lose, Y = draw, Z = win
    # match must conclude according to this

    total = 0
    with open(filename) as file:
        for line in file:
            if line[2] == "Z":
                # winning strategy
                win_hand = strategy_win[line[0]]
                total += (6 + score[win_hand])
            elif line[2] == "Y":
                # draw strategy
                same_hand = convert[line[0]]
                total += (3 + score[same_hand])
            else:
                total += score[strategy_lose[line[0]]]

    return total


if __name__ == '__main__':
    print(rps_strategy_revealed(filename))
