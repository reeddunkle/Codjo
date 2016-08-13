'''
sorted_search.py
Input:
You have an element x, and a list named listy.
The list contains sorted, positive integers.
Find the index at which an element x occurs in listy.
If x occurs multiple times, you may return any of those indices.

Output:
Return a single integer that represents the index
at which the input element x occurs in the input listy.
If element x is not in listy, return -1.
'''


def find(x, listy):
    min_index = 0
    max_index = len(listy)

    while min_index < max_index:
        pointer = (min_index + max_index) // 2

        if listy[pointer] == x:
            return pointer

        elif listy[pointer] > x:
            max_index = pointer

        elif listy[pointer] < x:
            min_index = pointer

    return -1
