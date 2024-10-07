from typing import Optional

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing
# together the nodes of the first two lists.

# Return the head of the merged linked list.

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
   
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def print(self):
        print("Hello World")

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Destroys original lists - do not use original lists after merging.
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list1.val < list2.val:
            head_new = list1
            list1 = list1.next
        else:
            head_new = list2
            list2 = list2.next
        tail_new = head_new
        while list1 or list2:
            # If one list is empty, append the other list to the new list.
            if list1 is None:
                tail_new.next = list2
                return head_new
            if list2 is None:
                tail_new.next = list1
                return head_new
            if list1.val < list2.val:
                tail_new.next = list1
                tail_new = tail_new.next
                list1 = list1.next
            else:
                tail_new.next = list2
                tail_new = tail_new.next
                list2 = list2.next
        return head_new


if __name__ == "__main__":
    s = Solution()
    s.print()
