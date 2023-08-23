from typing import List


class Solution:
    # recursive cached solution
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)/2
        # base-case
        if int(target) != target:
            return False

        cache = {}
        def rec(i=0, res=0):
            if res == target:
                return True
            if (i, res) in cache:
                return cache[(i, res)]
            if i >= len(nums):
                return False
            case_1 = rec(i+1, res + nums[i])
            case_2 = rec(i+1, res)
            cache[(i, res)] =  case_1 or case_2
            return case_1 or case_2

        return rec()

    # tabulation + space optimized solution
    def canPartition_1(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return False