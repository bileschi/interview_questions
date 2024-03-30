struct Solution;

impl Solution {
    pub fn find_max_length(nums: Vec<i32>) -> i32 {
        // Carry the cumulative sum, counting the number of '1's between
        // position 0 and i, minus the number of '0's between position 0 and i, but
        // there is no need to store the whole thing simultaneously.  

        // For each position, we record the first time we see that cumulative
        // sum (including 0 at position -1).  If we see that cumulative sum again,
        // we know that the number of '1's and '0's between the two positions is
        // the same.  We can then compare the size of the span to the largest span
        // seen so far.

        // :type nums: List[int]
        // :rtype: int
        let mut max_span_len = 0 as i32;
        let mut cum_sum = 0 as i32;
        let mut first_seen_dict = std::collections::HashMap::new();
        first_seen_dict.insert(0 as i32, -1 as i32);
        for i in 0..nums.len() {
            cum_sum += if nums[i] == 1 {1} else {-1};
            if first_seen_dict.contains_key(&cum_sum) {
                max_span_len = std::cmp::max(
                    max_span_len, i as i32 - first_seen_dict[&cum_sum]);
            } else {
                first_seen_dict.insert(cum_sum, i as i32);
            }
        }
        return max_span_len;        
    }
}

fn main() {
    println!("Hello, world!");
    let x = Solution::find_max_length(vec![0, 1]);
    println!("{}", x);
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_normal_cases() {
        assert_eq!(Solution::find_max_length(vec![0, 1]), 2);
        assert_eq!(Solution::find_max_length(vec![0,1,0]), 2);
        assert_eq!(Solution::find_max_length(vec![0,1,0,0,1,1,0]), 6);
        assert_eq!(Solution::find_max_length(vec![0,0,0,1,1,1,0]), 6);
    }

    #[test]
    fn test_edge_cases() {
        assert_eq!(Solution::find_max_length(vec![]), 0);
        assert_eq!(Solution::find_max_length(vec![0]), 0);
        assert_eq!(Solution::find_max_length(vec![1]), 0);
        assert_eq!(Solution::find_max_length(vec![0,0,0,0]), 0);
    }
}