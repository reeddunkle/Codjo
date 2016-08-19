# Optimizing — Part 2

In [Part 1](https://github.com/reeddunkle/Codjo/blob/master/Talking_Points/Optimizing_Part1.md) I talked through the concepts, and tried to lay a foundation.

In this part I'll just focus on associating the terms with their code. There are countless ways to code certain complexities, so just try to get a feel for what the code is doing, rather than the specific implementation I'm showing.

This part is a bit of a cheat sheet for interviewing — the terms, the code to avoid, and the code to write. It is incomplete. I'm starting with the common stuff, the "basics", the stuff you're most likely to have to deal with in an interview.

#### Constant — `O(1)`

**Time**

```python
def is_list(container):
    return type(container) == list
```

You might pass it a huge list, but it isn't concerned with how big it is. It's just doing a `type` check.

Examples of **constant** time complexity built-in methods are:
`append`, `__getitem__`, `__setitem__`, and `len`

**Space**

```python
def binary_search(value, listy, low, high):
    while low <= high:
        mid = (low + high) // 2
        middle = listy[mid]

        if middle == element:
            return mid

        elif middle > element:
            high = mid - 1

        else:
            low = mid + 1

    return -1
```

No matter how large `listy` is, you're only storing a constant number of variables/values each iteration.

Note: Some of you wrote `binary_search` using list-splicing. In Python, list-splicing creates a new copy of the list each time. That means more space each time.

#### Linear — `O(N)`

**Time**

```python
def print_list(lst):
    for thing in list:
        print(thing)
```

It loops through the entire list, printing each element.

Examples of **linear** time complexity built-in methods are:
`copy`, `del`, `x in s` (membership), `min` and `max`

**Space**

```python
def square_list(lst):
    return [x**2 for x in lst]
```

It stores a new list with the same number of elements.

#### Logarithmic — `O(log(N))`

**Time**

```python
def binary_search(value, listy, low, high):
    while low <= high:
        mid = (low + high) // 2
        middle = listy[mid]

        if middle == element:
            return mid

        elif middle > element:
            high = mid - 1

        else:
            low = mid + 1

    return -1
```

Each iteration, it cuts its search space in half.

**Space**

Logarithmic space-complexity isn't talked about as much. If you were storing every number (or node, in a binary search tree) you visit, that would be logarithmic space.

#### "Linearithmic" — `O(N log(N))`

**Time**

For now, I'm not going to post code for sorting so that we can cover it in the upcoming weeks. The idea is that you have to go through the entire input, and for each one, you can perform a logarithmic function.

Examples of `O(N log(N))` time complexity built-in methods are:
`sorted` and `sort`

**Space**

Again, `O(N log(N))` space isn't common.

#### Quadratic — `O(N²)`

**Time**

```python
def is_palindrome(word):
    for i in range(len(text)):
        if text[i] != text[-1-i]:
            return False

    return True

def make_palindrome(word):
    for i in range(len(word)):
        if is_palindrome(word):
            return word
        else:
            if word[i] != word[-1-i]:
                word[i] == word[-1-i]

    return -1
```

Each iteration in `make_palindrome` calls `is_palindrome`.

**Space**

Imagine storing multiple copies of the input.

#### Exponential — `O(2ⁿ)`

**Time**

```python
def fib(n):
    '''Returns the first n Fibonacci numbers.'''
    if n <= 1:
        return n

    return fib(n - 2) + fib(n - 1)
```

Its growth doubles for every 1 of the input.

**Space**

The example of `fib` is actually exponential in space complexity also. It creates two copies for every 1 input.


#### Interview Notes
Beware of `O(N²)`, `O(N³)`, `O(N⁴)`, and `O(2ⁿ)` in interviews!