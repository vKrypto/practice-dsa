"""
Nov 7, 2022, 10:58 PM
Given a singly linked list and an integer k, remove the kth last element from the list.
k is guaranteed to be smaller than the length of the list.
The list is very long, so making more than one pass is prohibitively expensive.
Do this in constant space and in one pass.
"""
from typing import List

class Node:

    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None
    

class LinkedList:
    def display(self):
        items = []
        head = self.head
        while head:
            items.append(str(head.val))
            head = head.next
        print(" -> ".join(items))


    def __init__(self, vals:List) -> None:
        """
        convert list to linked List
        """
        cur_head = head = None
        for value in vals:
            temp = Node(value)
            if head is None:
                cur_head = head = temp
            else:
                cur_head.next = temp
                cur_head = cur_head.next
        self.head = head


class Solution(LinkedList):
    def __init__(self, vals: List, k:int) -> None:
        super().__init__(vals)
        self.display()
        self.remove_Kth_node_from_last(k)
        self.display()

    def remove_Kth_node_from_last(self, k:int) -> LinkedList:
        slow = fast = self.head 
        # make a window of size k between slow, fast
        for _ in range(k):
            fast = fast.next

        # slide window to end of list
        while fast.next:
            fast = fast.next
            slow = slow.next

        # slow is our nth node form last, let's remove it
        slow.next = slow.next.next

class TestCase:

    def __init__(self):
        self.inputs =  [
            [list(range(20)), 11]
        ]

    def test(self):
        for input in self.inputs:
            Solution(*input)

TestCase.test()