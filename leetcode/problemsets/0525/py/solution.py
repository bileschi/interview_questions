"""
Given a binary array nums, return the maximum length of a contiguous subarray
with an equal number of 0 and 1.


Example 1:

Input: nums = [0,1] Output: 2 Explanation: [0, 1] is the longest contiguous
subarray with an equal number of 0 and 1. Example 2:

Input: nums = [0,1,0] Output: 2 Explanation: [0, 1] (or [1, 0]) is a longest
contiguous subarray with equal number of 0 and 1.
 

Constraints:

1 <= nums.length <= 1e5 
nums[i] is either 0 or 1.
"""
# import numpy as np

class Solution(object):

    def findMaxLength(self, nums):
        # return(self.simple_brute_force_findMaxLength(nums))
        # return(self.complex_efficient_findMaxLength(nums))
        return(self.simpler_efficient_findMaxLength(nums))

    def simpler_efficient_findMaxLength(self, nums):
        """
        Carry the cumulative sum, counting the number of '1's between
        position 0 and i, minus the number of '0's between position 0 and i, but
        there is no need to store the whole thing simultaneously.  

        For each position, we record the first time we see that cumulative
        sum (including 0 at position -1).  If we see that cumulative sum again,
        we know that the number of '1's and '0's between the two positions is
        the same.  We can then compare the size of the span to the largest span
        seen so far.

        :type nums: List[int]
        :rtype: int
        """
        max_span_len = 0
        cum_sum = 0
        first_seen_dict = {0: -1}
        for i, v in enumerate(nums):
            if v == 1:
                cum_sum += 1
            else:
                cum_sum -= 1
            if cum_sum not in first_seen_dict:
                first_seen_dict[cum_sum] = i
            else:
                span_len = i - first_seen_dict[cum_sum]
                if span_len > max_span_len:
                    max_span_len = span_len
        return(max_span_len)


    def complex_efficient_findMaxLength(self, nums_as_list):
        """
        First create a cumulative sum, counting the number of '1's between
        position 0 and i, minus the number of '0's between position 0 and i.

        Then, for each position, we store the first time we see that cumulative
        sum. If we see it again, we know that the number of '1's and '0's
        between the two positions is the same.

        :type nums: List[int]
        :rtype: int
        """
        nums = np.array(nums_as_list)
        cumsum_diff = np.cumsum(nums == 1) - np.cumsum(nums == 0)
        # initialize diff of 0 at position -1.
        first_of_this_diff = {0: -1}
        last_of_this_diff = {0: -1}
        for i in range(0, len(cumsum_diff)):
            last_of_this_diff[cumsum_diff[i]] = i
            if cumsum_diff[i] not in first_of_this_diff:
                first_of_this_diff[cumsum_diff[i]] = i
        max_len = 0
        for diff in first_of_this_diff.keys():
            if diff in last_of_this_diff:
                if last_of_this_diff[diff] - first_of_this_diff[diff] > max_len:
                    max_len = last_of_this_diff[diff] - first_of_this_diff[diff]
        # print('first_of_this_diff', first_of_this_diff)
        # print('last_of_this_diff', last_of_this_diff)
        return(max_len)

    def simple_brute_force_findMaxLength(self, nums_as_list):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = np.array(nums_as_list)
        max_len = 0 # if all zeros or all ones
        # left point is 'a', inclusive
        # right point is 'b', inclusive
        for a in range(0, len(nums)):
            for b in range(0, len(nums)):
                this_len = b - a + 1
                if (b <= a):
                    continue
                num_zeros = sum(nums[a:(b+1)] == 0)
                num_ones = sum(nums[a:(b+1)] == 1)
                if num_zeros == num_ones:
                    if this_len > max_len:
                        max_len = this_len                    
        return max_len
    

if __name__ == '__main__':
    import numpy as np
    sol = Solution()
    num_tests = 100
    each_test_len = 1e5
    for _ in range(num_tests):
        sol.findMaxLength(list(np.random.randint(int(2), size=(int(each_test_len),))))