# https://leetcode.com/problems/combination-sum/description/
from typing import List


class Solution:
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

#T: O(2^T)
#S: O(N)