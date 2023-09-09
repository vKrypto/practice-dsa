# https://leetcode.com/problems/binary-tree-preorder-traversal/
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        current_node = root
        
        while stack or current_node:
            # go to left most node of current node.
            while current_node:
                stack.append(current_node)
                current_node = current_node.left
            
            current_node = stack.pop()
            res.append(current_node.val)
            current_node = current_node.right

        return res

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        current_node = root
        
        while stack or current_node:
            # go to left most node of current node.
            while current_node:
                res.append(current_node.val)
                stack.append(current_node)
                current_node = current_node.left
            
            current_node = stack.pop()
            current_node = current_node.right

        return res

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        current_node = root
        
        while stack or current_node:
            # go to left most node of current node.
            while current_node:
                stack.append(current_node)
                current_node = current_node.left
            
            current_node = stack.pop()
            res.append(current_node.val)
            current_node = current_node.right

        return res