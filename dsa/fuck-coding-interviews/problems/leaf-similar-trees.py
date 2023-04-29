# https://leetcode.com/problems/leaf-similar-trees/description/

from . import Optional, TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def leaf_node_list(self, root):
        node_val_list = []

        def get_leaf_node(node):
            if node is None:
                return
            if not (node.left or node.right):
                node_val_list.append(node.val)
            get_leaf_node(node.left)
            get_leaf_node(node.right)

        get_leaf_node(root)

        return node_val_list


    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l1 = self.leaf_node_list(root1)
        l2 = self.leaf_node_list(root2)
        return l1 == l2