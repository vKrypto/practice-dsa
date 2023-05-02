# https://leetcode.com/problems/invert-binary-tree/


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Runtime: 64 ms, faster than 26.54% of Python3 online submissions for Invert Binary Tree.
    # Memory Usage: 13.8 MB, less than 57.66% of Python3 online submissions for Invert Binary Tree.
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # cond 1: 
        if root is None:
            return
        
        # cond 2:
        if not(root.left or root.right):
            return root

        # invert child for this nodes.
        root.left , root.right = root.right, root.left
        
        # do recursively to their child.
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        
        return root