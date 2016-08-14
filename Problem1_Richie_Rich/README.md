Description
----

Sandy likes palindromes. A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as it does forward. For example, "madam" is a palindrome.

On her 7th birthday, Sandy's uncle, Richie Rich, offered her an n-digit check which she refused because the number was not a palindrome. Richie then challenged Sandy to make the number palindromic by changing no more than k digits. Sandy can only change 1 digit at a time, and cannot add digits to (or remove digits from) the number.

Given k and an n-digit number, help Sandy determine a palindrome number she can make by changing <= k digits.

Input Format
----

- The string of numbers that Sandy must attempt to make palindromic
- `k`, the maximum number of digits that can be altered

Treat the integers as numeric strings. Leading zeros are permitted and can't be ignored (So 0011 is not a palindrome, 0110 is a valid palindrome). A digit can be modified more than once. Each character in the number is a positive integer.


Output Format
----

Return a single palindrome number that can be made by changing no more than k digits; if this is not possible, return `-1`.


Explicit Challenge
----

- Make the number a palindrome by changing no more than k digits
- Write clean code
- Optimize your code

Extra Challenge
----

- How could you maximize the output number?
- Given only 1 change (`k = 1`), change `'3943'` to `'3993'` rather than `'3443'`
- Given 3 changes (`k = 3`), change `'3943'` to `'9999'`.


Local Testing
----

Download the test script (or copy and paste), and run it with the python interpreter. Your module must be named `richie_rich.py`, your function named `make_palindrome`, and the test script in the same directory as your solution (`richie_rich.py`).

Example:

```
python richie_rich_test.py
......ss
----------------------------------------------------------------------
Ran 8 tests in 0.000s

OK (skipped=2)
```


Notes
----

This problem may be too easy for the 72 hours given. The "Extra Goal" of maximizing the output is quite difficult though. I hope that the challenge will hold your interest, and facilitate good pairing discussion.


----

Taken from [this](https://www.hackerrank.com/challenges/richie-rich) Hacker Rank problem
