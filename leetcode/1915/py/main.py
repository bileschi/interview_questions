# 1915. Number of Wonderful Substrings

# A wonderful
# string is a string where at most one letter appears an odd number of times.

# For example, "ccjjc" and "abab" are wonderful, but "ab" is not.

# Given a string word that consists of the first ten lowercase English letters
# ('a' through 'j'), return the number of wonderful non-empty substrings in
# word. If the same substring appears multiple times in word, then count each
# occurrence separately.

# A substring is a contiguous sequence of characters in a string.

 

# Example 1:

# Input: word = "aba"
# Output: 4
# Explanation: The four wonderful substrings are underlined below:
# - "aba" -> "a"
# - "aba" -> "b"
# - "aba" -> "a"
# - "aba" -> "aba"
# Example 2:

# Input: word = "aabb"
# Output: 9
# Explanation: The nine wonderful substrings are underlined below:
# - "aabb" -> "a"
# - "aabb" -> "aa"
# - "aabb" -> "aab"
# - "aabb" -> "aabb"
# - "aabb" -> "a"
# - "aabb" -> "abb"
# - "aabb" -> "b"
# - "aabb" -> "bb"
# - "aabb" -> "b"
# Example 3:

# Input: word = "he"
# Output: 2
# Explanation: The two wonderful substrings are underlined below:
# - "he" -> "h"
# - "he" -> "e"
 

# Constraints:

# 1 <= word.length <= 105
# word consists of lowercase English letters from 'a' to 'j'.

import collections
import numpy as np

class Solution(object):
    def isWonderful(self,word):
        c = collections.Counter()
        c.update(word)
        num_odd = 0
        for (k,v) in c.items():
            if v % 2:
                num_odd += 1
            if num_odd > 1:
                return False
        return True

    def wonderfulSubstrings(self, word):
        return self.wonderfulSlidingWindow(word)

    def wonderfulSlidingWindow(self, word):
        """
        :type word: str
        :rtype: int
        """
        # sliding window approach.
        C = np.zeros((10, len(word)), int)
        for (i, c) in enumerate(word):
            c_idx = ord(c) - ord('a')
            C[c_idx, i] = 1
        CS = np.concatenate((np.zeros((10, 1)), np.cumsum(C, 1)), 1)
        num = 0
        # i and j here are end inclusive.
        for i in range(len(word)):
            for j in range(i+1, len(word)+1):
                if sum((CS[:, j] - CS[:, i]) % 2) <= 1:
                    num += 1
                else:
                    pass

        return num


    def wonderfulBrute(self, word):
        """
        :type word: str
        :rtype: int
        """
        num = 0
        for i in range(len(word)):
            for j in range(len(word) +1):
                #print(word[i:j])
                if word[i:j]:
                    if self.isWonderful(word[i:j]):
                        #print(f"*   {word[i:j]}")
                        num += 1
        return num
