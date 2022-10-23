# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        time complexity: o(n)
        Space complexity: O(n) 
        Runtime: 161 ms, faster than 28.36% of Python3 online submissions for Longest Substring Without Repeating Characters.
        Memory Usage: 14 MB, less than 93.09% of Python3 online submissions for Longest Substring Without Repeating Characters.
        """
        dp = {}
        max_len = 0
        start_from = 0
        for k, v in enumerate(s):
            last_found_index = dp.get(v, None)
            if last_found_index is not None and last_found_index + 1 > start_from:
                start_from = last_found_index + 1
            dp[v] = k
            max_len = max(max_len, k-start_from + 1)
        return max_len

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        time complexity: o(2n)
        Space complexity: O(n) 
        Runtime: 68 ms, faster than 90.67% of Python3 online submissions for Longest Substring Without Repeating Characters.
        Memory Usage: 14.1 MB, less than 49.73% of Python3 online submissions for Longest Substring Without Repeating Characters.
        """
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res