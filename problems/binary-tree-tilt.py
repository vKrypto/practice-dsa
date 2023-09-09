# https://leetcode.com/problems/binary-tree-tilt/description/


from . import  TreeNode
from typing import Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum_of_tilt_nodes = 0

    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.find_total_nodes_sum(root)
        return self.sum_of_tilt_nodes

    def find_total_nodes_sum(self, root: Optional[TreeNode]) -> int:
        """
        return total_sum of tree nodes and also modifies node value, recursively
        """
        if root:
            left_sum = self.find_total_nodes_sum(root.left)
            right_sum = self.find_total_nodes_sum(root.right)

            total_sum = root.val + left_sum + right_sum
            root.val = abs(left_sum-right_sum)
            self.sum_of_tilt_nodes += root.val
            return total_sum
        return 0
