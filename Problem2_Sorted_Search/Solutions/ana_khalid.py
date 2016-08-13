
def find(target, listy):

    lo = 0
    hi = len(listy) - 1

    while lo <= hi:
        mid = (hi + lo) // 2

        if target == listy[mid]:
            return mid

        elif target < listy[mid]:
            hi = mid - 1

        else:
            lo = mid + 1

    return -1
