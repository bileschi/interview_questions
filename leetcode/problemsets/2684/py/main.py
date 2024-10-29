# Solution to leetcode problem 2684
#
#
# You are given a 0-indexed m x n matrix grid consisting of positive integers.

# You can start at any cell in the first column of the matrix, and traverse the
# grid in the following way:

# From a cell (row, col), you can move to any of the cells: (row - 1, col + 1),
# (row, col + 1) and (row + 1, col + 1) such that the value of the cell you move
# to, should be strictly bigger than the value of the current cell. Return the
# maximum number of moves that you can perform.

from typing import List

class Solution(object):
 
    # Brute force solution:  Each cell in the leftmost column may be visited
    # at a move cost of zero.  For each cell in the next column, see if it
    # can be reached from teh previous column.  If so, mark that it may be reached.
    # Continue until the last column or no cells in a column can be reached.
    #
    # The number of moves is the index of the last column that is reached.
    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid) # number of rows.  2 <= m <= 4
        n = len(grid[0]) # number of cols.  2 <= n <= 1000
        currentColumnIdx = 0
        maxColumnIdx = 0
        currentColumnReachable = [True] * m
        while (currentColumnIdx < (n-1)) and any(currentColumnReachable):
            nextColumnReachable = [False] * m
            for i in range(m):
                if currentColumnReachable[i]:
                    for j in reversed(range(-1, 2)):
                        # if nextColumnReachable[i+j]: break # Short if we have already reached this cell
                        if (i+j >= 0) and (i+j < m) and (grid[i+j][currentColumnIdx+1] > grid[i][currentColumnIdx]):
                            nextColumnReachable[i+j] = True
                            maxColumnIdx = currentColumnIdx+1
            currentColumnIdx += 1
            currentColumnReachable = nextColumnReachable
        return maxColumnIdx
