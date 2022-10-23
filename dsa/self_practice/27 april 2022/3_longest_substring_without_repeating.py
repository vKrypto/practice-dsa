"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

class Solution:
    def bruteForce(self, s:str) -> int:
        """
        time Complexity: O(nlogn)
        Runtime: 66 ms, faster than 83.55% of Python3 online submissions for Longest Substring Without Repeating Characters.
        Memory Usage: 14 MB, less than 93.96% of Python3 online submissions for Longest Substring Without Repeating Characters.
        """
        temp = s[0]
        max_len = 0
        for i in s[1:]:
            # check if next char exist in substring: temp
            repeated_from = temp.find(i)
            if repeated_from != -1:
                # cut first of substring : temp
                temp = temp[repeated_from+1:]
            # add current word in temp
            temp += i
            max_len = max(max_len, len(temp))
        return max_len
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        return self.bruteForce(s)