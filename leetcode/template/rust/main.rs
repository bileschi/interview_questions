// Solution to leetcode problem DIGIT_GOES_HERE

struct Solution;
impl Solution {
    pub fn do_the_thing(_val: i32) -> bool {
        true
    }
}

fn main() {
    println!("Hello, world!");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_empty() {
        assert_eq!(Solution::do_the_thing(1234), true);
    }
}