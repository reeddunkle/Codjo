
def find(element, listy):
    index = 1

    while listy.element_at(index) != -1 and listy.element_at(index) < element:
        index *= 2

    return binary_search(element, listy, index // 2, index)


def binary_search(element, listy, low, high):
    mid = (low + high) // 2

    if low > high:
        return -1

    middle = listy.element_at(mid)

    if middle == element:
        return mid

    if middle > element or middle == -1:
        high = mid - 1
    else:
        low = mid + 1

    return binary_search(element, listy, low, high)



def my_len(listy):

    if listy.element_at(0) != -1:
        low = 0
        high = 1

        while listy.element_at(high) != -1:
            high, low = high * 2, high

# high = 8
# low = 4
        while low <= high:
            mid = (low + high) // 2
            middle = listy.element_at(mid)

            if listy.element_at(mid) != -1:
                low = mid + 1

            else:
                high = mid


    return 0


Binary Search
----

This was the solution I wrote for the first goal. We went over this in the code review. I've refactored it a little from what you saw. I changed the names of the variables to `low` and `high`. Originally I had `left` and `right`, but those weren't as good. I also adjusted my spacing to be consistent throughout the function.


```python
def find(x, listy):

    low = 0
    high = len(listy) - 1

    while low <= high:
        mid = (low + high) // 2

        if listy[mid] == x:
            return mid

        if x < listy[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1
```

Extra Challenge
----

Extra Goal? I don't know what to call this.

During Friday's code review, a few of us stayed on the call at the end and worked on this. The challenge was to not use the `__len__` method of the input list, and instead use a method called `element_at`, which given an index, returns the element at that index if it exists, or `-1` otherwise.

To determine the list's length in logarithmic time, we started writing this:

```python
def my_len(listy):

    if listy.element_at(0) != -1:
        low = 0
        high = 1

        while listy.element_at(high) != -1:
            high, low = high * 2, high
            #
            # Find length
            #

    return -1
```

We were trying to write a function that would tell us the length of the list. I was thinking at this point we could keep bouncing between low and high until we found the exact length.

But we didn't actually need to know the exact length of the list. We needed to set the search parameters and then look for our element. The way to do this was to build a binary search function with more traditional parameters:

```python
def binary_search(x, listy, low, high):
    while low <= high:
        mid = (low + high) // 2
        middle = listy[mid]

        if middle == x:
            return mid

        elif middle < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1
```

Around this point, I refactored `x` to use a better variable name. And started writing the `find` method using the code from `my_len` above:

```python
def find(element, listy):
    low = 0
    high = 1

    while listy.element_at(high) != -1:
        high, low = high * 2, high

[...]
```

At this point, we could ignore `low`, and just call `binary_search` like this:

```
return binary_search(element, listy, 0, high)
```

This assumes our goal is to find the first index at returns `-1` from listy. This tricked me at first. The goal, actually, is to find the first index that returns a value that's _larger_ than `element`. It might return `-1` before we have that information, but the former is much better information.

So we change the while-loop's condition to check for that, and suddenly `low` becomes very useful. We know that `element` is trapped between the two:

```python
def find(element, listy):
    low = 0
    high = 1

    while listy.element_at(high) != -1 and listy.element_at(high) < element:
        high, low = high * 2, high


    return binary_search(element, listy, low, high)
```

This looks like what we want. Now what about `binary_search`?

```python
def binary_search(element, listy, low, high):
    while low <= high:
        mid = (low + high) // 2
        middle = listy.element_at(mid)

        if middle == element:
            return mid

        elif middle > element:
            high = mid - 1

        else:
            low = mid + 1

    return -1
```

There's a bug. See if you can spot it?

```
.
.
.
.
.
.
.
.
.
.
.
.
.
.
```

Spoiler:

`high` could be an index that is out of range, and will return `-1`. Because we know that all of the list's integers are positive, we can treat `-1` as a number that's greater than and not equal to element, and add a check:

```python
def binary_search(element, listy, low, high):
    while low <= high:
        mid = (low + high) // 2
        middle = listy.element_at(mid)

        if middle == element:
            return mid

        elif middle > element or middle == -1:
            high = mid - 1

        else:
            low = mid + 1

    return -1
```

This is how we solved it last night. As I'm writing this, though, I see another, possibly simpler solution to handling that "bug" above. We could check if `element` is less than `middle` first, rather than checking if it is greater than `middle` first, and use and `else` to cover the case of `middle` being greater than `element` or equal to `-1`:

```python
def binary_search(element, listy, low, high):
    while low <= high:
        mid = (low + high) // 2
        middle = listy.element_at(mid)

        if middle == element:
            return mid

        elif middle < element:
            low = mid + 1

        else:
            high = mid - 1

    return -1
```

This feels hacky, because `-1` is definitely less than `element`, so it would throw our function out of whack. But I think we're safe because `low` will always be less than or equal to `high`, and only `high` can return `-1`.

Our final code is:

```python
def find(element, listy):
    low = 0
    high = 1

    while listy.element_at(high) != -1 and listy.element_at(high) < element:
        high, low = high * 2, high

    return binary_search(element, listy, low, high)


def binary_search(element, listy, low, high):
    while low <= high:
        mid = (low + high) // 2
        middle = listy.element_at(mid)

        if middle == element:
            return mid

        elif middle < element:
            low = mid + 1

        else:
            high = mid - 1

    return -1
```

That's it. Let me know if you can break it!

----

At the end, we also made a recursive version of `binary_search`. Here's the code:

```
def binary_search(element, listy, low, high):
    mid = (low + high) // 2

    if low > high:
        return -1

    middle = listy.element_at(mid)

    if middle == element:
        return mid

    if middle > element or middle == -1:
        high = mid - 1
    else:
        low = mid + 1

    return binary_search(element, listy, low, high)
```
