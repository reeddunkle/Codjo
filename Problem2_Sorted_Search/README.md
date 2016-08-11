# Sorted Search

Description
----

This challenge is different than most coding challenges. In order to expand the sorts of challenges we do, I want to make sure that we cover some algorithms you'll be expected to know about and be able to code in order to solve other problems in the future, such as in an interview.

Here's the problem:

>**Given a sorted list of positive integers, and an element x, return the index number of that element in the list. If element is not present, return `-1`.**

We have to search a lot in coding. This week's problem covers one of the staple searching algorithms. I'm not going to reveal the name of the algorithm for now, because it is so common that Google will have coding solutions as well as explanations.

Instead, I want you to think about the problem. Think hard about it, and see if you can come up with some ideas on how to increase performance.

Unfortunately, the tests I've written don't test your function's performance. You could return an element's index by simply looping over the entire list until you find it. You could use Python's built-in `index()` method.

I've provided tests to help you get started. But the real challenge, rather than passing the tests, is to come up with the best way to pass the tests.

There aren't that many ways to go about this problem. If you're banging your head against the wall, go ahead and Google for searching algorithms. Try not to peek at any code solutions, though. Just read what you're supposed to do, and spend the time figuring out how to code it.


Input Format
----

You are given an element x, and a list named `listy`, which contains **sorted, positive integers**. Find the index at which an element x occurs in `listy`. If x occurs multiple times, you may return any of those indices.


Output Format
----

Return a single integer that represents the index at which the input element x occurs in the input `listy`. If element x is not in `listy`, return `-1`.

Explicit Goals
----

During the code review for [Problem1](https://github.com/reeddunkle/Codjo/tree/master/Problem1_Richie_Rich) we talked about optimizing for time and space. In the References directory I wrote an [explaination](https://github.com/reeddunkle/Codjo/blob/master/References/Optimizing.md) of these concepts (5-min read), and included are terms which I'll use for this problem like "linear time". The first goal is to read that.

This is first an exercise in problem solving. Finding an element in a list in linear time is pretty straight forward. You loop through the list until you find it. This isn't a bad place to start, though. This is goal number 2.

In this problem I challenge you to learn a better way. That's goal number 3, and the main goal of this problem. I'll publish some hints in the upcoming days if you can't think of how you could do this.


1. Read this 5-min read on [Optimization](https://github.com/reeddunkle/Codjo/blob/master/References/Optimizing.md)
2. Find the index in `listy` at which element x occurs
3. **Look for a way to do this in less than linear time: `O(n)`**
4. Write well-named functions and variables
5. (Don't use the `index` method)


Extra Goals
----

Imagine that `listy` is not a normal list structure, but a modified structure that has no `__len__` method. By this I mean that you can't call `len()` on `listy`. Instead, `listy` has a method called `element_at(i)` method, which returns the element at index `i` in `O(1)` time. If `i` is beyond the bounds of the data structure, it returns `-1`. (For this reason, `listy` only supports positive integers.) Can you use `element_at(i)` to complete the challenge above while still keeping the run-time below `O(n)`?

Local Testing
----

Download the test script (or copy and paste), and run it with the python interpreter.

**Note:** I don't have a way of testing your run-time. We'll discuss it in code-review.


----

Taken from _Cracking the Coding Interview, 6th Edition_ p.150
