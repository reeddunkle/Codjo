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
    max_index = len(listy)
    min_index = 0

    while True:
        pointer = (max_index - min_index)//2 + min_index
        if listy == []:
            return -1
        elif listy[pointer] == x:
            return pointer
        elif abs(max_index - min_index) <= 1: #we've run out of list to check!
            return -1
        elif listy[pointer] > x:
            max_index = pointer
        elif listy[pointer] < x:
            min_index = pointer