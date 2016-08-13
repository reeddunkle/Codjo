import unittest

from sorted_search import find


class NoLengthMethod(Exception):
    pass


class Listy(list):

    def __len__(self):
        raise NoLengthMethod('No __len__ method found.')

    def element_at(self, i):
        try:
            return self.__getitem__(i)
        except IndexError:
            return -1


class SortedSearchTests(unittest.TestCase):

    def test_finds_index1(self):
        listy = [2, 4, 7, 22, 23, 55, 65, 102, 10002]
        x = 65
        self.assertEqual(6, find(x, listy))


    def test_finds_index2(self):
        listy = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1376]
        x = 1376
        self.assertEqual(12, find(x, listy))


    def test_finds_index3(self):
        listy = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1376]
        x = 4
        self.assertEqual(0, find(x, listy))


    def test_not_found(self):
        listy = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1376]
        x = 16
        self.assertEqual(-1, find(x, listy))


    def test_empty_listy(self):
        listy = []
        x = 42
        self.assertEqual(-1, find(x, listy))


    def test_large_listy(self):
        listy = range(1000000)
        x = 999999
        self.assertEqual(999999, find(x, listy))


    # @unittest.skip('Extra Credit: No __len__ method.')
    def test_no_length_method(self):
        listy = Listy(list(range(200)))
        x = 100
        self.assertEqual(100, find(x, listy))


if __name__ == '__main__':
    unittest.main()