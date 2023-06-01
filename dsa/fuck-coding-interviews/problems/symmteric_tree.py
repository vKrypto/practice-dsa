"""
https://leetcode.com/problems/symmetric-tree/description/
"""


from typing  import Optional
from . import TreeNode


class Solution:
    def isSymmetric_1(self, root: Optional[TreeNode]) -> bool:
        """
        using depth first traversal
        """
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)
        return dfs(root.left, root.right)


    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        using level order traversal
        """
        current_level = [root]
        while any(current_level):
            next_level = []
            for node in current_level:
                if node is None:
                    continue
                next_level.extend([node.left, node.right])
        
            left, right = 0 , len(next_level) - 1
            while left < right:
                left_val = next_level[left].val if next_level[left] else None
                right_val = next_level[right].val if next_level[right] else None
                if not (left_val  == right_val):
                    return False
                left += 1
                right -= 1
            current_level = next_level
        return True
            