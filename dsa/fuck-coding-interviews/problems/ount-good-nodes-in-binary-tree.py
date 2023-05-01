# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

from . import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.good_nodes_count = 0

    def goodNodes(self, root: TreeNode, path=[]) -> int:
        if root is None:
            return

        # increment counter is condition true
        if not path or root.val >= max(path):
            self.good_nodes_count += 1
            

        self.goodNodes(root.left, path + [root.val])
        self.goodNodes(root.right, path + [root.val])

        return self.good_nodes_count