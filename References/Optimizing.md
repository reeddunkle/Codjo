# Optimizing

During the code review for [Problem1](https://github.com/reeddunkle/Codjo/tree/master/Problem1_Richie_Rich), a few times we mentioned the idea of optimizing. Optimizing is something you'll hear people talk about all the time, and I'd like to cover it as best I understand it (I don't have a CS background), and de-mystify it a little I hope.

**Note:** I'm going to be assuming Python3. For the Python2 equivalent, instead of using `range` you should use `xrange`.

### Big O

From [Wikipedia](https://en.wikipedia.org/wiki/Big_O_notation):
> In computer science, big O notation is used to classify algorithms by how they respond to changes in input size, such as how the processing time of an algorithm changes as the problem size becomes extremely large.

### Time

Using the example of the `is_palindrome` method that I made for [the test](https://github.com/reeddunkle/Codjo/blob/master/Problem1_Richie_Rich/richie_rich_test.py) for Problem1, I talked about the idea of how much time it requires. When talking about how much time a function requires, people use terms like "time complexity", and "run time", and they will represent it using the "Big O" notation. Here's the method:

```python
def is_palindrome(text):
    for i in range(len(text)//2):
        if text[i] != text[-1-i]:
            return False

    return True
```

Let's say the input is `1234554321` and so `text` has a length of 10. When you ask, "What is my time complexity?", that's an official-sounding way of asking, "Given this input, how many times does my method to do something?"

In this example, the method has `text` of length 10, and it assigns `i` to each number in the range of 0 to half the length of `text`. In the for-loop, `i` is going to be each number from `0...10//2`.

Now, you might point out that this function could exit the loop midway with its `return False` statement. Whether it does that or not is out of our control, though, and so another thing you'll hear people talk about is "worse case scenario". That's the part we can try to control and optimize.

This idea of only needing to go half-way through the input came up in our group discussion, and someone said that they hadn't realized until later that they only needed to iterate through half of the input. Instead they used something like this:

```python
def is_palindrome(text):
    for i in range(len(text)):
        if text[i] != text[-1-i]:
            return False

    return True
```

With the same input of `1234554321`, `i` is going to be assigned each number in the range of 0 to the entire length of `text`, which is `0...10`.

I should point out that, despite these all being toy examples, addressing the problem of "Given an input, how many times do I need to do something" is a real-life consideration for real-life programs. And these same basic ideas that we've already covered are the same:

- Do I need to go through the entire input one time?
- Can I get away with only going through half of the input?

There are a few terms you should be aware of that people use to talk about them. For the example above where the function has to iterate through the entirety of the input, they say that it has a **linear** time complexity (or run-time). Linear, because the larger your input, the larger the time complexity. The "Big O" notation for this is `O(n)`.

For the first example, where you only have to go through half of the input, the Big O notation is `O(n/2)`.

One thing that doesn't seem obvious at first, is that when you have to go through `n` a set number of times, they usually drop the constant. Take this example, with this input `[0, 4, 6, 3, 2, 7, 5, 1, 8, 8]`:

```python
def print_twice(numbers):
    for num in numbers:
        print(num)

    for num in numbers:
        print(num)
```

It has to go through the input twice. So it would be `O(2n)`. If you ask any CS person, they will point out that constants (the `2` in this case) aren't very important when talking about really big numbers.

Regardless of that, what you and I need to know for practical purposes like interviews, is that we don't include the constants in Big O. So for this example the time complexity would still be `O(n)`.

Now, take _this_ example, with the same input `[0, 4, 6, 3, 2, 7, 5, 1, 8, 8]`:

```python
def bubble_sort(numbers):
    for i in range(len(numbers)):
        for k in range(len(numbers)):
            if numbers[i] < numbers[k]:
                numbers[i], numbers[k] = numbers[k], numbers[i]

    return numbers
```

`numbers` has a length of 10, so `i` will become each number from `0...10`, and `k` will also become each number from `0...10`. But the catch is that `k` is going to perform `n` operations for every one of `i`.

`i` is going to start of at `0`, and then `k` will go through the loop. Then `i` will become `1`, and `k` will going through the loop, etc.

So now it's `O(n-squared)`, which is called "quadratic".

There are common benchmarks for different types of algorithms, namely sorting and searching. I'll cover searching when we go over [Problem2](https://github.com/reeddunkle/Codjo/tree/master/Problem2_Sorted_Search), and we'll do sorting in the near future. You should be aware that [Bubble Sort is notoriously bad](https://youtu.be/k4RRi_ntQc8).


Another common one is "constant time", which is written as `O(1)`. This means that regardless of the size of the input, your function only has to do a set, constant number of operations.

Here's a short, pointless example using the same input as above, `[0, 4, 6, 3, 2, 7, 5, 1, 8, 8]`:

```python
def print_first_five(numbers):
    for i in range(5):
        print(numbers[i])
```

It wouldn't matter if the input were 200 instead of 10, right? It's just going to print the first five numbers in the list. This is "constant time".

You can read about Big O on , but I want you to be aware of two more common ones: `O(log(n))` and `O(N log(n))`. The first is the goal for searching, and the second is the goal for sorting. Again, I'll cover this more later.



Space
----

Space complexity is talked about in the same way as time complexity. and the common concepts are the same, "constant", "linear", and "quadratic" for example.

Your function's is how much simultaneous memory your function requires. When judging the space complexity of a function, they look for how much memory your function uses in addition to the initial input.

I'll go through some simple examples. For all of them, let's assume my input is the same I've been using `numbers = [0, 4, 6, 3, 2, 7, 5, 1, 8, 8]`:

**`O(1)`**

```python
def constant_space(numbers)
    new_list = []
    for i in xrange(5):
        new_list.append(numbers[i])

    return new_list
```

Here's another example of constant space from above:

```python
def bubble_sort(numbers):
    for i in range(len(numbers)):
        for k in range(len(numbers)):
            if numbers[i] < numbers[k]:
                numbers[i], numbers[k] = numbers[k], numbers[i]

    return numbers
```

The first function creates a new list and adds the first five numbers from the input to it. No matter how large `numbers` is, the function only requires a constant 5-length list to be held in memory.

`bubble_sort` on the other hand requires no additional memory. It destroys the original input by mutating it in place, something you'll hear some people criticize in general, but in return it doesn't take up any additional space.

**`O(n)`**

```python
def linear_space(numbers)
    new_list = []
    for i in range(n):
        new_list.append(numbers[i])

    return new_list
```

This function requires an n-length list to be held in memory, as it's simply copying the current input.


Time vs. Space
----

Time and space are sometimes competing with one another. You've probably heard people in every field talk about "design tradeoffs". In CS, there tends to be a tradeoff between time and space. Of course you want to try to minimize the requirements of both, but at some level you'll probably find yourself talking about design tradeoffs.

A simple example is caching. A cache holds in memory some information that you've already spent time calculating, in order to speed up retrieving that information the next time you want it. Given the same input, it saves you the run-time. In other words, you're using extra space to reduce the run-time.

At one end of the spectrum, you could imagine a cache that holds the result of every calculation your function might perform. It's space complexity would be infinite, but its time complexity given this utopian cache could be constant.

On the other end of the spectrum there is no cache, and so it must perform the calculations every time it is run. The space complexity would be constant, but it pays its time complexity with every run.
