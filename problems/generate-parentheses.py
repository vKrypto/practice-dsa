# https://leetcode.com/problems/generate-parentheses/description/
from typing import List


class Solution:
    def generateParenthesis_rec(self, n: int) -> List[str]:
        
        res = []
        def dfs(st="", open_count=0, close_count=0):
            # base-condition
            if close_count == n and open_count == n:
                res.append(st)
                return
            # invalid condition
            if open_count < close_count:
                return

            # left branch
            if open_count <= n:
                dfs(st + "(", open_count+1, close_count )
            # right branch
            if close_count <= n:
                dfs(st + ")", open_count, close_count+1 )
            
        dfs()
        return res

    def generateParenthesis_backtrack(self, n: int) -> List[str]:
        """
        using decision tree with DFS-backtrack
        """
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res
