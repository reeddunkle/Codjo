

def make_palindrome(s, max_moves):
    arr = list(s)
    arr_length = len(arr)
    half_length = arr_length // 2
    is_odd = arr_length % 2
    half_length += is_odd

    def opp(i):
        return arr_length-1-i

    diffs = {i if arr[opp(i)] > arr[i] else opp(i)
             for i in range(half_length) if arr[i] != arr[opp(i)]}

    diff_length = len(diffs)

    if diff_length > max_moves:
        return -1

    left_overs = max_moves - diff_length
    i = 0
    while left_overs > 0 and i < half_length:
        if i not in diffs and opp(i) in diffs:
            if arr[i] != '9':
                diffs.add(i)
                left_overs -= 1

        elif opp(i) not in diffs and i in diffs:
            if arr[opp(i)] != '9':
                diffs.add(opp(i))
                left_overs -= 1

        elif i not in diffs and opp(i) not in diffs:
            if left_overs > 1:
                if arr[i] != '9':
                    # Both sides are the same
                    diffs.add(i)
                    diffs.add(opp(i))
                    left_overs -= 2

            else:
                if i == half_length-1 and is_odd:
                    diffs.add(i)
                    left_overs -= 1

        i += 1

    for diff in diffs:
        arr[diff] = '9' if opp(diff) in diffs else arr[opp(diff)]

    return ''.join(arr)


if __name__ == '__main__':

    len_s, k = input().split()
    k = int(k)
    s = input()
    output = make_palindrome(s, k)

    print(output)
