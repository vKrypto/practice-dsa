from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def rec(i):
            if i >= len(nums):
                return [0]
            next_res = rec(i+1)
            res = []
            for j in next_res:
                res.append(j + nums[i])
                res.append(j - nums[i])
            return res

        count = 0
        for i in rec(0):
            if i == target:
                count += 1
        return count
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        prev = [0]
        for i in range(len(nums)-1, -1, -1):
            res = []
            for j in prev:
                res.append(j + nums[i])
                res.append(j - nums[i])
            prev = res

        count = 0
        for i in prev:
            if i == target:
                count += 1
        
        return count
    

    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {}  # (index, total) -> # of ways

        def rec(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = rec(i + 1, total + nums[i]) + rec(i + 1, total - nums[i])
            return dp[(i, total)]

        return rec(0, 0)
