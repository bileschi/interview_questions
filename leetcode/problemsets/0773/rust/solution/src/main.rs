// Solution to leetcode problem 0773
//
// cargo run --manifest-path problemsets/0773/rust/solution/Cargo.toml"

// struct Solution;
// impl Solution {
//     pub fn do_the_thing(_val: i32) -> bool {
//         true
//     }
// }

// fn main() {
//     println!("Hello, world!");
// }

// #[cfg(test)]
// mod tests {
//     use super::*;

//     #[test]
//     fn test_empty() {
//         assert_eq!(Solution::do_the_thing(1234), true);
//     }
// }




// Solution to leetcode problem 0773
//
// cargo run --manifest-path problemsets/0773/rust/solution/Cargo.toml"


use std::collections::{HashMap, VecDeque, HashSet};
use once_cell::sync::Lazy; // For lazy static initialization

// Type alias for clarity, representing the flattened board state [0..5]
type BoardState = [i32; 6];

// --- Constants ---

// The target solved state
const SOLVED_STATE: BoardState = [1, 2, 3, 4, 5, 0];

// Precomputed indices that can be swapped with the tile at a given index.
// Index: 0 1 2
//        3 4 5
const SWAPPABLE_INDICES: [&[usize]; 6] = [
    &[1, 3],    // Index 0 neighbours
    &[0, 2, 4], // Index 1 neighbours
    &[1, 5],    // Index 2 neighbours
    &[0, 4],    // Index 3 neighbours
    &[1, 3, 5], // Index 4 neighbours
    &[2, 4],    // Index 5 neighbours
];

// --- Precomputation Logic using Lazy Static ---

// Use `once_cell::sync::Lazy` to compute the state-to-cost map once, thread-safely.
static STATE_TO_COST: Lazy<HashMap<BoardState, i32>> = Lazy::new(|| {
    precompute_states()
});

// Performs BFS starting from the solved state to find costs for all reachable states.
fn precompute_states() -> HashMap<BoardState, i32> {
    let mut state_to_cost: HashMap<BoardState, i32> = HashMap::new();
    let mut queue: VecDeque<(BoardState, i32)> = VecDeque::new();

    // Start BFS from the solved state with cost 0
    state_to_cost.insert(SOLVED_STATE, 0);
    queue.push_back((SOLVED_STATE, 0));

    while let Some((current_state, current_cost)) = queue.pop_front() {
        for next_state in get_possible_moves(&current_state) {
            // If we haven't seen this state before, record its cost and add to queue
            if !state_to_cost.contains_key(&next_state) {
                state_to_cost.insert(next_state, current_cost + 1);
                queue.push_back((next_state, current_cost + 1));
            }
        }
    }
    println!("Precomputed {} reachable states.", state_to_cost.len()); // Informative
    state_to_cost
}

// Generates all possible next states from a given state by swapping the '0'.
fn get_possible_moves(state: &BoardState) -> Vec<BoardState> {
    let mut possible_moves = Vec::new();

    // Find the index of the empty tile (0)
    let zero_index = state.iter().position(|&tile| tile == 0)
        .expect("Board state must contain a 0."); // Should always succeed for valid states

    // Iterate through the indices that can be swapped with the zero tile
    for &swap_target_index in SWAPPABLE_INDICES[zero_index] {
        let mut next_state = *state; // Copy the current state array
        // Perform the swap
        next_state.swap(zero_index, swap_target_index);
        possible_moves.push(next_state);
    }

    possible_moves
}

// --- Solution Struct and Methods ---

pub struct Solution;

impl Solution {
    // Main method to find the minimum number of moves
    pub fn sliding_puzzle(board: Vec<Vec<i32>>) -> i32 {
        // 1. Validate the input board
        if !Self::is_valid_board(&board) {
            return -1;
        }

        // 2. Flatten the 2x3 board into a 1D array representation
        let mut current_state: BoardState = [0; 6];
        let mut k = 0;
        for i in 0..2 {
            for j in 0..3 {
                current_state[k] = board[i][j];
                k += 1;
            }
        }

        // 3. Look up the precomputed cost for the state
        // Access the lazily initialized map. It will be computed on first access.
        STATE_TO_COST.get(&current_state)
                     .map(|&cost| cost) // Dereference the cost if found
                     .unwrap_or(-1)     // Return -1 if the state is not found (unreachable)
    }

