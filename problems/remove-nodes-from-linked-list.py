# https://leetcode.com/problems/remove-nodes-from-linked-list/description/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode(next=head)
        cur_head = new_head

        def find_max(cur_head):
            if cur_head.next is None:
                return 0
            right_max = find_max(cur_head.next)
            if cur_head.next.val < right_max:
                next_node = cur_head.next
                cur_head.next = next_node.next
                next_node.next = None
            else:
                right_max = cur_head.next.val
            return right_max

        find_max(cur_head)

        return new_head.next
