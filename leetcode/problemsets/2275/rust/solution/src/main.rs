// Solution to leetcode problem 2275

struct Solution;
impl Solution {
    pub fn largest_combination(candidates: Vec<i32>) -> i32 {
        let mut bit_counts = vec![0; 24];
        for candidate in candidates {
            let  num = candidate;
            for i in 0..24 { 
                if (num & (1 << i)) != 0 {
                    bit_counts[i] += 1;
                }
            }
        }
        return bit_counts.iter().max().unwrap().clone();
    }
}

fn main() {
    println!("Hello, world!");
    let mysol = Solution::largest_combination(vec![3, 30, 34, 5, 9]);
    println!("{}", mysol);
    let case_1 = Solution::largest_combination(vec![16,17,71,62,12,24,14]);
    println!("{} ==? 4", case_1);
    let case_2 = Solution::largest_combination(vec![8, 8]);
    println!("{} ==? 2", case_2);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_basic() {
        assert_eq!(Solution::largest_combination(vec![16,17,71,62,12,24,14]), 4);
        assert_eq!(Solution::largest_combination(vec![8, 8]), 2);
    }
}