    // Helper function to validate the board dimensions and contents
    fn is_valid_board(board: &Vec<Vec<i32>>) -> bool {
        if board.len() != 2 { return false; }
        if board.get(0).map_or(true, |row| row.len() != 3) { return false; }
        if board.get(1).map_or(true, |row| row.len() != 3) { return false; }

        let mut seen = HashSet::with_capacity(6);
        let mut count = 0;
        for i in 0..2 {
            for j in 0..3 {
                let val = board[i][j];
                if val < 0 || val > 5 { return false; } // Must be 0-5
                if !seen.insert(val) { return false; } // Check for duplicates
                count += 1;
            }
        }

        count == 6 && seen.len() == 6 // Ensure exactly 6 unique numbers 0-5
    }
}

fn main() {
    println!("Hello, world!");
    println!("Create a simple board and what we calculate.");
    let board = vec![vec![4, 1, 2], vec![5, 0, 3]];
    let result = Solution::sliding_puzzle(board);
    println!("Result: {}", result); // Should print the number of moves to solve
}


// --- Tests ---
#[cfg(test)]
mod tests {
    use super::*; // Import items from parent module (Solution, helpers)

    // Helper to create HashSet for comparing move results irrespective of order
    fn moves_to_set(moves: Vec<BoardState>) -> HashSet<BoardState> {
        moves.into_iter().collect()
    }

    #[test]
    fn test_basic_eq_num_moves() {
        assert_eq!(Solution::sliding_puzzle(vec![vec![1,2,3], vec![4,0,5]]), 1);
        assert_eq!(Solution::sliding_puzzle(vec![vec![4,1,2], vec![5,0,3]]), 5);
    }

    #[test]
    fn test_no_solution_eq_neg_1() {
        // This state is known to be unreachable from the solved state.
        assert_eq!(Solution::sliding_puzzle(vec![vec![1,2,3], vec![5,4,0]]), -1);
    }

    #[test]
    fn test_invalid_board_eq_neg_1() {
        let invalid_boards = vec![
            vec![vec![1,2,3], vec![4,5,6]],  // Wrong number range
            vec![vec![1,2,3], vec![4,5]],    // Wrong inner dimension
            vec![vec![1,2,0], vec![4,5,0]],  // Duplicate number (0)
            vec![vec![1,2], vec![4,5,0]],    // Wrong inner dimension
            vec![vec![1,2,3]],               // Wrong outer dimension
            vec![],                          // Empty board
        ];
        for board in invalid_boards {
            assert_eq!(Solution::sliding_puzzle(board), -1);
        }
    }

     #[test]
    fn test_get_possible_moves_1() {
        let start_state: BoardState = [1, 2, 3, 0, 4, 5]; // Zero at index 3
        let moves = get_possible_moves(&start_state);
        let expected_moves = vec![
            [0, 2, 3, 1, 4, 5], // Swapped with index 0
            [1, 2, 3, 4, 0, 5], // Swapped with index 4
        ];
        // Compare sets to ignore order differences
        assert_eq!(moves_to_set(moves), moves_to_set(expected_moves));
    }

    #[test]
    fn test_get_possible_moves_2() {
        let start_state: BoardState = [1, 0, 3, 4, 2, 5]; // Zero at index 1
        let moves = get_possible_moves(&start_state);
        let expected_moves = vec![
            [0, 1, 3, 4, 2, 5], // Swapped with index 0
            [1, 3, 0, 4, 2, 5], // Swapped with index 2
            [1, 2, 3, 4, 0, 5], // Swapped with index 4
        ];
         // Compare sets to ignore order differences
        assert_eq!(moves_to_set(moves), moves_to_set(expected_moves));
    }

    #[test]
    fn test_precompute_states_size() {
        // Access the map to trigger computation if not already done
        let map = &*STATE_TO_COST;
        // As noted, only half the permutations are reachable.
        assert_eq!(map.len(), 360);
    }

     #[test]
    fn test_solved_state_cost_zero() {
         assert_eq!(Solution::sliding_puzzle(vec![vec![1,2,3], vec![4,5,0]]), 0);
     }
}
