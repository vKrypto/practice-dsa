# https://leetcode.com/problems/3sum-closest/
from typing import List

class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Runtime: 304 ms, faster than 66.81% of Python3 online submissions for 3Sum Closest.
        Memory Usage: 13.9 MB, less than 71.20% of Python3 online submissions for 3Sum Closest.
        """
        closest_sum = None
        nums.sort()
        for index in range(len(nums)-2):
            # pick 3 pointers
            i, j, k = index, index +1, len(nums) -1
            # move last 2 pointers
            while j < k:
                running_sum = nums[i] + nums[j] + nums[k]
                # update closest sum 
                if closest_sum is None or abs(closest_sum - target) > abs(running_sum - target):
                    closest_sum = running_sum
                # update pointers (j , k)
                if running_sum > target:
                    k -= 1
                elif running_sum < target:
                    j += 1
                else:
                    return running_sum
                
        return closest_sum