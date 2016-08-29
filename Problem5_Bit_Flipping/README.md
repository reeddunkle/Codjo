# Flipping Bits

Hi everyone! I'm interviewing this week, and quite occupied, so for now I'm going to give y'all a pretty lousy write up. I'm sorry about this.

Problem
----

You're given a list of positive integers. Convert each number in turn to a 32-bit, unsigned binary numbers, flip the bits, and print the new decimal number.

I'll give you an example, but I'm going to ask you to do more research on your own this week.

**Example 1:**

Input:
`1`

As an unsigned, 32-bit binary, this is:
`00000000000000000000000000000001`

You flip its bits:
`11111111111111111111111111111110`

Which in decimal is:
`4294967294`

----

Read [this article](https://wiki.python.org/moin/BitwiseOperators) and beware of unsigned vs. signed! (Read other articles too.)

Tests?

We've taken this week's problem from [THIS](https://www.hackerrank.com/challenges/flipping-bits) Hacker Rank problem. For now you can run tests on their interface.

Note:
At Hacker Rank, you need to read in their inputs and print their answers. Each time you call `input()` (or `raw_input()` in Python2), you'll read in one line of their input.

This is their sample input:

```
3
2147483647
1
0
```

So you can do something like this...

```python
number_of_entries = input()
```

...to get `3`, and then call `input()` that many times to fetch the remaining lines.

Good luck!