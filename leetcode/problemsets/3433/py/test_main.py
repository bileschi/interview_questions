# Tests for leetcode problem 3433

import main
import unittest

class TestMain(unittest.TestCase):
    def test_case_1(self):
        s = main.Solution()
        numberOfUsers = 2
        events = [["MESSAGE","10","id1 id0"],
                  ["OFFLINE","11","0"],
                  ["MESSAGE","71","HERE"]]
        count_msgs = s.countMentions(numberOfUsers, events)
        self.assertEqual(count_msgs, [2, 2])

    def test_case_2(self):
        s = main.Solution()
        numberOfUsers = 2
        events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","12","ALL"]]
        count_msgs = s.countMentions(numberOfUsers, events)
        self.assertEqual(count_msgs, [2, 2])

    def test_case_3(self):
        s = main.Solution()
        numberOfUsers = 2
        events = [["OFFLINE","10","0"],["MESSAGE","12","HERE"]]
        count_msgs = s.countMentions(numberOfUsers, events)
        self.assertEqual(count_msgs, [0, 1])

if __name__ == '__main__':
    unittest.main()
