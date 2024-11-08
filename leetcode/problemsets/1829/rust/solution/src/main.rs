// Solution to leetcode problem 1829
//
// cargo run --manifest-path problemsets/1829/rust/solution/Cargo.toml"
//
// finished in 10m without ide.
// runtime 0ms!

impl Solution {
    pub fn get_maximum_xor(nums: Vec<i32>, maximum_bit: i32) -> Vec<i32> {
        let mut ret_arr = vec![0; nums.len()];
        let target_value = (1<<maximum_bit) - 1;
        let mut parity_so_far = 0;
        for (i_num, &num) in nums.iter().enumerate() {
            parity_so_far = parity_so_far ^ num;
            ret_arr[nums.len() - i_num - 1] = i32::from(parity_so_far ^ target_value);
        }
        return ret_arr;
    }
}
