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
    pub fn replace_value_in_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        let root = if let Some(root) = root {
            root
        } else {
            return None;
        };
        // Queue of (node, sibling_sum)
        // root.val is sufficient here since root has no siblings.
        let mut queue = vec![(root.clone(), root.borrow().val)];
        while !queue.is_empty() {
            // At this point in the code, all the nodes in the queue are at the
            // same depth.
            let n_at_this_depth = queue.len();
            let mut level_sum = 0;
            for (node, _) in queue.iter() {
                level_sum += node.borrow().val;
            }

            let mut next_level_queue = vec![];
            // For every element in this depth:
            //   0. Remove it from the queue.
            //   1. Replace its value with (level_sum - siblings_sum).
            //   2. Calculate the sum of its children.
            //   3. Enclude the children in the next_level_queue.
            // Finally – replace the queue with the next_level_queue.
            for (node, siblings_sum) in queue.drain(0..n_at_this_depth) {
                let mut node = node.borrow_mut();
                // println!("Change node {} to {} - {} ({})", node.val, level_sum, siblings_sum, level_sum - siblings_sum);
                node.val = level_sum - siblings_sum;
                let mut children_sum = 0;
                if let Some(left) = node.left.clone() {
                    children_sum += left.borrow().val;
                }
                if let Some(right) = node.right.clone() {
                    children_sum += right.borrow().val;
                }
                if let Some(left) = node.left.clone() {
                    // println!("  Enquing left node ({}, {})", left.borrow().val, children_sum);
                    next_level_queue.push((left, children_sum));
                }
                if let Some(right) = node.right.clone() {
                    // println!("  Enquing right node ({}, {})", right.borrow().val, children_sum);
                    next_level_queue.push((right, children_sum));
                }
            }
            queue = next_level_queue;
        }
        Some(root)
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
        assert_eq!(Solution::replace_value_in_tree(None), None);
    }

    #[test]
    fn test_one_node() {
        let root = Rc::new(RefCell::new(TreeNode::new(1)));
        let expected = Rc::new(RefCell::new(TreeNode::new(0)));
        assert_eq!(Solution::replace_value_in_tree(Some(root)), Some(expected));
    }

    #[test]
    fn test_tree_with_two_nodes() {
        let root = Some(Rc::new(RefCell::new(TreeNode::new(1))));
        let two = Some(Rc::new(RefCell::new(TreeNode::new(2))));
        root.as_ref().unwrap().borrow_mut().right = two;
        
        let expected = Some(Rc::new(RefCell::new(TreeNode::new(0))));
        expected.as_ref().unwrap().borrow_mut().right = Some(Rc::new(RefCell::new(TreeNode::new(0))));
        assert_eq!(Solution::replace_value_in_tree(root), expected);
    }

    // in:           out:
    // 1             0
    // ├ 2           ├ 0
    // └ 3           └ 0
    #[test]
    fn test_case_3() {
        let root = Some(Rc::new(RefCell::new(TreeNode::new(1))));
        let two = Some(Rc::new(RefCell::new(TreeNode::new(2))));
        let three = Some(Rc::new(RefCell::new(TreeNode::new(3))));
        root.as_ref().unwrap().borrow_mut().left = two;
        root.as_ref().unwrap().borrow_mut().right = three;

        let expected = Some(Rc::new(RefCell::new(TreeNode::new(0))));
        let a = Some(Rc::new(RefCell::new(TreeNode::new(0))));
        let b = Some(Rc::new(RefCell::new(TreeNode::new(0))));
        expected.as_ref().unwrap().borrow_mut().left = a;
        expected.as_ref().unwrap().borrow_mut().right = b;

        assert_eq!(Solution::replace_value_in_tree(root), expected);
    }
    //     in:           out:
    // a   5             0
    // b   ├ 4           ├ 0
    // c   │ ├ 1         │ ├ 7
    // d   │ └ 10        │ └ 7
    // e   └ 9           └ 0
    // f     ├ None        ├ None
    // g     └ 7           └ 11

    #[test]
    fn test_case_4() {
        let root = Some(Rc::new(RefCell::new(TreeNode::new(5))));
        let four = Some(Rc::new(RefCell::new(TreeNode::new(4))));
        let nine = Some(Rc::new(RefCell::new(TreeNode::new(9))));
        let one = Some(Rc::new(RefCell::new(TreeNode::new(1))));
        let ten = Some(Rc::new(RefCell::new(TreeNode::new(10))));
        let seven = Some(Rc::new(RefCell::new(TreeNode::new(7))));

        root.as_ref().unwrap().borrow_mut().left = four.clone();
        root.as_ref().unwrap().borrow_mut().right = nine.clone();
        four.as_ref().unwrap().borrow_mut().left = one;
        four.as_ref().unwrap().borrow_mut().right = ten;
        nine.as_ref().unwrap().borrow_mut().right = seven;
        
        let expected = Some(Rc::new(RefCell::new(TreeNode::new(0))));
        let b = Some(Rc::new(RefCell::new(TreeNode::new(0))));
        let c = Some(Rc::new(RefCell::new(TreeNode::new(7))));
        let d = Some(Rc::new(RefCell::new(TreeNode::new(7))));
        let e = Some(Rc::new(RefCell::new(TreeNode::new(0))));
        let g = Some(Rc::new(RefCell::new(TreeNode::new(11))));
        expected.as_ref().unwrap().borrow_mut().left = b.clone();
        expected.as_ref().unwrap().borrow_mut().right = e.clone();
        b.as_ref().unwrap().borrow_mut().left = c;
        b.as_ref().unwrap().borrow_mut().right = d;
        e.as_ref().unwrap().borrow_mut().right = g;

        assert_eq!(Solution::replace_value_in_tree(root), expected);
    }




}