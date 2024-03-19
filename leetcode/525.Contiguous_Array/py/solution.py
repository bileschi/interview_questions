"""
Given a binary array nums, return the maximum length of a contiguous subarray
with an equal number of 0 and 1.


Example 1:

Input: nums = [0,1] Output: 2 Explanation: [0, 1] is the longest contiguous
subarray with an equal number of 0 and 1. Example 2:

Input: nums = [0,1,0] Output: 2 Explanation: [0, 1] (or [1, 0]) is a longest
contiguous subarray with equal number of 0 and 1.
 

Constraints:

1 <= nums.length <= 105 nums[i] is either 0 or 1.Given a binary array nums,
return the maximum length of a contiguous subarray with an equal number of 0 and
1.

 

Example 1:

Input: nums = [0,1] Output: 2 Explanation: [0, 1] is the longest contiguous
subarray with an equal number of 0 and 1. Example 2:

Input: nums = [0,1,0] Output: 2 Explanation: [0, 1] (or [1, 0]) is a longest
contiguous subarray with equal number of 0 and 1.
 

Constraints:

1 <= nums.length <= 105 nums[i] is either 0 or 1.
"""

import numpy as np

class Solution(object):

    def findMaxLength(self, nums):
        # return(self.simple_brute_force_findMaxLength(nums))
        return(self.complex_efficient_findMaxLength(nums))

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