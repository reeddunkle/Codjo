

def make_palindrome(s, max_moves):
    arr = list(s)
    moves = 0

    for i in range(len(s)//2):
        a = arr[i]
        z = arr[-1-i]

        if a != z:
            moves += 1
            if z > a:
                arr[i] = z
            else:
                arr[-1-i] = a

        if moves >  max_moves:
            return -1

    return ''.join(arr)


if __name__ == '__main__':

    len_s, k = input().split()
    k = int(k)
    s = input()

    output = make_palindrome(s, k)
    print(output)
