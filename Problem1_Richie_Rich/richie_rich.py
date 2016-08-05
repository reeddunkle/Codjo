'''palindrome problem, solved by Lin Liu and Elaine Chan'''

def is_palindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[-1-i]:
            return False
    else:
        return True

def change_letter(s):
    for i in range(len(s)//2):
        #if s[i] != s[-1-i]:
        if s[i] != s[len(s) - i-1]:
            if s[i] < s[-1-i]:
                s = s[:i] + s[-1-i] + s[i+1:]
            else:
                s = s[:(len(s) - i -1)] + s[i] + s[len(s) -i:]
            return(s)

def make_palindrome(n_digits, k):
    n_str = str(n_digits)
    if is_palindrome(n_str):
        return(n_str)
    else:
        n_str = change_letter(n_str)
        k = k - 1
        if k >= 0:
            if is_palindrome(n_str):
                return(n_str)
            else:
                a = make_palindrome(n_str, k)
                return (a)
        elif k < 0:
            return (-1)
