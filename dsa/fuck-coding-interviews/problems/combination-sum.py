# https://leetcode.com/problems/combination-sum/description/
from typing import List


class Solution:
    # time: o(n*n), space: o(N)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        def dfs(total=0, index=0):
            if total == target:
                res.append(cur.copy())
                return
            elif total > target:
                return

            for i in range(index, len(candidates)):
                cur.append(candidates[i])
                dfs(total+candidates[i], i)
                cur.pop()
        dfs()

        return res
    
    # time: o(2*n), space: o(n)
    def combinationSum_optimized(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res

#T: O(2^T)
#S: O(N)