# Solution to leetcode problem 2577
#
# m == grid.length
# n == grid[i].length
# 2 <= m, n <= 1000
# 4 <= m * n <= 105
# 0 <= grid[i][j] <= 105
# grid[0][0] == 0

import collections
from typing import List, Tuple, Set
from queue import PriorityQueue


Position = Tuple[int, int]
Time = int
HashableState = Tuple[Time, Position]

class Solution(object):

    def minimumTime(self, grid: List[List[int]]) -> int:
        """
        :type grid: List[List[int]]
        :rtype: int
        """ 
        if grid[0][1] > 1 and grid[1][0] > 1:
            # If we cannot move to the right or down, return -1.
            return -1
        # Solve via Djikstra's algorithm:
        # Maintain a priority queue of positions, sorted by time to reach.
        queue = PriorityQueue(maxsize=0)
        visited_pos : Set[Position]= set()
        m = len(grid)
        n = len(grid[0])
        end_pos = (m - 1, n - 1)
        # Add the starting position to the queue.  Queue is sorted by time.
        starting_pos = (0, 0)
        starting_time = 0
        queue.put((starting_time, starting_pos))
        while not queue.empty():
            curr_state = queue.get()

            # print(f"X: {queue=}, {curr_state=}")
            curr_time, curr_pos = curr_state
            # If we are at the end, return the time.
            if curr_pos == end_pos:
                return curr_time
            # If we have already visited this position, continue.
            if curr_pos in visited_pos:
                continue
            visited_pos.add(curr_pos)
            next_states = self.get_next_states(grid, curr_state, visited_pos)
            for next_state in next_states:
                queue.put(next_state)
                # print(f" XXX queue size is now {queue.qsize()}")
        # If we have exhausted all possible states, return -1.
        return -1

    def get_next_states(
            self,
            grid: List[List[int]], 
            curr_state: HashableState,
            visited_pos: Set[Position]) -> List[HashableState]:
        # Get the next states from the current state.
        # Valid next states are:
        #  On the board.
        #  Not visited.
        #  +1 time if currtime +1 >= new_pos_min_time.
        #  new_pos_min_time if diff is even.
        #  new_pos_min_time + 1 if diff is odd.

        curr_time, curr_pos = curr_state
        y, x = curr_pos
        next_states = []
        # Check all 4 directions.
        m = len(grid)
        n = len(grid[0])
        for dy, dx in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            new_x = x + dx
            new_y = y + dy
            new_pos = (new_y, new_x)
            if new_pos in visited_pos:
                continue
            if 0 <= new_x < n and 0 <= new_y < m:
                # If the time is greater than or equal to the grid value,
                # we can move to that position at time + 1
                new_pos_min_time = grid[new_y][new_x]
                if curr_time + 1 >= new_pos_min_time:
                    next_states.append((curr_time + 1, new_pos))
                else:
                    diff_time = new_pos_min_time - curr_time
                    if diff_time % 2 == 0:
                        next_states.append((new_pos_min_time+1, new_pos))
                    else:
                        next_states.append((new_pos_min_time, new_pos))
        return next_states
