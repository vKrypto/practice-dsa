# https://leetcode.com/problems/construct-string-from-binary-tree/

# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        """
        Runtime: 103 ms, faster than 46.68% of Python3 online submissions for Construct String from Binary Tree.
        Memory Usage: 16.4 MB, less than 37.40% of Python3 online submissions for Construct String from Binary Tree.
        """
        if root:
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

