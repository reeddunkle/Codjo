# Optimizing

Optimizing your program means optimizing its time and space requirements. Common considerations are searching and sorting algorithms.

Time
----

To optimize for time complexity in your program, you want to track how many times your program needs to do something.

Let's say you're given a list as an input of length 10:

```python
input = [0, 4, 6, 3, 2, 7, 5, 1, 8, 8]
```

If this is your program:

```python
def return_first_num(input):
    return input[0]
```

It doesn't matter how big your input is, this program has a **constant** time complexity. It's doing a set number of things (in this case it's doing one thing) that doesn't depend on the size of your input at all. This isn't a practical example though.

What if you want to search for an `8`?

```python
def find_eight(input):
    for n in input:
        if n == 8:
            return n

    return None
```

Its time complexity is `N`, which means that it is the length of the input. Worst case scenario, it has to go the entire way through the input to see if it finds an `8`. This is called **linear**. The longer the input, the longer the time complexity.

It's pretty common to have your program do something a certain amount of time based on its input. When optimizing for time, you want to try to reduce this number.

What if you try to sort the input using Bubble Sort?

```python
def bubble_sort(input):
    for i in range(len(input)):
        for k in range(len(input)):
            if input[i] < input[k]:
                input[i], input[k] = input[k], input[i]

    return input
```

Given your input of length 10, how many times do you have to go through it now? N*N. That's `N-squared`.

It's worth trying to optimize at this point.


Notice this function to check whether something is a palindrome:

```python
is_palindrome(input):
    for i in range(len(input)//2):
        if input[i] != input[-1-i]:
            return False
    return True
```

Given an input of length `N`, what's its time complexity? `N/2`.


Space
----

Space is how much simultaneous memory your program requires. I'm pretty sure when judging the space complexity of a program, they look for how much memory your program uses in addition to the initial input.


If you have a list of length `N`, that must be held in memory during the entire execution, your space requirement is `N`. This is the case for `find_eight`. It's also true for `is_palindrome`. But with `bubble_sort` it's not.

Look again:

```python
def bubble_sort(input):
    for i in range(len(input)):
        for k in range(len(input)):
            if input[i] < input[k]:
                input[i], input[k] = input[k], input[i]

    return input
```

Let's assume you're using Python2. What does `range` return?

```
>>> a = range(10)
>>> type(a)
<type 'list'>
```

It returns a list. Your function actually generates two lists of length `N`, so its space complexity, like its time complexity, is N*N => `N-squared`.


When optimizing for space you want to require as little memory as possible.


Time vs. Space
----

Often these two compete. If you want to optimize for space, but you can take as much time as you need, you're then running through your input lots and lots of times, but maybe only ever holding one item in memory in addition to the input.

On the other hand, if you're optimizing for time, you could have lots of extra data structures holding bits of information, but perhaps you only need to run the entire way through your input twice in total.

The concept of this tradeoff would do better with examples. I'll try to flesh this out more in the future.

Regardless of the tradeoff, when trying to optimize you should still try to reduce both time and space simultaneously as much as possible.
