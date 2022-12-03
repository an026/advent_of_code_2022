filename_small = "input_day_3_small.txt"
filename = "input_day_3.txt"


def rucksack_search(filename: str) -> int:
    # goal: group each line in threes, find common letter in that group
    total = 0
    myPriority = {
        "a": 1, "A": 27,
        "b": 2, "B": 28,
        "c": 3, "C": 29,
        "d": 4, "D": 30,
        "e": 5, "E": 31,
        "f": 6, "F": 32,
        "g": 7, "G": 33,
        "h": 8, "H": 34,
        "i": 9, "I": 35,
        "j": 10, "J": 36,
        "k": 11, "K": 37,
        "l": 12, "L": 38,
        "m": 13, "M": 39,
        "n": 14, "N": 40,
        "o": 15, "O": 41,
        "p": 16, "P": 42,
        "q": 17, "Q": 43,
        "r": 18, "R": 44,
        "s": 19, "S": 45,
        "t": 20, "T": 46,
        "u": 21, "U": 47,
        "v": 22, "V": 48,
        "w": 23, "W": 49,
        "x": 24, "X": 50,
        "y": 25, "Y": 51,
        "z": 26, "Z": 52
    }
    with open(filename) as file:
        data = file.read().strip()

    # list of strings, split at each new line
    rucksack_list = data.split('\n')

    index = 0

    # len(6) - 2 = 4, index < 4, bc [0 1 2 3 4 5]
    while index < len(rucksack_list) - 2:

        bag1 = rucksack_list[index]
        bag2 = rucksack_list[index + 1]
        bag3 = rucksack_list[index + 2]

        for item in bag1:
            if item in bag2 and item in bag3:
                total += myPriority[item]
                break

        index += 3

    return total


if __name__ == '__main__':
    print(rucksack_search(filename))
