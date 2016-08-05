# Max Output

A solution to **maximize the numeric output** of making a numeric-string palindromic in a
limited number of moves.

Solution 1
----

The first solution `richie_rich_max1.py` is a greedy attempt to maximize the output: When making the number palindromic, always use the larger of the two numbers.

It seems like this could work. With this input:

```
k = 1
n = '3943'
max_output = '3993'
```

It will arrive at `9` and `4`, and turn `4` into `9`, thus maximizing the output.

Here's a test where this strategy won't work:

```
k = 3
n = '092282'

# Expected result:
# max_output = '992299'
# k = 0
```

The first difference is `0` and `2`, it will take the larger and change `0` to `2`. This is where things stand at that point:

```
k = 2
n = '292282'
```

The next difference it finds is `9` and `8`, following suit:

```
k = 1
n = '292292'
```

Now it's a palindrome. But it isn't maximized.

#### Hints

You have 1 move left over. That's not against the rules, but it does tell you important information. How does that let you maximize the output?

What if you have two moves left over at the end? How does that let you maximize the output?

Another example:

```
k = 4
n = '11119111'

# Expected result:
# max_output = '91199119'
# k = 1
```

Solution 2
----

See `richie_rich_max_complete.py` for the code.
