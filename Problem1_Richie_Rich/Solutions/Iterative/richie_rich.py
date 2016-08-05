'''
    Iterative solution to richie_rich.py
'''

def make_palindrome(string, moves_left):
    '''Given string and a number of moves remaining, attempts to
    make the string palindromic, each change costs 1 move. Returns
    the string as a palindrome, or -1 if not enough moves.
    '''
    arr = list(string)

    for i in range(len(arr)//2):

        if not moves_left:
            return -1

        if arr[i] != arr[-1-i]:
            arr[i] = arr[-1-i]      # Arbitrarily assign one to the other
            moves_left -= 1

    return ''.join(arr)
