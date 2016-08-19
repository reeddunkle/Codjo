# Optimizing

Foreword
----

In writing this, I've read a lot of different explanations of these topics. Every one of them made these concepts feels very academic, and stuffy. And a lot of them made mistakes.

Up until now, I was following suit, trying to dutifully cover each concept the way that I learned them myself. I'm going to try something new.

A substantial percentage of you all are here because you want to get a programming job one day. And a substantial subset of you don't have CS degrees or engineering degrees.

I'm going to write this for you, those of you who want to learn as much as you can, but want to focus on learning first what you need to get hired — those of us who need to hack the process a bit.

There is another percentage of you who are in school, or happy in your current field, and perhaps are participating in this primarily for the educational aspect. To you, I promise to not write anything that I'm not confident is correct. And it will be worth supplementing what I'm going to write, with a more traditional explanation, which you can find anywhere by Googling these terms.

The interview process will usually have you writing code at some point. It will have you working through an algorithm at some point. And it will have you discussing your code and your algorithm process with your interviewer.

Yes, you want to optimize your code for its own sake. But for now, I'm going to focus on optimizing to get you a job, and it will get you well on your way to writing better code for its own sake.

Contents
----

These topics — complexity, optimization, and "big O" — are notoriously confusing for beginners. They feel intimidating, confusing, and ambiguous. That's OK. It's normal. For now, just learn to be okay with those feelings.

You need to know enough to be able to talk about this stuff with an interviewer, and to be able to spot and improve costly code.

In Part 1, I'm going to get the worst part out of the way first. I'll introduce the topics, and provide explanations and code examples. This part will be more academic and boring. Just read it, take in as much as you can for now. This part will help you "talk shop" with an interviewer (and your peers after you get hired). You'll want to know this stuff, but for now don't let it bog you down too much.

In Part 2 there will be a re-cap, a cheat-sheet of sorts. I will pair code samples with terms so that you can spot the patterns. This is going to be incomplete. The thing to focus on are the sorts of common methods and loops that we write everyday, so that when you're writing you know what to avoid.

**Note:** In my examples I'm using Python3. For the Python2 equivalent, use `xrange` instead of `range`.

Big O
----

Big O notation is used to indicate how an algorithm responds to different input sizes:

