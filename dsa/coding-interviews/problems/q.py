# https://www.youtube.com/watch?v=JHzX-57dgn0&ab_channel=KeertiPurswani
"""
find number of possible contigus sustering which is a permutation o given sub string.
s = "abcabcabc"
sub = "abc"

count = ?
ans = ["abc", "bca", "cab", "abc", "bca", "cab", "abc"]
"""

from typing import Counter


class Solution:
    """
    time complexity: O(n) n = len(string)
    Sapce Complexity: o(m) m == len(substring)
    
    """
    def count_permutation_1(self, s:str, sub:str) -> int:
        n = len(s)
        m = len(sub)
        i = 0
        total_matched = 0
        sub_map = Counter(sub)
        while n-m-i> 0:
            window = str[i:i+m]
            if Counter(window) == sub_map:
                total_matched += 1
            i += 1
        return total_matched


    def count_permutation_2(self, s:str, sub:str) -> int:
        n = len(s)
        m = len(sub)
        i = 0
        total_matched = 0
        sub_map = Counter(sub)
        window_map = None
        while n-m-i> 0:
            window = str[i:i+m]
            if window_map == None:
                window_map = Counter(window)
            else:
                window_map[s[i-1]] -= 1
                window_map[s[i-1 + m]] = window_map.get(s[i-1 + m], 0) + 1
            if window_map == sub_map:
                total_matched += 1
            i += 1
        return total_matched