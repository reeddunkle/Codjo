**Description:**

Sandy likes palindromes. A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as it does forward. For example, **madam** is a palindrome.

On her 7th birthday, Sandy's uncle, Richie Rich, offered her an n-digit check which she refused because the number was not a palindrome. Richie then challenged Sandy to make the number palindromic by changing no more than  digits. Sandy can only change 1 digit at a time, and cannot add digits to (or remove digits from) the number.

Given k and an n-digit number, help Sandy determine a palindrome number she can make by changing <= k digits.

**Notes:**
- Treat the integers as numeric strings. Leading zeros are permitted and can't be ignored (So 0011 is not a palindrome, 0110 is a valid palindrome). A digit can be modified more than once.
- Each character i in the number is a positive integer

**Input Format**

The first line contains two space-separated integers, `n` (the number of digits in the number) and `k` (the maximum number of digits that can be altered), respectively.
The second line contains an n-digit string of numbers that Sandy must attempt to make palindromic.


**Output Format**

Return a sigle palindrome number that can be made by changing no more than k digits; if this is not possible, return `-1`.


**Explicit Goals:**
- Make the number a palindrome by changing no more than k digits
- Write clean code
- Optimize your code

**Optional Goals:**
- How could you maximize the output number?