[Wikipedia](https://en.wikipedia.org/wiki/Big_O_notation):
> In computer science, big O notation is used to classify algorithms by how they respond to changes in input size, such as how the processing time of an algorithm changes as the problem size becomes extremely large.

When we talk about an algorithm's complexity, we want to describe at what rate the algorithm grows when we change the input size. The goal of optimizing is to reduce that response and improve its performance.

The notation looks like this: `O(N)`, `O(1)`. (That's only two examples.)


Time Complexity
----

#### Linear — `O(N)`

Look at this example of `is_palindrome` from [Problem1's tests](https://github.com/reeddunkle/Codjo/blob/master/Problem1_Richie_Rich/richie_rich_test.py):

```python
def is_palindrome(text):
    for i in range(len(text)//2):
        if text[i] != text[-1-i]:
            return False

    return True
```

During the code review I went over how much time the function requires, and I used the terms "time complexity", and "runtime". These describe the same thing.

To measure its time complexity, we talked about it responds to inputs of different sizes.

If the input is `"1234554321"`, it's length is 10: `len(text) == 10`.

If it goes the whole way through the for-loop, it will assign to `i` the numbers `0, 1, 2, 3, 4`

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

This runtime has a **linear** growth rate. The "Big O" notation for linear is `O(N)`.

#### Quadratic — `O(N²)`

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

#### Drop The Constants

This is counter-intuitive, so pay attention to this part.

Consider this example:

```python
def print_twice(numbers):
    for num in numbers:
        print(num)

    for num in numbers:
        print(num)
```

There are two for-loops that each loop n-times, and so it would seem to follow that its time complexity would be `O(2N)`. It isn't. It's just `O(N)`.

And in the first example of `is_palindrome`:

```python
def is_palindrome(text):
    for i in range(len(text)//2):
        if text[i] != text[-1-i]:
            return False

    return True
```

You'd think that its complexity is `O(N/2)`. Again, though, it's `O(N)`.

This is hard to get used to.

Big O only describes the rate of increase. It expresses how the algorithm scales, how fast the complexity grows with its input. In these examples, the runtime grows at a linear rate.

It's definitely possible for `O(N²)` to run faster than `O(N)` code. You want to use big O to think about how the performance is going to change with big (really big) inputs. There will be a point where _N²_ might be as good as, say, _100N_, but at some point when the input size changes enough, it will start to be worse.

We just need to accept that it doesn't mean that `O(N)` is always better than `O(N²)`.

In absolute efficiency terms, _N/2_ iterations is preferable to _2N_, and the former should definitely be used over the latter. But in relative terms, they grow at more or less the same speed, which means that they are both preferable (at some point) over _N²_.

The main takeaway from this is to drop the constants when you're talking to an interviewer. Best case, you'll sound like an amateur. Worst case, the interviewer will treat this as a "gotcha".

#### Constant — `O(1)`

A **constant** growth rate means that, no matter how the input changes, your function's performance remains contant. It means that its performance doesn't depend on the input size.

Here's a short, pointless example using the same input as above, `[0, 4, 6, 3, 2, 7, 5, 1, 8, 8]`:

```python
def print_first_five(numbers):
    for i in range(5):
        print(numbers[i])
```

It wouldn't matter if the input size were 200 instead of 10. It's just going to print the first five numbers in the list. This function's complexity responds to changes in input size at a constant rate, `O(1)`.

#### Logarthmic — `O(log(N))`

This is the benchmark for searching through a sorted input.

If you need to search for an element, you can use binary search to search through a sorted input in **logarithmic** time, `O(log(N))`. We covered this in [Problem2](https://github.com/reeddunkle/Codjo/tree/master/Problem2_Sorted_Search).

It's the same for searching in a binary search tree.

#### "Linearithmic" — `O(N log(N))`

We'll go over sorting algorithms in the near future, but you should be aware that my earlier example of [Bubble Sort is notoriously bad](https://youtu.be/k4RRi_ntQc8) (`O(N²)`).

Better algorithms like quick sort and merge sort achieve `O(N log(N))`. [Some people](https://en.wikipedia.org/wiki/Time_complexity#Linearithmic_time) call `O(N log(N))` "linearithmic" as shorthand. Personally, I just say "N log N".

#### Exponential — `O(2ⁿ)`

An example of this is a recursive Fibonacci function:

```python
def fib(n):
    '''Returns the first n Fibonacci numbers.'''
    if n <= 1:
        return n

    return fib(n - 2) + fib(n - 1)
```

Its growth doubles for every 1 of the input.


#### I didn't mention...

`O(N³)` or `O(N⁴)`

For now, just be aware that they exist.

#### Best Case, Worst Case, and Expected Case

Back to the example of `is_palindrome`:

```python
def is_palindrome(text):
    for i in range(len(text)//2):
        if text[i] != text[-1-i]:
            return False

    return True
```

You might point out that this function could exit the loop midway with its `return False` statement, and you're right. It could even exit with the first calculation and achieve `O(1)`.

We can describe complexity in three different ways:
- **best case**
- **worst case**
- **expected case**.

Usually, people don't talk about best case time complexity. It isn't that useful.

As for distinguishing between expected and worst case, I haven't found a satisfying explanation yet.

This is Gayle Laakmann McDowell's explanation in _Cracking the Coding Interview_:
> For many—probably most—algorithms, the worst case and the expected case are the same. Sometimes they're different, though, and we need to describe both of the runtimes.

Just before she says this, she explains the best, worst, and expected runtimes for quick sort (`O(N)`, `O(N²)`, and `O(N log(N))` respectively). Usually, people describe quick sort's big O as `O(N log(N))`, which is its expected time.

On the other hand, with `is_palindrome`, no one would think to calculate its expected case by averaging the best and the worst. They would just say that the expected is the same as the worst.

For now, forgive this less-than-perfect explanation.


Space Complexity
----

Space complexity is talked about the same way as time complexity.

Your function's space complexity refers to how your algorithm's space requirements change as you change the input size.

I'll go through some simple examples. For all of them, let's assume the input is `[0, 4, 6, 3, 2, 7, 5, 1, 8, 8]`.

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

The first function creates a new list and adds the first five numbers from the input. No matter how large `numbers` is, the function only requires a constant 5-length list to be held in memory.

`bubble_sort` on the other hand requires no additional memory. It destroys the original input by mutating it in place (which is often criticized), but in return it doesn't take up any additional space.

**`O(N)`**

```python
def linear_space(numbers)
    new_list = []
    for i in range(n):
        new_list.append(numbers[i])

    return new_list
```

This `linear_space` function requires an _n_-length list to be held in memory, as it's simply copying the current input. The larger the input, the larger `new_list` will swell.


Time vs. Space
----

It's common to find time and space competing with one another. People in every field talk about "design trade-offs". In CS, there tends to be a trade-off between time and space. You definitely want to minimize both, but at some level you'll probably find yourself facing design trade-offs.

An example where you face a trade-off is with caching. In order to speed up retrieving information,  a cache stores some information that you've already spent time calculating. This way, if the same information is requested (if you have the same input) you can skip running the calculations and just grab the answer you have stored. Given the same input, it spares you the runtime. The trade off is that you're using extra space to decrease your runtime.

At one end of the spectrum, you could imagine a cache that holds the result of every calculation your function might perform. Its space complexity would be infinite, but its time complexity given this idealistic cache would be constant.

On the other end of the spectrum, imagine that there is no cache, and so your function has to run its calculations every time. You don't incur any extra space, but you have to run a calculation with every input.
