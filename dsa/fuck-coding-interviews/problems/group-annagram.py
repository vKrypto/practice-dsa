"""
url : https://leetcode.com/problems/group-anagrams/
"""
from typing import List


class Solution:
    
    def sortString(self, s)->str:
        return "".join(sorted(s.lower()))
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        using Hashmap
        time complexity: o(n*mlogm)
        space complexity: o(m*n)
        Runtime: 108 ms, faster than 98.40% of Python3 online submissions for Group Anagrams.
        Memory Usage: 17.1 MB, less than 89.28% of Python3 online submissions for Group Anagrams.
        """
        pairs  = {
            self.sortString(strs[0]):[strs[0]]
        }
        for i in range(1, len(strs)):
            tmp = self.sortString(strs[i])
            if tmp in pairs:
                pairs[tmp].append(strs[i])
            else:
                pairs[tmp] = [strs[i]]

        return [val for val in pairs.values()]