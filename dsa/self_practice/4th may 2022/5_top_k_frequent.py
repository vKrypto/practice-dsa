# url: https://leetcode.com/problems/top-k-frequent-elements
from collections import Counter

class Solution(object):
    def topKFrequent_1(self, nums, k):
        """
        Runtime: 125 ms, faster than 60.71% of Python3 online submissions for Top K Frequent Elements.
        Memory Usage: 18.6 MB, less than 90.93% of Python3 online submissions for Top K Frequent Elements.
        """
        dic = Counter(nums)       
        print(dic)
        arr = sorted(dic, key = dic.get, reverse = True)
        print(arr)
        return arr[:k]

    def topKFrequent(self, nums, k):
        """
        Runtime: 110 ms, faster than 79.35% of Python3 online submissions for Top K Frequent Elements.
        Memory Usage: 18.5 MB, less than 90.93% of Python3 online submissions for Top K Frequent Elements.
        """
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        
        arr = sorted(dic, key = dic.get, reverse = True)
        return arr[:k]


print(Solution().topKFrequent_1([1,2,3,4,5,5,5,5,6,6,6], 5))