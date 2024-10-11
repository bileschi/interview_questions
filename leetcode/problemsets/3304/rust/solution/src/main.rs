struct Solution;

// use std::collections::HashMap;


impl Solution {
    /* Build a Vec of the integer values expected at the
    * kth position of the string.
    */
    
    pub fn kth_character(k: i32) -> char {
        let mut vec : Vec<u32> = Vec::<u32>::with_capacity(500);
        vec.push(0 + 'a' as u32);
        while vec.len() < 500 {
            let prev_len = vec.len();
            for i in 0..prev_len {
                vec.push(1 + vec[i]);
                if vec.len() == 500 {
                    break;
                }
            }
        }
        let idx = usize::try_from(k-1).unwrap();
        return char::from_u32(vec[idx]).unwrap();
    }
}

fn main() {
    println!("Hello, world!");
    for i in 1..11 {
        println!("{:?}", Solution::kth_character(i));
    }
    // println!("{:?}", Solution::kth_character(1));
    // println!("{:?}", Solution::kth_character(5));
    // println!("{:?}", Solution::kth_character(10));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_normal_cases() {
        assert_eq!(Solution::kth_character(5), 'b');
        assert_eq!(Solution::kth_character(10), 'c');
    }

}
