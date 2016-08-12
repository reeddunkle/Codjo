# I think find, item, and ordered_list are all good variable names for this
# exercise.  I added a docstring, which may seem silly and super obvious
# but it's a good habit to pick up.
def find(item, ordered_list):
    """Return the index where item appears in ordered_list, or -1."""
    length = len(ordered_list)

    # You had two different cases in which you returned -1 without making a
    # recursive call: if the list is empty or if the list is of length 1
    # but it doesn't contain the item.  Both cases are handled by this if
    if length <= 1:
        return 0 if item in ordered_list else -1

    # I prefer using all of "ordered_list[index]" instead of "number"
    # because it's still short enough, and it makes it apparent that you
    # are looking at the element in the position given by index.  Using
    # only "number" makes it a little ambiguous as to which element it is,
    # and "number" is too close to "item".
    index = length//2
    # number = ordered_list[index]

    # The multiple ifs that you have left are now if-elif-else, which makes
    # it clearer that only one of them is ever going to be executed.  This
    # code suffers from what we were talking about last time: there are
    # multiple return statements, and a couple of them are not really near
    # the end of the function, which is where it naturally ends.  However,
    # I have left them there because a) the code is short enough that it
    # doesn't cause much trouble (by this I mean the code immediately
    # preceeding the return statements is only one or two lines long, not
    # that the find function is short), and b) the if-elif-else makes it
    # clear that only one return is ever going to be reached.
    if item == ordered_list[index]:
        return index

    elif item < ordered_list[index]:
        return find(item, ordered_list[:index])

    else:
        cur_index = index
        index = find(item, ordered_list[index:])
        return index + cur_index if index != -1 else -1

    # Final comment: this was well-written but the thing that jumps out is
    # that there is an assymetry in how the cases are handled.  When the
    # item is less than the element at the current index, you just return
    # the recursive call; if it's larger, then you have to fix the returned
    # value by adding it to the current index.  There's a way of handling
    # both in the same way, and returning just the return value of the
    # recursive call.  Furthermore, every time you are calling the fin
    # function, you are calling it on a new list (when you do
    # ordered_list[index:], python creates a whole new list in memory).
    # There's a way of circumventing this memory usage too.  You can fix
    # both my last comments with the same solution!