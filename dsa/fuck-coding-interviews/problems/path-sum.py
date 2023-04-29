# coding: utf-8
"""
https://leetcode.com/problems/path-sum/
"""
from . import *

class TreeNode:  # pragma: no cover
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        class ReturnTrue(Exception):
            pass

        def is_leaf(node):
            return not node.left and not node.right

        def inorder_traverse(node, parent_sum=0):
            if not node:
                return

            node.current_sum = node.val + parent_sum
            if is_leaf(node) and node.current_sum == sum:
                raise ReturnTrue

            inorder_traverse(node.left, node.current_sum)
            node
            inorder_traverse(node.right, node.current_sum)

        try:
            inorder_traverse(root)
        except ReturnTrue:
            return True
        return False
    
    def hasPathSum_2(self, root: Optional[TreeNode], targetSum: int, rootPathSum:int=0) -> bool:
        if root:
            rootPathSum += root.val
            if self.hasPathSum(root.left, targetSum, rootPathSum):
                return True
            if self.hasPathSum(root.right, targetSum, rootPathSum):
                return True
            if not(root.right or root.left):
                return rootPathSum == targetSum