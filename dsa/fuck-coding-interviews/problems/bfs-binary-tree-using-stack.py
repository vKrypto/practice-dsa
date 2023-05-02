# https://leetcode.com/problems/binary-tree-preorder-traversal/
from typing import List, Optional

# Definition for a binary tree node.
from queue import Queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        q = Queue()
        q.put(root)
        res = []
        while not q.empty():
            temp = q.get()
            res.append(temp.val)
            if temp.left:
                q.put(temp.left)
            if temp.right:
                q.put(temp.right)
        return res

    def postorderTraversal(self, root: Optional[TreeNode]):
        pass

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        dqueue
        [cur_node.left, cur_node, cur_node.right]
        if (cur_node = None)
            temp = deque.pop()
            res.append
        """
        q = Queue()
        q.put(root)
        res = []
        while not q.empty():
            temp = q.get()
            res.append(temp.val)
            if temp.left:
                q.put(temp.left)
            if temp.right:
                q.put(temp.right)
        return res