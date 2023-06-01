# https://leetcode.com/problems/copy-list-with-random-pointer/

from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # step 1: add a node along every node.
        cur_node = head
        while cur_node:
            cur_node.next = Node(cur_node.val, cur_node.next)
            cur_node = cur_node.next.next
        
        # step 2: map random pointer data
        cur_node = head
        while cur_node:
            cur_node.next.random = cur_node.random.next if cur_node.random else None
            cur_node = cur_node.next.next
        

        # step 3: remove old nodes.
        cur_node = head.next
        while cur_node.next:
            cur_node.next = cur_node.next.next
            cur_node = cur_node.next

        return head.next