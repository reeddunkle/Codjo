

def is_even(listy):
    return len(listy)%2 == 0

def find(x, listy):

    if len(listy) == 0:
        return -1

    half = len(listy)//2

    if listy_even(listy):
        listy_left = listy[:half]
        listy_right = listy[half:]
    else:
        listy_left = listy[:half + 1]
        listy_right = listy[half + 1:]

    max_left = listy_left[-1]
    max_right = listy_right[-1]

    if x > max_left:
        for i in range(len(listy_right)):
            if listy_right[i] == x:
                return i + len(listy_left)

    else:
        for i in range(len(listy_left)):
            if listy_left[i] == x:
                return i

    return -1
