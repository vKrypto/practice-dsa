# https://leetcode.com/problems/all-possible-full-binary-trees/submissions/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        cache = {0:[], 1 :[TreeNode()]}
        
        def rec(n):
            if n in cache:
                return cache[n]
            res = []
            for i in range(1,n):
                left = rec(i)
                right = rec(n-i-1)
                for t1 in left:
                    for t2 in right:
                        res.append(TreeNode(0, t1, t2))
            cache[n] = res
            return res

        return rec(n)