# https://leetcode.com/problems/find-the-duplicate-number/
from typing import List, Optional


class Solution:
    def findDuplicate_2(self, nums: List[int]) -> int:
        """
        time complexity: o(nlogn)
        space complexity: O(1)
        Runtime: 1024 ms, faster than 25.19% of Python3 online submissions for Find the Duplicate Number.
        Memory Usage: 27.9 MB, less than 93.18% of Python3 online submissions for Find the Duplicate Number.
        """
        nums.sort()
        for i in nums:
            if i > 0 and nums[i] == nums[i-1]:
                return nums[i]
        return None

    def findDuplicateSet(self, nums: List[int]) -> int:  # type: ignore
        """
        :using set
        time Complexity: o(n)
        space Complexity: o(n)
        Runtime: 1472 ms, faster than 43.22% of Python3 online submissions for Find the Duplicate Number.
        Memory Usage: 30.2 MB, less than 21.03% of Python3 online submissions for Find the Duplicate Number.
        """
        s = set()
        for num in nums:
            if num not in s:
                s.add(num)
            else:
                return num

    def findDuplicate(self, nums: List[int]) -> int:
        """
        # using dp
        time Complexity: o(n)
        space Complexity: o(n)
        Runtime: 630 ms, faster than 97.30% of Python3 online submissions for Find the Duplicate Number.
        Memory Usage: 32.2 MB, less than 11.12% of Python3 online submissions for Find the Duplicate Number.
        """
        dp = {}
        for i in nums:
            if i in dp:
                return i
            else:
                dp[i] = 1
                
    def findDuplicate11(self, nums: List[int]) -> int:
        """
        : using hair and tortoise ( floyed algorithm)
        time Complexity: o(n)
        space Complexity: o(1)
        Runtime: 1373 ms, faster than 52.33% of Python3 online submissions for Find the Duplicate Number.
        Memory Usage: 27.9 MB, less than 58.01% of Python3 online submissions for Find the Duplicate Number.
        """
        slow = nums[0]
        fast = nums[0]
        while 1:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # Find the "entrance" to the cycle.
        ptr1 = nums[0]
        ptr2 = slow
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
        return ptr1