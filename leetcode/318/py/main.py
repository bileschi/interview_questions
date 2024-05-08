# Given a string array words, return the maximum value of length(word[i]) *
# length(word[j]) where the two words do not share common letters. If no such
# two words exist, return 0.

 

# Example 1:
# Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16
# Explanation: The two words can be "abcw", "xtfn".

# Example 2:
# Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
# Output: 4
# Explanation: The two words can be "ab", "cd".

# Example 3:
# Input: words = ["a","aa","aaa","aaaa"]
# Output: 0
# Explanation: No such pair of words.
 

# Constraints:

# 2 <= words.length <= 1000
# 1 <= words[i].length <= 1000
# words[i] consists only of lowercase English letters.
import collections

class Solution(object):
    def share_letter(self, w1, w2, word_to_bitstring):
        bs1 = word_to_bitstring[w1]
        bs2 = word_to_bitstring[w2]
        return bs1 & bs2 > 0

    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        len_to_words = collections.defaultdict(list)
        word_to_bitstring = {}
        for w in words:
            s = set(w)
            bitstring = 0
            for c in s:
                bitstring = bitstring | (1 << ord(c) - ord('a'))
            word_to_bitstring[w] = bitstring
        for w in words:
            len_to_words[len(w)].append(w)
        
        lens = len_to_words.keys()
        schedule_set = set()
        for len1 in lens:
            for len2 in lens:
                schedule_set.add((len1 * len2, len1, len2))
        sorted_schedule = []
        for x in schedule_set:
            sorted_schedule.append(x)
        sorted_schedule.sort(key = lambda x : -x[0])

        for s in sorted_schedule:
            wl1 = len_to_words[s[1]]
            wl2 = len_to_words[s[2]]
            prod_len = s[0]
            for w1 in wl1:
                for w2 in wl2:
                    if not self.share_letter(w1, w2, word_to_bitstring):
                        return(prod_len)
        return 0
            

