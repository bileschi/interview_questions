# 773. Sliding Puzzle On an 2 x 3 board, there are five tiles labeled from 1 to
# 5, and an empty square represented by 0. A move consists of choosing 0 and a
# 4-directionally adjacent number and swapping it.

# The state of the board is solved if and only if the board is
# [[1,2,3],[4,5,0]].

# Given the puzzle board board, return the least number of moves required so
# that the state of the board is solved. If it is impossible for the state

from typing import Dict, List, Tuple

HashableGameState = Tuple[int, int, int, int, int, int]

def _precompute_states() -> Dict[HashableGameState, int]:
    # BFS brute force to compute all states and their costs
    # starting from the solved state.
    # use a tuple as a representation of the board.
    state_to_cost = {(1, 2, 3, 4, 5, 0): 0}
    # The BFS queue
    end_state = (1, 2, 3, 4, 5, 0)
    zero_cost = 0
    queue = [(end_state, zero_cost)]
    while queue:
        # pop the first element
        [cur_state, cur_cost] = queue.pop(0)
        for next_state in _get_possible_moves(cur_state):
            if next_state not in state_to_cost:
                state_to_cost[next_state] = cur_cost + 1
                queue.append((next_state, cur_cost + 1))
    return state_to_cost


# [[0, 1, 2],
#  [3, 4, 5]]
SWAPPABLE_INDICIES = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4],
    4: [1, 3, 5],
    5: [2, 4]
}

def _get_possible_moves(state: HashableGameState) -> List[HashableGameState]:
    # Warning: Assumes HashableGameState is valid.
    # find the index of the zero.
    idx_of_zero = state.index(0)
    # get the list of swappable indicies.
    swappable_indicies = SWAPPABLE_INDICIES[idx_of_zero]
    # produce a state for each swappable index.
    out = []
    for si in swappable_indicies:
        # swap the zero with the number at the swappable index.
        new_state = list(state)
        new_state[idx_of_zero], new_state[si] = new_state[si], new_state[idx_of_zero]
        out.append(tuple(new_state))
    return out

class Solution:
    # There are only 6 permuted numbers in the board, so there are only
    # 6! = 720 states.
    # The full set of states can be computed by BFS brute force.
    def __init__(self):
        self._state_to_cost = _precompute_states()

    def valid_board(self, board: List[List[int]]) -> bool:
        if not board:
            return False
        if len(board) != 2:
            return False
        if len(board[0]) != 3:
            return False
        if len(board[1]) != 3:  
            return False
        values = set(board[0] + board[1])
        if len(values) != 6:
            return False
        if len(values.union(set(range(6)))) != 6:
            return False
        return True


    def slidingPuzzle(self, board: List[List[int]]) -> int:
        if not self.valid_board(board):
            return -1
        state = tuple(board[0] + board[1])
        if not state in self._state_to_cost:
            # The state is not reachable.
            return -1
        return self._state_to_cost.get(state)
        

