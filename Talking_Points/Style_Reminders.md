
# _Style_

A lot of the same style concepts have come up in our code review. I thought I would make a quick list.
**Note:** This is only going to refactor for style, not for overall better code.

----

In this code snippet, we're going to:

1. Space out the code
2. Correct the inline comment
3. Make the code read more logically

Change this...

```python
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
```

To this...

```python
def find(x, listy):
    # Change these to read from first to last
    min_index = 0
    max_index = len(listy)

    # Space this out to give our eyes some room to breathe
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
```
