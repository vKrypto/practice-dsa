from typing import List


class Solution2:
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
    



class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # recursive way + memoization
        t = sum(nums)/2
        if t != int(t):
            return False
        n = len(nums)
        memo = {}
        nums.sort(reverse=True)

        def rec(i, total=0):
            if total > t or i >= n:
                return False
            res = False
            if (i, total) in memo:
                return memo[(i,total)]
            if total == t:
                res = True
            elif rec(i+1, nums[i]+total):
                res = True
            elif rec(i+1, total):
                res = True
            
            memo[(i, total)] = res
            return res
        
        return rec(0)
            
    def canPartition_2(self, nums: List[int]) -> bool:
        # iterative way
        target = sum(nums)/2
        if target != int(target):
            return False
        s = set([0])
        nums.sort(reverse=True)

        for i in nums:
            temp = set()
            for j in s:
                if i + j == target:
                    return True
                temp.add(i+j)
            s.update(temp)
        return False

    def canPartition_3(self, nums: List[int]) -> bool:
        # bit-manipulation
        if not nums or sum(nums) %2 :
            return False
        target = sum(nums)//2
        cur = 1 << target
        for coin in nums:
            cur |= cur >> coin
        return cur & 1