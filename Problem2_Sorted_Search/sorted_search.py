

def find(x, listy):

    first = 0
    last = len(listy)-1
    index = -1

    while first <= last and index == -1:
        mid = (first + last) // 2

        if listy[mid] == x:
            index = mid

        else:
            if x < listy[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return index
