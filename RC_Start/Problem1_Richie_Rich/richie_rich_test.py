import unittest

from richie_rich import make_palindrome


def is_palindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[-1-i]:
            return False
    else:
        return True


class PalindromeTests(unittest.TestCase):

    def test_make_palindrome_shift_one(self):
        actual = make_palindrome('3943', 1)

        self.assertTrue(actual != -1)
        self.assertTrue(is_palindrome(actual))


    def test_make_palindrome_shift_three(self):
        actual = make_palindrome('092282', 3)

        self.assertTrue(actual != -1)
        self.assertTrue(is_palindrome(actual))


    def test_make_palindrome_four(self):
        actual = make_palindrome('11119111', 4)

        self.assertTrue(actual != -1)
        self.assertTrue(is_palindrome(actual))


    def test_make_palindrome_eight(self):
        actual = make_palindrome('128392759430124', 8)

        self.assertTrue(actual != -1)
        self.assertTrue(is_palindrome(actual))


    def test_make_palindrome_fails_one(self):
        actual = make_palindrome('0011', 1)

        self.assertEqual(actual, -1)


    def test_make_palindrome_fails_two(self):
        actual = make_palindrome('123456789123456789', 1)

        self.assertEqual(actual, -1)


    @unittest.skip('Extra Credit: Maximizes the numeric output.')
    def test_maximizes_output_one(self):
        actual = make_palindrome('092282', 3)

        self.assertEqual(actual, '992299')


    @unittest.skip('Extra Credit: Maximizes the numeric output.')
    def test_maximizes_output_two(self):
        actual = make_palindrome('11119111', 4)

        self.assertEqual(actual, '91199119')


if __name__ == '__main__':
    unittest.main()
