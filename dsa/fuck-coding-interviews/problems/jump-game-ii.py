# https://leetcode.com/problems/jump-game-ii/

from typing import List

class Solution:
    # linear greedy solution
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        res = [0]* n

        for i in range(n-2, -1, -1):
            min_val = n
            # try all jump possible from this node
            for j in range(1, nums[i]+1):
                if i + j < n:
                    min_val = min(min_val, 1+ res[i+j])
                if min_val ==1:
                    break
            
            res[i] = min_val
        
        return res[0]

    # approach 2: space optimized linear greedy solution, two pointer solutions
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        res = 0
        while r < (len(nums) - 1):
            maxJump = 0
            for i in range(l, r + 1):
                maxJump = max(maxJump, i + nums[i])
            l = r + 1
            r = maxJump
            res += 1
        return res
