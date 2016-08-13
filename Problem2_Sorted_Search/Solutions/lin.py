'''
RC Start Codjo problem 2, written by Liu Liu, August 11, 2016.
The challenge was not to use len() function of the list structure but use the pre-defined Listy type.
I wrote a my_len() function to obtain the length.
Although the time complexity was cut half through looping half length of the list, the time needed to finish testing did not decrease, compared to directly calling len() function.
'''

class NoLengthMethod(Exception):
    pass

class Listy(list):
    def __len__(self):
        raise NoLengthMethod('No __len__ method found.')

    def element_at(self, i):
        try:
            return self.__getitem__(i)

        except IndexError:
            return -1

def left_num (listy, index):
    return Listy.element_at(listy, index)

def right_num (listy, index):
    return Listy.element_at(listy, -1-index)

def my_len(listy):
    '''Obtain the length of the Listy'''
    index = 0
    left = left_num(listy, index)
    right = right_num(listy, index)
    while left < right:
        index = index + 1
        left = left_num(listy, index)
        right = right_num(listy, index)
    if left == right:
        if left_num(listy, index+1) == right_num(listy, index+1):
            return (index + 1) * 2
        else:
            return (index * 2) + 1
    else:
        return index * 2

def find(num, alist):
    listy = Listy(alist)
    index = 0
    left = left_num(listy, index)
    right = right_num(listy, index)

    while left <= right and left != -1:
        if left == num:
            return index
        elif right == num:
            return my_len(listy) - 1 - index
        else:
            index = index + 1
            left = left_num(listy, index)
            right = right_num(listy, index)

    return -1
