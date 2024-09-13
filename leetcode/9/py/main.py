# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:

# -231 <= x <= 231 - 1
 

# Follow up: Could you solve it without converting the integer to a string?

class Solution(object):
    def isPalindrome(self, x):
        return self.isPalindromeString(x)

    def isPalindromeString(self, x):
        """
        :type x: int
        :rtype: bool
        """
        fwd = str(x)
        rev = fwd[-1::-1]
        return(fwd == rev)

    def isPalindromeNoString(self, x):
        if x < 0:
            return False
        tmp = x
        y = 0
        while tmp > 0:
            y *= 10
            y += tmp % 10
            tmp = tmp // 10
        return x == y
        
