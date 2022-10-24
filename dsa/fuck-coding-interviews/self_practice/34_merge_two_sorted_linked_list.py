# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    """
    Runtime: 54 ms, faster than 71.55% of Python3 online submissions for Merge Two Sorted Lists.
    Memory Usage: 13.9 MB, less than 79.22% of Python3 online submissions for Merge Two Sorted Lists.
    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # make sure both links are not null.
        if not(list1 and list2):
            return list1 or list2
        
        new_head = cur_head = ListNode()
        
        while list1 and list2:
            if list1.val <= list2.val:
                cur_head.next = list1
                list1 = list1.next
            else:
                cur_head.next = list2
                list2 = list2.next
            cur_head = cur_head.next
        
        cur_head.next = list1 or list2
        return new_head.next
        