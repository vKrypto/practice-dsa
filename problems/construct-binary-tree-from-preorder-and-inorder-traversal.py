from . import TreeNode
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def buildTree(self, pre_order: List[int], in_order: List[int]) -> Optional[TreeNode]:
        if pre_order and in_order:
            root_node_val = pre_order.pop(0)
            root_node = TreeNode(root_node_val)

            root_index = in_order.index(root_node_val)
            left_tree = in_order[:root_index]
            right_tree = in_order[root_index+1:]

            root_node.left = self.buildTree(pre_order, left_tree)
            root_node.right = self.buildTree(pre_order, right_tree)
            return root_node