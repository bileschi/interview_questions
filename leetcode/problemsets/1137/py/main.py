# The Tribonacci sequence Tn is defined as follows: 

# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

# Given n, return the value of Tn.

 

# Example 1:

# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
# Example 2:

# Input: n = 25
# Output: 1389537
 

# Constraints:

# 0 <= n <= 37
# The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
import time


class RecursiveSolution(object):
    def __init__(self):
        self.memory = {0: 0, 1: 1, 2: 1}

    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.memory:
            return self.memory[n]
        else:
            self.memory[n] = (
                self.tribonacci(n-1) +
                self.tribonacci(n-2) +
                self.tribonacci(n-3))
            return(self.memory[n])

class IterativeSolution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        
        v_minus3 = 0
        v_minus2 = 1
        v_minus1 = 1
        v_0 = None
        for i in range(3,n+1):
            v_0 = v_minus1 + v_minus2 + v_minus3
            v_minus3 = v_minus2
            v_minus2 = v_minus1
            v_minus1 = v_0            
        return v_0

Solution = IterativeSolution
# Interestingly, the recursive solution is faster than iterative solution
#
# $ python3 main.py
# Iterative = 0.00001907 s
# Recursive = 0.00000310 s


if __name__ == '__main__':
    i_sol = IterativeSolution()
    r_sol = RecursiveSolution()
    N = 37

    t1 = time.time()
    r_sol.tribonacci(N)
    t2 = time.time()
    print(f"Iterative = {t2 - t1:.8f} s")

    t1 = time.time()
    i_sol.tribonacci(N)
    t2 = time.time()
    print(f"Recursive = {t2 - t1:.8f} s")

    print('hi')