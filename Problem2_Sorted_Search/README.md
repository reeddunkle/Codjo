# Sorted Search

Description
----

Searching is something we have to do a lot. How can we do it efficiently?


Input Format
----

You are given an element x, and a list named `listy`, which contains **sorted, positive integers**. Find the index at which an element x occurs in `listy`. If x occurs multiple times, you may return any of those indices.


Output Format
----

Return a single integer that represents the index at which the input element x occurs in the input `listy`. If element x is not in `listy`, return `-1`.

Explicit Goals
----

This is first an exercise in problem solving. Finding an element in a list in linear time is pretty straight forward. You go through the list until you find it, right?

The challenge is to learn a better way. I'll publish some hints in the upcoming days if you can't think of how you could do this.

During the code review for [Problem1](https://github.com/reeddunkle/Codjo/tree/master/Problem1_Richie_Rich) we talked about optimizing for time and space. In the [references](https://github.com/reeddunkle/Codjo/tree/master/References) directory, I've published an article explaining these concepts, and some of the terms I'll use for this problem, like "linear run-time".

1. Find the index in `listy` at which element x occurs
2. Look for a way to do this in less than N (linear) run-time (`O(n)`)
3. Write well-named functions and variables
4. (Don't use the `index` method)

Extra Goals
----

Imagine that `listy` is not a normal list structure, but a modified structure that has no `__len__` method. By this I mean that you can't call `len()` on `listy`. Instead, `listy` has a method called `element_at(i)` method, which returns the element at index `i` in `O(1)` time. If `i` is beyond the bounds of the data structure, it returns `-1`. (For this reason, `listy` only supports positive integers.) Can you use `element_at(i)` to complete the challenge above while still keeping the run-time below `O(n)`?

Local Testing
----

Download the test script (or copy and paste), and run it with the python interpreter.

**Note:** I don't have a way of testing your run-time. We'll discuss it in code-review.


----

Taken from _Cracking the Coding Interview, 6th Edition_ p.150
