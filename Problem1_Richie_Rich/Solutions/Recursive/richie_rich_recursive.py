'''
    Recursive solution to richie_rich.py
'''

def _make_palindrome(arr, moves_left, i=0):
    if i >= len(arr)//2:        # Base case 1: i has reached the middle of the list
        return ''.join(arr)

    if not moves_left:          # Base case 2: no moves left
        return -1

    if arr[i] != arr[-1-i]:     # arr[-1-i] is the same as arr[len(arr)-1-i]
        arr[i] = arr[-1-i]
        moves_left -= 1

    # Instead of list splicing, you increment an index pointer (i)
    return _make_palindrome(arr, moves_left, i+1)


def make_palindrome(input, k):
    '''Given string and a number of moves remaining, attempts to
    make the string palindromic, each change costs 1 move. Returns
    the string as a palindrome, or -1 if not enough moves.
    '''
    return _make_palindrome(list(input), k)

