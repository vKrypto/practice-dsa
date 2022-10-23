# https://leetcode.com/problems/maximum-subarray/


class Solution:
    """
    time Complexity: O(n)
    Space Complexity: O(1)
    Runtime: 775 ms, faster than 92.02% of Python3 online submissions for Maximum Subarray.
    Memory Usage: 27.8 MB, less than 77.54% of Python3 online submissions for Maximum Subarray.
    pattern: prev subarray cant be negative, dynamic programming: compute max sum for each prefix
    """
    def maxSubArray(self, nums: List[int]) -> int:
        # assign default values.
        max_res = float('-infinity')
        local_sum = 0

        for i in nums:
            local_sum = local_sum + i
            max_res = max(max_res, local_sum)
            if local_sum <= 0:
                local_sum=0
            
        return max_res

    
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub = cursub = -float('inf')     
        for num in nums:
		    #if max is num, we start a new subarray from this num
			#if max is num + cursub, we include this num to the current subarray we computed from previous numbers
            cursub = max(num+cursub, num)
			#we keep track of the subarray with the maximum sums
            maxsub = max(cursub, maxsub)
            
        return maxsub