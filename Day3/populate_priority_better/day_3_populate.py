# TODO: How can I populate the priority dictionary faster?
# code

def populate_priority(c : str) -> int:
    score = 0
    c = c[0]
    if c.isupper():
        score += ord(c) - ord('A') + 27
    else:
        score += ord(c) - ord('a') + 1

    return score

if __name__ == '__main__':
    print(populate_priority('rr'))
