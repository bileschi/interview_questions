// Definition for a binary tree node.

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
  pub val: i32,
  pub left: Option<Rc<RefCell<TreeNode>>>,
  pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
  #[inline]
  pub fn new(val: i32) -> Self {
    TreeNode {
      val,
      left: None,
      right: None
    }
  }
}

struct Solution;
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn flip_equiv(root1: Option<Rc<RefCell<TreeNode>>>, root2: Option<Rc<RefCell<TreeNode>>>) -> bool {
        if root1.is_none() && root2.is_none() {
            return true;
        }
        if root1.is_none() || root2.is_none() {
            return false;
        }
        let root1 = root1.unwrap();
        let root2 = root2.unwrap();
        if root1.borrow().val != root2.borrow().val {
            return false;
        }

        return (Solution::flip_equiv(
            root1.borrow().left.clone(),
            root2.borrow().left.clone(),
        ) && Solution::flip_equiv(
            root1.borrow().right.clone(),
            root2.borrow().right.clone(),
        )) || (Solution::flip_equiv(
            root1.borrow().left.clone(),
            root2.borrow().right.clone(),
        ) && Solution::flip_equiv(
            root1.borrow().right.clone(),
            root2.borrow().left.clone(),
        ));
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
        assert_eq!(Solution::flip_equiv(None, None), true);
    }
}