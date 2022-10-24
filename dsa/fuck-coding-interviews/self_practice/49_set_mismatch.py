# https://leetcode.com/problems/set-mismatch/



from typing import List


class Solution:
    """
    Runtime: 222 ms, faster than 88.88% of Python3 online submissions for Set Mismatch.
    Memory Usage: 16.4 MB, less than 6.35% of Python3 online submissions for Set Mismatch.
    """
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        missing = list(set(range(1,len(nums)+1)) - set(nums))
        temp = None
        for  i in nums:
            if temp == i:
                return [i, missing[0]]
            temp = i
