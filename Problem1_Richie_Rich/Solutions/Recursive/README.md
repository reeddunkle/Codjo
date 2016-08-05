# Recursive

A recursive solution to make a numeric-string palindromic in a
limited number of moves.

I used a helper method `_make_palindrome` to perform the recursion for two reasons:

1. I needed to make the string into a list. This let me do the conversion in the original function, and pass it to the recursive function. I'm not positive how I would have done it this in just the original function, but it would have involved some ugly techniques, the two that come to mind are global variables, or converting the string to a list with each call.

2. I needed to track the pointer.

I could have included (2) in the original function with less fuss than (1) would have required, but this extra function lets me contain the messy variable tracking in the helper function, and keep my main function tidy. (This was one of the first techniques @leo taught me at RC.)
