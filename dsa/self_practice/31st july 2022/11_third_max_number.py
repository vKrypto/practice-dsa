# https://leetcode.com/problems/third-maximum-number/submissions/



class Solution:
    # Runtime: 100 ms, faster than 29.26% of Python3 online submissions for Third Maximum Number.
    # Memory Usage: 15.6 MB, less than 21.12% of Python3 online submissions for Third Maximum Number.
    # need optimization
    def thirdMax(self, nums: List[int]) -> int:
        l = list(set(nums))
        l.sort()
        if len(l) > 2:
            l.pop()
            l.pop()
            return l.pop()
        return l[-1]
    
    # Runtime: 62 ms, faster than 84.95% of Python3 online submissions for Third Maximum Number.
    # Memory Usage: 14.9 MB, less than 79.03% of Python3 online submissions for Third Maximum Number.
    # time complexity: o(n) and space complexity: o(1)
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        temp = None
        removed = 0
        for i in nums[::-1]:
            if temp is None or temp != i:
                if removed == 2:
                    return i
                removed += 1
            temp = i
        return nums[-1]