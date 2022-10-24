"""
url: https://leetcode.com/problems/valid-anagram/
"""
from collections import Counter

class Solution:
    """
    time Complexity: o(nlogn)
    space Complexity: o(n)
    Runtime: 87 ms, faster than 23.65% of Python3 online submissions for Valid Anagram.
    Memory Usage: 15.2 MB, less than 11.98% of Python3 online submissions for Valid Anagram.
    """
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False
        s = list(s)
        s.sort()
        t = list(t)
        t.sort()
        for i in range(len_s):
            if s[i] != t[i]:
                return False
        return True
            
    def isAnagram_1(self, s: str, t: str) -> bool:
        """
        time Complexity: o(n)
        space Complexity: o(n)
        Runtime: 56 ms, faster than 72.37% of Python3 online submissions for Valid Anagram.
        Memory Usage: 14.6 MB, less than 26.50% of Python3 online submissions for Valid Anagram.
        """
        len_s = len(s)
        len_t = len(t)
        if len_t != len_s:
            return False
        # group string
        group_s = {}
        for i in s:
            group_s[i] = group_s.get(i, 0) + 1
        
        # group string
        group_t = {}
        for i in t:
            group_t[i] = group_t.get(i, 0) + 1
        
        # compare. grouping
        for i in s:
            if group_t.get(i) != group_s.get(i):
                return False
        return True

    def isAnagram_2(self, s: str, t: str) -> bool:
        """
        time Complexity: o(n)
        space Complexity: o(n)
        Runtime: 46 ms, faster than 90.31% of Python3 online submissions for Valid Anagram.
        Memory Usage: 14.3 MB, less than 99.80% of Python3 online submissions for Valid Anagram.
        """
        len_s = len(s)
        len_t = len(t)
        if len_t != len_s:
            return False
        # group string
        group_s = Counter(s)
        group_t = Counter(t)

        # compare. grouping
        for i, v in group_t.items():
            if v != group_s.get(i):
                return False
        return True

    def isAnagram_3(self, s: str, t: str) -> bool:
        """
        Runtime: 59 ms, faster than 65.74% of Python3 online submissions for Valid Anagram.
        Memory Usage: 15.1 MB, less than 11.98% of Python3 online submissions for Valid Anagram.
        """
        len_s = len(s)
        len_t = len(t)
        if len_t != len_s:
            return False
        # group string
        s = sorted(s)
        t = sorted(t)
        for i in range(len_s):
            if s[i] != t[i]:
                return False
        return True
            