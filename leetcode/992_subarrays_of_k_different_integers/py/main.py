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
import collections

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

def v3(nums, k):
    n = 0
    for i in range(len(nums)):
        unqiue_so_far = set()
        n_unique = 0
        for j in range(i, len(nums)):
            # we already have this value
            if nums[j] in unqiue_so_far:
                if n_unique == k:
                    n+=1
                continue
            # new value
            # if this would push us over, we're done with this i
            if n_unique == k:
                break
            unqiue_so_far.add(nums[j])
            n_unique += 1
            if n_unique == k:
                n+=1
    return(n)

def v4(nums, k):
    nk = v4_helper(nums, k)
    nk_minus = v4_helper(nums, k-1)
    return nk - nk_minus

def v4_helper(nums, k):
    # returns the number of subarrays w/ k *or fewer* uniq
    if k == 0:
        return 0
    # n is how many subarrays w/ k *or fewer* uniq so far.
    n = 0
    # i is the left point inclusive.  j is the right point inclusive. We count
    # all subarrays between i and j which **include point j**. If the span has
    # more than k unique valueswe increment i until it does not, and continue.
    i = 0
    count_in_subarray = collections.Counter()
    num_non_zero_count = 0
    for j in range(len(nums)):
        # j has been incremented .. do the book keeping.
        v = nums[j]
        if count_in_subarray[v] == 0:
            num_non_zero_count += 1
        count_in_subarray[v] += 1
        # If the span has more than k unique values, increment i until there
        # are only k in the valid span.
        # Do the book keeping to remove the values at
        # i before incrementing.
        while num_non_zero_count > k:
            v = nums[i]
            count_in_subarray[v] -= 1
            if count_in_subarray[v] == 0:
                num_non_zero_count -= 1
            i+=1
        # If the span has <= k uniqe values, increment the total with all unque
        # subarrays that end with k.
        if num_non_zero_count <= k:
            n += j - i + 1

    return(n)


if __name__ == "__main__":
    N = 10000
    big_array_of_ones = [1] * N

    # f = brute_force
    # t1 = time.time()
    # assert(f(big_array_of_ones, 1) ==  N * (N+1) / 2)
    # t2 = time.time()
    # print(f"brute force = {t2 - t1:.2f} seconds")

    f = v2
    t1 = time.time()
    assert(f(big_array_of_ones, 1) ==  N * (N+1) / 2)
    t2 = time.time()
    print(f"v2 = {t2 - t1:.2f} seconds")

    f = v3
    t1 = time.time()
    assert(f(big_array_of_ones, 1) ==  N * (N+1) / 2)
    t2 = time.time()
    print(f"v3 = {t2 - t1:.2f} seconds")


    f = v4
    t1 = time.time()
    assert(f(big_array_of_ones, 1) ==  N * (N+1) / 2)
    t2 = time.time()
    print(f"v4 = {t2 - t1:.2f} seconds")

