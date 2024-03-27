from typing import List


class Solution:
    
    # recursive solution
    def rob_recursive(self, nums: List[int]) -> int:
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
    
    # iterative solution
    def rob_iterative(self, nums: List[int]) -> int:
        dp = [0]* len(nums) + [0]*3

        for i in range(len(nums)-1, -1, -1):
            dp[i] = nums[i] +  max(dp[i+2], dp[i+3])

        return max(dp[0], dp[1])
    
    # iterative memory optimized solution
    def rob_iterative_optimized(self, nums: List[int]) -> int:
        a, b, c = 0, 0, 0
        for num in nums:
            a, b, c = num +  max(b, c), a, b
        return max(a, b)
    
    
    # iterative memory optimized solution
    def rob(self, nums: List[int]) -> int:
        last, last_last = 0, 0
        for n in nums:
            last_last, last = last, max(n + last_last, last)
        return last