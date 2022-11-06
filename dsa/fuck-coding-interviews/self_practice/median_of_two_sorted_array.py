"""
https://leetcode.com/problems/median-of-two-sorted-arrays/
"""

from typing import List
        
class Solution:
    
    def bruteForce(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Runtime: 98 ms, faster than 83.48% of Python3 online submissions for Median of Two Sorted Arrays.
        Memory Usage: 14.2 MB, less than 69.82% of Python3 online submissions for Median of Two Sorted Arrays.
        """
        nums = nums1 + nums2
        nums.sort()
        l = len(nums)
        if l%2==0:
            return (nums[l//2] + nums[l//2-1])/2
        else:
            return nums[(l+1)//2 -1]
        
        
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        runtime time-complexity: O(log(min(m+n)))
        Runtime: 97 ms, faster than 84.27% of Python3 online submissions for Median of Two Sorted Arrays.
        Memory Usage: 14.2 MB, less than 69.82% of Python3 online submissions for Median of Two Sorted Arrays.
        """
        total = len(nums1) + len(nums2)
        half = total // 2
        # make sure nums 1 is smaller or equal to nums2
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        # iterate smaller list..
        l, r = 0, len(nums1) -1
        while True:
            i = (l+r)//2 # for nums1 
            j = half - i - 2 # for nums 2
            
            l1 = nums1[i] if i >=0 else float('-infinity')
            r1 = nums1[i+1] if i+1 < len(nums1) else float('infinity') 
            l2 = nums2[j] if j >=0 else float('-infinity')
            r2 = nums2[j+1] if j+1 < len(nums2) else float('infinity') 
            
            # valid condition
            if l1 <= r2 and l2 <= r1:
                # for odd.
                if total % 2:
                    return min(r1,r2)
                return (max(l1,l2)+ min(r1,r2))/2
            
            elif l1 > r2:
                r = i-1
            else:
                l = i + 1