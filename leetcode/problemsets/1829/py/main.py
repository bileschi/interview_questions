from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        ret_arr = [0]*len(nums)
        target_value = (2**maximumBit) - 1
        parity_so_far = 0
        for i_num, num in enumerate(nums):
            parity_so_far = parity_so_far ^ num
            ret_arr[i_num] = parity_so_far ^ target_value
        ret_arr.reverse()
        return ret_arr