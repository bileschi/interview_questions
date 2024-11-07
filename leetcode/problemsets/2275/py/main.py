# Solution to leetcode problem 2275
#
# Largest bitwise and
# Given a set of integers, find the largest cardinality of a subset of integers
# such that the bitwise and of all integers in the subset is non-zero.
#
# Look at the bitwise representation of the integers.  For each position
# count how many integers have a 1 in that position.  Return the highest count.

from typing import List

class Solution(object):
 
    def largestCombination(self, candidates: List[int]) -> int:
        # Count the number of 1's in each bit position
        # only need 24 bits - max integer is 10^7 < 2^24
        bitCounts = [0] * 24
        for candidate in candidates:
            for i in range(32):
                if (candidate & (1 << i)) > 0:
                    bitCounts[i] += 1
        # Return the highest count
        return max(bitCounts)


