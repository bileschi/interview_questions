import main
import unittest

class TestMain(unittest.TestCase):

    def test_edge_cases(self):
        s = main.Solution()
        zero = main.ListNode(0)
        self.assert_ll_equal(s.mergeTwoLists(None, None), None)
        self.assert_ll_equal(s.mergeTwoLists(None, zero), zero)
        self.assert_ll_equal(s.mergeTwoLists(zero, None), zero)

    def test_base(self):
        s = main.Solution()
        l1 = self.make_ll([1])
        l2 = self.make_ll([2])
        expected = self.make_ll([1, 2])
        self.assert_ll_equal(s.mergeTwoLists(l1, l2), expected)


    def test_with_dups(self):
        s = main.Solution()
        l1 = self.make_ll([1, 2, 4])
        l2 = self.make_ll([1, 3, 4])
        expected = self.make_ll([1, 1, 2, 3, 4, 4])
        self.assert_ll_equal(s.mergeTwoLists(l1, l2), expected)

    def make_ll(self, l):
        if len(l) == 0:
            return None
        head = main.ListNode(l[0])
        ptr = head
        for i in range(1, len(l)):
            ptr.next = main.ListNode(l[i])
            ptr = ptr.next
        return head

    def assert_ll_equal(self, l1, l2):
        while l1 is not None and l2 is not None:
            self.assertEqual(l1.val, l2.val)
            l1 = l1.next
            l2 = l2.next
        self.assertEqual(l1, l2)

if __name__ == '__main__':
    unittest.main()