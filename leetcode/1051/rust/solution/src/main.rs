use::std::iter::zip;

struct Solution;

impl Solution {
    pub fn height_checker(heights: Vec<i32>) -> i32 {
        let mut s = heights.clone();
        s.sort();
        let mut count = 0;
        for (i, j) in zip(heights, s) {
            if i != j {
                count += 1;
            }
        }
        return count;
    }
}

fn main() {
    println!("Hello, world!");
    println!("{}", Solution::height_checker(vec![1,1,4,2,1,3]));
    println!("{}", Solution::height_checker(vec![5,1,2,3,4]));
    println!("{}", Solution::height_checker(vec![1,2,3,4,5]));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_normal_cases() {
        assert_eq!(Solution::height_checker(vec![1,1,4,2,1,3]), 3);
        assert_eq!(Solution::height_checker(vec![5,1,2,3,4]), 5);
        assert_eq!(Solution::height_checker(vec![1,2,3,4,5]), 0);
    }

    #[test]
    fn test_edge_cases() {
        assert_eq!(Solution::height_checker(vec![]), 0);
        assert_eq!(Solution::height_checker(vec![1]), 0);
        assert_eq!(Solution::height_checker(vec![1,1]), 0);
    }
}