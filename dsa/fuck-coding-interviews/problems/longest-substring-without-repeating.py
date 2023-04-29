# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring_1(self, s: str) -> int:
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

    def lengthOfLongestSubstring_2(self, s:str) -> int:
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
    