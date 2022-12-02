filename = 'input.txt'

# part 1
def maxValue(filename : str) -> int:
    myList = []
    with open(filename) as file:
        group = 0
        for line in file:
            if line != '\n':
                group += int(line)
            else:
                myList.append(group)
                group = 0

    return max(myList)

# part 2
def topThree(filename : str) -> int:
    myList = []
    with open(filename) as file:
        group = 0
        for line in file:
            if line != '\n':
                group += int(line)
            else:
                myList.append(group)
                group = 0

    totalTopThree = 0
    for i in range(3):
        maxCal =  max(myList)
        myList.remove(maxCal)
        totalTopThree += maxCal
    return totalTopThree



if __name__ == '__main__':
    # print(maxValue(filename))
    print(topThree(filename))