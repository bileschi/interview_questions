# Given two version numbers, version1 and version2, compare them.

# Version numbers consist of one or more revisions joined by a dot '.'. Each
# revision consists of digits and may contain leading zeros. Every revision
# contains at least one character. Revisions are 0-indexed from left to right,
# with the leftmost revision being revision 0, the next revision being revision
# 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.

# Revisions are compared using their integer value ignoring any leading zeros.
# To compare version numbers, compare their revisions in left-to-right order.
# This means that revisions 1 and 001 are considered equal. If a version number
# does not specify a revision at an index, then treat the revision as 0. For
# example, version 1.0 is less than version 1.1 because their revision 0s are
# the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

# Return the following:

# If version1 < version2, return -1.
# If version1 > version2, return 1.
# Otherwise, return 0.
 

# Example 1:

# Input: version1 = "1.01", version2 = "1.001"
# Output: 0
# Explanation: Ignoring leading zeroes, both "01" and "001" represent the same
#   integer "1".

# Example 2:

# Input: version1 = "1.0", version2 = "1.0.0"
# Output: 0
# Explanation: version1 does not specify revision 2, which means it is
#   treated as "0".

# Example 3:

# Input: version1 = "0.1", version2 = "1.1"
# Output: -1
# Explanation: version1's revision 0 is "0", while version2's revision 0
#  is "1". 0 < 1, so version1 < version2.

class Solution(object):
    def compareVersionBrute(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        MAX_L = 500
        sp1 = [int(x) for x in version1.split(".")]
        while len(sp1) < MAX_L:
            sp1.append(0)
        sp2 = [int(x) for x in version2.split(".")]
        while len(sp2) < MAX_L:
            sp2.append(0)
        for i in range(500):
            if (sp1[i] < sp2[i]):
                return -1
            if (sp1[i] > sp2[i]):
                return 1
        return 0
        
    def compareV2(self, version1, version2):
        """
        as above, but don't auto pad with strings
        """
        sp1 = [int(x) for x in version1.split(".")]
        sp2 = [int(x) for x in version2.split(".")]

        for i in range(min(len(sp1), len(sp2))):
            if (sp1[i] < sp2[i]):
                return -1
            if (sp1[i] > sp2[i]):
                return 1
        for i in range(len(sp2), len(sp1)):
            if(sp1[i]>0):
                return 1
        for i in range(len(sp1), len(sp2)):
            if(sp2[i]>0):
                return -1
        return 0

    def compareV3(self, version1, version2):
        """
        as above, but don't convert to string until you have to
        """
        sp1 = version1.split(".")
        sp2 = version2.split(".")

        for i in range(min(len(sp1), len(sp2))):
            x = int(sp1[i])
            y = int(sp2[i])
            if x < y:
                return -1
            if (x > y):
                return 1
        for i in range(len(sp2), len(sp1)):
            if int(sp1[i]) > 0:
                return 1
        for i in range(len(sp1), len(sp2)):
            if int(sp2[i]) > 0:
                return -1
        return 0
