# https://leetcode.com/problems/jump-game/submissions/


from typing import List


class Solution:

    # recursive memoized solution
    def canJump_1(self, nums: List[int]) -> bool:
        # top down, memoized, recursive dp
        len_nums = len(nums)
        # base-case
        if len_nums <= 1:
            return True

        memo = [None] * len_nums
        
        def rec(index=len_nums):
            
            # try jump from this index
            for j in range(nums[index]):
                new_index = index -j -1
                if memo[new_index] is None:
                    memo[new_index] = rec(new_index)
                    if memo[new_index]:
                        return True
                elif memo[new_index]:
                    return True
                    
            # otherwise return False
            return False

        return rec()

    # linear solution
    def canJump(self, nums:List):
        n = len(nums)
        target = n-1

        for i in range(n-2, -1, -1):
            if i + nums[i] >= target:
                target = i

        return target == 0