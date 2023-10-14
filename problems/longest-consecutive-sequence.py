
# https://leetcode.com/problems/longest-consecutive-sequence/
from typing import List

class Solution:
    def longestConsecutive_1(self, nums: List[int]) -> int:
        nums.sort()

        last = None
        count = 0
        g_count = 0
        for i in nums:
            if last is None or i == last +1:
                count += 1
                last = i 
            else:
                last = i
                count = 1
            g_count = max(g_count, count)
        
        return g_count
    
    """
    Runtime: 231 ms, faster than 78.73% of Python3 online submissions
    Memory Usage: 23.3 MB, less than 98.17% of Python3 online submissions
    """
    def longestConsecutive_1_optimized(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        temp = 1 # local max
        max_length = 1 # global max
        for i, v in enumerate(nums):
            if i > 0  and( v == nums[i-1]+1 or  v == nums[i-1]):
                if  v == nums[i-1]:
                    continue
                temp += 1
            else:
                max_length = max(max_length, temp)
                temp = 1
        return max(max_length, temp)
        
    
    def longestConsecutive_2(self, nums: List[int]) -> int:
        num_set  = set(nums)

        def count_connected(num):
            case_1 = case_2 = 0
            num_set.remove(num)

            if num-1 in num_set:
                case_1 = count_connected(num-1)
            
            if num+1 in num_set:
                case_2 = count_connected(num+1)
            
            return 1 + case_1 + case_2

        res = 0
        for i in nums:
            if i in num_set:
                res = max(res, count_connected(i))

        return res

    def longestConsecutive_2_optimized(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in num_set:
            if n - 1 not in num_set:
                length = 1
                while (n + length) in num_set:
                    length += 1
                longest = max(length, longest)
        return longest

    # union-find method:
    def longestConsecutive_3(self, nums: List[int]) -> int:
        pass