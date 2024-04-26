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
import numpy as np

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


def v5(nums, k):
    if k == 0:
        return 0
    # n is how many subarrays w/ uniq so far.
    n = 0
    # [i_k, j] are the end points (inclusive) for subarrays that contain 
    # *at most* k unique values.
    # [i_m, j] are the end points (inclusive) for subarrays that contain 
    # *at most* k-1 unique values.

    # Algo sketch - we increment j until the [i_k, j] span includes
    # k unique values.  We then count the number of sub arrays containing j.
    # This set includes spans with k *or fewer* unique values.  We then
    # increment i_m until the [i_m, j] span contains only k-1 unique values.
    # We then count the number uf subarrays of this span containing j.
    # this is the number containing k-1 or fewer unique values.  The
    # difference between these two counts is the number of sub arrays
    # with exactly k values that end at point j.

    i_k = 0
    i_m = 0
    vals_in_subarray_k = [0] * (len(nums)+1)
    vals_in_subarray_m = [0] * (len(nums)+1)
    len_vals_in_subarray_k = 0
    len_vals_in_subarray_m = 0
    for j in range(len(nums)):
        # j has been incremented .. do the book keeping.
        v = nums[j]
        if vals_in_subarray_k[v] == 0:
            len_vals_in_subarray_k += 1
        vals_in_subarray_k[v] += 1
        if vals_in_subarray_m[v] == 0:
            len_vals_in_subarray_m += 1
        vals_in_subarray_m[v] += 1
        # If the span has more than k unique values, increment i_k until there
        # are only k in the valid span.
        while len_vals_in_subarray_k > k:
            v = nums[i_k]
            vals_in_subarray_k[v] -= 1
            if vals_in_subarray_k[v] == 0:
                len_vals_in_subarray_k -= 1
            i_k+=1
        while len_vals_in_subarray_m > (k-1):
            v = nums[i_m]
            vals_in_subarray_m[v] -= 1
            if vals_in_subarray_m[v] == 0:
                len_vals_in_subarray_m -= 1
            i_m+=1
        # If the [i_k, j] span has k unique values, increment the total and
        # subtract the num unique in the [i_m, j] span.
        if len_vals_in_subarray_k == k:
            # n += num_in_ik_span - num_in_im_span 
            # n += ((j - i_k) + 1) - ((j - i_m) + 1) 
            n += (i_m - i_k) 
    return(n)

def v6(nums, k):
    # n is how many subarrays w/ uniq so far.
    n = 0
    # [i, j] are the end points (inclusive) for a sliding window subarray.
    #
    #
    #  [L] [          C            ]  [ R ]
    #  (i) (i+1)       ...       (j)  (j+1)
    #

    # We increment j until there are exactly k elements in the span [i, j].  We
    # then increment i

    N = len(nums)
    if N == 0:
        return 0
    vals_in_ij_span = [0] * (N+1)
    num_uniq_in_ij_span = 0
    n = 0
    i = 0
    j = 0
    valid_i_range = 0
    while j < N:
        # add the j'th element.
        if vals_in_ij_span[nums[j]] == 0:
            num_uniq_in_ij_span += 1
        vals_in_ij_span[nums[j]] += 1
        # If we've moved into a region where there are now more than k in the
        # span, increase the left pointer and reset the size of the valid range.
        if num_uniq_in_ij_span > k:
            vals_in_ij_span[nums[i]] -= 1
            if vals_in_ij_span[nums[i]] == 0:
                num_uniq_in_ij_span -= 1
            i += 1
            valid_i_range = 0
        
        # If the current span has exactly k, continue moving the left pointer
        # and calculate the size of the range for this region.
        if num_uniq_in_ij_span == k:
            # If the span would still be valid if we move the left pointer, do
            # it.
            while vals_in_ij_span[nums[i]] > 1:
                vals_in_ij_span[nums[i]] -= 1
                if vals_in_ij_span[nums[i]] == 0:
                    num_uniq_in_ij_span -= 1
                i += 1
                valid_i_range += 1
            n += valid_i_range + 1
        
        j += 1
    return n



if __name__ == "__main__":
    N = 1234567
    big_array_of_ones = [1] * N
    big_random_array = list(np.random.randint(1, 10, 1234567))
    
    # f = brute_force
    # t1 = time.time()
    # assert(f(big_array_of_ones, 1) ==  N * (N+1) / 2)
    # t2 = time.time()
    # print(f"brute force = {t2 - t1:.2f} seconds")

    # f = v2
    # t1 = time.time()
    # assert(f(big_array_of_ones, 1) ==  N * (N+1) / 2)
    # t2 = time.time()
    # print(f"v2 = {t2 - t1:.2f} seconds")

    # f = v3
    # t1 = time.time()
    # assert(f(big_array_of_ones, 1) ==  N * (N+1) / 2)
    # t2 = time.time()
    # print(f"v3 = {t2 - t1:.2f} seconds")

    def ones_test(f):
        t1 = time.time()
        assert(f(big_array_of_ones, 1) ==  N * (N+1) / 2)
        t2 = time.time()
        print(f"ones: {f.__name__} = {t2 - t1:.2f} seconds")

    def rand_test(f,):
        t1 = time.time()
        f(big_random_array, 6)
        t2 = time.time()
        print(f"random: {f.__name__} = {t2 - t1:.2f} seconds")

    for f in [v4, v5, v6]:
        ones_test(f)
        rand_test(f)
        print("----")
