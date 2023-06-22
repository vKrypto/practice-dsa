from typing import List

class Solution:
    # time: o(2n), space: o(1)
    # split into two house-robber-problem, [0,n-1], [1, n] 
    def house_rob_1(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        # from [0,n-1]
        last, last_last = 0, 0
        for i in range(len(nums)-1):
            n = nums[i]
            last_last, last = last, max(n + last_last, last)
        res_1 = last
        
        # from [1,n]
        last, last_last = 0, 0
        for i in range(1, len(nums)):
            n = nums[i]
            last_last, last = last, max(n + last_last, last)
        return max(last, res_1)

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return max(nums)

        def house_rob(from_index, to_index):
            last, last_last = 0, 0
            for i in range(from_index, to_index):
                n = nums[i]
                last_last, last = last, max(n + last_last, last)
            return last        

        res_1 = house_rob(0, n-1)
        res_2 = house_rob(1, n)
        return max(res_1, res_2)