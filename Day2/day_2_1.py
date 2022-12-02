filename = 'input_day2.txt'
# part 1
def rps_strategy(filename : str) -> int:
    # A = Rock, B = Paper, C = Scissors
    # X = Rock, Y = Paper, Z = Scissors
    strategy_win = {
        "A" : "Y",
        "B" : "Z",
        "C" : "X"
    }

    convert = {
        "A": "X",
        "B": "Y",
        "C": "Z"
    }

    score = {
        "X" : 1,
        "Y" : 2,
        "Z" : 3
    }

    total = 0
    with open(filename) as file:
        for line in file:
            # winning match
            if strategy_win[line[0]] == line[2]:
                total += 6
            elif convert[line[0]] == line[2]:
                total += 3
            total += score[line[2]]

    return total

if __name__ == '__main__':
    print(rps_strategy(filename))

