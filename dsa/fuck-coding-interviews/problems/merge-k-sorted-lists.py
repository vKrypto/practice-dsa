# coding: utf-8
"""
https://leetcode.com/problems/merge-k-sorted-lists/
"""
import heapq
from . import Optional, List, ListNode


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def gen_nodes(node):
            while node:
                yield node
                node = node.next

        linked_lists = [gen_nodes(head) for head in lists]
        sorted_nodes = heapq.merge(*linked_lists, key=lambda node: node.val)
        dummy_head = last_node = ListNode()
        for node in sorted_nodes:
            last_node.next = node
            last_node = node

        return dummy_head.next


class Solution_2:

    # space complexity: o(m) and time complexity=o(m*n)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merge_list = merge_list_head = ListNode()

        while True:
            # step 1: find min node val
            min_val = None
            for linked_list in lists:
                if linked_list and (min_val is None or linked_list.val < min_val):
                    min_val = linked_list.val
                
            # step 2: check if head_node.val is equal to min_val and advance head node by 1 node.
            nodes = []
            i = 0
            while i < len(lists):
                linked_list = lists[i]
                if linked_list and linked_list.val == min_val:
                    nodes.append(linked_list)
                    lists[i] = lists[i].next
                i += 1

            # step3: add all nodes to merged_lists
            for node in nodes:
                merge_list.next = node
                merge_list = node

            # write base code to exit loop
            if len(nodes) == 0 or not any(lists):
                return merge_list_head.next