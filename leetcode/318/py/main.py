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

ScheduleItem = collections.namedtuple("ScheduleItem", ["prod", "len1", "len2"]) 

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        len_to_words = collections.defaultdict(list)
        # convert all words to bitstrings for faster comparison
        word_to_bitstring = {}
        for w in words:
            s = set(w)
            bitstring = 0
            for c in s:
                bitstring = bitstring | (1 << ord(c) - ord('a'))
            word_to_bitstring[w] = bitstring

        # Schedule comparisons in order of decreasing product of length
        # so as to enable short circult.
        for w in words:
            len_to_words[len(w)].append(w)
        lens = len_to_words.keys()
        schedule_set = set()
        # Each schedule item has the form (prod, len1, len2)
        for len1 in lens:
            for len2 in lens:
                if len1 >= len2:
                    schedule_set.add(ScheduleItem(
                        prod=len1 * len2,
                        len1=len1,
                        len2=len2))
        sorted_schedule = []
        for x in schedule_set:
            sorted_schedule.append(x)
        sorted_schedule.sort(key = lambda x : x.prod, reverse=True)

        # compare words along schedule
        for s in sorted_schedule:
            # if len1 == len2, we can skip some of the comparisons
            if s.len1 == s.len2:
                wl = len_to_words[s.len1]
                for i1, w1 in enumerate(wl):
                    for w2 in wl[(i1+1):]:
                        if not word_to_bitstring[w1] & word_to_bitstring[w2]:
                            return(s.prod)
            else:
                wl1 = len_to_words[s.len1]
                wl2 = len_to_words[s.len2]
                for w1 in wl1:
                    for w2 in wl2:
                        if not word_to_bitstring[w1] & word_to_bitstring[w2]:
                            return(s.prod)
        return 0


