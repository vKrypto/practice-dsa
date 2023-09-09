# https://leetcode.com/problems/palindromic-substrings/description/

class Solution:

    def is_palindrome(self, x:str) -> bool:
        if not x:
            return False
        return x == x[::-1]

    # brute force, time: o(n*2), space: o(n*2)/o(1)
    def countSubstrings_brute_force(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(len(s)):
                if self.is_palindrome(s[i:j+1]):
                    res += 1
        return res


    def countSubstrings(self, s: str) -> int:
        res = {"max_count": 0}
        
        def check_pali(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res["max_count"] += 1
                left -= 1
                right += 1
            
        for i in range(len(s)):
            check_pali(i, i)
            check_pali(i, i + 1)
        return res["max_count"]