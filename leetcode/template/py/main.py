# Solution to leetcode problem DIGIT_GOES_HERE

class Solution(object):
 
    def countGen(self, gen):
        count = 0
        for dummy in gen:
            count += 1
        return(count)
    

    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        s = sorted(heights)
        g = ( (x,y) for (x,y) in zip(heights, s) if x != y)
        return(self.countGen( g ))
    