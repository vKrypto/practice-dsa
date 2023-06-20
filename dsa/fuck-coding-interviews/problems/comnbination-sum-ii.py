# https://leetcode.com/problems/combination-sum-ii/description/


from . import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        paths = []
        def backtrack(index=0 , sum_yet=0, depth=0):
            # terminating condition:
            if sum_yet > target:
                return
            elif sum_yet == target:
                res.append(paths.copy())
                return
            else:
                prev = None
                for i in range(index, len(candidates)):
                    if prev is not None and candidates[i] == prev:
                        continue
                    paths.append(candidates[i])
                    backtrack(i+1, sum_yet+candidates[i], depth+1)
                    paths.pop()
                    prev = candidates[i]

        backtrack()
        return res