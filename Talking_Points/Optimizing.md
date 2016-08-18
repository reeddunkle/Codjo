# Optimizing

During the code reviews we inevitably end up talking about ways to optimize your code. I'm going to explain different concepts, and point out things to beware of to help you write better code.

**Note:** In my examples I'm using Python3. For the Python2 equivalent, use `xrange` instead of `range`.

Big O
----

If you've joined in the code reviews, you've heard us talk about "big O notation". It's used to indicate how an algorithm responds to different input sizes:

[Wikipedia](https://en.wikipedia.org/wiki/Big_O_notation):
> In computer science, big O notation is used to classify algorithms by how they respond to changes in input size, such as how the processing time of an algorithm changes as the problem size becomes extremely large.

This is what we mean when we talk about an algorithm's "complexity". We want to measure at what rate the algorithm grows when we change the input size.

We can say that an algorithm's complexity measures how the function responds when you change the input size, which is another way of defining its performance. The goal of optimizing, then, is to reduce that response and improve its performance.


Time Complexity
----

#### Linear

Look at this example of `is_palindrome` from [Problem1's tests](https://github.com/reeddunkle/Codjo/blob/master/Problem1_Richie_Rich/richie_rich_test.py):

```python
def is_palindrome(text):
    for i in range(len(text)//2):
        if text[i] != text[-1-i]:
            return False

    return True
```

During the code review I went over how much time the function requires, and I used the terms "time complexity", and "runtime". These describe the same thing.

To measure its time complexity, I asked, "How does the function respond to inputs of different sizes?"

Let's say the input to `is_palindrome` is `"1234554321"`, and so `len(text) == 10`. Before it completes, the for-loop will assign to `i` the numbers `0, 1, 2, 3, 4`

If _N_ represents the size (length) of the input, in the worst case scenario this function needs to loop _N/2_ times.

When this came up in our discussion, someone said that they hadn't realized until later that they only needed to iterate through half of the input. Instead they used something like this:

```python
def is_palindrome(text):
    for i in range(len(text)):
        if text[i] != text[-1-i]:
            return False

    return True
```

With the same input, the function now needs to loop _N_ times (where _N_ is the size of the input).

There are a few more terms I'll introduce that people use when talking about complexity.

In the example above, where the function has to iterate _N_ times, they say that it has a **linear** time complexity (or runtime), because the time complexity grows linearly with its input size. The "Big O" notation for this is `O(N)`.

#### Quadratic

Now take this example with the input `[0, 4, 6, 3, 2, 7, 5, 1, 8, 8]`:

```python
def bubble_sort(numbers):
    for i in range(len(numbers)):
        for k in range(len(numbers)):
            if numbers[i] < numbers[k]:
                numbers[i], numbers[k] = numbers[k], numbers[i]

    return numbers
```

`numbers` has a length of 10, so `i` will be assigned each number from `0...10`, and `k` will also be assigned each number from `0...10`. The catch is that `k` is going to perform _N_ operations for every one of `i`.

`i` is going to start of at `0`, and then `k` will go through the loop. Then `i` will become `1`, and `k` will going through the loop, etc.

This is `O(N²)`, which grows at a **quadratic** rate.

#### Drop the Constants

Consider this example:

```python
def print_twice(numbers):
    for num in numbers:
        print(num)

    for num in numbers:
        print(num)
```

There are two for-loops that each loop n-times, and so it would seem to follow that its time complexity would be `O(2N)`. It isn't, however, it's still just `O(N)`.

And in the first example of `is_palindrome`:

```python
def is_palindrome(text):
    for i in range(len(text)//2):
        if text[i] != text[-1-i]:
            return False

    return True
```

You'd think that its complexity is `O(N/2)`. Again, though, it's `O(N)`.

This is really hard to get used to.

Big O only describes the rate of increase. It expresses how the algorithm scales, how fast the complexity grows with its input. In these examples, the runtime grows at a linear rate.

It's definitely possible for `O(N²)` to run faster than `O(N)` code. You want to use big O to think about how the performance is going to change with big (really big) inputs. There will be a point where _N²_ might be as good as, say, _100N_, but at some point when the input size changes enough, it will start to be worse.

We just need to accept that it doesn't mean that `O(N)` is always better than `O(N²)`.

In absolute efficiency terms, _N/2_ iterations is preferable to _2N_, and the former should definitely be used over the latter. But in relative terms, they grow at more or less the same speed, which means that they are both preferable (at some point) over _N²_.

#### Constant

The last one I'm going to cover before talking about space complexity is **constant**, which is `O(1)`. This means no matter how the input changes, your function's performance is contant.

Here's a short, pointless example using the same input as above, `[0, 4, 6, 3, 2, 7, 5, 1, 8, 8]`:

```python
def print_first_five(numbers):
    for i in range(5):
        print(numbers[i])
```

It wouldn't matter if the input size were 200 instead of 10. It's just going to print the first five numbers in the list. This function's complexity responds to changes in input size at a constant rate, `O(1)`.

#### Logarthmic and "Linearithmic"

There are common benchmarks for different types of algorithms that are worth learning.

For example, if your input is sorted, you can use binary search to find an element in **logarithmic** time, `O(log(N))`. We covered this in [Problem2](https://github.com/reeddunkle/Codjo/tree/master/Problem2_Sorted_Search).

We'll do sorting algorithms in the near future, but you should be aware that [Bubble Sort is notoriously bad](https://youtu.be/k4RRi_ntQc8) at `O(N²)`. Better algorithms like quick sort and merge sort achieve `O(N log(N))`. [Some people](https://en.wikipedia.org/wiki/Time_complexity#Linearithmic_time) call `O(N log(N))` "linearithmic" as shorthand. Personally, I just say "N log N".

#### Exponential

`O(2ⁿ)` complexity is called **exponential**. An example is a recursive Fibonacci function:

```python
def fib(n):
    '''Returns the first n Fibonacci numbers.'''
    if n <= 1:
        return n

    return fib(n - 2) + fib(n - 1)
```

**Note:** Beware of `O(N²)` and `O(2ⁿ)` in interviews! That's usually a red flag, and indicates that there is room for improvement.

#### Best Case, Worst Case, and Expected Case

Back to the example of _is_palindrome_ one last time:

```python
def is_palindrome(text):
    for i in range(len(text)//2):
        if text[i] != text[-1-i]:
            return False

    return True
```

You might point out that this function could exit the loop midway with its `return False` statement, and you're right. It could exit with the first calculation even and get an `O(1)` in the best case.

You can actually describe your complexity in three different ways, **best case**, **worst case**, and **expected case**.

Usually, people don't talk about best case time complexity. It isn't that useful.

As for distinguishing between expected and worst case, I haven't read a good explanation yet.

This is Gayle Laakmann McDowell's explanation in _Cracking the Coding Interview_:
> For many—probably most—algorithms, the worst case and the expected case are the same. Sometimes they're different, though, and we need to describe both of the runtimes.

Just before she says this, she explains the best, worst, and expected runtimes for quick sort (`O(N)`, `O(N²)`, and `O(N log(N))` respectively). The number people care about with quick sort is almost always `O(N log(N))`.

On the other hand, with `is_palindrome`, no one would think to calculate an expected case by averaging the best and the worst. They would just say that the expected is the same as the worst.

For now, forgive my less-than-perfect explanation of this. At least you're aware of this, if you weren't before.


Space Complexity
----

Space complexity is talked about in the same way as time complexity.

Your function's space complexity refers to how your function's space requirements change as you change the input size.

I'll go through some simple examples. For all of them, let's assume the input is still `[0, 4, 6, 3, 2, 7, 5, 1, 8, 8]`.

First, two examples of constant space:

**`O(1)`**

```python
def constant_space(numbers)
    new_list = []
    for i in xrange(5):
        new_list.append(numbers[i])

    return new_list
```

and...

```python
def bubble_sort(numbers):
    for i in range(len(numbers)):
        for k in range(len(numbers)):
            if numbers[i] < numbers[k]:
                numbers[i], numbers[k] = numbers[k], numbers[i]

    return numbers
```

The first function creates a new list and adds the first five numbers from the input to it. No matter how large `numbers` is, the function only requires a constant 5-length list to be held in memory.

`bubble_sort` on the other hand requires no additional memory. It destroys the original input by mutating it in place (which is something you'll hear people criticize), but in return it doesn't take up any additional space.

**`O(N)`**

```python
def linear_space(numbers)
    new_list = []
    for i in range(n):
        new_list.append(numbers[i])

    return new_list
```

This `linear_space` function requires an n-length list to be held in memory, as it's simply copying the current input. The larger the input, the larger `new_list` will swell.


Time vs. Space
----

It's common to find time and space competing with one another. People in every field talk about "design trade-offs". In CS, there tends to be a trade-off between time and space. You definitely want to minimize both, but at some level you'll probably find yourself facing design trade-offs.

An example where you face a trade-off is with caching. A cache holds in memory some information that you've already spent time calculating, in order to speed up retrieving that information the next time you want it. Given the same input, it spares you the runtime. In other words, you're using extra space to increase speed.

At one end of the spectrum, you could imagine a cache that holds the result of every calculation your function might perform. Its space complexity would be infinite, but its time complexity given this (idealistic) cache could be constant.

On the other end of the spectrum, imagine that there is no cache, and so your function has to run its calculations every time. You save space at the cost of time.
