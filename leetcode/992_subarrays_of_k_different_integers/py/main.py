# Given an integer array nums and an integer k, return the number of good subarrays of nums.

# A good array is an array where the number of different integers in that array is exactly k.

# For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
# A subarray is a contiguous part of an array.

 

# Example 1:

# Input: nums = [1,2,1,2,3], k = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
# Example 2:

# Input: nums = [1,2,1,3,4], k = 3
# Output: 3
# Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# 1 <= nums[i], k <= nums.length

import time

def subarraysWithKDistinct(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    result = brute_force(nums, k)

def brute_force(nums, k):
    n = 0
    for i in range(len(nums)):
        for j in range(len(nums)+1):
            n_unique = len(set(nums[i:j]))
            if n_unique == k:
                n+=1
    return(n)


def v2(nums, k):
    n = 0
    for i in range(len(nums)):
        vals_so_far = set()
        for j in range(i, len(nums)):
            vals_so_far.add(nums[j])
            n_unique = len(vals_so_far)
            if n_unique == k:
                n+=1
            if n_unique > k:
                break
    return(n)
                                             
if __name__ == "__main__":
    N = 1000
    big_array_of_ones = [1] * N
    f = brute_force
    t1 = time.time()
    assert(f(big_array_of_ones, 1) ==  N * (N+1) / 2)
    t2 = time.time()
    print(f"brute force = {t2 - t1:.2f} seconds")

    f = v2
    t1 = time.time()
    assert(f(big_array_of_ones, 1) ==  N * (N+1) / 2)
    t2 = time.time()
    print(f"brute force = {t2 - t1:.2f} seconds")

    