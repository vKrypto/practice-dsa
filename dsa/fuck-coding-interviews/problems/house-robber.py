from typing import List


class Solution:
    
    # recursive solution: TLE
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return max(nums)

        dp = [0] * len(nums)

        def dfs(index):
            if index > len(nums)-1:
                return 0
            elif index in dp:
                return dp[index]
            
            dp[index] = nums[index] + max(dfs(index+2), dfs(index+3))
            return dp[index]

        return max(dfs(0), dfs(1))
    
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2