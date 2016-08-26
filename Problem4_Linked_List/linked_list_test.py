import unittest

from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.list = LinkedList()


    def tearDown(self):
        self.list = None


    def test_append(self):
        self.list.append("Mr. Green")

        self.assertTrue(self.list.head.data == "Mr. Green")
        self.assertTrue(self.list.head.next_node is None)


    def test_append_two(self):
        self.list.append("Mr. Green")
        self.list.append("Miss Scarlet")

        self.assertTrue(self.list.head.data == "Miss Scarlet")

        new_head = self.list.head.next_node
        self.assertTrue(new_head.data == "Mr. Green")


    def test_next_node(self):
        self.list.append("Prof. Plum")
        self.list.append("Mrs. Peacock")
        self.list.append("Mr. Boddy")

        self.assertTrue(self.list.head.data == "Mr. Boddy")

        new_head = self.list.head.next_node
        self.assertTrue(new_head.data == "Mrs. Peacock")

        last = new_head.next_node
        self.assertTrue(last.data == "Prof. Plum")


    def test_len(self):
        self.list.append("Prof. Plum")
        self.list.append("Mrs. Peacock")
        self.list.append("Mr. Boddy")

        length = self.list.__len__()

        self.assertTrue(length == 3)


    def test_len_zero(self):
        length = self.list.__len__()

        self.assertTrue(length == 0)


    def test_len_one(self):
        self.list.append("Prof. Plum")
        length = self.list.__len__()

        self.assertTrue(length == 1)


    def test_succeed_getitem(self):
        self.list.append("Prof. Plum")
        self.list.append("Mrs. Peacock")
        self.list.append("Mr. Boddy")

        result = self.list.__getitem__(0)
        self.assertTrue(result == "Mr. Boddy")

        result = self.list.__getitem__(1)
        self.assertTrue(result == "Mrs. Peacock")

        result = self.list.__getitem__(2)
        self.assertTrue(result == "Prof. Plum")


    def test_fail_getitem(self):
        self.list.append("Prof. Plum")
        self.list.append("Mrs. Peacock")

        with self.assertRaises(IndexError):
            self.list.__getitem__(2)


    @unittest.skip('Extra Challenge: pop method.')
    def test_pop(self):
        self.list.append("Prof. Plum")
        self.list.append("Mrs. Peacock")
        self.list.append("Mr. Boddy")

        old_head = self.list.pop()
        self.assertTrue(old_head.data == "Mr. Boddy")

        new_head = self.list.head
        self.assertTrue(new_head.data == "Mrs. Peacock")

        new_length = len(self.list)
        self.assertTrue(new_length == 2)


    @unittest.skip('Extra Challenge: pop method.')
    def test_pop_empty_list(self):
        with self.assertRaises(IndexError):
            self.list.pop()


    @unittest.skip('Extra Challenge: __delitem__ method.')
    def test_delete(self):
        self.list.append("Prof. Plum")
        self.list.append("Mrs. Peacock")
        self.list.append("Mr. Boddy")

        # Delete the list head
        self.list.__delitem__(0)
        self.assertTrue(self.list.head.data == "Mrs. Peacock")

        # Delete the list tail
        self.list.__delitem__(1)
        self.assertTrue(self.list.head.next_node is None)

        new_length = len(self.list)
        self.assertTrue(new_length == 1)


    @unittest.skip('Extra Challenge: __delitem__ method.')
    def test_delete_value_not_in_list(self):
        self.list.append("Prof. Plum")
        self.list.append("Mrs. Peacock")
        self.list.append("Mr. Boddy")

        with self.assertRaises(IndexError):
            self.list.__delitem__(3)


    @unittest.skip('Extra Challenge: __delitem__ method.')
    def test_delete_empty_list(self):
        with self.assertRaises(IndexError):
            self.list.__delitem__(1)


    @unittest.skip('Extra Challenge: __delitem__ method.')
    def test_delete_next_reassignment(self):
        self.list.append("Prof. Plum")
        self.list.append("Mrs. White")
        self.list.append("Mrs. Peacock")
        self.list.append("Mr. Boddy")

        self.list.__delitem__(1)
        self.list.__delitem__(1)

        self.assertTrue(self.list.head.next_node.data == "Prof. Plum")


if __name__ == '__main__':
    unittest.main()
