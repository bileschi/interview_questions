from collections import Counter

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        neg_cnt = Counter(filter(lambda x : x < 0, nums))
        pos_cnt = Counter(filter(lambda x : x > 0, nums))
        # count the number of zeros in nums
        num_zeros = Counter(filter(lambda x : x is 0, nums))[0]
        trips = []
        # solution types:
        # A [- - +]
        # B [- + +]
        # C [- 0 +]
        # D [0 0 0]

        # A [- - +]
        for pos in pos_cnt:
            for neg in neg_cnt:
                rem = -(pos + neg)
                if rem > neg:
                    continue
                if rem in neg_cnt:
                    if (neg != rem) or (neg_cnt[neg] > 1):
                        trips.append([rem, neg, pos])



        # B [- + +]
        for neg in neg_cnt:
            for pos in pos_cnt:
                rem = -(pos + neg)
                if rem < pos:
                    continue
                if rem in pos_cnt:
                    if (pos != rem) or (pos_cnt[pos] > 1):
                        trips.append([neg, pos, rem])

        # C
        if num_zeros >= 1:
            for neg in neg_cnt:
                if -neg in pos_cnt:
                    trips.append([neg, 0, -neg])
        # D
        if num_zeros >= 3:
            trips.append([0, 0, 0])
        return(trips)


