#
# @lc app=leetcode id=606 lang=python3
#
# [606] Construct String from Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return
        res_str = str(root.val)
        if root.left or root.right:
            left_str = self.tree2str(root.left) or ""
            # if left_str:
            res_str += f"({left_str})"
            right_str = self.tree2str(root.right) or ""
            if right_str:
                res_str += f"({right_str})"
        return res_str
        

# @lc code=end

