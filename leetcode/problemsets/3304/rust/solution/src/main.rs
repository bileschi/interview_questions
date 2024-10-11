struct Solution;

fn increment_char(c: char) -> char {
    let mut val = c as u32;
    val += 1;
    if val > 'z' as u32 {
        val = 'a' as u32;
    }
    return char::from_u32(val).unwrap();
}   


impl Solution {
    /* Build a Vec of the integer values expected at the
    * kth position of the string.
    *
    * TODO: find a way to build this vector one time 
    * outside of the solution, rather than on each invocation.
    */
    
    pub fn kth_character(k: i32) -> char {
        let mut vec : Vec<char> = Vec::<char>::with_capacity(500);
        vec.push(char::from_u32('a' as u32).unwrap());
        while vec.len() < 500 {
            let prev_len = vec.len();
            for i in 0..prev_len {
                vec.push(increment_char(vec[i]));
                if vec.len() == 500 {
                    break;
                }
            }
        }
        let idx = usize::try_from(k-1).unwrap();
        return vec[idx];
    }
}

fn main() {
    for i in 1..11 {
        println!("{:?}", Solution::kth_character(i));
    }
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
